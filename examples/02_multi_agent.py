from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
import time
import sys
from pathlib import Path
# Add parent directory to path for utils import
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.visualization import (
    print_crew_startup, 
    print_execution_start, 
    print_execution_complete, 
    print_outputs_saved
)
load_dotenv()

QWEN_MODEL = "ollama/qwen2.5:7b"

class ResearchFindings(BaseModel):
    key_technologies: List[str] = Field(..., description="Names and one-line description")
    smart_city_case_studies: List[str] = Field(..., description="City + project + outcome")
    major_challenges: List[str]
    future_opportunities: List[str]
    sources: List[str] = Field(..., description="URLs, minimum 8 from 2024–2025")

class FinalArticle(BaseModel):
    title: str
    introduction: str
    body_sections: List[str]
    conclusion: str
    references: List[str]

researcher = Agent(
    role="Senior Energy & Urban Systems Researcher",
    goal="Deliver verifiably accurate, source-backed research on sustainable energy in smart cities as of Nov 2025",
    backstory="""You are ex-McKinsey, now lead researcher at a Tier-1 think tank.
    You NEVER state a fact without a primary 2024–2025 source.
    You think step-by-step, use tools aggressively, and cite everything.""",
    llm=QWEN_MODEL,
    temperature=0.0,
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    verbose=True,
    allow_delegation=False,
    max_iter=30,
)

writer = Agent(
    role="Award-Winning Tech Journalist",
    goal="Transform rigorous research into compelling, accessible 1000-word articles",
    backstory="""You write for Wired, The Atlantic, and MIT Technology Review.
    You turn complex topics into narratives that non-experts love.
    You aim for clarity, rhythm, and subtle storytelling.""",
    llm=QWEN_MODEL,
    temperature=0.72,
    verbose=True,
    allow_delegation=False,
)

editor = Agent(
    role="Former New York Times Standards Editor",
    goal="Produce publication-ready copy with perfect grammar, flow, and factual accuracy",
    backstory="""You edited 300+ long-form features. You are ruthless about clarity,
    consistency, and source attribution. If something is wrong, you fix or flag it.""",
    llm=QWEN_MODEL,
    temperature=0.1,
    verbose=True,
    allow_delegation=False,
)

research_task = Task(
    description="Research 'Sustainable Energy Solutions for Smart Cities' as of November 2025",
    expected_output="Structured research findings with citations",
    agent=researcher,
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    output_pydantic=ResearchFindings,
    output_file="outputs/01_research.json",
)

writing_task = Task(
    description="""Using the research findings, write a 900–1100 word article titled
    'How Smart Cities Are Winning the Energy Revolution'.
    Make it engaging for a general audience while staying 100% faithful to sources.""",
    expected_output="Complete article in Markdown with proper headings",
    agent=writer,
    context=[research_task],
    output_pydantic=FinalArticle,
    output_file="outputs/02_draft_article.md",
)

editing_task = Task(
    description="Edit the draft into publication-ready form. Fix style, grammar, flow, and verify every claim still matches sources.",
    expected_output="Final polished article",
    agent=editor,
    context=[research_task, writing_task],
    output_file="outputs/FINAL_sustainable_energy_smart_cities.md",
    human_input=True,
)

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.hierarchical,
    manager_llm=QWEN_MODEL,
    verbose=True,
    memory=True,
    cache=True,
    embedder={"provider": "ollama"},
)

if __name__ == "__main__":
    # Visualization: Show setup
    print_crew_startup(
        crew=crew,
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        model=QWEN_MODEL,
        process="Hierarchical",
        memory=True,
        cache=True,
        verbose=True,
        estimated_time="3-5 minutes (with web research)"
    )
    
    start_time = time.time()
    
    print_execution_start()
    
    result = crew.kickoff()
    
    print_execution_complete(start_time, result)
    
    print_outputs_saved([
        research_task.output_file,
        writing_task.output_file,
        editing_task.output_file
    ])

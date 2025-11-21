from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
load_dotenv()

QWEN_MODEL = "ollama/qwen2.5:7b"

class ResearchReport(BaseModel):
    trends: List[str]
    challenges: List[str]
    opportunities: List[str]
    case_studies: List[str]
    predictions_5y: List[str]
    sources: List[str]

researcher = Agent(
    role="Senior Medical Technology Researcher",
    goal="Deliver verifiably accurate, source-backed analysis on AI in healthcare",
    backstory="""You are a former McKinsey healthcare consultant turned AI researcher.
    You never state a fact without a 2024–2025 primary source. You think step-by-step,
    use tools extensively, and refuse to speculate.""",
    llm=QWEN_MODEL,
    temperature=0.0,
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    verbose=True,
    allow_delegation=False,
    max_iter=25,
    max_rpm=60,
)

task = Task(
    description="Research 'The Future of AI in Healthcare' as of November 2025",
    expected_output="Comprehensive report with cited sources",
    agent=researcher,
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    output_pydantic=ResearchReport,
    output_file="reports/ai_healthcare_2025.md",
    human_input=False,
)

crew = Crew(
    agents=[researcher],
    tasks=[task],
    process=Process.hierarchical,
    manager_llm=QWEN_MODEL,
    verbose=True,
    memory=True,
    cache=True,
)

result = crew.kickoff()
print(result)

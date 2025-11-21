from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os
import time
import sys
from pathlib import Path

# Add parent directory to path for visualization import
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.visualization import (
    print_crew_startup, 
    print_execution_start, 
    print_execution_complete, 
    print_outputs_saved
)
load_dotenv()

# Clear any old ChromaDB data to avoid embedding conflicts
os.environ['CREWAI_TELEMETRY_OPT_OUT'] = '1'

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
    max_iter=5,  # Reduced for faster testing
    max_rpm=60,
)

task = Task(
    description="Research 'The Future of AI in Healthcare' as of November 2025. Limit to 3-5 items per category for a quick overview.",
    expected_output="Brief 100 words report with 3-5 items per category and cited sources",
    agent=researcher,
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    output_pydantic=ResearchReport,
    output_file="reports/ai_healthcare_2025.md",
    human_input=False,
)

crew = Crew(
    agents=[researcher],
    tasks=[task],
    process=Process.sequential,  # Sequential is faster than hierarchical for single agent
    verbose=True,  # Show detailed execution flow
    memory=False,  # Disabled temporarily to avoid embedding conflicts
    cache=True,
    # embedder={"provider": "ollama"},  # Will enable once ChromaDB is cleared
)

# Visualization: Show setup
print_crew_startup(
    crew=crew,
    agents=[researcher],
    tasks=[task],
    model=QWEN_MODEL,
    process="Sequential",
    memory=False,
    cache=True,
    verbose=True,
    estimated_time="2-5 minutes (with web research)"
)

start_time = time.time()

print_execution_start()

result = crew.kickoff()

print_execution_complete(start_time, result)

print_outputs_saved([task.output_file])

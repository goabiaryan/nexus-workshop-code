from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
import os
load_dotenv()

os.makedirs("launch_outputs", exist_ok=True)

QWEN_MODEL = "ollama/qwen2.5:7b"

class MarketAnalysis(BaseModel):
    market_size_2025: str
    growth_cagr: str
    top_competitors: List[str]
    customer_pain_points: List[str]
    pricing_benchmarks: List[str]
    sources: List[str] = Field(..., min_items=10)

class LaunchStrategy(BaseModel):
    positioning: str
    target_personas: List[str]
    differentiation: str
    go_to_market_channels: List[str]
    success_metrics: List[str]

class MarketingPackage(BaseModel):
    headline: str
    landing_page_copy: str
    social_posts: List[str]
    email_sequence: List[str]

class TechDocs(BaseModel):
    user_guide_wordcount: int
    api_overview: str
    faq_items: int

market_researcher = Agent(
    role="Senior Market Intelligence Analyst",
    goal="Deliver 2025-accurate, source-backed market analysis on AI productivity tools",
    backstory="""Ex-Gartner, now running intelligence at a $2B SaaS unicorn.
    You NEVER cite anything pre-2024. You use tools until you have ≥10 primary sources.""",
    llm=QWEN_MODEL,
    temperature=0.0,
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    verbose=True,
    allow_delegation=False,
    max_iter=35,
)

product_strategist = Agent(
    role="Chief Product Strategy Officer",
    goal="Turn raw market data into winning launch strategy",
    backstory="""Led launches of Notion, Slack, and Figma competitors.
    You think in frameworks (Jobs-to-be-Done, Blue Ocean, etc.) and always quantify.""",
    llm=QWEN_MODEL,
    temperature=0.2,
    verbose=True,
)

marketing_writer = Agent(
    role="Growth Marketing Lead",
    goal="Create launch content that converts",
    backstory="""Ex-Intercom, built growth at two unicorns.
    You write like April Dunford + Julian Shapiro. Every word earns its place.""",
    llm=QWEN_MODEL,
    temperature=0.75,
    verbose=True,
)

tech_writer = Agent(
    role="Developer Relations Engineer",
    goal="Ship docs that users actually read",
    backstory="""Wrote the original Stripe and Vercel docs.
    You obsess over clarity and zero onboarding friction.""",
    llm=QWEN_MODEL,
    temperature=0.3,
    verbose=True,
)

coordinator = Agent(
    role="Launch Program Manager",
    goal="Orchestrate perfect execution and catch every gap before launch",
    backstory="""Ran 50+ enterprise SaaS launches. Nothing ships on your watch unless it's flawless.""",
    llm=QWEN_MODEL,
    temperature=0.1,
    allow_delegation=True,
    verbose=True,
)

market_task = Task(
    description="Deep 2025 market research on AI-powered productivity tools for remote teams",
    expected_output="Structured JSON market analysis with ≥10 sources",
    agent=market_researcher,
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    output_pydantic=MarketAnalysis,
    output_file="launch_outputs/01_market_analysis.json",
)

strategy_task = Task(
    description="Build the definitive launch strategy based on the market research",
    expected_output="Structured launch strategy",
    agent=product_strategist,
    context=[market_task],
    output_pydantic=LaunchStrategy,
    output_file="launch_outputs/02_strategy.json",
)

marketing_task = Task(
    description="Create all launch marketing assets using the approved strategy",
    expected_output="Complete marketing package",
    agent=marketing_writer,
    context=[market_task, strategy_task],
    output_pydantic=MarketingPackage,
    output_file="launch_outputs/03_marketing_package.md",
    async_execution=True,
)

tech_docs_task = Task(
    description="Write world-class technical documentation for the new product",
    expected_output="Technical documentation suite",
    agent=tech_writer,
    context=[strategy_task],
    output_pydantic=TechDocs,
    output_file="launch_outputs/04_tech_docs/",
    async_execution=True,
)

final_review_task = Task(
    description="""Produce the final Launch Readiness Report.
    Validate every deliverable, highlight risks, and give go/no-go recommendation.""",
    expected_output="Final launch readiness report in Markdown",
    agent=coordinator,
    context=[market_task, strategy_task, marketing_task, tech_docs_task],
    output_file="launch_outputs/FINAL_LAUNCH_READINESS.md",
    human_input=True,
)

crew = Crew(
    agents=[market_researcher, product_strategist, marketing_writer, tech_writer, coordinator],
    tasks=[market_task, strategy_task, marketing_task, tech_docs_task, final_review_task],
    process=Process.hierarchical,
    manager_llm=QWEN_MODEL,
    verbose=True,
    memory=True,
    cache=True,
    embedder={"provider": "ollama"},
    max_rpm=60,
)

if __name__ == "__main__":
    print("Launching 2025-grade Product Launch Crew (Slide 13 in real life)")
    result = crew.kickoff()
    print("\n" + "="*70)
    print("LAUNCH READY – All files in ./launch_outputs/")
    print("="*70)

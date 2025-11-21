# Quick Reference Guide

## Imports

```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
load_dotenv()
```

## Agent Definition Template

```python
agent = Agent(
    role="Agent Role Name",
    goal="What the agent aims to achieve",
    backstory="""Detailed context about the agent's background,
    expertise, and approach to tasks.""",
    llm="claude-3-5-sonnet-20241022",  # or "gpt-4o-2024-11-20"
    temperature=0.0,  # Lower for factual tasks, higher for creative
    tools=[SerperDevTool(), ScrapeWebsiteTool()],  # Optional
    verbose=True,  # See agent's thinking process
    allow_delegation=False,  # Can this agent delegate tasks?
    max_iter=25,  # Maximum iterations for agent
)
```

## Task Definition Template

```python
task = Task(
    description="""Detailed description of what needs to be done.
    Be specific about requirements and expectations.""",
    agent=agent,  # Which agent handles this task
    expected_output="Description of what the output should look like",
    tools=[SerperDevTool(), ScrapeWebsiteTool()],  # Optional
    context=[previous_task],  # Explicit task dependencies
    output_pydantic=YourModel,  # Optional: structured output
    output_file="outputs/result.md",  # Optional: save to file
    async_execution=True,  # Optional: run in parallel
)
```

## Crew Definition Template

```python
crew = Crew(
    agents=[agent1, agent2, agent3],
    tasks=[task1, task2, task3],
    process=Process.hierarchical,  # or Process.sequential
    manager_llm="claude-3-5-sonnet-20241022",  # For hierarchical
    verbose=True,  # Boolean: True for detailed output, False for quiet
    memory=True,  # Enable memory
    cache=True,  # Enable caching
    embedder={"provider": "openai"},  # For memory/embeddings
)
```

## Structured Outputs (Pydantic)

```python
from pydantic import BaseModel, Field
from typing import List

class ResearchReport(BaseModel):
    trends: List[str]
    challenges: List[str]
    opportunities: List[str]
    sources: List[str] = Field(..., min_items=5)

task = Task(
    description="Research topic X",
    agent=agent,
    output_pydantic=ResearchReport,  # Structured output
    output_file="outputs/research.json"
)
```

## Execution

```python
result = crew.kickoff()
print(result)
```

## Common Process Types

- **Process.sequential**: Tasks execute one after another in order
- **Process.hierarchical**: Tasks can have dependencies and run in parallel when possible (recommended for 2025)

## Agent Best Practices

1. **Role**: Be specific (e.g., "Senior Research Analyst" not just "Researcher")
2. **Goal**: Make it actionable and measurable
3. **Backstory**: Include expertise, approach, and personality traits (crucial for behavior)
4. **LLM**: Use appropriate model (claude-3-5-sonnet-20241022 or gpt-4o-2024-11-20)
5. **Temperature**: Lower (0.0-0.2) for factual tasks, higher (0.7-0.8) for creative
6. **Tools**: Add SerperDevTool/ScrapeWebsiteTool for research tasks
7. **Verbose**: Set to `True` during development for debugging

## Task Best Practices

1. **Description**: Be detailed and specific
2. **Expected Output**: Clearly define what success looks like
3. **Context**: Use `context=[task]` for explicit dependencies (recommended)
4. **Tools**: Add tools to tasks that need web search/scraping
5. **Output Pydantic**: Use structured outputs for better results
6. **Output File**: Save results to files for review
7. **Async Execution**: Use `async_execution=True` for parallel tasks
8. **Assignment**: Assign to the most appropriate agent

## Common Patterns

### Pattern: Research → Create → Review
```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

researcher = Agent(
    role="Researcher",
    goal="Gather accurate information",
    backstory="Expert researcher...",
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    verbose=True
)

writer = Agent(role="Writer", goal="Create content", ...)
editor = Agent(role="Editor", goal="Refine content", ...)

research_task = Task(
    description="Research topic X",
    agent=researcher,
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    output_file="outputs/research.json"
)

writing_task = Task(
    description="Write article based on research",
    agent=writer,
    context=[research_task],  # Explicit dependency
    output_file="outputs/article.md"
)

editing_task = Task(
    description="Edit the article",
    agent=editor,
    context=[research_task, writing_task],
    output_file="outputs/final.md"
)

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.hierarchical,
    manager_llm="claude-3-5-sonnet-20241022",
    verbose=True,  # Boolean: True for detailed output
    memory=True,
    cache=True
)
```

### Pattern: Parallel Specialists
```python
# Multiple agents work on different aspects simultaneously
marketing_agent = Agent(role="Marketing Specialist", ...)
tech_agent = Agent(role="Technical Writer", ...)

# Tasks can run in parallel using async_execution
marketing_task = Task(
    agent=marketing_agent,
    async_execution=True,  # Runs in parallel
    ...
)
tech_task = Task(
    agent=tech_agent,
    async_execution=True,  # Runs in parallel
    ...
)
```

## Debugging Tips

1. **Use verbose mode**: `verbose=True` on agents and crew for detailed output
2. **Check task dependencies**: Ensure tasks are in the right order
3. **Review agent reasoning**: Verbose output shows agent thinking
4. **Test individually**: Run single agents before complex crews
5. **Refine descriptions**: More detail = better results

## Environment Variables

```bash
# Required for LLM providers
export OPENAI_API_KEY="your-key"
export ANTHROPIC_API_KEY="your-key"

# Required for SerperDevTool (web search)
export SERPER_API_KEY="your-key"
```

Or use `.env` file:
```
OPENAI_API_KEY=your-key
ANTHROPIC_API_KEY=your-key
SERPER_API_KEY=your-key
```

## Quick Commands

```bash
# Run examples
python examples/01_basic_agent.py
python examples/02_multi_agent.py
python examples/03_advanced_orchestration.py

# Install dependencies
pip install -r requirements.txt

# Check Python version
python --version
```

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | Activate venv, install requirements (including crewai-tools) |
| API key error | Check .env file, verify key is valid (including SERPER_API_KEY for tools) |
| Tasks in wrong order | Use `context=[task]` for explicit dependencies, use Process.hierarchical |
| Poor results | Refine agent backstory, add task details, check temperature settings |
| Import errors | Check Python version (3.8+), reinstall crewai and crewai-tools |
| Tool errors | Ensure SERPER_API_KEY is set for SerperDevTool |


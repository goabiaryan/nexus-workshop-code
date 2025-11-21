# Workshop: Build Your First Agent / Multi-Agent System

## Description

This hands-on workshop is designed for anyone looking to get started with Agentic AI, addressing one of the community's most common questions: **"How do I get started?"**

Using the popular open-source **CrewAI** framework, you'll learn how to build and orchestrate a team of autonomous agents to accomplish complex, multi-step tasks. You'll discover how to define an agent's role, goal, and backstory to simplify task decomposition.

## What You'll Learn

- ✅ How to set up and configure CrewAI
- ✅ How to define agents with roles, goals, and backstories
- ✅ How to create tasks and assign them to agents
- ✅ How to orchestrate multiple agents working together
- ✅ How to handle complex task decomposition
- ✅ Best practices for building production-ready agent systems

## Prerequisites

- Python 3.8 or higher
- Basic understanding of Python programming
- Familiarity with AI/ML concepts (helpful but not required)
- **Ollama** (for local models - see [OLLAMA_SETUP.md](OLLAMA_SETUP.md)) OR
- **Hugging Face API key** (for cloud models)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd packt-event
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API keys (required):

**Quick setup (recommended):**
```bash
# macOS/Linux
./setup_secrets.sh

# Windows (PowerShell)
.\setup_secrets.ps1
```

**Or manually:**
```bash
# Copy the template
cp .env.example .env

# Edit .env and add your keys:
# - SERPER_API_KEY (required, get free key at https://serper.dev)
# - OPENAI_API_KEY or ANTHROPIC_API_KEY (choose one)
```

**Required API Keys:**
- **SERPER_API_KEY**: Required for examples. Get free key at [serper.dev](https://serper.dev)
- **LLM Provider**: Choose one:
  - **OPENAI_API_KEY**: [Get key](https://platform.openai.com/api-keys)
  - **ANTHROPIC_API_KEY**: [Get key](https://console.anthropic.com/)

## Workshop Structure

### 1. Basic Example: Single Agent (`examples/01_basic_agent.py`)
Start here! Learn how to create your first agent and have it complete a simple task.

### 2. Multi-Agent System (`examples/02_multi_agent.py`)
See how multiple agents can work together, each with specialized roles.

### 3. Advanced Orchestration (`examples/03_advanced_orchestration.py`)
Explore complex task decomposition and agent coordination for real-world scenarios.

## Quick Start

Run the basic example:
```bash
python examples/01_basic_agent.py
```

## Key Concepts

### Agent Definition
An agent in CrewAI has three key components:
- **Role**: What the agent does (e.g., "Researcher", "Writer", "Editor")
- **Goal**: What the agent aims to achieve
- **Backstory**: Context that helps the agent understand its purpose

### Task Decomposition
CrewAI automatically breaks down complex tasks into manageable subtasks, assigning them to the most appropriate agents based on their roles and capabilities.

### Crew Orchestration
A Crew coordinates multiple agents, managing task assignment, execution order, and result aggregation.

## Examples Overview

### Example 1: Basic Agent
A simple research agent that gathers information on a topic.

### Example 2: Multi-Agent System
A content creation team with:
- **Researcher**: Gathers information
- **Writer**: Creates content
- **Editor**: Reviews and refines

### Example 3: Advanced Orchestration
A complex system demonstrating:
- Hierarchical process orchestration
- Parallel task execution with `async_execution`
- Structured outputs with Pydantic models
- Explicit task dependencies with `context`
- File output management
- Memory and caching

## Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)
- [CrewAI Community](https://discord.gg/crewai)

## Secrets Management

For detailed information on setting up and managing your API keys securely, see [SECRETS.md](SECRETS.md).

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'crewai'` or `'crewai_tools'`
- **Solution**: Make sure you've activated your virtual environment and installed all requirements: `pip install -r requirements.txt`

**Issue**: API key errors
- **Solution**: Ensure you have API keys set in your `.env` file:
  - `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` for LLM providers
  - `SERPER_API_KEY` for web search tools (SerperDevTool)
- CrewAI can work with local models. Check the documentation for local setup options.

**Issue**: Tool errors (SerperDevTool, ScrapeWebsiteTool)
- **Solution**: Make sure `SERPER_API_KEY` is set in your `.env` file. Get a free key at [serper.dev](https://serper.dev)

## Next Steps

After completing this workshop:
1. Experiment with different agent roles, goals, and LLM models
2. Try building your own multi-agent system
3. Explore CrewAI's advanced features:
   - Tools (SerperDevTool, ScrapeWebsiteTool, custom tools)
   - Structured outputs with Pydantic models
   - Memory and caching
   - Parallel task execution
   - Hierarchical process orchestration
4. Join the CrewAI community to share your projects!

## License

This workshop material is provided for educational purposes.

## Contributing

Found an issue or have a suggestion? Please open an issue or submit a pull request!


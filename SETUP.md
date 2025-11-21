# Setup Instructions

## Quick Setup (5 minutes)

### Step 1: Prerequisites

Ensure you have Python 3.8 or higher installed:
```bash
python --version
```

### Step 2: Clone and Navigate

```bash
cd "/Users/jarvis/Documents/content creation/packt event"
```

### Step 3: Create Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure API Keys (Required)

**Option A: Using the setup script (Recommended)**

**macOS/Linux:**
```bash
./setup_secrets.sh
```

**Windows (PowerShell):**
```powershell
.\setup_secrets.ps1
```

**Option B: Manual setup**

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your API keys:
```bash
# For LLM providers (choose one or both)
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=your-key-here

# For web search tools (required for examples)
SERPER_API_KEY=your-key-here
# Get a free key at https://serper.dev
```

**Required API Keys:**
- **SERPER_API_KEY**: Required for examples (web search). Get a free key at [serper.dev](https://serper.dev) (2,500 searches/month free)
- **LLM Provider**: Choose one:
  - **OPENAI_API_KEY**: Get at [platform.openai.com](https://platform.openai.com/api-keys)
  - **ANTHROPIC_API_KEY**: Get at [console.anthropic.com](https://console.anthropic.com/)

**Note**: CrewAI can work with local models too. See the [CrewAI documentation](https://docs.crewai.com/) for local setup options.

### Step 6: Verify Installation

Run the basic example:
```bash
python examples/01_basic_agent.py
```

If you see output from the agent, you're all set! 🎉

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'crewai'`

**Solution:**
1. Make sure your virtual environment is activated (you should see `(venv)` in your terminal)
2. Reinstall: `pip install -r requirements.txt`

### Issue: API Key Errors

**Solution:**
1. Check that your `.env` file exists and has the correct key names:
   - `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` (for LLM)
   - `SERPER_API_KEY` (for web search tools - get free key at serper.dev)
2. Verify your API keys are valid
3. For local models, check CrewAI documentation for setup
4. Make sure to restart your terminal/IDE after adding keys to `.env`

### Issue: Import Errors

**Solution:**
1. Ensure you're in the project directory
2. Make sure all dependencies are installed: `pip install -r requirements.txt`
3. This includes: `crewai[anthropic]`, `crewai-tools`, `pydantic`, `python-dotenv`
4. Try: `pip install --upgrade "crewai[anthropic]" crewai-tools`

### Issue: "Anthropic native provider not available"

**Solution:**
1. Install CrewAI with Anthropic support: `pip install "crewai[anthropic]>=0.28.0"`
2. Or reinstall requirements: `pip install -r requirements.txt`
3. The `[anthropic]` extra installs the `anthropic` package needed for Claude models

### Issue: Python Version

**Solution:**
- CrewAI requires Python 3.8+
- Check your version: `python --version`
- If needed, install a newer Python version

## Alternative: Using Docker

If you prefer Docker:

```bash
# Build the image
docker build -t crewai-workshop .

# Run an example
docker run -it --env-file .env crewai-workshop python examples/01_basic_agent.py
```

## Getting Help

- Check the [CrewAI Documentation](https://docs.crewai.com/)
- Join the [CrewAI Discord](https://discord.gg/crewai)
- Review the examples in this repository
- Get Serper API key: [serper.dev](https://serper.dev) (free tier available)

## Next Steps

Once setup is complete:
1. Read the README.md for an overview
2. Follow the WORKSHOP_GUIDE.md for step-by-step instructions
3. Run the examples in order: 01 → 02 → 03
4. Experiment with your own agents and tasks!


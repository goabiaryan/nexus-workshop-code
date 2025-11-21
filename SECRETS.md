# 🔐 Secrets Management Guide

This guide explains how to securely manage your API keys for the CrewAI workshop.

## Quick Start

1. **Run the setup script:**
   ```bash
   # macOS/Linux
   ./setup_secrets.sh
   
   # Windows (PowerShell)
   .\setup_secrets.ps1
   ```

2. **Edit `.env` file** with your actual API keys

3. **Done!** Your secrets are now configured securely.

## Security Best Practices

### ✅ DO:
- ✅ Use `.env` file for local development (already in `.gitignore`)
- ✅ Keep your `.env` file local and never commit it
- ✅ Use `.env.example` as a template (safe to commit)
- ✅ Rotate keys if they're accidentally exposed
- ✅ Use environment-specific keys (dev/staging/prod)

### ❌ DON'T:
- ❌ Commit `.env` file to version control
- ❌ Share API keys in chat, email, or screenshots
- ❌ Hardcode keys in your source code
- ❌ Use production keys in development

## Required API Keys

### 1. SERPER_API_KEY (Required)
**Purpose:** Web search tool for research agents

**How to get:**
1. Visit [serper.dev](https://serper.dev)
2. Sign up for free account
3. Get your API key from dashboard
4. Free tier: 2,500 searches/month

**Add to `.env`:**
```bash
SERPER_API_KEY=your-actual-key-here
```

### 2. LLM Provider Key (Choose One)

#### Option A: OpenAI (GPT models)
**Purpose:** LLM for agents

**How to get:**
1. Visit [platform.openai.com](https://platform.openai.com/api-keys)
2. Sign up/login
3. Create new API key
4. Copy key (shown only once!)

**Add to `.env`:**
```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

#### Option B: Anthropic (Claude models)
**Purpose:** LLM for agents (used in examples)

**How to get:**
1. Visit [console.anthropic.com](https://console.anthropic.com/)
2. Sign up/login
3. Create API key
4. Copy key

**Add to `.env`:**
```bash
ANTHROPIC_API_KEY=your-actual-key-here
```

## File Structure

```
packt-event/
├── .env.example          # Template (safe to commit)
├── .env                  # Your actual keys (NEVER commit)
├── setup_secrets.sh      # Setup script (macOS/Linux)
├── setup_secrets.ps1     # Setup script (Windows)
└── SECRETS.md            # This file
```

## Verifying Your Setup

After setting up your `.env` file, verify it works:

```bash
# Check that .env exists
ls -la .env

# Verify keys are loaded (should NOT show placeholder values)
grep -v "^#" .env | grep -v "^$"
```

Then run an example:
```bash
python examples/01_basic_agent.py
```

If you see errors about missing API keys, check:
1. `.env` file exists
2. Keys are correctly named (no typos)
3. Keys are not placeholder values
4. You've restarted your terminal/IDE after creating `.env`

## Troubleshooting

### Issue: "API key not found"
**Solution:**
- Check `.env` file exists in project root
- Verify key names match exactly (case-sensitive)
- Ensure no extra spaces or quotes around values
- Restart terminal/IDE after creating `.env`

### Issue: "Invalid API key"
**Solution:**
- Verify key is correct (copy-paste, no extra characters)
- Check key hasn't expired or been revoked
- For Serper: Ensure you've activated your account

### Issue: Keys not loading
**Solution:**
- Make sure `python-dotenv` is installed: `pip install python-dotenv`
- Verify `load_dotenv()` is called in your scripts
- Check `.env` file is in the same directory as your script

## Production Deployment

For production, use proper secrets management:

- **Cloud platforms:** Use their secrets managers (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager)
- **CI/CD:** Use environment variables or secrets in your pipeline
- **Docker:** Use Docker secrets or environment variables
- **Kubernetes:** Use Kubernetes secrets

Never hardcode keys or commit them to repositories!

## Need Help?

- Check [CrewAI Documentation](https://docs.crewai.com/) for API setup
- Join [CrewAI Discord](https://discord.gg/crewai) for community support
- Review the examples in this repository

## Key Rotation

If you suspect a key is compromised:

1. **Immediately revoke** the key in your provider's dashboard
2. **Generate a new key**
3. **Update your `.env` file** with the new key
4. **Test** that everything still works
5. **Review** your git history to ensure old key wasn't committed

Remember: Prevention is better than cure - never commit secrets!


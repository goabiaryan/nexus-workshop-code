# Ollama Setup Guide for Qwen 2.5

This guide will help you set up Ollama to run Qwen 2.5 locally (free, no API costs).

## Quick Setup

### Step 0: Install LiteLLM (Required for Ollama support)

```bash
pip install litellm>=1.0.0
```

Or install from requirements:
```bash
pip install -r requirements.txt
```

### Step 1: Install Ollama

**macOS:**
```bash
# Download and install from https://ollama.ai
# Or use Homebrew:
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download the installer from [ollama.ai](https://ollama.ai)

### Step 2: Start Ollama

```bash
# Ollama should start automatically, but if not:
ollama serve
```

**Verify Ollama is running:**
```bash
curl http://localhost:11434
```

You should see a response. If not, make sure Ollama is running.

### Step 3: Pull Qwen 2.5 Model

```bash
ollama pull qwen2.5:7b
```

This will download the Qwen 2.5 7B model (about 4.4GB). The first time may take a few minutes.

### Step 4: Verify Installation

```bash
ollama list
```

You should see `qwen2.5:7b` in the list.

### Step 5: Test the Model

```bash
ollama run qwen2.5:7b "Hello, how are you?"
```

If you get a response, Ollama is working correctly!

## Alternative: Other Qwen Models

You can also use other Qwen variants:

```bash
# Smaller model (faster, less memory)
ollama pull qwen2.5:3b

# Larger model (better quality, more memory)
ollama pull qwen2.5:14b

# Or the original Qwen 2.1
ollama pull qwen2.1:7b
```

Then update the model name in the examples:
- `QWEN_MODEL = "ollama/qwen2.5:3b"` (for 3B model)
- `QWEN_MODEL = "ollama/qwen2.5:14b"` (for 14B model)

## Using Hugging Face Instead

If you prefer to use Hugging Face's Inference API instead of Ollama:

1. Get a Hugging Face API key from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

2. Add to your `.env` file:
```
HUGGINGFACE_API_KEY=your-key-here
```

3. Update the model in examples:
```python
QWEN_MODEL = "huggingface/Qwen/Qwen2.5-7B-Instruct"
```

## Troubleshooting

### Issue: "Connection refused" or "Cannot connect to Ollama"

**Solution:**
1. Make sure Ollama is running: `ollama serve`
2. Check if it's running on the default port: `curl http://localhost:11434`
3. On some systems, you may need to set: `OLLAMA_BASE_URL=http://localhost:11434`

### Issue: Model not found

**Solution:**
1. Make sure you've pulled the model: `ollama pull qwen2.5:7b`
2. Verify it's installed: `ollama list`
3. Try running it directly: `ollama run qwen2.5:7b`

### Issue: Out of memory

**Solution:**
1. Use a smaller model: `ollama pull qwen2.5:3b`
2. Close other applications
3. On macOS, increase available memory

### Issue: Slow performance

**Solution:**
1. Use a smaller model (3B instead of 7B)
2. Make sure you have enough RAM (7B needs ~8GB, 3B needs ~4GB)
3. Close other applications
4. Consider using GPU acceleration (see Ollama docs)

## Benefits of Using Ollama

✅ **Free** - No API costs
✅ **Local** - Your data stays on your machine
✅ **Fast** - No network latency
✅ **Private** - No data sent to external services
✅ **Offline** - Works without internet (after initial download)

## Next Steps

Once Ollama is set up, you can run the examples:

```bash
python examples/01_basic_agent.py
```

The examples are already configured to use `ollama/qwen2.5:7b`!


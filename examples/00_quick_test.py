"""Super simple test - just verify Ollama is working"""
import requests
import json

print("🧪 Testing Ollama connection...")

# Test 1: Check if Ollama is running
try:
    response = requests.get("http://localhost:11434/api/tags", timeout=2)
    if response.status_code == 200:
        models = response.json().get("models", [])
        model_names = [m["name"] for m in models]
        print(f"✅ Ollama is running")
        print(f"   Available models: {', '.join(model_names)}")
    else:
        print(f"❌ Ollama returned status {response.status_code}")
        exit(1)
except Exception as e:
    print(f"❌ Cannot connect to Ollama: {e}")
    print("   Make sure Ollama is running: ollama serve")
    exit(1)

# Test 2: Quick generation test
print("\n🧪 Testing model generation...")
try:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:7b",
            "prompt": "Say 'Hello, CrewAI!' in one sentence.",
            "stream": False
        },
        timeout=30
    )
    if response.status_code == 200:
        result = response.json()
        answer = result.get("response", "").strip()
        print(f"✅ Model responded:")
        print(f"   {answer}")
    else:
        print(f"❌ Generation failed: {response.status_code}")
        print(f"   {response.text}")
except Exception as e:
    print(f"❌ Generation error: {e}")
    exit(1)

print("\n✅ All tests passed! CrewAI setup is working.")
print("   You can now run the full examples.")

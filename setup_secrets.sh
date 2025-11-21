#!/bin/bash

# Setup script for creating .env file from template
# This script helps you set up your API keys securely

echo "🔐 CrewAI Workshop - Secrets Setup"
echo "=================================="
echo ""

# Check if .env already exists
if [ -f .env ]; then
    echo "⚠️  .env file already exists!"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Keeping existing .env file. Exiting."
        exit 0
    fi
fi

# Copy template
if [ ! -f .env.example ]; then
    echo "❌ Error: .env.example file not found!"
    exit 1
fi

cp .env.example .env
echo "✅ Created .env file from template"
echo ""

# Instructions
echo "📝 Next steps:"
echo "1. Open .env in your editor"
echo "2. Replace the placeholder values with your actual API keys:"
echo ""
echo "   Required:"
echo "   - SERPER_API_KEY (get free key at https://serper.dev)"
echo ""
echo "   Choose one:"
echo "   - OPENAI_API_KEY (get at https://platform.openai.com/api-keys)"
echo "   - ANTHROPIC_API_KEY (get at https://console.anthropic.com/)"
echo ""
echo "3. Save the file"
echo ""
echo "🔒 Your .env file is already in .gitignore and won't be committed"
echo ""

# Check if keys are still placeholders
if grep -q "your-.*-api-key-here" .env; then
    echo "⚠️  Remember to replace the placeholder values with your actual keys!"
else
    echo "✅ Looks like you've already added your keys!"
fi


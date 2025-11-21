# PowerShell script for Windows users
# Setup script for creating .env file from template

Write-Host "🔐 CrewAI Workshop - Secrets Setup" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Check if .env already exists
if (Test-Path .env) {
    $response = Read-Host "⚠️  .env file already exists! Overwrite? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Host "Keeping existing .env file. Exiting."
        exit 0
    }
}

# Copy template
if (-not (Test-Path .env.example)) {
    Write-Host "❌ Error: .env.example file not found!" -ForegroundColor Red
    exit 1
}

Copy-Item .env.example .env
Write-Host "✅ Created .env file from template" -ForegroundColor Green
Write-Host ""

# Instructions
Write-Host "📝 Next steps:" -ForegroundColor Yellow
Write-Host "1. Open .env in your editor"
Write-Host "2. Replace the placeholder values with your actual API keys:"
Write-Host ""
Write-Host "   Required:"
Write-Host "   - SERPER_API_KEY (get free key at https://serper.dev)"
Write-Host ""
Write-Host "   Choose one:"
Write-Host "   - OPENAI_API_KEY (get at https://platform.openai.com/api-keys)"
Write-Host "   - ANTHROPIC_API_KEY (get at https://console.anthropic.com/)"
Write-Host ""
Write-Host "3. Save the file"
Write-Host ""
Write-Host "🔒 Your .env file is already in .gitignore and won't be committed" -ForegroundColor Green
Write-Host ""

# Check if keys are still placeholders
$content = Get-Content .env -Raw
if ($content -match "your-.*-api-key-here") {
    Write-Host "⚠️  Remember to replace the placeholder values with your actual keys!" -ForegroundColor Yellow
} else {
    Write-Host "✅ Looks like you've already added your keys!" -ForegroundColor Green
}


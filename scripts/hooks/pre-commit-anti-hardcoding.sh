#\!/bin/bash
# Pre-commit hook to detect hardcoded values

echo "🔍 Checking for hardcoded values..."

# TODO: Comprehensive patterns for hardcoded value detection
# TODO: Add domain-specific hardcoded pattern detection
# TODO: Include Azure service configuration hardcoding patterns
# TODO: Add machine learning parameter hardcoding detection
# TODO: Include API endpoint and credential hardcoding patterns
HARDCODED_PATTERNS=(
    "similarity_threshold\s*=\s*[0-9]"
    "processing_delay\s*=\s*[0-9]"
    "synthesis_weight\s*=\s*[0-9]"
    "temperature\s*=\s*[0-9]"
    "max_tokens\s*=\s*[0-9]"
    "embedding_dimension\s*=\s*1536"
    "cache_ttl\s*=\s*[0-9]"
    "timeout\s*=\s*[0-9]"
    "batch_size\s*=\s*[0-9]"
    "confidence_threshold\s*=\s*[0-9]"
    "mock_implementation"
    "TODO.*config"
    "hardcoded"
    "placeholder"
    "openai\.azure\.com"
    "api-version.*2024"
)

VIOLATIONS_FOUND=0

for pattern in "${HARDCODED_PATTERNS[@]}"; do
    if git diff --cached --name-only | xargs grep -l "$pattern" 2>/dev/null; then
        echo "❌ HARDCODED VALUE DETECTED: $pattern"
        git diff --cached --name-only | xargs grep -n "$pattern"
        VIOLATIONS_FOUND=1
    fi
done

if [ $VIOLATIONS_FOUND -eq 1 ]; then
    echo ""
    echo "🚨 COMMIT BLOCKED: Hardcoded values detected\!"
    echo "   This system uses intelligent, data-driven configuration."
    echo "   Please use the workflow bridge system instead."
    echo ""
    echo "   To bypass for development: git commit --no-verify"
    exit 1
fi

echo "✅ No hardcoded values detected. Commit allowed."

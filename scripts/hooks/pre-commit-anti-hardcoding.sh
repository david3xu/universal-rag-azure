#!/bin/bash
# Pre-commit hook to detect hardcoded values and data type violations

echo "🔍 Checking for hardcoded values and data type violations..."

VIOLATIONS_FOUND=0

# Determine scope: staged files (pre-commit) or all files (test mode)
if [ "$1" = "--test" ]; then
    echo "🧪 TEST MODE: Checking entire codebase..."
    STAGED_FILES=$(find /workspace/universal-rag-azure -name "*.py" -not -path "*/models/*" -not -path "*/docs/*")
    SCOPE_DESC="entire codebase"
else
    echo "🔍 PRE-COMMIT MODE: Checking staged files..."
    STAGED_FILES=$(git diff --cached --name-only --diff-filter=AM | grep "\.py$" || true)
    SCOPE_DESC="staged files"
fi

# Check for data type violations
echo "🔍 Checking for centralized data type violations in $SCOPE_DESC..."

if [ -n "$STAGED_FILES" ]; then
    # Check for function return type violations
    RETURN_TYPE_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n "-> Dict\[str, Any\]:" 2>/dev/null || true)
    if [ -n "$RETURN_TYPE_VIOLATIONS" ]; then
        echo "❌ FUNCTION RETURN TYPE VIOLATION: -> Dict[str, Any]"
        echo "   Use centralized models from models/ directory instead"
        echo "   Violations found:"
        echo "$RETURN_TYPE_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for local BaseModel definitions (outside models/ directory)
    LOCAL_MODELS=$(echo "$STAGED_FILES" | xargs grep -n "^[^#]*class.*BaseModel" 2>/dev/null | grep -v "# TODO" | grep -v "models/" || true)
    if [ -n "$LOCAL_MODELS" ]; then
        echo "❌ LOCAL MODEL DEFINITION VIOLATION: class.*BaseModel"
        echo "   Define models in models/ directory instead"
        echo "   Violations found:"
        echo "$LOCAL_MODELS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for hardcoded value patterns
    echo "🔍 Checking for hardcoded values in $SCOPE_DESC..."
    
    # Check for hardcoded numeric values (decimal numbers)
    NUMERIC_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n -E "[^a-zA-Z0-9_](0\.[0-9]+|[1-9]\.[0-9]+)" 2>/dev/null | grep -v "# TODO" | grep -v "version" | grep -v "isoformat" | grep -v "float" || true)
    if [ -n "$NUMERIC_VIOLATIONS" ]; then
        echo "❌ HARDCODED NUMERIC VALUES DETECTED"
        echo "   Use configuration system instead of hardcoded decimals"
        echo "   Violations found:"
        echo "$NUMERIC_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for hardcoded integer bounds (max, min functions with numbers)
    BOUNDS_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n -E "(max|min)\([0-9]+," 2>/dev/null | grep -v "# TODO" || true)
    if [ -n "$BOUNDS_VIOLATIONS" ]; then
        echo "❌ HARDCODED BOUNDS/LIMITS DETECTED"
        echo "   Use centralized bounds from configuration"
        echo "   Violations found:"
        echo "$BOUNDS_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for hardcoded temperature values
    TEMP_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n "temperature.*=.*[0-9]" 2>/dev/null | grep -v "# TODO" || true)
    if [ -n "$TEMP_VIOLATIONS" ]; then
        echo "❌ HARDCODED TEMPERATURE DETECTED"
        echo "   Use configuration system instead"
        echo "   Violations found:"
        echo "$TEMP_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for hardcoded max_tokens values
    TOKENS_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n "max_tokens.*=.*[0-9]" 2>/dev/null | grep -v "# TODO" || true)
    if [ -n "$TOKENS_VIOLATIONS" ]; then
        echo "❌ HARDCODED MAX_TOKENS DETECTED"
        echo "   Use configuration system instead"
        echo "   Violations found:"
        echo "$TOKENS_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for hardcoded list literals (especially stopwords)
    LIST_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n "\[.*'.*',.*'.*'\]" 2>/dev/null | grep -v "# TODO" | grep -v "prompt" || true)
    if [ -n "$LIST_VIOLATIONS" ]; then
        echo "❌ HARDCODED LIST VALUES DETECTED"
        echo "   Use centralized configuration for lists (stopwords, etc.)"
        echo "   Violations found:"
        echo "$LIST_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for hardcoded API versions
    API_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n "api-version.*2024" 2>/dev/null || true)
    if [ -n "$API_VIOLATIONS" ]; then
        echo "❌ HARDCODED API VERSION DETECTED"
        echo "   Use configuration system instead"
        echo "   Violations found:"
        echo "$API_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for enum value implementations
    ENUM_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n "=.*[\"'][a-zA-Z_]*[\"']" 2>/dev/null | grep -E "(TECHNICAL|CREATIVE|ANALYTICAL)" | grep -v "# TODO" || true)
    if [ -n "$ENUM_VIOLATIONS" ]; then
        echo "❌ HARDCODED ENUM VALUES DETECTED"
        echo "   Use TODO-driven implementation instead"
        echo "   Violations found:"
        echo "$ENUM_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for hardcoded prompts (should be centralized)
    PROMPT_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n -E "\"role\".*\"system\"" 2>/dev/null | grep -v "# TODO" || true)
    if [ -n "$PROMPT_VIOLATIONS" ]; then
        echo "❌ HARDCODED PROMPT DETECTED"
        echo "   Use centralized prompt templates from prompt_flows/ directory"
        echo "   Violations found:"
        echo "$PROMPT_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
    # Check for hardcoded content strings in prompts
    CONTENT_VIOLATIONS=$(echo "$STAGED_FILES" | xargs grep -n -E "\"content\".*\"You are" 2>/dev/null | grep -v "# TODO" || true)
    if [ -n "$CONTENT_VIOLATIONS" ]; then
        echo "❌ HARDCODED PROMPT CONTENT DETECTED"
        echo "   Use centralized jinja2 templates from prompt_flows/"
        echo "   Violations found:"
        echo "$CONTENT_VIOLATIONS" | sed 's/^/     /'
        VIOLATIONS_FOUND=1
    fi
    
else
    echo "   No Python files to check in $SCOPE_DESC"
fi

# Final result
if [ $VIOLATIONS_FOUND -eq 1 ]; then
    echo ""
    echo "🚨 COMMIT BLOCKED: Violations detected!"
    echo "   This system uses intelligent, data-driven configuration."
    echo "   Please use the centralized models and configuration system instead."
    echo ""
    echo "   To bypass for development: git commit --no-verify"
    exit 1
fi

echo "✅ No violations detected. Commit allowed."
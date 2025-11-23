#!/bin/bash
# Script to verify gzip compression is working on solarityai.com

echo "🔍 Verifying Gzip Compression for Solarity AI"
echo "=============================================="
echo ""

DOMAIN="solarityai.com"

# Check if domain is provided
if [ ! -z "$1" ]; then
    DOMAIN="$1"
fi

echo "Testing domain: $DOMAIN"
echo ""

# Function to check gzip
check_gzip() {
    local url="$1"
    local file_type="$2"
    
    echo "📄 Checking: $file_type"
    echo "URL: $url"
    
    # Get response with headers
    response=$(curl -sI -H "Accept-Encoding: gzip, deflate" "$url")
    
    # Check for Content-Encoding header
    if echo "$response" | grep -qi "Content-Encoding: gzip"; then
        echo "✅ GZIP: ENABLED"
        
        # Get Content-Length if available
        content_length=$(echo "$response" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r')
        if [ ! -z "$content_length" ]; then
            echo "   Compressed size: $content_length bytes"
        fi
        
        # Get uncompressed size for comparison
        uncompressed=$(curl -s "$url" | wc -c)
        if [ ! -z "$content_length" ] && [ "$uncompressed" -gt 0 ]; then
            ratio=$(echo "scale=1; ($content_length * 100) / $uncompressed" | bc)
            echo "   Compression ratio: ~${ratio}% of original"
        fi
    else
        echo "❌ GZIP: NOT ENABLED or not compressed"
    fi
    
    # Check for Vary header (indicates compression support)
    if echo "$response" | grep -qi "Vary:.*Accept-Encoding"; then
        echo "✅ Vary header: Present (good for caching)"
    fi
    
    echo ""
}

# Test different file types
echo "1️⃣ Testing HTML file..."
check_gzip "https://$DOMAIN/index.html" "HTML"

echo "2️⃣ Testing CSS file..."
check_gzip "https://$DOMAIN/assets/css/ud-styles.css" "CSS"

echo "3️⃣ Testing JavaScript file..."
check_gzip "https://$DOMAIN/assets/js/main.js" "JavaScript"

echo "4️⃣ Testing JSON file (if exists)..."
check_gzip "https://$DOMAIN/assets/data/testimonials.json" "JSON"

echo ""
echo "📊 Summary:"
echo "If you see ✅ GZIP: ENABLED for all files, compression is working!"
echo ""
echo "💡 Tip: You can also check in browser DevTools:"
echo "   - Open Network tab"
echo "   - Look for 'Content-Encoding: gzip' in response headers"
echo "   - Compare 'Size' vs 'Transferred' columns"


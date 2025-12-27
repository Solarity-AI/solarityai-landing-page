#!/bin/bash
# Quick script to reload nginx via Ansible

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔄 Reloading Nginx Configuration..."
echo ""

# Run the Ansible playbook
ansible-playbook reload-nginx.yml

echo ""
echo "✅ Done! Nginx should now be using the updated configuration."
echo ""
echo "💡 To verify gzip is working, run:"
echo "   cd .. && ./verify-gzip.sh"


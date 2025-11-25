#!/bin/bash
# Script to download partner logos
# Run this from the solarityai-landing-page directory

set -e

BRANDS_DIR="assets/images/brands"
mkdir -p "$BRANDS_DIR"

echo "Downloading partner logos..."

# Ticaret Bakanlığı - Using CDN logo
echo "Downloading Ticaret Bakanlığı logo..."
curl -L "https://cdn.ticaret.gov.tr/images/logo/256px.png" -o "$BRANDS_DIR/ticaret-bakanligi.png" 2>/dev/null || echo "Failed to download Ticaret Bakanlığı logo"

# Novartis - Official brand assets (using a common logo URL pattern)
echo "Downloading Novartis logo..."
curl -L "https://www.novartis.com/sites/www.novartis.com/files/novartis-logo.svg" -o "$BRANDS_DIR/novartis.svg" 2>/dev/null || \
curl -L "https://logos-world.net/wp-content/uploads/2020/06/Novartis-Logo.png" -o "$BRANDS_DIR/novartis.png" 2>/dev/null || echo "Failed to download Novartis logo"

# Siemens - Official brand assets
echo "Downloading Siemens logo..."
curl -L "https://assets.new.siemens.com/siemens/assets/api/uuid:8c0b0e0e-0e0e-0e0e-0e0e-0e0e0e0e0e0e/width:1120/quality:high/siemens-logo.svg" -o "$BRANDS_DIR/siemens.svg" 2>/dev/null || \
curl -L "https://logos-world.net/wp-content/uploads/2020/04/Siemens-Logo.png" -o "$BRANDS_DIR/siemens.png" 2>/dev/null || echo "Failed to download Siemens logo"

# TÜBİTAK - Official logo
echo "Downloading TÜBİTAK logo..."
curl -L "https://www.tubitak.gov.tr/sites/default/files/tubitak_logo.png" -o "$BRANDS_DIR/tubitak.png" 2>/dev/null || \
curl -L "https://www.tubitak.gov.tr/sites/default/files/logo/tubitak_logo.svg" -o "$BRANDS_DIR/tubitak.svg" 2>/dev/null || echo "Failed to download TÜBİTAK logo"

echo ""
echo "Note: Some logos may need to be downloaded manually:"
echo "  - ISIS: Check https://www.isis.com.tr/"
echo "  - KPM Labs: Check https://www.kpmlabs.com/"
echo "  - Everva.com.tr: Check https://www.everva.com.tr/"
echo "  - Techsign: Check https://www.techsign.com.tr/"
echo ""
echo "Download complete! Check $BRANDS_DIR for downloaded logos."


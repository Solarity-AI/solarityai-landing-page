# SEO Setup for SolarityAI Landing Page

This document outlines the SEO optimizations added to help Google index the landing page.

## Files Created

### 1. `robots.txt`
- Located at the root of the website
- Allows all search engines to crawl the site
- Points to the sitemap location
- Blocks admin/private directories

### 2. `sitemap.xml`
- Contains all important pages of the website
- Includes priority and change frequency for each page
- Located at: `https://solarityai.com/sitemap.xml`

## HTML Enhancements

### Added to `index.html`:

1. **Canonical URL**: Prevents duplicate content issues
   ```html
   <link rel="canonical" href="https://solarityai.com/" />
   ```

2. **Sitemap Reference**: Helps search engines find the sitemap
   ```html
   <link rel="sitemap" type="application/xml" href="/sitemap.xml" />
   ```

3. **Structured Data (JSON-LD)**: 
   - WebSite schema for better search understanding
   - Organization schema for business information

4. **Updated Meta Tags**: 
   - Fixed Open Graph URLs to use correct domain
   - Fixed Twitter Card URLs to use correct domain

## Next Steps for Google Indexing

1. **Submit to Google Search Console**:
   - Go to https://search.google.com/search-console
   - Add property: `https://solarityai.com` (and `https://www.solarityai.com` if needed)
   - Verify ownership (DNS, HTML file, or meta tag)
   - Submit sitemap: `https://solarityai.com/sitemap.xml`

2. **Request Indexing**:
   - After verification, use "URL Inspection" tool
   - Request indexing for the homepage and key pages

3. **Monitor**:
   - Check indexing status in Search Console
   - Monitor search performance and impressions

## Testing

After deployment, verify:
- `https://solarityai.com/robots.txt` is accessible
- `https://solarityai.com/sitemap.xml` is accessible
- Structured data is valid (use Google's Rich Results Test)
- Canonical URLs are correct

## Notes

- Update `lastmod` dates in `sitemap.xml` when pages are updated
- Keep sitemap.xml synchronized with actual pages
- Monitor Search Console for crawl errors


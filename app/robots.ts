import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: ["/admin/", "/private/", "/api/"],
      },
      // Block AI training crawlers
      {
        userAgent: ["GPTBot", "Google-Extended", "CCBot", "anthropic-ai", "Claude-Web", "Omgilibot", "FacebookBot", "PerplexityBot"],
        disallow: "/",
      },
    ],
    sitemap: "https://solarityai.com/sitemap.xml",
  };
}

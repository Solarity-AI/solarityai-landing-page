import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",
  images: {
    unoptimized: true,
    localPatterns: [
      {
        pathname: "/assets/**",
        search: "",
      },
      {
        pathname: "/assets/**",
        search: "?v=20260207",
      },
    ],
  },
};

export default nextConfig;

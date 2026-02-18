import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
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

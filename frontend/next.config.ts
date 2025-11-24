import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Explicitly set the project root to avoid multiple lockfile warnings
  outputFileTracingRoot: '/home/xsolai/hdd/Projects/cameleon-poc-showcase',
  
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'lh3.googleusercontent.com',
        pathname: '/aida-public/**',
      },
    ],
  },
  
  // Environment variables
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
  },
};

export default nextConfig;


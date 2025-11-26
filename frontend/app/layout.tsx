import type { Metadata } from "next";
import "./globals.css";
import { ErrorBoundary } from "./components/common";

export const metadata: Metadata = {
  title: "Cameleon - AI Fashion Stylist",
  description: "Your personal AI-powered wardrobe and outfit generator",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="overflow-hidden h-screen" suppressHydrationWarning>
      <head>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" />
      </head>
      <body className="font-display soft-gradient text-text-light dark:text-text-dark overflow-hidden h-screen" suppressHydrationWarning>
        <ErrorBoundary>
          {children}
        </ErrorBoundary>
      </body>
    </html>
  );
}


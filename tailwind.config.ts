import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        primary: "#e8ba30",
        "background-light": "#f8f7f6",
        "background-dark": "#211d11",
        "text-light": "#1b180e",
        "text-dark": "#f3f0e7",
        "text-muted-light": "#97854e",
        "text-muted-dark": "#a19983",
        "card-light": "#fcfbf8",
        "card-dark": "#2a261a",
        "border-light": "#f3f0e7",
        "border-dark": "#3b3421",
        "placeholder-light": "#97854e",
        "placeholder-dark": "#8a7d55",
        "charcoal": "#36454F",
        "taupe": "#96897B",
        "off-white": "#FAF9F6",
      },
      fontFamily: {
        display: ["Manrope", "sans-serif"],
      },
      borderRadius: {
        DEFAULT: "0.5rem",
        lg: "1rem",
        xl: "1.5rem",
        full: "9999px",
      },
      scale: {
        '80': '0.8',
        '85': '0.85',
        '90': '0.9',
        '95': '0.95',
      },
    },
  },
  plugins: [],
};
export default config;


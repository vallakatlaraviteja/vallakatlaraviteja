import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-inter)", "system-ui", "sans-serif"],
      },
      colors: {
        ink: {
          50: "#f7f7f8",
          100: "#eeeef0",
          900: "#0b0b0c",
          950: "#050506",
        },
        accent: {
          500: "#5b8def",
          600: "#3b71e8",
        },
      },
    },
  },
  plugins: [],
};

export default config;

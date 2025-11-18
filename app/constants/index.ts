// Application-wide constants

export const BODY_TYPES = [
  { id: "Triangle", label: "Triangle", icon: "change_history", transform: "" },
  { id: "Inverted Triangle", label: "Inverted Triangle", icon: "change_history", transform: "-scale-y-100" },
  { id: "Round", label: "Round", icon: "circle", transform: "" },
  { id: "Rectangle", label: "Rectangle", icon: "crop_square", transform: "" },
  { id: "Trapezium", label: "Trapezium", icon: "hexagon", transform: "" },
  { id: "Not Sure", label: "Not Sure", icon: "help", transform: "" },
] as const;

export const HEIGHT_RANGES = ["Petite", "Regular", "Tall"] as const;

export const VOLUME_RANGES = ["Lean", "Mid", "Plus"] as const;

export const STYLE_CATEGORIES = [
  "Smart Casual",
  "Summer Date",
  "Dinner Out",
  "Office Look",
] as const;

export const STYLE_PREFERENCES = [
  "Smart Casual",
  "Formal",
  "Streetwear",
  "Bohemian",
  "Minimalist",
  "Classic",
] as const;

export const COLOR_PALETTES = [
  "Neutral & Earth Tones",
  "Bold & Bright",
  "Pastels",
  "Monochrome",
  "Jewel Tones",
] as const;

export const BUDGET_RANGES = [
  "Budget-Friendly",
  "Mid-Range",
  "Premium",
  "Luxury",
] as const;

// Default user profile picture
export const DEFAULT_PROFILE_PICTURE = "https://lh3.googleusercontent.com/aida-public/AB6AXuCgyx43deMJXdxwSV6CSDmpDiAqkKPoxbKEJahnnRBIcoMDjZ_DxDeUguHlJng7r2a3wGrxReHgAKaPLnUsF7Hb41DduomvjzSZf91ThUQFkoMvUPc8FBHVYYsclK3JgGsK6ded4p1ll6t5bkpNOWpqDSXNd5r5_TZKBrwIbvXIa0Nx1kq3z3GA_btD7douPDKd0k-HFTK04r-IC0R3H5ziQWXnZjutKvCRces8EaamLKXL9zeh-evPTSJXvof90f5jSmYyEeVzv0U";

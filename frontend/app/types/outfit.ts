export interface OutfitItem {
  id: number;
  type: string;
  image: string;
  name: string;
  brand: string;
}

export interface Outfit {
  id: string;
  title: string;
  vibe: string;
  items: OutfitItem[];
  generatedAt: Date;
  reasoning?: string;
  style_tips?: string[];
  color_harmony?: string;
}


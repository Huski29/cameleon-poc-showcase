// Outfit and outfit generation types

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
}


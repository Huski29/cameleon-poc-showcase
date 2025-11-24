// Wardrobe and clothing item types

export type ClothingCategory = "tops" | "bottoms" | "shoes" | "accessories";

export interface WardrobeItem {
  id: number;
  category: ClothingCategory;
  image: string;
  alt: string;
  title: string;
  description: string;
}


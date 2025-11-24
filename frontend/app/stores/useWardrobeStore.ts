'use client';

import { create } from 'zustand';
import type { WardrobeItem, ClothingCategory } from '../types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface WardrobeState {
  items: WardrobeItem[];
  isLoading: boolean;
  error: string | null;
  fetchItems: () => Promise<void>;
  addItem: (item: Omit<WardrobeItem, 'id'>) => Promise<void>;
  removeItem: (id: number) => Promise<void>;
  getItemsByCategory: (category: ClothingCategory) => WardrobeItem[];
}

export const useWardrobeStore = create<WardrobeState>()((set, get) => ({
  items: [],
  isLoading: false,
  error: null,
  
  fetchItems: async () => {
    set({ isLoading: true, error: null });
    try {
      const response = await fetch(`${API_URL}/api/v1/wardrobe`);
      if (!response.ok) throw new Error('Failed to fetch wardrobe items');
      
      const data = await response.json();
      
      // Transform backend format to frontend format
      const items: WardrobeItem[] = data.map((item: any) => ({
        id: item.id,
        category: item.category,
        image: item.image,
        alt: item.alt,
        title: item.title,
        description: item.description,
      }));
      
      set({ items, isLoading: false });
    } catch (error) {
      set({ error: (error as Error).message, isLoading: false });
    }
  },
  
  addItem: async (item) => {
    set({ isLoading: true, error: null });
    try {
      const response = await fetch(`${API_URL}/api/v1/wardrobe`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(item),
      });
      
      if (!response.ok) throw new Error('Failed to add item');
      
      const data = await response.json();
      const newItem: WardrobeItem = {
        id: data.id,
        category: data.category,
        image: data.image,
        alt: data.alt,
        title: data.title,
        description: data.description,
      };
      
      set((state) => ({ 
        items: [...state.items, newItem],
        isLoading: false,
      }));
    } catch (error) {
      set({ error: (error as Error).message, isLoading: false });
    }
  },
  
  removeItem: async (id) => {
    set({ isLoading: true, error: null });
    try {
      const response = await fetch(`${API_URL}/api/v1/wardrobe/${id}`, {
        method: 'DELETE',
      });
      
      if (!response.ok) throw new Error('Failed to remove item');
      
      set((state) => ({ 
        items: state.items.filter(i => i.id !== id),
        isLoading: false,
      }));
    } catch (error) {
      set({ error: (error as Error).message, isLoading: false });
    }
  },
  
  getItemsByCategory: (category) => 
    get().items.filter(i => i.category === category),
}));


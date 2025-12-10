'use client';

import { create } from 'zustand';
import type { WardrobeItem, ClothingCategory } from '../types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface WardrobeState {
  items: WardrobeItem[];
  categoryCounts: Record<ClothingCategory, number>; // Track total counts per category
  isLoading: boolean;
  error: string | null;
  fetchItems: (limit?: number) => Promise<void>;
  fetchItemsByCategory: (category: ClothingCategory, limit?: number, offset?: number) => Promise<WardrobeItem[]>;
  addItem: (item: Omit<WardrobeItem, 'id'>) => Promise<void>;
  removeItem: (id: number) => Promise<void>;
  getItemsByCategory: (category: ClothingCategory) => WardrobeItem[];
}

export const useWardrobeStore = create<WardrobeState>()((set, get) => ({
  items: [],
  categoryCounts: {
    tops: 0,
    bottoms: 0,
    shoes: 0,
    accessories: 0,
  },
  isLoading: false,
  error: null,
  
  fetchItems: async (limit: number = 100) => {
    set({ isLoading: true, error: null });
    try {
      // Use pagination to avoid loading all items at once
      const params = new URLSearchParams({
        limit: limit.toString(),
        offset: '0',
      });
      const response = await fetch(`${API_URL}/api/v1/wardrobe?${params}`);
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
  
  fetchItemsByCategory: async (category: ClothingCategory, limit: number = 15, offset: number = 0) => {
    try {
      const params = new URLSearchParams({
        category,
        limit: limit.toString(),
        offset: offset.toString(),
      });
      
      const response = await fetch(`${API_URL}/api/v1/wardrobe?${params}`);
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
      
      // Update items in store (append if offset > 0, replace if offset = 0)
      if (offset === 0) {
        // Replace items for this category
        set((state) => ({
          items: [
            ...state.items.filter(i => i.category !== category),
            ...items
          ],
        }));
      } else {
        // Append new items
        set((state) => ({
          items: [...state.items, ...items],
        }));
      }
      
      return items;
    } catch (error) {
      set({ error: (error as Error).message });
      return [];
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


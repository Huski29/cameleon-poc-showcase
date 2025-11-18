'use client';

import { create } from 'zustand';
import type { WardrobeItem, ClothingCategory } from '../types';
import { mockWardrobeItems } from '../lib/mock-data';

interface WardrobeState {
  items: WardrobeItem[];
  isLoading: boolean;
  addItem: (item: WardrobeItem) => void;
  removeItem: (id: number) => void;
  getItemsByCategory: (category: ClothingCategory) => WardrobeItem[];
}

export const useWardrobeStore = create<WardrobeState>()((set, get) => ({
  items: mockWardrobeItems,
  isLoading: false,
  
  addItem: (item) => set((state) => ({ 
    items: [...state.items, item] 
  })),
  
  removeItem: (id) => set((state) => ({ 
    items: state.items.filter(i => i.id !== id) 
  })),
  
  getItemsByCategory: (category) => 
    get().items.filter(i => i.category === category),
}));


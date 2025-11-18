'use client';

import { create } from 'zustand';
import type { Outfit } from '../types';
import { mockOutfits } from '../lib/mock-data';
import { generateId } from '../lib/utils';

interface OutfitState {
  currentOutfit: Outfit | null;
  savedOutfits: Outfit[];
  outfitHistory: Outfit[];
  isGenerating: boolean;
  generateOutfit: (prompt: string, preferences?: any) => Promise<void>;
  saveOutfit: (outfit: Outfit) => void;
  setCurrentOutfit: (outfit: Outfit | null) => void;
}

export const useOutfitStore = create<OutfitState>()((set, get) => ({
  currentOutfit: null,
  savedOutfits: [],
  outfitHistory: [],
  isGenerating: false,
  
  generateOutfit: async (prompt, preferences) => {
    set({ isGenerating: true });
    
    // Simulate API call with mock data
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    // Create a mock generated outfit
    const outfit: Outfit = {
      ...mockOutfits[0],
      id: generateId(),
      generatedAt: new Date(),
    };
    
    set((state) => ({ 
      currentOutfit: outfit,
      outfitHistory: [...state.outfitHistory, outfit],
      isGenerating: false 
    }));
  },
  
  saveOutfit: (outfit) => set((state) => ({
    savedOutfits: [...state.savedOutfits, outfit]
  })),
  
  setCurrentOutfit: (outfit) => set({ currentOutfit: outfit }),
}));


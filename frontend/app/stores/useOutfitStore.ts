'use client';

import { create } from 'zustand';
import type { Outfit } from '../types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface OutfitState {
  currentOutfit: Outfit | null;
  savedOutfits: Outfit[];
  outfitHistory: Outfit[];
  isGenerating: boolean;
  error: string | null;
  generateOutfit: (prompt: string, preferences?: any) => Promise<void>;
  saveOutfit: (outfitId: string) => Promise<void>;
  setCurrentOutfit: (outfit: Outfit | null) => void;
  fetchHistory: () => Promise<void>;
  fetchSaved: () => Promise<void>;
}

export const useOutfitStore = create<OutfitState>()((set, get) => ({
  currentOutfit: null,
  savedOutfits: [],
  outfitHistory: [],
  isGenerating: false,
  error: null,
  
  generateOutfit: async (prompt, preferences) => {
    set({ isGenerating: true, error: null });
    
    try {
      const response = await fetch(`${API_URL}/api/v1/outfits/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt,
          category: preferences?.category,
        }),
      });
      
      if (!response.ok) throw new Error('Failed to generate outfit');
      
      const data = await response.json();
      
      // Transform backend format to frontend format
      const outfit: Outfit = {
        id: data.id,
        title: data.title,
        vibe: data.vibe,
        items: data.items.map((item: any) => ({
          id: item.id,
          type: item.type,
          image: item.image,
          name: item.name,
          brand: item.brand,
        })),
        generatedAt: new Date(data.generated_at),
      };
      
      set((state) => ({ 
        currentOutfit: outfit,
        outfitHistory: [outfit, ...state.outfitHistory],
        isGenerating: false,
      }));
    } catch (error) {
      set({ error: (error as Error).message, isGenerating: false });
    }
  },
  
  saveOutfit: async (outfitId: string) => {
    try {
      const response = await fetch(`${API_URL}/api/v1/outfits/${outfitId}/save`, {
        method: 'POST',
      });
      
      if (!response.ok) throw new Error('Failed to save outfit');
      
      const data = await response.json();
      const outfit: Outfit = {
        id: data.id,
        title: data.title,
        vibe: data.vibe,
        items: data.items.map((item: any) => ({
          id: item.id,
          type: item.type,
          image: item.image,
          name: item.name,
          brand: item.brand,
        })),
        generatedAt: new Date(data.generated_at),
      };
      
      set((state) => ({
        savedOutfits: [...state.savedOutfits, outfit],
      }));
    } catch (error) {
      set({ error: (error as Error).message });
    }
  },
  
  setCurrentOutfit: (outfit) => set({ currentOutfit: outfit }),
  
  fetchHistory: async () => {
    try {
      const response = await fetch(`${API_URL}/api/v1/outfits/history`);
      if (!response.ok) throw new Error('Failed to fetch outfit history');
      
      const data = await response.json();
      const history: Outfit[] = data.map((outfit: any) => ({
        id: outfit.id,
        title: outfit.title,
        vibe: outfit.vibe,
        items: outfit.items.map((item: any) => ({
          id: item.id,
          type: item.type,
          image: item.image,
          name: item.name,
          brand: item.brand,
        })),
        generatedAt: new Date(outfit.generated_at),
      }));
      
      set({ outfitHistory: history });
    } catch (error) {
      set({ error: (error as Error).message });
    }
  },
  
  fetchSaved: async () => {
    try {
      const response = await fetch(`${API_URL}/api/v1/outfits`);
      if (!response.ok) throw new Error('Failed to fetch saved outfits');
      
      const data = await response.json();
      const saved: Outfit[] = data.map((outfit: any) => ({
        id: outfit.id,
        title: outfit.title,
        vibe: outfit.vibe,
        items: outfit.items.map((item: any) => ({
          id: item.id,
          type: item.type,
          image: item.image,
          name: item.name,
          brand: item.brand,
        })),
        generatedAt: new Date(outfit.generated_at),
      }));
      
      set({ savedOutfits: saved });
    } catch (error) {
      set({ error: (error as Error).message });
    }
  },
}));


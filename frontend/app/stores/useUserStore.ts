'use client';

import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { UserProfile, StyleAvatar, StylePreferences} from '../types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface UserState {
  profile: UserProfile | null;
  isLoading: boolean;
  error: string | null;
  fetchProfile: () => Promise<void>;
  setProfile: (profile: UserProfile) => void;
  updateAvatar: (avatar: Partial<StyleAvatar>) => Promise<void>;
  updatePreferences: (prefs: Partial<StylePreferences>) => Promise<void>;
  updateUser: (user: Partial<UserProfile['user']>) => Promise<void>;
  updateGender: (gender: 'male' | 'female') => Promise<void>;
}

export const useUserStore = create<UserState>()(
  persist(
    (set) => ({
      profile: null,
      isLoading: false,
      error: null,
      
      fetchProfile: async () => {
        set({ isLoading: true, error: null });
        try {
          const response = await fetch(`${API_URL}/api/v1/users/profile`);
          if (!response.ok) throw new Error('Failed to fetch profile');
          
          const data = await response.json();
          
          // Transform backend format to frontend format
          const profile: UserProfile = {
            user: {
              id: data.id,
              name: data.name,
              email: data.email,
              profilePicture: data.profile_picture || '',
              gender: data.gender || 'female',
            },
            avatar: {
              height: data.height,
              volume: data.volume,
              bodyType: data.body_type,
            },
            preferences: {
              stylePreference: data.style_preference,
              colorPalette: data.color_palette,
              budget: data.budget,
            },
          };
          
          set({ profile, isLoading: false });
        } catch (error) {
          set({ error: (error as Error).message, isLoading: false });
        }
      },
      
      setProfile: (profile) => set({ profile }),
      
      updateAvatar: async (avatar) => {
        set({ isLoading: true, error: null });
        try {
          const response = await fetch(`${API_URL}/api/v1/users/avatar`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              height: avatar.height,
              volume: avatar.volume,
              body_type: avatar.bodyType,
            }),
          });
          
          if (!response.ok) throw new Error('Failed to update avatar');
          
          const data = await response.json();
          
          set((state) => ({
            profile: state.profile ? {
              ...state.profile,
              avatar: {
                height: data.height,
                volume: data.volume,
                bodyType: data.body_type,
              },
            } : null,
            isLoading: false,
          }));
        } catch (error) {
          set({ error: (error as Error).message, isLoading: false });
        }
      },
      
      updatePreferences: async (prefs) => {
        set({ isLoading: true, error: null });
        try {
          const response = await fetch(`${API_URL}/api/v1/users/preferences`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              style_preference: prefs.stylePreference,
              color_palette: prefs.colorPalette,
              budget: prefs.budget,
            }),
          });
          
          if (!response.ok) throw new Error('Failed to update preferences');
          
          const data = await response.json();
          
          set((state) => ({
            profile: state.profile ? {
              ...state.profile,
              preferences: {
                stylePreference: data.style_preference,
                colorPalette: data.color_palette,
                budget: data.budget,
              },
            } : null,
            isLoading: false,
          }));
        } catch (error) {
          set({ error: (error as Error).message, isLoading: false });
        }
      },
      
      updateUser: async (user) => {
        set({ isLoading: true, error: null });
        try {
          const response = await fetch(`${API_URL}/api/v1/users/profile`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              name: user.name,
              email: user.email,
              profile_picture: user.profilePicture,
              gender: user.gender,
            }),
          });
          
          if (!response.ok) throw new Error('Failed to update user');
          
          const data = await response.json();
          
          set((state) => ({
            profile: state.profile ? {
              ...state.profile,
              user: {
                ...state.profile.user,
                name: data.name,
                email: data.email,
                profilePicture: data.profile_picture || '',
                gender: data.gender || 'female',
              },
            } : null,
            isLoading: false,
          }));
        } catch (error) {
          set({ error: (error as Error).message, isLoading: false });
        }
      },
      
      updateGender: async (gender) => {
        set({ isLoading: true, error: null });
        try {
          const response = await fetch(`${API_URL}/api/v1/users/profile`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ gender }),
          });
          
          if (!response.ok) throw new Error('Failed to update gender');
          
          const data = await response.json();
          
          set((state) => ({
            profile: state.profile ? {
              ...state.profile,
              user: {
                ...state.profile.user,
                gender: data.gender,
              },
            } : null,
            isLoading: false,
          }));
        } catch (error) {
          set({ error: (error as Error).message, isLoading: false });
        }
      },
    }),
    { 
      name: 'user-store',
      skipHydration: true,
    }
  )
);


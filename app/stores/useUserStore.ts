'use client';

import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { UserProfile, StyleAvatar, StylePreferences} from '../types';
import { mockUserProfile } from '../lib/mock-data';

interface UserState {
  profile: UserProfile | null;
  setProfile: (profile: UserProfile) => void;
  updateAvatar: (avatar: Partial<StyleAvatar>) => void;
  updatePreferences: (prefs: Partial<StylePreferences>) => void;
  updateUser: (user: Partial<UserProfile['user']>) => void;
}

export const useUserStore = create<UserState>()(
  persist(
    (set) => ({
      profile: mockUserProfile,
      
      setProfile: (profile) => set({ profile }),
      
      updateAvatar: (avatar) => set((state) => ({
        profile: state.profile ? {
          ...state.profile,
          avatar: { ...state.profile.avatar, ...avatar }
        } : null
      })),
      
      updatePreferences: (prefs) => set((state) => ({
        profile: state.profile ? {
          ...state.profile,
          preferences: { ...state.profile.preferences, ...prefs }
        } : null
      })),
      
      updateUser: (user) => set((state) => ({
        profile: state.profile ? {
          ...state.profile,
          user: { ...state.profile.user, ...user }
        } : null
      })),
    }),
    { 
      name: 'user-store',
      // Prevent hydration errors in Next.js
      skipHydration: true,
    }
  )
);


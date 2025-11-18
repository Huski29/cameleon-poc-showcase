'use client';

import { create } from 'zustand';
import type { Notification } from '../types';
import { mockNotifications } from '../lib/mock-data';

interface UIState {
  notifications: Notification[];
  unreadCount: number;
  markAsRead: (id: number) => void;
  markAllAsRead: () => void;
}

export const useUIStore = create<UIState>()((set) => ({
  notifications: mockNotifications,
  unreadCount: mockNotifications.filter(n => n.unread).length,
  
  markAsRead: (id) => set((state) => {
    const notification = state.notifications.find(n => n.id === id);
    if (!notification || !notification.unread) return state;
    
    return {
      notifications: state.notifications.map(n => 
        n.id === id ? { ...n, unread: false } : n
      ),
      unreadCount: state.unreadCount - 1
    };
  }),
  
  markAllAsRead: () => set((state) => ({
    notifications: state.notifications.map(n => ({ ...n, unread: false })),
    unreadCount: 0
  })),
}));


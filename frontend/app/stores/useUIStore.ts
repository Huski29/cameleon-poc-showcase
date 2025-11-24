'use client';

import { create } from 'zustand';
import type { Notification } from '../types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface UIState {
  notifications: Notification[];
  unreadCount: number;
  isLoading: boolean;
  error: string | null;
  fetchNotifications: () => Promise<void>;
  markAsRead: (id: number) => Promise<void>;
  markAllAsRead: () => Promise<void>;
}

export const useUIStore = create<UIState>()((set) => ({
  notifications: [],
  unreadCount: 0,
  isLoading: false,
  error: null,
  
  fetchNotifications: async () => {
    set({ isLoading: true, error: null });
    try {
      const response = await fetch(`${API_URL}/api/v1/notifications`);
      if (!response.ok) throw new Error('Failed to fetch notifications');
      
      const data = await response.json();
      const notifications: Notification[] = data.map((notif: any) => ({
        id: notif.id,
        text: notif.text,
        time: notif.time,
        unread: notif.unread,
      }));
      
      const unreadCount = notifications.filter(n => n.unread).length;
      
      set({ notifications, unreadCount, isLoading: false });
    } catch (error) {
      set({ error: (error as Error).message, isLoading: false });
    }
  },
  
  markAsRead: async (id) => {
    try {
      const response = await fetch(`${API_URL}/api/v1/notifications/${id}/read`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
      });
      
      if (!response.ok) throw new Error('Failed to mark notification as read');
      
      set((state) => {
        const notification = state.notifications.find(n => n.id === id);
        if (!notification || !notification.unread) return state;
        
        return {
          notifications: state.notifications.map(n => 
            n.id === id ? { ...n, unread: false } : n
          ),
          unreadCount: state.unreadCount - 1
        };
      });
    } catch (error) {
      set({ error: (error as Error).message });
    }
  },
  
  markAllAsRead: async () => {
    try {
      const response = await fetch(`${API_URL}/api/v1/notifications/read-all`, {
        method: 'PUT',
      });
      
      if (!response.ok) throw new Error('Failed to mark all notifications as read');
      
      set((state) => ({
        notifications: state.notifications.map(n => ({ ...n, unread: false })),
        unreadCount: 0
      }));
    } catch (error) {
      set({ error: (error as Error).message });
    }
  },
}));


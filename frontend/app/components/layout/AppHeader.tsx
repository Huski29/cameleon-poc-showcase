"use client";

import { useState, useRef, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Logo } from "./Logo";
import { useUserStore } from "../../stores/useUserStore";
import { useUIStore } from "../../stores/useUIStore";

export default function AppHeader() {
  const router = useRouter();
  const [showNotifications, setShowNotifications] = useState(false);
  const [showProfile, setShowProfile] = useState(false);
  const notifRef = useRef<HTMLDivElement>(null);
  const profileRef = useRef<HTMLDivElement>(null);
  
  const { profile } = useUserStore();
  const { notifications, fetchNotifications, markAsRead } = useUIStore();

  useEffect(() => {
    fetchNotifications();
  }, [fetchNotifications]);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent | TouchEvent) => {
      if (notifRef.current && !notifRef.current.contains(event.target as Node)) {
        setShowNotifications(false);
      }
      if (profileRef.current && !profileRef.current.contains(event.target as Node)) {
        setShowProfile(false);
      }
    };

    const handleScroll = () => {
      setShowNotifications(false);
      setShowProfile(false);
    };

    document.addEventListener("mousedown", handleClickOutside);
    document.addEventListener("touchstart", handleClickOutside);
    window.addEventListener("scroll", handleScroll);
    
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
      document.removeEventListener("touchstart", handleClickOutside);
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  const unreadCount = notifications.filter(n => n.unread).length;

  return (
    <header className="sticky top-0 z-50 w-full px-3 sm:px-4 md:px-6 lg:px-8 bg-white/40 dark:bg-black/20 backdrop-blur-lg border-b border-border-light dark:border-border-dark">
      <div className="mx-auto max-w-screen-xl">
        <div className="flex items-center justify-between h-16 sm:h-20">
          <div className="flex items-center gap-2 sm:gap-4 text-text-light dark:text-text-dark">
            <Logo />
            <h1 
              className="text-lg sm:text-xl font-black tracking-tighter cursor-pointer" 
              onClick={() => router.push("/generate")}
            >
              Cameleon
            </h1>
          </div>

          <div className="flex items-center gap-2 sm:gap-4">
            <nav className="hidden md:flex items-center gap-4 lg:gap-6">
              <a 
                className="text-sm font-medium hover:text-primary transition-colors cursor-pointer" 
                onClick={() => router.push("/wardrobe")}
              >
                Wardrobe
              </a>
              <a className="text-sm font-medium hover:text-primary transition-colors cursor-pointer" href="#">
                Style Guide
              </a>
              <a className="text-sm font-medium hover:text-primary transition-colors cursor-pointer" href="#">
                Inspiration
              </a>
            </nav>

            <div className="flex items-center gap-2">
              {/* Notifications Dropdown */}
              <div className="relative" ref={notifRef}>
                <button 
                  onClick={() => {
                    setShowNotifications(!showNotifications);
                    setShowProfile(false);
                  }}
                  aria-label={`Notifications${unreadCount > 0 ? ` (${unreadCount} unread)` : ''}`}
                  aria-expanded={showNotifications}
                  aria-haspopup="true"
                  className="flex cursor-pointer items-center justify-center rounded-full h-9 w-9 sm:h-10 sm:w-10 bg-primary/20 dark:bg-primary/30 text-text-light dark:text-text-dark hover:bg-primary/30 dark:hover:bg-primary/40 transition-colors relative"
                >
                  <span className="material-symbols-outlined text-lg sm:text-xl" aria-hidden="true">notifications</span>
                  {unreadCount > 0 && (
                    <span className="absolute top-1 right-1 flex h-4 w-4 items-center justify-center rounded-full bg-red-500 text-[9px] font-bold text-white" aria-hidden="true">
                      {unreadCount}
                    </span>
                  )}
                </button>

                {showNotifications && (
                  <div 
                    className="fixed sm:absolute left-2 right-2 sm:left-auto sm:right-0 top-[4.5rem] sm:top-auto mt-0 sm:mt-2 w-auto sm:w-80 max-w-md bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark rounded-xl shadow-2xl overflow-hidden backdrop-blur-lg z-50"
                    role="menu" 
                    aria-label="Notifications menu"
                  >
                    <div className="p-3 sm:p-4 border-b border-border-light dark:border-border-dark">
                      <h3 className="font-bold text-sm sm:text-base text-text-light dark:text-text-dark">Notifications</h3>
                    </div>
                    <div className="max-h-64 sm:max-h-96 overflow-y-auto scrollbar-custom">
                      {notifications.map((notif) => (
                        <div 
                          key={notif.id}
                          onClick={() => {
                            markAsRead(notif.id);
                            setShowNotifications(false);
                          }}
                          role="menuitem"
                          tabIndex={0}
                          onKeyPress={(e) => {
                            if (e.key === 'Enter' || e.key === ' ') {
                              e.preventDefault();
                              markAsRead(notif.id);
                              setShowNotifications(false);
                            }
                          }}
                          className={`p-3 sm:p-4 hover:bg-background-light dark:hover:bg-background-dark transition-colors cursor-pointer border-b border-border-light/50 dark:border-border-dark/50 last:border-b-0 active:bg-primary/10 ${
                            notif.unread ? 'bg-primary/5' : ''
                          }`}
                        >
                          <div className="flex items-start gap-3">
                            {notif.unread && (
                              <div className="w-2 h-2 bg-primary rounded-full mt-1.5 flex-shrink-0"></div>
                            )}
                            <div className="flex-1">
                              <p className="text-sm font-medium text-text-light dark:text-text-dark">{notif.text}</p>
                              <p className="text-xs text-text-muted-light dark:text-text-muted-dark mt-1">{notif.time}</p>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Profile Dropdown */}
              <div className="relative" ref={profileRef}>
                <div 
                  onClick={() => {
                    setShowProfile(!showProfile);
                    setShowNotifications(false);
                  }}
                  role="button"
                  tabIndex={0}
                  aria-label="User profile menu"
                  aria-expanded={showProfile}
                  aria-haspopup="true"
                  onKeyPress={(e) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                      e.preventDefault();
                      setShowProfile(!showProfile);
                      setShowNotifications(false);
                    }
                  }}
                  className="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-9 sm:size-10 cursor-pointer ring-2 ring-transparent hover:ring-primary/30 transition-all"
                  style={{
                    backgroundImage: `url('${profile?.user.profilePicture}')`
                  }}
                  data-alt="User profile picture"
                />

                {showProfile && (
                  <div 
                    className="fixed sm:absolute left-2 right-2 sm:left-auto sm:right-0 top-[4.5rem] sm:top-auto mt-0 sm:mt-2 w-auto sm:w-64 bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark rounded-xl shadow-2xl overflow-hidden backdrop-blur-lg z-50"
                    role="menu" 
                    aria-label="Profile menu"
                  >
                    <div className="p-3 sm:p-4 border-b border-border-light dark:border-border-dark">
                      <p className="font-bold text-sm sm:text-base text-text-light dark:text-text-dark">{profile?.user.name}</p>
                      <p className="text-xs sm:text-sm text-text-muted-light dark:text-text-muted-dark">{profile?.user.email}</p>
                    </div>
                    <div className="py-2">
                      <button 
                        onClick={() => {
                          router.push("/profile");
                          setShowProfile(false);
                        }}
                        role="menuitem"
                        className="w-full px-3 sm:px-4 py-2.5 text-left text-xs sm:text-sm font-medium text-text-light dark:text-text-dark hover:bg-background-light dark:hover:bg-background-dark transition-colors flex items-center gap-3 active:bg-primary/10"
                      >
                        <span className="material-symbols-outlined text-lg sm:text-xl" aria-hidden="true">person</span>
                        Profile Settings
                      </button>
                      <button 
                        onClick={() => {
                          router.push("/wardrobe");
                          setShowProfile(false);
                        }}
                        role="menuitem"
                        className="w-full px-3 sm:px-4 py-2.5 text-left text-xs sm:text-sm font-medium text-text-light dark:text-text-dark hover:bg-background-light dark:hover:bg-background-dark transition-colors flex items-center gap-3 active:bg-primary/10"
                      >
                        <span className="material-symbols-outlined text-lg sm:text-xl" aria-hidden="true">checkroom</span>
                        My Wardrobe
                      </button>
                      <button 
                        onClick={() => setShowProfile(false)}
                        role="menuitem"
                        className="w-full px-3 sm:px-4 py-2.5 text-left text-xs sm:text-sm font-medium text-text-light dark:text-text-dark hover:bg-background-light dark:hover:bg-background-dark transition-colors flex items-center gap-3 active:bg-primary/10"
                      >
                        <span className="material-symbols-outlined text-lg sm:text-xl" aria-hidden="true">favorite</span>
                        Saved Outfits
                      </button>
                    </div>
                    <div className="border-t border-border-light dark:border-border-dark">
                      <button 
                        onClick={() => setShowProfile(false)}
                        role="menuitem"
                        className="w-full px-3 sm:px-4 py-2.5 text-left text-xs sm:text-sm font-medium text-red-600 dark:text-red-400 hover:bg-background-light dark:hover:bg-background-dark transition-colors flex items-center gap-3 active:bg-primary/10"
                      >
                        <span className="material-symbols-outlined text-lg sm:text-xl" aria-hidden="true">logout</span>
                        Sign Out
                      </button>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}


"use client";

import { useEffect, useState } from "react";
import AppHeader from "../components/layout/AppHeader";
import { CustomSelect } from "../components/forms";
import { useUserStore } from "../stores/useUserStore";
import { HEIGHT_RANGES, VOLUME_RANGES, STYLE_PREFERENCES, COLOR_PALETTES, BUDGET_RANGES } from "../constants";

export default function ProfilePage() {
  const { profile, updateUser, updateAvatar, updatePreferences, fetchProfile, isLoading } = useUserStore();
  const [isSaving, setIsSaving] = useState(false);
  
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    gender: "female" as "male" | "female",
    height: "Regular",
    volume: "Mid",
    bodyType: "Rectangle",
    stylePreference: "Smart Casual",
    colorPalette: "Neutral & Earth Tones",
    budget: "Mid-Range"
  });

  // Fetch profile from backend on mount
  useEffect(() => {
    fetchProfile();
  }, [fetchProfile]);

  // Initialize form data from profile
  useEffect(() => {
    if (profile) {
      setFormData({
        name: profile.user.name,
        email: profile.user.email,
        gender: profile.user.gender as "male" | "female",
        height: profile.avatar.height,
        volume: profile.avatar.volume,
        bodyType: profile.avatar.bodyType,
        stylePreference: profile.preferences.stylePreference,
        colorPalette: profile.preferences.colorPalette,
        budget: profile.preferences.budget,
      });
    }
  }, [profile]);

  const handleSave = async () => {
    setIsSaving(true);
    try {
      // Only send non-empty values
      const userUpdate: any = {};
      if (formData.name) userUpdate.name = formData.name;
      if (formData.email) userUpdate.email = formData.email;
      if (formData.gender) userUpdate.gender = formData.gender;
      
      await updateUser(userUpdate);
      await updateAvatar({
        height: formData.height as any,
        volume: formData.volume as any,
        bodyType: formData.bodyType as any,
      });
      await updatePreferences({
        stylePreference: formData.stylePreference,
        colorPalette: formData.colorPalette,
        budget: formData.budget,
      });
      
      // Refresh profile data from backend to ensure UI is in sync
      await fetchProfile();
      
      console.log('Profile updated successfully');
    } catch (error) {
      console.error('Error updating profile:', error);
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="relative flex h-screen w-full flex-col overflow-hidden font-display bg-gradient-to-br from-[#fdfbf7] to-[#f4f1ea] dark:bg-gradient-to-br dark:from-[#2a261a] dark:to-[#211d11] text-text-light dark:text-text-dark">
      <AppHeader />

      {/* Main Content - Scrollable */}
      <main className="flex-1 w-full max-w-4xl mx-auto py-6 sm:py-8 lg:py-12 px-3 sm:px-4 md:px-6 lg:px-8 overflow-y-auto [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]">
        <div className="flex flex-col gap-6 sm:gap-8 overflow-visible">
          {/* Header */}
          <div className="flex flex-col gap-2">
            <h1 className="text-2xl sm:text-3xl md:text-4xl font-black leading-tight tracking-[-0.033em] text-text-light dark:text-text-dark">
              Profile Settings
            </h1>
            <p className="text-sm sm:text-base font-medium leading-normal text-text-muted-light dark:text-text-muted-dark">
              Manage your style preferences and account details
            </p>
          </div>

          {/* Profile Picture Section */}
          <div className="bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark rounded-xl p-6 backdrop-blur-sm">
            <h2 className="text-xl font-bold mb-4 text-text-light dark:text-text-dark">Profile Picture</h2>
            <div className="flex items-center gap-6">
              <div 
                className="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-24 ring-2 ring-border-light dark:ring-border-dark"
                style={{
                  backgroundImage: `url('${profile?.user.profilePicture}')`
                }}
              />
              <button className="px-5 py-2.5 rounded-lg bg-primary text-text-light font-semibold text-sm hover:opacity-90 transition-opacity">
                Change Photo
              </button>
            </div>
          </div>

          {/* Personal Information */}
          <div className="bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark rounded-xl p-6 backdrop-blur-sm">
            <h2 className="text-xl font-bold mb-6 text-text-light dark:text-text-dark">Personal Information</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="flex flex-col gap-2">
                <label className="text-sm font-semibold text-text-light dark:text-text-dark">Full Name</label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                  className="w-full px-4 py-3 rounded-xl border border-border-light dark:border-border-dark bg-card-light dark:bg-card-dark text-text-light dark:text-text-dark focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50 backdrop-blur-sm"
                />
              </div>
              <div className="flex flex-col gap-2">
                <label className="text-sm font-semibold text-text-light dark:text-text-dark">Email</label>
                <input
                  type="email"
                  value={formData.email}
                  onChange={(e) => setFormData({...formData, email: e.target.value})}
                  className="w-full px-4 py-3 rounded-xl border border-border-light dark:border-border-dark bg-card-light dark:bg-card-dark text-text-light dark:text-text-dark focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50 backdrop-blur-sm"
                />
              </div>
              <div className="md:col-span-2 md:max-w-[calc(50%-0.75rem)]">
                <CustomSelect
                  label="Gender"
                  value={formData.gender === "male" ? "Male" : "Female"}
                  onChange={(value) => setFormData({...formData, gender: value.toLowerCase() as "male" | "female"})}
                  options={["Female", "Male"]}
                />
              </div>
            </div>
          </div>

          {/* Style Avatar */}
          <div className="bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark rounded-xl p-6 backdrop-blur-sm overflow-visible">
            <h2 className="text-xl font-bold mb-6 text-text-light dark:text-text-dark">Style Avatar</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 overflow-visible">
              <CustomSelect
                label="Height Range"
                value={formData.height}
                onChange={(value) => setFormData({...formData, height: value})}
                options={[...HEIGHT_RANGES]}
              />
              <CustomSelect
                label="Volume Range"
                value={formData.volume}
                onChange={(value) => setFormData({...formData, volume: value})}
                options={[...VOLUME_RANGES]}
              />
              <div className="md:col-span-2 md:max-w-[calc(50%-0.75rem)]">
                <CustomSelect
                  label="Body Type"
                  value={formData.bodyType}
                  onChange={(value) => setFormData({...formData, bodyType: value})}
                  options={["Triangle", "Inverted Triangle", "Round", "Rectangle", "Trapezium", "Not Sure"]}
                />
              </div>
            </div>
          </div>

          {/* Style Preferences */}
          <div className="bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark rounded-xl p-6 backdrop-blur-sm overflow-visible">
            <h2 className="text-xl font-bold mb-6 text-text-light dark:text-text-dark">Style Preferences</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 overflow-visible">
              <CustomSelect
                label="Preferred Style"
                value={formData.stylePreference}
                onChange={(value) => setFormData({...formData, stylePreference: value})}
                options={[...STYLE_PREFERENCES]}
              />
              <CustomSelect
                label="Color Palette"
                value={formData.colorPalette}
                onChange={(value) => setFormData({...formData, colorPalette: value})}
                options={[...COLOR_PALETTES]}
              />
              <div className="md:col-span-2 md:max-w-[calc(50%-0.75rem)]">
                <CustomSelect
                  label="Budget Range"
                  value={formData.budget}
                  onChange={(value) => setFormData({...formData, budget: value})}
                  options={[...BUDGET_RANGES]}
                />
              </div>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex flex-col sm:flex-row gap-3 justify-end">
            <button className="px-6 py-3 rounded-xl border border-border-light dark:border-border-dark text-text-light dark:text-text-dark font-semibold hover:bg-background-light dark:hover:bg-background-dark transition-colors">
              Cancel
            </button>
            <button 
              onClick={handleSave}
              disabled={isSaving}
              className="px-6 py-3 rounded-xl bg-primary text-text-light font-semibold hover:opacity-90 transition-opacity disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              {isSaving ? (
                <>
                  <svg className="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  <span>Saving...</span>
                </>
              ) : (
                <span>Save Changes</span>
              )}
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}


"use client";

import { useRouter } from "next/navigation";
import { useOutfitStore } from "../stores/useOutfitStore";
import { useEffect, useState } from "react";
import AppHeader from "../components/layout/AppHeader";

export default function OutfitResultPage() {
  const router = useRouter();
  const { currentOutfit, saveOutfit, generateOutfit } = useOutfitStore();
  const [isSaving, setIsSaving] = useState(false);

  // Redirect to generate page if no outfit is available
  useEffect(() => {
    if (!currentOutfit) {
      router.push("/generate");
    }
  }, [currentOutfit, router]);

  const handleTryOn = () => {
    router.push("/try-on");
  };

  const handleSaveOutfit = async () => {
    if (!currentOutfit) return;
    setIsSaving(true);
    try {
      await saveOutfit(currentOutfit.id);
    } finally {
      setIsSaving(false);
    }
  };

  const handleNewSuggestion = () => {
    router.push("/generate");
  };

  if (!currentOutfit) {
    return null; // Will redirect in useEffect
  }

  // Create a 2x2 grid of items (fill with first 4 items)
  const outfitItems = currentOutfit.items.slice(0, 4);

  return (
    <div className="relative flex h-screen w-full flex-col overflow-hidden font-display bg-gradient-to-br from-[#fdfbf7] to-[#f4f1ea] dark:bg-gradient-to-br dark:from-[#2a261a] dark:to-[#211d11] text-text-light dark:text-text-dark scale-page-80">
      <AppHeader />

      {/* Main Content */}
      <main className="flex-1 w-full max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 w-full">
          {/* Left: 2x2 Grid of Outfit Items */}
          <div className="grid grid-cols-2 grid-rows-2 gap-6 aspect-square max-h-[80vh]">
            {outfitItems.map((item, index) => (
              <div 
                key={item.id || index}
                className="bg-card-light dark:bg-card-dark p-2 rounded-xl shadow-lg shadow-black/5 backdrop-blur-sm border border-white/50 dark:border-black/20"
              >
                <div 
                  className="w-full h-full bg-center bg-no-repeat bg-cover rounded-lg"
                  style={{ backgroundImage: `url("${item.image}")` }}
                  title={item.name}
                />
              </div>
            ))}
          </div>

          {/* Right: Outfit Details */}
          <div className="flex flex-col justify-center gap-8 py-8">
            <div className="flex flex-col gap-2">
              <p className="text-4xl lg:text-5xl font-black leading-tight tracking-[-0.033em] text-text-light dark:text-text-dark">
                {currentOutfit.title}
              </p>
              <p className="text-base font-medium leading-normal text-text-muted-light dark:text-text-muted-dark">
                Vibe: {currentOutfit.vibe}
              </p>
            </div>

            {/* Items List */}
            <div className="flex flex-col border border-border-light dark:border-border-dark rounded-xl bg-card-light dark:bg-card-dark overflow-hidden backdrop-blur-sm">
              {currentOutfit.items.map((item, index) => (
                <div 
                  key={item.id || index}
                  className={`flex items-center gap-4 min-h-[72px] py-2 px-4 justify-between ${
                    index < currentOutfit.items.length - 1 ? 'border-b border-border-light dark:border-border-dark' : ''
                  }`}
                >
                  <div className="flex items-center gap-4">
                    <div 
                      className="bg-center bg-no-repeat aspect-square bg-cover rounded-lg size-10"
                      style={{ backgroundImage: `url("${item.image}")` }}
                      title={item.name}
                    />
                    <div className="flex flex-col justify-center">
                      <p className="text-base font-medium leading-normal line-clamp-1 text-text-light dark:text-text-dark">
                        {item.brand ? `${item.brand} - ${item.name}` : item.name}
                      </p>
                      <p className="text-sm font-normal leading-normal line-clamp-2 text-text-muted-light dark:text-text-muted-dark">
                        {item.type}
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Action Buttons */}
            <div className="flex flex-col sm:flex-row items-center gap-3 w-full mt-4">
              <button 
                onClick={handleTryOn}
                className="flex w-full sm:w-auto sm:flex-1 min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 px-6 bg-primary text-text-light text-base font-bold leading-normal tracking-[0.015em] hover:opacity-90 transition-opacity"
              >
                <span className="truncate">Try On</span>
              </button>

              <button 
                onClick={handleNewSuggestion}
                className="flex w-full sm:w-auto min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 px-6 bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark text-text-light dark:text-text-dark text-base font-bold leading-normal tracking-[0.015em] hover:bg-border-light dark:hover:bg-border-dark transition-colors backdrop-blur-sm"
              >
                <span className="truncate">New Suggestion</span>
              </button>

              <button 
                onClick={handleSaveOutfit}
                disabled={isSaving}
                className="flex max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 w-12 bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark text-text-light dark:text-text-dark gap-2 text-sm font-bold leading-normal tracking-[0.015em] hover:bg-border-light dark:hover:bg-border-dark transition-colors backdrop-blur-sm disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span className="material-symbols-outlined text-2xl">favorite</span>
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}


"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useOutfitStore } from "../stores/useOutfitStore";
import { useWardrobeStore } from "../stores/useWardrobeStore";
import { STYLE_CATEGORIES } from "../constants";
import { Logo } from "../components/layout/Logo";

export default function GeneratePage() {
  const router = useRouter();
  const [inputValue, setInputValue] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);
  const { generateOutfit } = useOutfitStore();
  const { items, fetchItems } = useWardrobeStore();

  useEffect(() => {
    fetchItems();
  }, [fetchItems]);

  const handleOpenWardrobe = () => {
    router.push("/wardrobe");
  };

  const handleGenerateOutfit = async () => {
    setIsGenerating(true);
    try {
      await generateOutfit(inputValue, { category: selectedCategory });
      router.push("/outfit-result");
    } catch (error) {
      console.error("Failed to generate outfit:", error);
    } finally {
      setIsGenerating(false);
    }
  };

  const wardrobePreview = items.slice(0, 6);

  return (
    <div className="relative flex min-h-screen w-full flex-col overflow-x-hidden">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full px-4 sm:px-8 md:px-12 py-3">
        <div className="glassmorphic mx-auto flex max-w-7xl items-center justify-between whitespace-nowrap rounded-xl px-6 py-3 shadow-sm">
          <div className="flex items-center gap-4 text-text-light dark:text-text-dark">
            <Logo />
            <h2 className="text-xl font-bold tracking-tight">Cameleon</h2>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex flex-1 items-center justify-center p-3 sm:p-4 md:p-6 lg:p-8">
        <div className="grid w-full max-w-5xl grid-cols-1 gap-6 sm:gap-8 lg:grid-cols-3">
          {/* Left Section - Main Input */}
          <div className="flex flex-col items-center justify-center gap-4 sm:gap-6 lg:col-span-2">
            <div className="w-full rounded-xl bg-card-light/50 dark:bg-card-dark/50 p-4 sm:p-6 md:p-8 lg:p-10 shadow-lg border border-border-light dark:border-border-dark">
              <h1 className="mb-4 sm:mb-6 text-center text-xl sm:text-2xl md:text-3xl font-bold tracking-tight text-text-light dark:text-text-dark">
                Describe what you need today…
              </h1>

              {/* Textarea */}
              <div className="w-full">
                <textarea
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  className="min-h-36 w-full resize-none rounded-xl border border-border-light bg-background-light p-4 text-base font-normal leading-normal text-text-light placeholder:text-placeholder-light focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50 dark:border-border-dark dark:bg-background-dark dark:text-text-dark dark:placeholder:text-placeholder-dark dark:focus:border-primary"
                  placeholder="e.g., A stylish and comfortable outfit for a weekend brunch with friends."
                />
              </div>

              {/* Category Pills */}
              <div className="mt-6 flex flex-wrap items-center justify-center gap-3">
                {STYLE_CATEGORIES.map((category) => (
                  <div
                    key={category}
                    onClick={() => setSelectedCategory(category)}
                    className={`cursor-pointer rounded-full border px-4 py-1.5 text-sm font-medium transition-colors ${
                      selectedCategory === category
                        ? "border-primary bg-primary/20 dark:bg-primary/30"
                        : "border-border-light bg-background-light hover:bg-primary/20 dark:border-border-dark dark:bg-background-dark dark:hover:bg-primary/30"
                    }`}
                  >
                    {category}
                  </div>
                ))}
              </div>

              {/* Generate Button */}
              <div className="w-full pt-8">
                <button 
                  onClick={handleGenerateOutfit}
                  disabled={isGenerating || !inputValue.trim()}
                  className="flex h-12 w-full min-w-[84px] cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-xl bg-primary px-5 text-base font-bold text-text-light transition-transform hover:scale-105 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
                >
                  {isGenerating ? (
                    <>
                      <svg className="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      <span>Generating...</span>
                    </>
                  ) : (
                    <>
                      <span 
                        className="material-symbols-outlined !text-xl" 
                        style={{ fontVariationSettings: "'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 20" }}
                      >
                        auto_awesome
                      </span>
                      <span>Generate Outfit</span>
                    </>
                  )}
                </button>
              </div>
            </div>
          </div>

          {/* Right Section - Wardrobe */}
          <div 
            onClick={handleOpenWardrobe}
            className="glassmorphic flex h-fit flex-col gap-4 rounded-xl p-4 shadow-lg cursor-pointer transition-all hover:shadow-xl"
          >
            <button className="flex w-full items-center justify-between rounded-lg bg-background-light/50 p-3 text-sm font-semibold text-text-light transition-colors hover:bg-background-light/80 dark:bg-background-dark/50 dark:text-text-dark dark:hover:bg-background-dark/80">
              <span className="flex items-center gap-2">
                <span 
                  className="material-symbols-outlined !text-xl" 
                  style={{ fontVariationSettings: "'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 20" }}
                >
                  dresser
                </span>
                <span>My Wardrobe</span>
              </span>
              <span 
                className="material-symbols-outlined !text-xl transition-transform group-hover:translate-x-1" 
                style={{ fontVariationSettings: "'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 20" }}
              >
                arrow_forward
              </span>
            </button>

            <div className="hide-scrollbar">
              <div className="grid grid-cols-2 gap-3">
                {wardrobePreview.map((item) => (
                  <div key={item.id} className="relative aspect-square w-full rounded-lg overflow-hidden bg-gradient-to-br from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-800">
                    <img
                      alt={item.alt}
                      className="w-full h-full object-cover"
                      src={item.image}
                      onError={(e) => {
                        const target = e.currentTarget;
                        target.style.display = 'none';
                        const parent = target.parentElement;
                        if (parent) {
                          parent.innerHTML = `<div class="flex items-center justify-center w-full h-full">
                            <span class="material-symbols-outlined text-2xl text-gray-400">image_not_supported</span>
                          </div>`;
                        }
                      }}
                    />
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}


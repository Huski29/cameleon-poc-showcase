"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useOutfitStore } from "../stores/useOutfitStore";
import AppHeader from "../components/layout/AppHeader";

export default function TryOnPage() {
  const router = useRouter();
  const { currentOutfit } = useOutfitStore();
  const [tryOnImage, setTryOnImage] = useState<string | null>(null);

  useEffect(() => {
    // Get try-on image from localStorage
    const storedImage = localStorage.getItem('tryOnImage');
    if (storedImage) {
      setTryOnImage(storedImage);
    } else if (!currentOutfit) {
      // If no try-on image and no outfit, redirect to generate
      router.push("/generate");
    }
  }, [currentOutfit, router]);

  // Use current outfit items if available, fallback to mock data
  const outfitDetails = currentOutfit?.items || [];

  return (
    <div className="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden font-display bg-background-light dark:bg-background-dark text-text-light dark:text-text-dark scale-page-80">
      <AppHeader />

      {/* Main Content */}
      <main className="flex-1 w-full max-w-screen-xl mx-auto py-8 lg:py-16 px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-start">
          {/* Left Panel: Image Preview */}
          <div className="lg:col-span-7 flex w-full justify-center">
            <div className="w-[90%] max-w-[calc(36rem*0.9)] aspect-[3/4] bg-card-light dark:bg-card-dark p-2 rounded-xl shadow-lg shadow-black/5">
              {tryOnImage ? (
                <img 
                  src={tryOnImage}
                  alt="Virtual try-on result"
                  className="rounded-lg w-full h-full object-cover"
                />
              ) : (
                <div className="flex items-center justify-center h-full text-text-muted-light dark:text-text-muted-dark">
                  <div className="text-center">
                    <p className="text-lg font-medium">Generating your try-on...</p>
                    <p className="text-sm mt-2">This may take a moment</p>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Right Panel: Details and Actions */}
          <div className="lg:col-span-5 flex flex-col gap-8">
            <div className="flex flex-col gap-2">
              <p className="text-4xl font-black leading-tight tracking-[-0.033em] text-text-light dark:text-text-dark">
                {currentOutfit?.title || "Virtual Try-On"}
              </p>
              <p className="text-base font-medium leading-normal text-text-muted-light dark:text-text-muted-dark">
                Vibe: {currentOutfit?.vibe || "Stylish"}
              </p>
            </div>

            {/* Items List */}
            <div className="flex flex-col border border-border-light dark:border-border-dark rounded-xl bg-card-light dark:bg-card-dark overflow-hidden">
              {outfitDetails.map((item, index) => (
                <div 
                  key={item.id}
                  className={`flex items-center gap-4 min-h-[72px] py-2 px-4 justify-between ${
                    index < outfitDetails.length - 1 ? 'border-b border-border-light dark:border-border-dark' : ''
                  }`}
                >
                  <div className="flex items-center gap-4">
                    <div 
                      className="bg-center bg-no-repeat aspect-square bg-cover rounded-lg size-14"
                      style={{ backgroundImage: `url("${item.image}")` }}
                      data-alt={item.alt}
                    />
                    <div className="flex flex-col justify-center">
                      <p className="text-base font-medium leading-normal line-clamp-1 text-text-light dark:text-text-dark">
                        {item.name}
                      </p>
                      <p className="text-sm font-normal leading-normal line-clamp-2 text-text-muted-light dark:text-text-muted-dark">
                        {item.category}
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Action Buttons */}
            <div className="flex flex-col sm:flex-row items-center gap-3 w-full">
              <button className="flex w-full sm:w-auto sm:flex-1 min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 px-6 bg-primary text-text-light text-base font-bold leading-normal tracking-[0.015em] hover:opacity-90 transition-opacity">
                <span className="truncate">Try On</span>
              </button>

              <button className="flex w-full sm:w-auto min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 px-6 bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark text-text-light dark:text-text-dark text-base font-bold leading-normal tracking-[0.015em] hover:bg-border-light dark:hover:bg-border-dark transition-colors">
                <span className="truncate">New Suggestion</span>
              </button>

              <button className="flex max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 w-12 bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark text-text-light dark:text-text-dark gap-2 text-sm font-bold leading-normal tracking-[0.015em] hover:bg-border-light dark:hover:bg-border-dark transition-colors">
                <span className="material-symbols-outlined text-2xl">favorite</span>
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}


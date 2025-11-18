"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useUserStore } from "./stores/useUserStore";
import { BODY_TYPES, HEIGHT_RANGES, VOLUME_RANGES } from "./constants";
import { RangeSlider, BodyTypeSelector } from "./components/forms";
import { Logo } from "./components/layout/Logo";
import type { BodyType } from "./types";

export default function HomePage() {
  const router = useRouter();
  const { profile, updateAvatar } = useUserStore();
  
  // Initialize from store after hydration
  const [heightRange, setHeightRange] = useState(1);
  const [volumeRange, setVolumeRange] = useState(1);
  const [selectedBodyType, setSelectedBodyType] = useState("");

  // Sync with store after hydration
  useEffect(() => {
    if (profile?.avatar) {
      const heightIndex = HEIGHT_RANGES.indexOf(profile.avatar.height);
      const volumeIndex = VOLUME_RANGES.indexOf(profile.avatar.volume);
      setHeightRange(heightIndex !== -1 ? heightIndex : 1);
      setVolumeRange(volumeIndex !== -1 ? volumeIndex : 1);
      setSelectedBodyType(profile.avatar.bodyType);
    }
  }, [profile]);

  const handleGenerateAvatar = () => {
    // Update store with selected values
    updateAvatar({
      height: HEIGHT_RANGES[heightRange],
      volume: VOLUME_RANGES[volumeRange],
      bodyType: selectedBodyType as BodyType,
    });
    router.push("/avatar-confirmation");
  };

  return (
    <div className="relative flex h-screen min-h-[800px] w-full flex-col bg-background-light dark:bg-background-dark overflow-hidden">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 z-10 w-full glassmorphic-header">
        <div className="mx-auto flex max-w-7xl items-center justify-between whitespace-nowrap px-4 sm:px-6 py-3 sm:py-4">
          <div className="flex items-center gap-2 sm:gap-3 text-[#1b180e] dark:text-[#f8f7f6]">
            <Logo />
            <h2 className="text-lg sm:text-xl font-bold leading-tight tracking-[-0.015em]">Cameleon</h2>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex h-full flex-1 items-center justify-center py-5 px-3 sm:px-4 md:px-6 lg:px-8 overflow-x-hidden">
        <div className="main-card flex w-full max-w-4xl flex-col rounded-xl border border-solid border-[#f3f0e7]/50 dark:border-[#383325]/50 p-4 sm:p-6 md:p-8">
          <h1 className="text-[#1b180e] dark:text-[#f8f7f6] tracking-light text-xl sm:text-2xl md:text-3xl font-bold leading-tight text-center pb-4 sm:pb-6">
            Create Your Style Avatar
          </h1>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6 md:gap-8">
            {/* Left Column: Upload & Sliders */}
            <div className="flex flex-col gap-4 sm:gap-6">
              {/* Selfie Upload */}
              <div className="flex flex-col items-center gap-3 sm:gap-4 rounded-lg border-2 border-dashed border-[#e7e1d0] dark:border-[#383325] px-4 sm:px-6 py-6 sm:py-8 text-center">
                <div className="flex flex-col items-center gap-2">
                  <p className="text-[#1b180e] dark:text-[#f8f7f6] text-sm sm:text-base font-bold leading-tight tracking-[-0.015em]">
                    Upload Your Selfie
                  </p>
                  <p className="text-[#1b180e]/70 dark:text-[#f8f7f6]/70 text-xs sm:text-sm font-normal leading-normal">
                    Drag & drop or click to browse
                  </p>
                </div>
                <button className="mt-2 flex min-w-[84px] cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-full h-9 sm:h-10 px-4 sm:px-5 bg-[#f3f0e7] dark:bg-[#383325] text-[#1b180e] dark:text-[#f8f7f6] text-xs sm:text-sm font-bold leading-normal tracking-[0.015em] hover:bg-[#e7e1d0] dark:hover:bg-[#4a4433] transition-colors" aria-label="Choose file to upload">
                  <span className="material-symbols-outlined text-base sm:text-lg" aria-hidden="true">upload</span>
                  <span className="truncate">Choose File</span>
                </button>
              </div>

              {/* Sliders */}
              <div className="flex flex-col gap-4 sm:gap-6 rounded-lg border border-solid border-[#f3f0e7]/80 dark:border-[#383325]/80 p-4 sm:p-6">
                <h2 className="text-[#1b180e] dark:text-[#f8f7f6] text-base sm:text-lg font-bold leading-tight tracking-[-0.015em] text-center">
                  Define Your Proportions
                </h2>

                <RangeSlider
                  label="Height Range"
                  value={heightRange}
                  onChange={setHeightRange}
                  labels={["Petite", "Regular", "Tall"]}
                />

                <RangeSlider
                  label="Volume Range"
                  value={volumeRange}
                  onChange={setVolumeRange}
                  labels={["Lean", "Mid", "Plus"]}
                />
              </div>
            </div>

            {/* Right Column: Body Type & Generate Button */}
            <div className="flex flex-col justify-between gap-4 sm:gap-6">
              {/* Body Type Selection */}
              <div className="flex flex-col gap-3 sm:gap-4">
                <h2 className="text-[#1b180e] dark:text-[#f8f7f6] text-base sm:text-lg font-bold leading-tight tracking-[-0.015em] text-center">
                  Select Your Body Type
                </h2>
                <BodyTypeSelector
                  bodyTypes={BODY_TYPES}
                  selectedBodyType={selectedBodyType}
                  onSelect={setSelectedBodyType}
                />
              </div>

              {/* Generate Button */}
              <div className="mt-auto pt-3 sm:pt-4">
                <button
                  onClick={handleGenerateAvatar}
                  disabled={!selectedBodyType}
                  aria-label="Generate your style avatar"
                  className="flex w-full cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 sm:h-14 px-5 sm:px-6 bg-primary text-[#1b180e] text-sm sm:text-base font-bold leading-normal tracking-[0.015em] shadow-lg shadow-primary/20 transition-transform hover:scale-[1.02] active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
                >
                  <span className="truncate">Generate Avatar</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

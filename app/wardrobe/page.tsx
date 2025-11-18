"use client";

import { useRouter } from "next/navigation";
import { useWardrobeStore } from "../stores/useWardrobeStore";
import { WardrobeCategory } from "../components/wardrobe";
import { Logo } from "../components/layout/Logo";

export default function WardrobePage() {
  const router = useRouter();
  const { getItemsByCategory } = useWardrobeStore();

  const handleClose = () => {
    router.back();
  };

  const topsItems = getItemsByCategory('tops');
  const bottomsItems = getItemsByCategory('bottoms');

  return (
    <div className="relative flex h-screen w-full flex-col items-center justify-center overflow-hidden bg-gradient-to-b from-[#F5F5DC] to-[#FFFDD0] p-4">
      {/* Background content */}
      <div 
        className="absolute inset-0 z-0 bg-cover bg-center opacity-20" 
        style={{
          backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuA_yIMI_daMGU3kqRKGJM0h9s6Bt8NkmLcPu4fvypBxzfX0Pyi_Ex9vuXSaNml8subaaZOouJwijp52oWP9RTlHHWJSz6AKuAX-x2rRZt3muGfR4PdDwsNDOBSI3giwRhUOPdmGpzD7NIlZrigvzEWb3aJONm9aTcUmQQu3WyfLX9Dfl3j5BJoRYFfJAylIl8CVDPhh0oOo1NkbuD_sXPOdvWxsiPl27EdRjUwuPUg9w57EONy06aQfn1VIoAzE4DfjWFjcQLHMfP4')"
        }}
      />
      <div className="absolute inset-0 z-0 bg-background-light/30 dark:bg-background-dark/30 backdrop-blur-sm" />

      {/* Glassmorphic Header */}
      <header className="absolute top-0 left-0 right-0 z-10 flex items-center justify-between whitespace-nowrap border-b border-solid border-white/20 bg-white/20 px-10 py-3 backdrop-blur-lg">
        <div className="flex items-center gap-4 text-[#36454F] dark:text-[#FAF9F6]">
          <Logo />
          <h2 className="text-[#36454F] dark:text-[#FAF9F6] text-lg font-bold leading-tight tracking-[-0.015em]">
            Cameleon
          </h2>
        </div>
      </header>

      {/* Wardrobe Modal */}
      <div className="relative z-20 flex h-full max-h-[90vh] w-full max-w-6xl flex-col rounded-xl bg-[#FAF9F6]/80 dark:bg-background-dark/80 shadow-2xl shadow-black/10 backdrop-blur-xl dark:border dark:border-white/10">
        {/* Modal Header */}
        <div className="flex flex-shrink-0 items-center justify-between gap-3 border-b border-black/10 p-4 dark:border-white/10">
          <p className="text-[#36454F] dark:text-[#FAF9F6] text-xl font-bold leading-tight tracking-[-0.033em]">
            Your Wardrobe
          </p>
          <button 
            onClick={handleClose}
            className="flex h-8 w-8 cursor-pointer items-center justify-center overflow-hidden rounded-full bg-black/5 text-[#96897B] transition-colors hover:bg-black/10 dark:bg-white/5 dark:text-[#FAF9F6] dark:hover:bg-white/10"
          >
            <span 
              className="material-symbols-outlined text-xl" 
              style={{ fontVariationSettings: "'wght' 300" }}
            >
              close
            </span>
          </button>
        </div>

        {/* Modal Content */}
        <div className="flex-1 overflow-y-auto p-2 sm:p-6">
          <div className="layout-content-container flex flex-1 flex-col">
            <WardrobeCategory title="Tops" items={topsItems} />
            <WardrobeCategory title="Bottoms" items={bottomsItems} />
          </div>
        </div>
      </div>
    </div>
  );
}


"use client";

import { useRouter } from "next/navigation";
import AppHeader from "../components/layout/AppHeader";

export default function OutfitResultPage() {
  const router = useRouter();

  const handleTryOn = () => {
    router.push("/try-on");
  };
  const outfitItems = [
    {
      id: 1,
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuBgU4xfgJrU2aXBE9XPeov-MAAZ3WdMRZysP_oTiRyyO42wx-WC1lBL_Mvu1O0OJAghFI3GtZLWU0wJLMhr1Z2Q8aYUB0khNjGcA-8um9w1yblwzhasvP3D3gtqR0XYpDdvMu89Oa8XAqUp8pRNNjpXFASaQJvh6qKP7Dul51eGlvmpACED95PfpVw7owhUmKMfexZp4g1UwRyBQ15b-c87Et2CePjNq28QlFJoH6fudP_BRb4bjcWuCDx2AgGnsl_dW_KzV5W6XpM",
      alt: "A beige cashmere sweater"
    },
    {
      id: 2,
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAeXzvW_pow7xw0s8Ys7tnqHZiE2tqIqNrN-E3RAGYfviCOe3ExH6CrVsnc0x-qPRaArOd3Vj7QBbjceKUtMwPngbM0cVzwmwVdu7zRxscNu226gext6oLwAxj9NalusOR7J8wsoL_ImCdCQ1SLEuA_WKoKOyYazgzVSNMWDuQqXuaGASf1W4xV_2ST3v1yy7miKAMbV6RF9f6DDA9-6qGP6IAFyoqsNkvve8is6135ztcuw_VL-LBEM4hfNrTGc8J7VCU8Ubb7k94",
      alt: "A light beige trench coat"
    },
    {
      id: 3,
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAmWyESzGnsflEfIb5Udk0zhK7zCrRoTbDBiZPofeGqcRAhzQmpjKV9puczWjuNIsMH2KYdP5P5Z_EyimtX3Z6JCKAzNFyqp5TyAwUsxLElMXJDkGYrqtTEXK7azDrCdtBCHmS4JJUN1Mf2OpFi6--e9yyTUwDwljWcTFpi10tpZ3hSj0mhurqRpcUXsSVgIwqYd64aERMRNGWaUgoASkYtwsk5LQ4h-hgKa4apqhKXnAMsbc4ADmTu4Rj5ozKCrXFg_Ge-47MmrD0",
      alt: "White linen trousers"
    },
    {
      id: 4,
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuBAzwb-uYf0c58eM99hccHYUHYZlE5sujm0civnbSRKox47TkuOnbAPUXps8Gq-wXKItmgSgvayn2NFwc3kD-QBaetTlvhs0Utzh_9C8XoNKkjWBXfeMo5fOv3lFVeTQJ1HZ41Q9UZU_pZDw33tEk07cszhR-rDfy_XZAoA8NTl-d6lMRSyisCkcTI5oGGj5AHfaiaEQikwo_Y2T3Nizjrf2R-uu6ztBZuu2RGA8UhufuHCCTrjEEMzQUYju8UizV_l5S0-Cy4fWog",
      alt: "Brown leather loafers"
    }
  ];

  const outfitDetails = [
    {
      id: 1,
      name: "Zegna - Cashmere Sweater",
      category: "Top",
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuBgU4xfgJrU2aXBE9XPeov-MAAZ3WdMRZysP_oTiRyyO42wx-WC1lBL_Mvu1O0OJAghFI3GtZLWU0wJLMhr1Z2Q8aYUB0khNjGcA-8um9w1yblwzhasvP3D3gtqR0XYpDdvMu89Oa8XAqUp8pRNNjpXFASaQJvh6qKP7Dul51eGlvmpACED95PfpVw7owhUmKMfexZp4g1UwRyBQ15b-c87Et2CePjNq28QlFJoH6fudP_BRb4bjcWuCDx2AgGnsl_dW_KzV5W6XpM",
      alt: "A beige cashmere sweater"
    },
    {
      id: 2,
      name: "Burberry - Trench Coat",
      category: "Layer",
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuCXw-4MkdXXsU8vuj2jQBxArSY6fccVsqlJi3Enr7Rdc7hf_UtlOWXXEDujj8agLiBm2v-YcG2B5gJXkQP87kKpxw6sxZVW60Rw2Wb_As1uotQx4qfa_kAwQpoAgHIp961mXsSUXX2rNCDBrjiQ_Y9e27ndMZq36jU40xrvZz1SsnumcG_UGIYrMxokYJ_DQUPeUJ-t-gEjDL5RrIic4axbf07QL5JgstYsm25GnRos7IxmLp1BhHDyJMbXpuBDGXsc_mCGpnTb0es",
      alt: "A light beige trench coat"
    },
    {
      id: 3,
      name: "Prada - Linen Trousers",
      category: "Bottom",
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAmWyESzGnsflEfIb5Udk0zhK7zCrRoTbDBiZPofeGqcRAhzQmpjKV9puczWjuNIsMH2KYdP5P5Z_EyimtX3Z6JCKAzNFyqp5TyAwUsxLElMXJDkGYrqtTEXK7azDrCdtBCHmS4JJUN1Mf2OpFi6--e9yyTUwDwljWcTFpi10tpZ3hSj0mhurqRpcUXsSVgIwqYd64aERMRNGWaUgoASkYtwsk5LQ4h-hgKa4apqhKXnAMsbc4ADmTu4Rj5ozKCrXFg_Ge-47MmrD0",
      alt: "White linen trousers"
    },
    {
      id: 4,
      name: "Gucci - Leather Loafers",
      category: "Shoe",
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuCUJy2OsFwfJEsnCaumEVKWRdt_x2fZqfVMOvCy7nfBXu-SVAR4W7aQkDRqkIDvlq7yqzrTVxPn8LByd5Osi8-5ciH7wbjfUEDU9pR7OFObZS8HKQPgIhWlavJk7TgnMQ8xgS1SIIQbfOKxycctpIkCEDv-fOHTCdANQSuE5qHxadyQUPBrvspcDY9MidM3t6qXZQiJeMjz4eKbQZgFwAeSpztSp22wT-Jgh0u_SI7f0hYETf7AZQDyMjZ1OL4v5l1QMdlQNr3ZRV4",
      alt: "Brown leather loafers"
    }
  ];

  return (
    <div className="relative flex h-screen w-full flex-col overflow-hidden font-display bg-gradient-to-br from-[#fdfbf7] to-[#f4f1ea] dark:bg-gradient-to-br dark:from-[#2a261a] dark:to-[#211d11] text-text-light dark:text-text-dark scale-page-80">
      <AppHeader />

      {/* Main Content */}
      <main className="flex-1 w-full max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 w-full">
          {/* Left: 2x2 Grid of Outfit Items */}
          <div className="grid grid-cols-2 grid-rows-2 gap-6 aspect-square max-h-[80vh]">
            {outfitItems.map((item) => (
              <div 
                key={item.id}
                className="bg-card-light dark:bg-card-dark p-2 rounded-xl shadow-lg shadow-black/5 backdrop-blur-sm border border-white/50 dark:border-black/20"
              >
                <div 
                  className="w-full h-full bg-center bg-no-repeat bg-cover rounded-lg"
                  style={{ backgroundImage: `url("${item.image}")` }}
                  data-alt={item.alt}
                />
              </div>
            ))}
          </div>

          {/* Right: Outfit Details */}
          <div className="flex flex-col justify-center gap-8 py-8">
            <div className="flex flex-col gap-2">
              <p className="text-4xl lg:text-5xl font-black leading-tight tracking-[-0.033em] text-text-light dark:text-text-dark">
                Coastal Cruise
              </p>
              <p className="text-base font-medium leading-normal text-text-muted-light dark:text-text-muted-dark">
                Vibe: Relaxed Fit
              </p>
            </div>

            {/* Items List */}
            <div className="flex flex-col border border-border-light dark:border-border-dark rounded-xl bg-card-light dark:bg-card-dark overflow-hidden backdrop-blur-sm">
              {outfitDetails.map((item, index) => (
                <div 
                  key={item.id}
                  className={`flex items-center gap-4 min-h-[72px] py-2 px-4 justify-between ${
                    index < outfitDetails.length - 1 ? 'border-b border-border-light dark:border-border-dark' : ''
                  }`}
                >
                  <div className="flex items-center gap-4">
                    <div 
                      className="bg-center bg-no-repeat aspect-square bg-cover rounded-lg size-10"
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
            <div className="flex flex-col sm:flex-row items-center gap-3 w-full mt-4">
              <button 
                onClick={handleTryOn}
                className="flex w-full sm:w-auto sm:flex-1 min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 px-6 bg-primary text-text-light text-base font-bold leading-normal tracking-[0.015em] hover:opacity-90 transition-opacity"
              >
                <span className="truncate">Try On</span>
              </button>

              <button className="flex w-full sm:w-auto min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 px-6 bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark text-text-light dark:text-text-dark text-base font-bold leading-normal tracking-[0.015em] hover:bg-border-light dark:hover:bg-border-dark transition-colors backdrop-blur-sm">
                <span className="truncate">New Suggestion</span>
              </button>

              <button className="flex max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-12 w-12 bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark text-text-light dark:text-text-dark gap-2 text-sm font-bold leading-normal tracking-[0.015em] hover:bg-border-light dark:hover:bg-border-dark transition-colors backdrop-blur-sm">
                <span className="material-symbols-outlined text-2xl">favorite</span>
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}


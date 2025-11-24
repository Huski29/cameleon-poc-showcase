"use client";

import AppHeader from "../components/layout/AppHeader";

export default function TryOnPage() {
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
      name: "Prada - Linen Trousers",
      category: "Bottoms",
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAmWyESzGnsflEfIb5Udk0zhK7zCrRoTbDBiZPofeGqcRAhzQmpjKV9puczWjuNIsMH2KYdP5P5Z_EyimtX3Z6JCKAzNFyqp5TyAwUsxLElMXJDkGYrqtTEXK7azDrCdtBCHmS4JJUN1Mf2OpFi6--e9yyTUwDwljWcTFpi10tpZ3hSj0mhurqRpcUXsSVgIwqYd64aERMRNGWaUgoASkYtwsk5LQ4h-hgKa4apqhKXnAMsbc4ADmTu4Rj5ozKCrXFg_Ge-47MmrD0",
      alt: "White linen trousers"
    },
    {
      id: 3,
      name: "Rolex - Submariner Watch",
      category: "Accessory",
      image: "https://lh3.googleusercontent.com/aida-public/AB6AXuDek28VfDyGD_nycoLKmRIIS0KA6BTzVB6P4KI0GklCbZD8O65cwn0fA7kNjHkangbwxyFwvwC6769NaEbtgAYfPg84KMKJaN6ZqMPqmrGGKcZNNtheigUmpFShqqjMY4ZkuaTC8zpP7XGNJ2lrwezRMA-OcBrLZzc5vNTeUX5LChc0BFug6FGRNY-UM8JDaVNJ64eocOnSjqjBa7-XQGow9KcWrCUJA0pJ8hYvaY8TJDW0jPLCGJ78-C9NhhJNVRuvQrIs4IOU8_Y",
      alt: "A luxury diver's watch"
    }
  ];

  return (
    <div className="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden font-display bg-background-light dark:bg-background-dark text-text-light dark:text-text-dark scale-page-80">
      <AppHeader />

      {/* Main Content */}
      <main className="flex-1 w-full max-w-screen-xl mx-auto py-8 lg:py-16 px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 items-start">
          {/* Left Panel: Image Preview */}
          <div className="lg:col-span-7 flex w-full justify-center">
            <div className="w-[90%] max-w-[calc(36rem*0.9)] aspect-[3/4] bg-card-light dark:bg-card-dark p-2 rounded-xl shadow-lg shadow-black/5">
              <div 
                className="w-full h-full bg-center bg-no-repeat bg-cover rounded-lg"
                style={{
                  backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuAUTHB72dQuCxoH1zmMmb3tcLTZZkrdJsaxXX8rOIaiBllkMmcTPv1i4Ry31B-d3jFlVpc-x3Mo-L2aZ4sr70H2ELdZPEBbTiYEUxQuez0daV4qakd8rGwvIL_ZUokh7cncOcYn04spzmMGAnLWxegN5iEazwb63nvgqz5P-FA6xP6KJQum3yvcRXKDhWRoxiWZ_A1LvQmZPuHT0zowxPHXtaZvZ1ssNhRDHtzpChiO8nbB2QRSfz6-N3UECsd1KVYJY4D0LkrYpI4')"
                }}
                data-alt="A model wearing a relaxed coastal outfit consisting of a cashmere sweater and linen trousers."
              />
            </div>
          </div>

          {/* Right Panel: Details and Actions */}
          <div className="lg:col-span-5 flex flex-col gap-8">
            <div className="flex flex-col gap-2">
              <p className="text-4xl font-black leading-tight tracking-[-0.033em] text-text-light dark:text-text-dark">
                Coastal Cruise
              </p>
              <p className="text-base font-medium leading-normal text-text-muted-light dark:text-text-muted-dark">
                Vibe: Relaxed Fit
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


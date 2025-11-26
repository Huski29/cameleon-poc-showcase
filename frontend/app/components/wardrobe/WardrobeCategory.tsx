'use client';

import { useState } from 'react';
import { WardrobeItem as WardrobeItemCard } from './WardrobeItem';
import type { WardrobeItem } from '../../types';

interface WardrobeCategoryProps {
  title: string;
  items: WardrobeItem[];
  onItemClick?: (item: WardrobeItem) => void;
}

const INITIAL_ITEMS = 7;
const LOAD_MORE_INCREMENT = 8;

export function WardrobeCategory({ title, items, onItemClick }: WardrobeCategoryProps) {
  const [visibleCount, setVisibleCount] = useState(INITIAL_ITEMS);
  
  const visibleItems = items.slice(0, visibleCount);
  const hasMore = visibleCount < items.length;
  
  const handleLoadMore = () => {
    setVisibleCount(prev => Math.min(prev + LOAD_MORE_INCREMENT, items.length));
  };
  
  return (
    <div>
      <h2 className="text-[#36454F] dark:text-[#FAF9F6] text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-5">
        {title}
      </h2>
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 p-4">
        {visibleItems.map((item) => (
          <WardrobeItemCard
            key={item.id}
            item={item}
            onClick={() => onItemClick?.(item)}
          />
        ))}
        
        {hasMore && (
          <button
            onClick={handleLoadMore}
            className="flex flex-col gap-3 rounded-xl bg-white/50 p-3 pb-4 shadow-lg shadow-black/5 transition-all hover:shadow-xl hover:shadow-black/10 dark:bg-white/5 cursor-pointer"
          >
            {/* Image Container with same aspect ratio as items */}
            <div className="relative w-full aspect-[3/4] rounded-lg overflow-hidden">
              {/* Background Image with Blur */}
              {items[visibleCount] && (
                <>
                  <img
                    src={items[visibleCount].image}
                    alt=""
                    className="absolute inset-0 w-full h-full object-cover blur-md scale-110"
                  />
                  <div className="absolute inset-0 bg-white/60 dark:bg-black/60" />
                </>
              )}
              
              {/* Content Overlay */}
              <div className="relative z-10 flex flex-col items-center justify-center h-full gap-2">
                <span className="material-symbols-outlined text-5xl text-[#36454F] dark:text-[#FAF9F6] drop-shadow-lg">
                  arrow_forward
                </span>
                <div className="text-center">
                  <p className="text-[#36454F] dark:text-[#FAF9F6] text-base font-semibold leading-normal drop-shadow-md">
                    Load More
                  </p>
                  <p className="text-[#96897B] dark:text-[#96897B]/80 text-sm font-normal leading-normal drop-shadow-md">
                    {items.length - visibleCount} more
                  </p>
                </div>
              </div>
            </div>
          </button>
        )}
      </div>
    </div>
  );
}


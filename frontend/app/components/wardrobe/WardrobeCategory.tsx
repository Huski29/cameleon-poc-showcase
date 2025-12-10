'use client';

import { useState, useEffect } from 'react';
import { WardrobeItem as WardrobeItemCard } from './WardrobeItem';
import { useWardrobeStore } from '../../stores/useWardrobeStore';
import type { WardrobeItem, ClothingCategory } from '../../types';

interface WardrobeCategoryProps {
  title: string;
  category: ClothingCategory;
  onItemClick?: (item: WardrobeItem) => void;
}

const INITIAL_ITEMS = 7;
const LOAD_MORE_INCREMENT = 8;

export function WardrobeCategory({ title, category, onItemClick }: WardrobeCategoryProps) {
  const { items, fetchItemsByCategory, isLoading } = useWardrobeStore();
  const [loadedCount, setLoadedCount] = useState(0);
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const [hasLoadedInitial, setHasLoadedInitial] = useState(false);
  const [hasMoreItems, setHasMoreItems] = useState(true);
  
  // Get items for this category from store
  const categoryItems = items.filter(i => i.category === category);
  const visibleItems = categoryItems.slice(0, loadedCount || INITIAL_ITEMS);
  
  // Initial load
  useEffect(() => {
    if (!hasLoadedInitial && !isLoading) {
      setHasLoadedInitial(true);
      fetchItemsByCategory(category, INITIAL_ITEMS, 0).then((newItems) => {
        if (newItems.length > 0) {
          setLoadedCount(newItems.length);
          // If we got fewer items than requested, there are no more
          if (newItems.length < INITIAL_ITEMS) {
            setHasMoreItems(false);
          }
        } else {
          setHasMoreItems(false);
        }
      });
    }
  }, [category, hasLoadedInitial, isLoading, fetchItemsByCategory]);
  
  const handleLoadMore = async () => {
    setIsLoadingMore(true);
    const nextOffset = loadedCount;
    
    try {
      const newItems = await fetchItemsByCategory(category, LOAD_MORE_INCREMENT, nextOffset);
      if (newItems.length > 0) {
        setLoadedCount(prev => prev + newItems.length);
        // If we got fewer items than requested, we've reached the end
        if (newItems.length < LOAD_MORE_INCREMENT) {
          setHasMoreItems(false);
        }
      } else {
        // No more items available
        setHasMoreItems(false);
      }
    } catch (error) {
      console.error('Failed to load more items:', error);
      setHasMoreItems(false);
    } finally {
      setIsLoadingMore(false);
    }
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
        
        {hasMoreItems && (
          <button
            onClick={handleLoadMore}
            className="flex flex-col gap-3 rounded-xl bg-white/50 p-3 pb-4 shadow-lg shadow-black/5 transition-all hover:shadow-xl hover:shadow-black/10 dark:bg-white/5 cursor-pointer"
          >
            {/* Image Container with same aspect ratio as items */}
            <div className="relative w-full aspect-[3/4] rounded-lg overflow-hidden">
              {/* Background Image with Blur */}
              {categoryItems[loadedCount] && (
                <>
                  <img
                    src={categoryItems[loadedCount].image}
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
                </div>
              </div>
            </div>
          </button>
        )}
      </div>
    </div>
  );
}


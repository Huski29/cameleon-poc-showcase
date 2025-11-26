import React, { memo, useState } from 'react';
import { WardrobeItem as WardrobeItemType } from '../../types';

interface WardrobeItemProps {
  item: WardrobeItemType;
  onClick?: () => void;
}

export const WardrobeItem = memo(function WardrobeItem({ item, onClick }: WardrobeItemProps) {
  const [imageError, setImageError] = useState(false);

  return (
    <div
      onClick={onClick}
      className="flex flex-col gap-3 rounded-xl bg-white/50 p-3 pb-4 shadow-lg shadow-black/5 transition-all hover:shadow-xl hover:shadow-black/10 dark:bg-white/5 cursor-pointer"
    >
      <div className="w-full aspect-[3/4] rounded-lg overflow-hidden bg-gradient-to-br from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-800">
        {imageError ? (
          <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-800">
            <div className="text-center p-4">
              <span className="material-symbols-outlined text-4xl text-gray-400 dark:text-gray-500 mb-2">
                image_not_supported
              </span>
              <p className="text-xs text-gray-500 dark:text-gray-400">{item.alt}</p>
            </div>
          </div>
        ) : (
          <img
            src={item.image}
            alt={item.alt}
            className="w-full h-full object-cover"
            onError={() => setImageError(true)}
            loading="lazy"
          />
        )}
      </div>
      <div>
        <p className="text-[#36454F] dark:text-[#FAF9F6] text-base font-semibold leading-normal">
          {item.title}
        </p>
        <p className="text-[#96897B] dark:text-[#96897B]/80 text-sm font-normal leading-normal">
          {item.description}
        </p>
      </div>
    </div>
  );
});

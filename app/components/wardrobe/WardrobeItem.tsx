import React, { memo } from 'react';
import { WardrobeItem as WardrobeItemType } from '../../types';

interface WardrobeItemProps {
  item: WardrobeItemType;
  onClick?: () => void;
}

export const WardrobeItem = memo(function WardrobeItem({ item, onClick }: WardrobeItemProps) {
  return (
    <div
      onClick={onClick}
      className="flex flex-col gap-3 rounded-xl bg-white/50 p-3 pb-4 shadow-lg shadow-black/5 transition-all hover:shadow-xl hover:shadow-black/10 dark:bg-white/5 cursor-pointer"
    >
      <div
        className="w-full bg-cover bg-center bg-no-repeat aspect-[3/4] rounded-lg"
        style={{ backgroundImage: `url("${item.image}")` }}
        data-alt={item.alt}
      />
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

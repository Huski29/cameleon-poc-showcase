import { WardrobeGrid } from './WardrobeGrid';
import type { WardrobeItem } from '../../types';

interface WardrobeCategoryProps {
  title: string;
  items: WardrobeItem[];
  onItemClick?: (item: WardrobeItem) => void;
}

export function WardrobeCategory({ title, items, onItemClick }: WardrobeCategoryProps) {
  return (
    <div>
      <h2 className="text-[#36454F] dark:text-[#FAF9F6] text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-5">
        {title}
      </h2>
      <WardrobeGrid items={items} onItemClick={onItemClick} />
    </div>
  );
}


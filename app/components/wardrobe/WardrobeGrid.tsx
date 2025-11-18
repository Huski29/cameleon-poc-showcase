import { WardrobeItem as WardrobeItemCard } from './WardrobeItem';
import type { WardrobeItem } from '../../types';

interface WardrobeGridProps {
  items: WardrobeItem[];
  onItemClick?: (item: WardrobeItem) => void;
}

export function WardrobeGrid({ items, onItemClick }: WardrobeGridProps) {
  return (
    <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4 p-4">
      {items.map((item) => (
        <WardrobeItemCard
          key={item.id}
          item={item}
          onClick={() => onItemClick?.(item)}
        />
      ))}
    </div>
  );
}


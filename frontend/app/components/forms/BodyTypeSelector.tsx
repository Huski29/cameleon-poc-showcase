"use client";

import React, { memo, useCallback } from 'react';
import { cn } from '../../lib/utils';

interface BodyType {
  id: string;
  label: string;
  icon: string;
  transform: string;
}

interface BodyTypeSelectorProps {
  bodyTypes: ReadonlyArray<BodyType>;
  selectedBodyType: string;
  onSelect: (bodyTypeId: string) => void;
}

export const BodyTypeSelector = memo(function BodyTypeSelector({ bodyTypes, selectedBodyType, onSelect }: BodyTypeSelectorProps) {
  const handleSelect = useCallback((id: string) => {
    onSelect(id);
  }, [onSelect]);

  return (
    <div className="grid grid-cols-2 gap-3" role="group" aria-label="Body type selection">
      {bodyTypes.map((type) => (
        <button
          key={type.id}
          onClick={() => handleSelect(type.id)}
          aria-label={`Select ${type.label} body type`}
          aria-pressed={selectedBodyType === type.id}
          className={cn(
            "group flex flex-col items-center justify-center gap-2 rounded-lg border p-4 text-center transition-all",
            selectedBodyType === type.id
              ? "bg-primary/30 border-primary ring-2 ring-primary"
              : "border-[#e7e1d0] dark:border-[#383325] hover:bg-primary/20 hover:border-primary/50 focus:bg-primary/30 focus:border-primary focus:ring-2 focus:ring-primary",
            "text-[#1b180e] dark:text-[#f8f7f6]"
          )}
        >
          <span className={cn(
            "material-symbols-outlined text-3xl opacity-70 group-hover:opacity-100",
            type.transform
          )}>
            {type.icon}
          </span>
          <span className="text-sm font-medium">{type.label}</span>
        </button>
      ))}
    </div>
  );
});

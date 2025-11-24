"use client";

import React, { memo, useCallback } from 'react';
import { cn } from '../../lib/utils';

interface RangeSliderProps {
  label: string;
  value: number;
  onChange: (value: number) => void;
  min?: number;
  max?: number;
  step?: number;
  labels: string[];
}

export const RangeSlider = memo(function RangeSlider({ 
  label, 
  value, 
  onChange, 
  min = 0, 
  max = 2, 
  step = 1, 
  labels 
}: RangeSliderProps) {
  const handleChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    onChange(Number(e.target.value));
  }, [onChange]);

  return (
    <div className="relative flex w-full flex-col items-start justify-between gap-3">
      <p className="text-[#1b180e] dark:text-[#f8f7f6] text-base font-medium leading-normal">
        {label}
      </p>
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={handleChange}
        aria-label={label}
        aria-valuemin={min}
        aria-valuemax={max}
        aria-valuenow={value}
        aria-valuetext={labels[value]}
        className="w-full h-1 bg-transparent cursor-pointer appearance-none focus:outline-none"
      />
      <div className="flex w-full justify-between text-xs text-[#1b180e]/60 dark:text-[#f8f7f6]/60 mt-1">
        {labels.map((label, index) => (
          <span key={index}>{label}</span>
        ))}
      </div>
    </div>
  );
});

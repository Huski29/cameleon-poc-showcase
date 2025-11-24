"use client";

import { useState, useRef, useEffect } from "react";
import { createPortal } from "react-dom";

interface CustomSelectProps {
  value: string;
  onChange: (value: string) => void;
  options: string[];
  label: string;
}

export function CustomSelect({ value, onChange, options, label }: CustomSelectProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [dropdownPosition, setDropdownPosition] = useState({ top: 0, left: 0, width: 0 });
  const buttonRef = useRef<HTMLButtonElement>(null);
  const dropdownRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node) &&
        buttonRef.current &&
        !buttonRef.current.contains(event.target as Node)
      ) {
        setIsOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  useEffect(() => {
    const updatePosition = () => {
      if (isOpen && buttonRef.current) {
        const rect = buttonRef.current.getBoundingClientRect();
        setDropdownPosition({
          top: rect.bottom + 8,
          left: rect.left,
          width: rect.width,
        });
      }
    };

    updatePosition();
    window.addEventListener('scroll', updatePosition, true);
    window.addEventListener('resize', updatePosition);

    return () => {
      window.removeEventListener('scroll', updatePosition, true);
      window.removeEventListener('resize', updatePosition);
    };
  }, [isOpen]);

  const handleOpen = () => {
    setIsOpen(true);
  };

  return (
    <div className="flex flex-col gap-2">
      <label className="text-sm font-semibold text-text-light dark:text-text-dark">{label}</label>
      <div className="relative">
        <button
          ref={buttonRef}
          type="button"
          onClick={handleOpen}
          className="w-full px-4 py-3 pr-10 rounded-xl border border-border-light dark:border-border-dark bg-card-light dark:bg-card-dark text-text-light dark:text-text-dark focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50 backdrop-blur-sm text-left"
        >
          {value}
        </button>
        <span className="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-text-muted-light dark:text-text-muted-dark pointer-events-none">
          expand_more
        </span>

        {isOpen &&
          typeof window !== "undefined" &&
          createPortal(
            <div
              ref={dropdownRef}
              className="fixed z-[9999] bg-card-light dark:bg-card-dark border border-border-light dark:border-border-dark rounded-xl shadow-xl overflow-hidden backdrop-blur-lg"
              style={{
                top: `${dropdownPosition.top}px`,
                left: `${dropdownPosition.left}px`,
                width: `${dropdownPosition.width}px`,
              }}
            >
              {options.map((option) => (
                <button
                  key={option}
                  type="button"
                  onClick={() => {
                    onChange(option);
                    setIsOpen(false);
                  }}
                  className={`w-full px-4 py-3 text-left transition-colors ${
                    value === option
                      ? "bg-primary text-white font-medium"
                      : "text-text-light dark:text-text-dark hover:bg-primary/10"
                  }`}
                >
                  {option}
                </button>
              ))}
            </div>,
            document.body
          )}
      </div>
    </div>
  );
}


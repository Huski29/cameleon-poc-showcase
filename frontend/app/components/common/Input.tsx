import React from 'react';
import { cn } from '../../lib/utils';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

export function Input({ 
  label, 
  error, 
  className, 
  id,
  ...props 
}: InputProps) {
  const inputId = id || `input-${Math.random().toString(36).substr(2, 9)}`;
  
  return (
    <div className="flex flex-col gap-2">
      {label && (
        <label 
          htmlFor={inputId}
          className="text-sm font-semibold text-text-light dark:text-text-dark"
        >
          {label}
        </label>
      )}
      <input
        id={inputId}
        className={cn(
          "w-full px-4 py-3 rounded-xl border border-border-light dark:border-border-dark",
          "bg-card-light dark:bg-card-dark text-text-light dark:text-text-dark",
          "focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50",
          "backdrop-blur-sm",
          error && "border-red-500 focus:border-red-500 focus:ring-red-500/50",
          className
        )}
        {...props}
      />
      {error && (
        <span className="text-sm text-red-600 dark:text-red-400">{error}</span>
      )}
    </div>
  );
}


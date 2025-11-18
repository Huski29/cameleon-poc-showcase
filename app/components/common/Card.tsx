import React from 'react';
import { cn } from '../../lib/utils';

interface CardProps {
  children: React.ReactNode;
  className?: string;
}

export function Card({ children, className }: CardProps) {
  return (
    <div
      className={cn(
        "rounded-xl border border-border-light dark:border-border-dark",
        "bg-card-light dark:bg-card-dark backdrop-blur-sm",
        "shadow-lg",
        className
      )}
    >
      {children}
    </div>
  );
}


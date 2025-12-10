import React, { memo } from 'react';
import Image from 'next/image';

export const Logo = memo(function Logo() {
  return (
    <div className="relative h-12 sm:h-16 w-auto">
      <Image
        src="/Cameleon_logo_new.png"
        alt="Cameleon"
        width={300}
        height={60}
        className="object-contain h-full w-auto"
        priority
      />
    </div>
  );
});

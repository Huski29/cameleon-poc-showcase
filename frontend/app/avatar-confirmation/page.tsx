"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { useUserStore } from "../stores/useUserStore";

export default function AvatarConfirmationPage() {
  const router = useRouter();
  const { profile, updateUser } = useUserStore();
  const [uploadedImage, setUploadedImage] = useState<string | null>(null);

  useEffect(() => {
    // Get the pending profile picture from localStorage
    const pendingImage = localStorage.getItem('pendingProfilePicture');
    if (pendingImage) {
      setUploadedImage(pendingImage);
    }
  }, []);

  const handleClose = () => {
    // Clear pending image
    localStorage.removeItem('pendingProfilePicture');
    router.back();
  };

  const handleConfirm = async () => {
    // Save the uploaded image to the database
    if (uploadedImage) {
      await updateUser({ profilePicture: uploadedImage });
      localStorage.removeItem('pendingProfilePicture');
    }
    router.push("/generate");
  };

  const handleRegenerate = () => {
    localStorage.removeItem('pendingProfilePicture');
    router.push("/");
  };

  // Determine which image to display
  const displayImage = uploadedImage || profile?.user?.profilePicture || "https://lh3.googleusercontent.com/aida-public/AB6AXuCFgDwjyKw1e07dYoAojo5sNtYx83L-mRY3sICsQUDEnQ5F9FNN1MWxsoVRhCuifaiJAFuzkSTbLzWIhK_anA7SrFic1qpj_ToWDgJzGPYyTcsF6r6f-xOX6s1NTo3eUggFototNJPiiJbtUuXXzl5bYIA4UUtmqf2u8VaQv1NjSpPPo9YFRM4oqucfPzrYEj5jCAzNwEuKX6OO6rS8M17KRbbbOF2HvcNmBJcMQDIiGBlQwgZ6ukrs0JzUWxK580ke2a2ZUpZnrxQ";

  return (
    <div className="relative flex min-h-screen w-full flex-col bg-gradient-to-b from-[#F5F1EA] to-[#FFFBF5] text-[#4A4A4A] dark:from-[#3a3529] dark:to-[#211d11] dark:text-gray-300">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 z-10 p-4">
        <div className="container mx-auto">
          <div className="glassmorphic flex items-center justify-between rounded-xl px-6 py-3 shadow-sm">
            <div className="flex items-center gap-3 text-[#4A4A4A] dark:text-white">
              <div className="size-6">
                <svg fill="currentColor" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
                  <g clipPath="url(#clip0_6_319)">
                    <path d="M8.57829 8.57829C5.52816 11.6284 3.451 15.5145 2.60947 19.7452C1.76794 23.9758 2.19984 28.361 3.85056 32.3462C5.50128 36.3314 8.29667 39.7376 11.8832 42.134C15.4698 44.5305 19.6865 45.8096 24 45.8096C28.3135 45.8096 32.5302 44.5305 36.1168 42.134C39.7033 39.7375 42.4987 36.3314 44.1494 32.3462C45.8002 28.361 46.2321 23.9758 45.3905 19.7452C44.549 15.5145 42.4718 11.6284 39.4217 8.57829L24 24L8.57829 8.57829Z" />
                  </g>
                  <defs>
                    <clipPath id="clip0_6_319">
                      <rect fill="white" height="48" width="48" />
                    </clipPath>
                  </defs>
                </svg>
              </div>
              <h2 className="text-xl font-bold tracking-tight">Cameleon</h2>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow flex items-center justify-center">
        {/* Background Image with Opacity */}
        <div 
          className="absolute inset-0 bg-cover bg-center opacity-20" 
          style={{
            backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuA_yIMI_daMGU3kqRKGJM0h9s6Bt8NkmLcPu4fvypBxzfX0Pyi_Ex9vuXSaNml8subaaZOouJwijp52oWP9RTlHHWJSz6AKuAX-x2rRZt3muGfR4PdDwsNDOBSI3giwRhUOPdmGpzD7NIlZrigvzEWb3aJONm9aTcUmQQu3WyfLX9Dfl3j5BJoRYFfJAylIl8CVDPhh0oOo1NkbuD_sXPOdvWxsiPl27EdRjUwuPUg9w57EONy06aQfn1VIoAzE4DfjWFjcQLHMfP4')"
          }}
        />

        {/* Modal Overlay */}
        <div className="fixed inset-0 z-40 flex items-center justify-center bg-black/50 p-4">
          <div className="relative w-full max-w-md mx-auto">
            <div className="glassmorphic flex flex-col overflow-hidden rounded-xl shadow-lg w-full">
              {/* Close Button */}
              <button 
                onClick={handleClose}
                className="absolute top-4 right-4 z-10 flex h-8 w-8 cursor-pointer items-center justify-center rounded-full bg-black/10 text-white transition-colors hover:bg-black/20 dark:bg-white/10 dark:hover:bg-white/20"
              >
                <span className="material-symbols-outlined text-xl">close</span>
              </button>

              {/* Avatar Image */}
              <div className="w-full">
                <img
                  alt="AI-generated full-body avatar of a person with stylish clothing in a soft, elegant setting."
                  className="w-full h-auto object-cover"
                  src={displayImage}
                />
              </div>

              {/* Action Buttons */}
              <div className="w-full p-6">
                <div className="flex w-full flex-col items-stretch gap-3">
                  <button 
                    onClick={handleConfirm}
                    className="flex h-12 min-w-[84px] w-full cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-lg bg-[#A67B5B] text-base font-bold text-white transition-opacity hover:opacity-90"
                  >
                    <span className="material-symbols-outlined text-xl">check_circle</span>
                    <span className="truncate">Confirm Avatar</span>
                  </button>

                  <button 
                    onClick={handleRegenerate}
                    className="flex h-12 min-w-[84px] w-full cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-lg border border-[#A67B5B]/50 bg-transparent text-base font-bold text-[#A67B5B] transition-colors hover:bg-[#A67B5B]/10 dark:text-[#d3bca8] dark:border-[#d3bca8]/50 dark:hover:bg-[#d3bca8]/10"
                  >
                    <span className="material-symbols-outlined text-xl">autorenew</span>
                    <span className="truncate">Regenerate Avatar</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}


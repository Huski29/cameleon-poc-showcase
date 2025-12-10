import type { UserProfile, WardrobeItem, Notification, Outfit } from '../types';
import { DEFAULT_PROFILE_PICTURE } from '../constants';

export const mockUserProfile: UserProfile = {
  user: {
    id: "user-1",
    name: "Sarah Johnson",
    email: "sarah.j@email.com",
    profilePicture: DEFAULT_PROFILE_PICTURE,
    gender: "female",
  },
  avatar: {
    height: "Regular",
    volume: "Mid",
    bodyType: "Rectangle",
  },
  preferences: {
    stylePreference: "Smart Casual",
    colorPalette: "Neutral & Earth Tones",
    budget: "Mid-Range",
  },
};

export const mockWardrobeItems: WardrobeItem[] = [
  {
    id: 1,
    category: "tops",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuDbri_km-ADGYg6rWqwctuYCw24n3O8E03OufwQ6sqYzkUwMydHjCiwsWEFiPmqLqWpvn0r6DiqVbd3d6IyPS67sIJMauQIVAe56LmDJTEOsVJ50sK7org0Lrs1tQF8xMt2oNVzL7XQPdW-tc2NyZnxd7pOr_eLOFT71OebCZGKabF2w_Ez-HnVfi-D7Ppdsp2Y4khQCocEtk2aZclidV0dJ1zU7SG1Ykg18I_7nXgQdqiag_pC8FObLfkCPPsqdxxWYs_AJVt3rKo",
    alt: "Cream cashmere crewneck sweater",
    title: "Everlane Cashmere",
    description: "Cream sweater, size M",
  },
  {
    id: 2,
    category: "tops",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuC1ngT1vBIsqU2HMo910q7DdqUb2wcyyeRSLsHErVzF-szAW8ghJNoINDjkplhGeQc2v_fh9Mkz2lqUWtmZ_F0CzvaROqryJLBXi8GHSw8vn5oSTQROzS2RE3hxL9msf3LVOfhaiJ8bHbwbuwt2yBZqEAtasu7tLgWbf6rX1aZvgX9cpD-NgjgnSDvOiGHcdIgXO8YjDRbM5VYFvJ8kXB1XulYIQ1JjnuG3a0KJbD_t8gezPC4EpPnJGmBV4VBNozisCRVfqMv9B8c",
    alt: "Blush pink silk camisole",
    title: "Silk Camisole",
    description: "Blush pink, size S",
  },
  {
    id: 3,
    category: "tops",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuA06C65_8XwfMF1HxRbk5WKB3nONXtGSkn07V_FXDJTsH6pRaUXsnqF2R_T8UqygdEYJEaweC1MW3p6kidMMSWdGPe0hEZ8gT7SI7CT6Ou1MXru6WeUVnH-HaDdnNnJhC8nm__9PIZz7S59LHeGaXrX0OiFHl8ymBx6KGR4t7pWQJs3-0QbNqexRIICDhUVrzdcTL5IbscE0TjhRRAkjxT6nvxUo4eqJ1pKQoSXMm0ZJrGpDWlBOuT2KY_N2PZUADKgrwnfrsNFnc0",
    alt: "Classic white t-shirt",
    title: "Classic White Tee",
    description: "Cotton blend, size S",
  },
  {
    id: 4,
    category: "tops",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuAmCBX0tVTlP74XG-t59FttALHCiI43nxZKYGNEvQ3M0A2NbcFiaDhkIR03l4AIIurNKUP0-ROUQqdpBDQTuCUe6X7fAj-HTxAqaZcTj3pHXQRANYWChV6xbPcZiXpvKXXs7IUoHM8SvWPEHMWuDsw5cnm8jDWjREsCPe1MhcNpistlnMDzgR6pPixLG6VcjiGsTMKGurjr7srX43zuRRTVVZLELvDPMsZI9KJkLX-ho7pXg-yk9tn4vrAvupjr9sbe_IUb4Rac7LU",
    alt: "Beige linen button-down shirt",
    title: "Linen Button-Down",
    description: "Beige, size M",
  },
  // Bottoms
  {
    id: 5,
    category: "bottoms",
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuCDBJQRrjpCChvtByKQu_VT88ooY90B8JdixF1YfNrrSvaDbTIjqd3oNLM9Mj1S5VwaVO0jEMuj80vk8xnSInQVoC70_-bH4PPKU-itM-2tCNU_9gD-tvUkjQ4pysxhgXFcZqLlKobO29gbsUB-ng4lHy2AByML4HHzmBjKDXlglka76WWsdwcLf80b_mviU4_KLPnPO9Xw8aVmAJIylmV8-505pVxd8xSo-FFEVCgtCq_mJMS349s1G9N6AmunnppyYGbbnkiEKxI",
    alt: "High-waisted denim jeans",
    title: "Levi's Wedgie Fit",
    description: "Light wash denim, size 27",
  },
];

export const mockWardrobePreviewItems = [
  {
    id: 1,
    alt: "Black t-shirt on a hanger",
    src: "https://lh3.googleusercontent.com/aida-public/AB6AXuDMH0BJDhkxd9l1GfYjqeGWJ5RMgFQrdV_6RpsMjp1sWX7TDdpbCcu5EStR2wTijy-OzR07AFHcKKSvBMr_8o21v85BI_mS1FaMgSwE791ZzzvbisiI6ErbGrfMJYAXiDWsd3RrRK9sd_CQZ3q60Jq7Ra7Ao0HlYpfQNtu9DTh3c5a61IXPsCrErGixtrpdjSMufLZ5Pl5-5_VtQ0q7oJPpRj0uHsw3oG4Gwb7IVsOtF2J4t9x6PcjETZfIUP5SSApJThWDSfRzGy0"
  },
  {
    id: 2,
    alt: "Beige hoodie on a hanger",
    src: "https://lh3.googleusercontent.com/aida-public/AB6AXuDu8fHo_Ys6sMBA6NUBCe_MUNIHS3a8e7vuqbJU48Og46ABl2TQ4CUxYtKLz7REH9ZBJi3UF4gX7IKtIMcsQk59xjTjv6E6dyHfABsqJzZ5pxhpnpbffw0bNFWnrDdcBD9aDW9FCcZSNbhDUtu0RAL2VrBDBksAGIw1U62CDchtHQMtX9zb6mrVpz18EMRHUkLMKyuad5CGIq_cozaneJiZWfpibGk9SDQ9NruUoi7bb2Vina9pTVcRsX8iL1IwYDOcNbBM3JjXkxk"
  },
  {
    id: 3,
    alt: "Folded blue jeans on a surface",
    src: "https://lh3.googleusercontent.com/aida-public/AB6AXuCTmt0nhDkW6RHPsFrY68bzCaaPwEz0LTrejBrRCr6DXYfNT-4Klvy-uVWR6qUDyxw_lCu38CQtQIck8IyDJJp5PEb2tEKx32cloDL4lZniryubqgSbNnAlph8cXpI3bZEOI-gKDdlf6dy_95B_1Uz00qVzLWA0ooBCbh4jQsJg8vE8ANRv7gCLtkXAZs9KB5qihpVaoolKyf76QB-aY3_TeOP8L5JcZrBnvJBt8G84nM9nrbVofZyFEB6eskWtezd4ab-thDcBUbA"
  },
  {
    id: 4,
    alt: "Red and white sports shoe",
    src: "https://lh3.googleusercontent.com/aida-public/AB6AXuBDs6HCpxVQH7PEp867mrXsdmdQhNxE2ivVyXjrMAugu70D7iSTwxe4-MaF6ZpSYJkRIVCVpwyGNZmin15ZBhuOvs15sm8A8PWZNR5oTd9LYvjXgBs8a490_CVZk_H2r_moPGxamYfaPuxkdoFsz2uC1oURN2t1HKZhmWpUy3DBVVcmB8o4HyvmOlUrkLSQ4o_XYGJ-S-JYcFnhsWnWsxnxvVwz4GOoPAVHHJ0HFXMjWj5h3ZjiFiVbnUuddDyhYErG27Ib5NCVE3c"
  },
  {
    id: 5,
    alt: "Stylish brown leather jacket",
    src: "https://lh3.googleusercontent.com/aida-public/AB6AXuD03mbG8m4iPKIge8TKt-a9rNISxy3wbZ-bZ3N-i_O-cXQyDVh0B_eWo8eT1Kg7Bpz1sWE3Zt9dcWwlRNJ44NzTPcGB932mAdYUAY2fgNMZ8w07Yu3z_sWP84mtjFzO2JzcE3bvEaGP2ZYHm-GF7HWqaoRfjGuj3EHkcWf_qMAbJGuBNVq6BpzTXc_wH5sw6lAMDl9cF8dRLQdJ7GvVZXQbvaEAjeRzs-g3GmJF8FiCyGnpUwL69Q69n86RYv5DzwAmQ0K0v7a4b_M"
  },
  {
    id: 6,
    alt: "Classic white sneakers",
    src: "https://lh3.googleusercontent.com/aida-public/AB6AXuDEY7ktEvJc6lpD2Y8RTviT3YHoJfQMaELgwVBe5FTlzh-OL581PhtrhnAC36x_UsF1Jr7LfkeJI5qUhio0TWGMbsiqSknVqSOGpXYToJIyibEFHOjSWLvMEWHJu9B51-HzbI02HwqjSRN4ClNjBdmGeDUfqak9ODNZKH1biAbl5wgmvGSJ305Hl4figvsZ3-PJm9veEmzp7BS4jIwdxgJ_uCKNvPEUY7nhnUFH1deRn5yBjfUNgSc4UVwO7LfaNCzcgw3sS6VPnTk"
  },
];

export const mockNotifications: Notification[] = [
  { id: 1, text: "New outfit suggestion available", time: "5m ago", unread: true },
  { id: 2, text: "Your wardrobe has been updated", time: "1h ago", unread: true },
  { id: 3, text: "Style Guide: Summer trends are here", time: "3h ago", unread: false },
  { id: 4, text: "New items added to your favorites", time: "5h ago", unread: false },
  { id: 5, text: "Coastal Cruise outfit is ready", time: "1d ago", unread: false },
  { id: 6, text: "Weekly style tips are available", time: "2d ago", unread: false },
  { id: 7, text: "Your avatar has been generated", time: "3d ago", unread: false },
  { id: 8, text: "New wardrobe items suggested", time: "4d ago", unread: false },
];

export const mockOutfits: Outfit[] = [
  {
    id: "outfit-1",
    title: "Smart Casual Weekend",
    vibe: "Relaxed yet put-together",
    items: [
      {
        id: 1,
        type: "Top",
        image: mockWardrobeItems[0].image,
        name: "Cashmere Sweater",
        brand: "Everlane",
      },
      {
        id: 2,
        type: "Bottom",
        image: mockWardrobeItems[4].image,
        name: "High-Waisted Jeans",
        brand: "Levi's",
      },
    ],
    generatedAt: new Date(),
  },
];


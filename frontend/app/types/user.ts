export type BodyType = 'Triangle' | 'Inverted Triangle' | 'Round' | 'Rectangle' | 'Trapezium' | 'Not Sure';
export type HeightRange = 'Petite' | 'Regular' | 'Tall';
export type VolumeRange = 'Lean' | 'Mid' | 'Plus';
export type Gender = 'male' | 'female' | 'unisex';

export interface User {
  id: string;
  name: string;
  email: string;
  profilePicture: string;
  gender: Gender;
}

export interface StyleAvatar {
  height: HeightRange;
  volume: VolumeRange;
  bodyType: BodyType;
}

export interface StylePreferences {
  stylePreference: string;
  colorPalette: string;
  budget: string;
}

export interface UserProfile {
  user: User;
  avatar: StyleAvatar;
  preferences: StylePreferences;
}


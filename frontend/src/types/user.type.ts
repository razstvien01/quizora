export interface IdentityDto {
  provider: string;
  providerUserId: string;
  authId: string;
}

export interface UserDto {
  email: string;
  firstName: string;
  lastName: string;
  picture?: string;
  role: string;
  identity: IdentityDto;
  provider: string;
}

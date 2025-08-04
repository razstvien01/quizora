import type { UserDto } from "@/types/user.type";

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const buildUserDto = (auth0User: any): UserDto => {
  const [provider, providerUserId] = auth0User.sub.split("|");
  console.log("Auth0 User:", auth0User);
  const identity = {
    provider,
    providerUserId,
    authId: auth0User.sub,
  };

  return {
    email: auth0User.email,
    firstName: auth0User.given_name || "",
    lastName: auth0User.family_name || "",
    picture: auth0User.picture,
    role: "student",
    identity,
    provider,
  };
};

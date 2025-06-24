import { useAuth0 } from "@auth0/auth0-react";
import { registerUser as register } from "@/services/authService";

export const useRegisterUser = () => {
  const { getAccessTokenSilently } = useAuth0();

  const registerUser = async () => {
    const token = await getAccessTokenSilently();
    return register(token);
  };

  return { registerUser };
};

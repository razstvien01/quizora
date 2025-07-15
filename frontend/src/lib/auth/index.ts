import { ROUTES } from "@/constants/routes";
import { useAuth0 } from "@auth0/auth0-react";

export function useAuthActions() {
  const {
    user,
    loginWithRedirect,
    logout,
    isAuthenticated,
    isLoading,
    getAccessTokenSilently,
  } = useAuth0();

  const handleLogin = async () => {
    await loginWithRedirect({
      appState: { returnTo: ROUTES.DASHBOARD },
    });
  };

  const handleLogout = async () => {
    logout({ logoutParams: { returnTo: window.location.origin } });
  };

  return {
    user,
    handleLogin,
    handleLogout,
    isAuthenticated,
    isLoading,
    getAccessTokenSilently,
  };
}

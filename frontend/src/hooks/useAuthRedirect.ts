import { ROUTES } from "@/constants/routes";
import { registerUser } from "@/services/authService";
import { useAuth0 } from "@auth0/auth0-react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export function useAuthRedirect(options?: { requireAuth?: boolean }) {
  const { isAuthenticated, isLoading, getAccessTokenSilently } = useAuth0();
  const navigate = useNavigate();

  useEffect(() => {
    const syncAndRedirect = async () => {
      try {
        const token = await getAccessTokenSilently();

        console.log(token);
        await registerUser(token);

        navigate(ROUTES.DASHBOARD);
      } catch (error) {
        console.error("Auth redirect/register error:", error);
      }
    };

    if (!isLoading) {
      if (isAuthenticated) syncAndRedirect();
      else if (options?.requireAuth) navigate(ROUTES.HOME);
    }
  }, [isAuthenticated, isLoading, getAccessTokenSilently, navigate, options]);
}

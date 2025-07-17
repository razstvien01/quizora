import { ROUTES } from "@/constants/routes";
import { useAuthActions } from "@/lib/auth";
import { registerUser } from "@/services/authService";
import { useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";

export function useAuthRedirect(options?: { requireAuth?: boolean }) {
  const { isAuthenticated, isLoading, getAccessTokenSilently, handleLogout } =
    useAuthActions();
  const navigate = useNavigate();
  const didRegisterRef = useRef(false); //? prevent multiple triggers

  useEffect(() => {
    const syncAndRedirect = async () => {
      try {
        const token = await getAccessTokenSilently();

        if (!didRegisterRef.current) {
          await registerUser(token);
          didRegisterRef.current = true;
        }

        navigate(ROUTES.DASHBOARD);
      } catch (error) {
        console.error("Auth redirect/register error:", error);
        if (options?.requireAuth) handleLogout();
      }
    };

    if (!isLoading && isAuthenticated && !didRegisterRef.current) {
      syncAndRedirect();
    } else if (!isLoading && !isAuthenticated && options?.requireAuth)
      navigate(ROUTES.HOME);
  }, [
    isAuthenticated,
    isLoading,
    getAccessTokenSilently,
    navigate,
    options,
    handleLogout,
  ]);
}

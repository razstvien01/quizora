export const API_BASE_URL =
  import.meta.env.VITE_API_URL || "http://localhost:8000/api";

export const API_ENDPOINTS = {
  REGISTER_USER: `${API_BASE_URL}/register/`,
  LOGIN_USER: `${API_BASE_URL}/login/`,
};

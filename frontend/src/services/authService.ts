import { API_ENDPOINTS } from "@/constants/api";
import axios from "axios";

export const registerUser = async (token: string) => {
  return axios.post(
    API_ENDPOINTS.REGISTER_USER,
    {},
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );
};

import { API_ENDPOINTS } from "@/constants/api";
import type { UserDto } from "@/types/user.type";
import axios from "axios";

export const registerUser = async (token: string, userDto: UserDto) => {
  return axios.post(API_ENDPOINTS.AUTH, userDto, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};

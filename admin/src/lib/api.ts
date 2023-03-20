import api from "@/api/$api";
import aspida from "@aspida/axios";
import axios from "axios";
import { stringify, parse } from "querystring";

const axiosInstance = axios.create();
axiosInstance.interceptors.request.use((config) => {
  console.log(config.url);
  // 末尾にスラッシュなかったら追加
  if (config.url && config.url[config.url.length - 1] !== "/") {
    config.url += "/";
  }
  return config;
});

export const defaultApi = api(
  aspida(axiosInstance, {
    baseURL: process.env.NEXT_PUBLIC_BACKEND_URL,
    paramsSerializer: {
      encode: parse as any,
      serialize: stringify as any,
    },
  })
);

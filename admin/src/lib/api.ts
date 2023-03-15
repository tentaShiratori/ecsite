import api from "@/api/$api";
import axiosClient from "@aspida/axios";
import axios from "axios";

export const defaultApi = api(
  axiosClient(axios.create({ baseURL: "http://localhost:8000" }))
);

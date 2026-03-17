import axios from "axios"

const API_URL = "https://supply-chain-assistant-4jy2.onrender.com/api"

const api = axios.create({
  baseURL: API_URL,
  headers: { "Content-Type": "application/json" }
})

export default api

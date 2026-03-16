import axios from "axios"

const API = import.meta.env.VITE_API_URL

export const sendMessage = async (message) => {
  const res = await axios.post(`${API}/chat`, { message })
  return res.data
}

export const uploadFile = async (file) => {
  const form = new FormData()
  form.append("file", file)
  const res = await axios.post(`${API}/upload`, form)
  return res.data
}

import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000/api";

export const getCustomers = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/customers`);
    return response.data.data; // clean backend response
  } catch (error) {
    console.error("API Error:", error.message);
    return [];
  }
};

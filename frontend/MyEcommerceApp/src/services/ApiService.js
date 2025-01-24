import axios from 'axios';

const API_URL = 'https://your-backend-api-url.com';

const ApiService = {
  getProducts: async () => {
    try {
      const response = await axios.get(`${API_URL}/products`);
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  },
};

export default ApiService;

import { ref, computed } from 'vue'
import axios from 'axios'

// Create axios instance with base configuration
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
})

// Request interceptor for adding auth tokens, etc.
apiClient.interceptors.request.use(
  (config) => {
    // Add auth token if available
    const token = localStorage.getItem('auth_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// Response interceptor for handling common errors
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle common HTTP errors
    if (error.response?.status === 401) {
      // Handle unauthorized - redirect to login
      localStorage.removeItem('auth_token')
      // You might want to emit an event or use a store action here
    }
    return Promise.reject(error)
  }
)

export function useApi(endpoint = '') {
  const loading = ref(false)
  const error = ref(null)
  const data = ref(null)

  // Computed property to check if request is idle
  const isIdle = computed(() => !loading.value && !error.value)

  // Generic request method
  const request = async (config) => {
    loading.value = true
    error.value = null
    
    try {
      const response = await apiClient(config)
      data.value = response.data
      return response;
    } catch (err) {
      if(err.status === 400){
        if(err.response.data){
          const errorArray = [];
          const data = err.response.data;
          Object.keys(data).forEach(property => {
            errorArray.push(`${property}: ${data[property]}`)
          });

          if(errorArray.length){
            return {
              errors: errorArray
            };
          }
        }
      }
      error.value = {
        message: err.response?.data?.message || err.message || 'An error occurred',
        status: err.response?.status,
        data: err.response?.data
      }
      throw error.value
    } finally {
      loading.value = false
    }
  }

  // GET request
  const get = async (url = endpoint, config = {}) => {
    return request({
      method: 'GET',
      url,
      ...config
    })
  }

  // POST request
  const post = async (url = endpoint, data = {}, config = {}) => {
    return request({
      method: 'POST',
      url,
      data,
      ...config
    })
  }

  // PUT request
  const put = async (url = endpoint, data = {}, config = {}) => {
    return request({
      method: 'PUT',
      url,
      data,
      ...config
    })
  }

  // PATCH request
  const patch = async (url = endpoint, data = {}, config = {}) => {
    return request({
      method: 'PATCH',
      url,
      data,
      ...config
    })
  }

  // DELETE request
  const del = async (url = endpoint, config = {}) => {
    return request({
      method: 'DELETE',
      url,
      ...config
    })
  }

  // Clear error state
  const clearError = () => {
    error.value = null
  }

  // Reset all state
  const reset = () => {
    loading.value = false
    error.value = null
    data.value = null
  }

  return {
    // State
    loading: computed(() => loading.value),
    error: computed(() => error.value),
    data: computed(() => data.value),
    isIdle,

    // Methods
    request,
    get,
    post,
    put,
    patch,
    delete: del,
    clearError,
    reset,

    // Axios instance for advanced usage
    apiClient
  }
}
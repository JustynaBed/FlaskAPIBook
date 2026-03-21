import axios from "axios";

export const fetchAuthors = () => {
  return axios.get("/api/v1/authors")
    .then(response => response.data)
}

export const deleteAuthor = (id) => {
  return axios.delete(`/api/v1/authors/${id}`)
    .then(response => response.data)
}

export const createAuthor = (data) => {
  return axios.post('/api/v1/authors', data)
    .then(response => response.data)
}

export const editAuthor = (data) => {
  return axios.put(`/api/v1/authors/${data.id}`, data)
    .then(response => response.data)
} 
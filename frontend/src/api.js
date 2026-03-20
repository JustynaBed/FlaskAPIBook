import axios from "axios";

export const fetchAuthors = () => {
  return axios.get("/api/v1/authors")
    .then(response => response.data);
};

export const deleteAuthor = (id) => {
  return axios.delete(`/api/v1/authors/${id}`)
    .then(response => response.data);
};
export const fetchAuthors = () => {
  let url = '/api/v1/authors'
  return fetch(url).then(response => 
    response.json())
}
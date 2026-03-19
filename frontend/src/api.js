export const fetchAuthors = () => {
  let url = '/api/v1/authors'
  return fetch(url).then(response => 
    response.json())
}

export const deleteAuthor = (id) => {
  let url = '/api/v1/authors/' + id
  return fetch(url, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },  
  }).then(response => 
    response.json())
}
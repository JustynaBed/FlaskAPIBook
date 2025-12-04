<template>
  <h1>{{ message }}</h1>
  <p>Liczba autoróww: {{ count }}</p>
  <AuthorList
    :authors="authors"
    @delete-author="deleteAuthor"
  />
  <AuthorForm @author-added="getAuthors" />
</template> 

<script setup>
import AuthorList from './AuthorsList.vue'
import AuthorForm from './AuthorForm.vue'
import { ref, onMounted } from 'vue'
import * as API from './api.js'

const authors = ref([])
const message = ref('')
const count = ref(0)

onMounted(() => {
  getAuthors()
})

const getAuthors = () => {
  console.log('1')
  API.fetchAuthors()
    .then((data) => {
      authors.value = data.data
      count.value = data.number_of_records
      message.value = data.success ? 'Lista autorów' : 'Błąd podczas pobierania danych'
    })
    .catch((error) => {
      console.error('Fetch error:', error)
      message.value = 'Błąd połączenia z serwerem'
    })
  // fetch('/api/v1/authors', {
  //   method: 'GET',
  //   headers: {
  //     'Content-Type': 'application/json',
  //   },
  // })
  //   .then((response) => response.json())
  //   .then((data) => {
  //     authors.value = data.data
  //     count.value = data.number_of_records
  //     message.value = data.success ? 'Lista autorów' : 'Błąd podczas pobierania danych'
  //   })
  //   .catch((error) => {
  //     console.error('Fetch error:', error)
  //     message.value = 'Błąd połączenia z serwerem'
  //   })
}

function deleteAuthor(authorId) {
  fetch(`/api/v1/authors/${authorId}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to delete author')
      }
      // Refresh the authors list after deletion
      getAuthors()
    })
    .catch((error) => {
      console.error('Delete error:', error)
      alert('Błąd podczas usuwania autora')
    })
}
</script>
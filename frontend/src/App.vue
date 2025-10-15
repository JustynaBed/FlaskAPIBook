<script setup>
// import { ref, onMounted } from "vue"

// const authors = ref([])
// const message = ref("")
// const count = ref(0)

// onMounted(() => {
//   // fetchAuthors()
// })

// function fetchAuthors() {
//   console.log('Fetch')
//   fetch('/api/v1/authors', {
//     method: 'GET',
//     headers: {
//       'Content-Type': 'application/json'
//     }
//   })
//   .then(response => response.json())
//   .then(data => {
//     console.log('data:', data)
//     authors.value = data.data
//     count.value = data.number_of_records
//     message.value = data.success ? 'Lista autorów' : 'Błąd podczas pobierania danych'
//   })
//   .catch(error => {
//     console.error('Fetch error:', error)
//     message.value = 'Błąd połączenia z serwerem'
//   })
// }
</script>

<template>
  <p>Vue3</p>
  <!-- <h1>{{ message }}</h1> -->
  <!-- <p>Liczba autorów: {{ count }}</p>

  <ul>
    <li v-for="author in authors" :key="author.id">
      {{ author.name }}
    </li>
  </ul> -->
</template> 
<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="first_name">First Name:</label>
      <input id="first_name" v-model="form.first_name" required />
    </div>
    <div>
      <label for="last_name">Last Name:</label>
      <input id="last_name" v-model="form.last_name" required />
    </div>
    <div>
      <label for="birth_date">Birth Date:</label>
      <input id="birth_date" type="date" v-model="form.birth_date" required />
    </div>
    <button type="submit">Add Author</button>
  </form>
</template>

<script setup>
import { reactive } from 'vue'
import { useStore } from 'vuex'

const form = reactive({
  first_name: '',
  last_name: '',
  birth_date: ''
})

const store = useStore()

async function submitForm() {
  try {
    const [year, month, day] = form.birth_date.split('-')
    const formattedDate = `${day}-${month}-${year}`

   await store.dispatch('authors/createAuthor', {
      first_name: form.first_name,
      last_name: form.last_name,
      birth_date: formattedDate
    })

    alert('Author added!')

    form.first_name = ''
    form.last_name = ''
    form.birth_date = ''


  } catch (error) {
    alert(error.response?.data?.message || error.message)
  }
}
</script>

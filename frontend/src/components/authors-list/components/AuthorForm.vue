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
    <button type="submit">
      {{ isEditMode ? 'Update Author' : 'Add Author'}}
    </button>
        <button v-if="isEditMode" type="button" @click="resetForm">
      Cancel
    </button>
  </form>
</template>

<script setup>
import { reactive, computed, watch } from 'vue'
import { useStore } from 'vuex'

const props = defineProps({
  author: {
    type: Object,
    default: null
  }
})

const form = reactive({
  first_name: '',
  last_name: '',
  birth_date: ''
})

watch(() => props.author, (author) => {
  if (author) {

    form.first_name = author.first_name || ''
    form.last_name = author.last_name || ''
    form.birth_date = formatDateToISO(author.birth_date)
  } else {
    form.first_name = ''
    form.last_name = ''
    form.birth_date = ''
  }
}, { immediate: true })

function formatDateToISO(dateStr) {
  if (!dateStr) return ''
  const [day, month, year] = dateStr.split('-')
  return `${year}-${month}-${day}`
}

function formatDateFromISO(dateStr) {
  if (!dateStr) return ''
  const [year, month, day] = dateStr.split('-')
  return `${day}-${month}-${year}`
}

const emit = defineEmits(['cancel', 'saved'])

const isEditMode = computed(() => {
  return props.author !== null && props.author !== undefined
})

const store = useStore()

function resetForm() {
  form.first_name = ''
  form.last_name = ''
  form.birth_date = ''
  emit('cancel')
}

async function submitForm() {
  try {
    const formattedDate = formatDateFromISO(form.birth_date)

    const payload = {
      first_name: form.first_name,
      last_name: form.last_name,
      birth_date: formattedDate
    }

    if (isEditMode.value) {
      payload.id = props.author.id
      await store.dispatch('authors/editAuthor', payload)
    } else {
      await store.dispatch('authors/createAuthor', payload)
    }
    resetForm()
    emit('saved')
  } catch (error) {
    alert(error.response?.data?.message || error.message)
  }
}
</script>

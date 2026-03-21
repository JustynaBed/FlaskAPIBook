<template>
  <li>
    {{ author.id }}. {{ author.first_name }}, {{author.last_name}}, {{ author.birth_date }}
    <button @click="onDelete(author.id)">Delete</button>
    <button @click="onEdit(author)">Edit</button>
  </li>
</template>

<script setup>
import { useStore } from "vuex";

defineProps({
  author: {
    type: Object,
    required: true
  }
})

const store = useStore()

const emit = defineEmits(['selected-author'])

function onDelete(id) {
  store.dispatch('authors/deleteAuthor', id)
}

function onEdit(author) {
  emit('selected-author', { ...author })
} 
</script>
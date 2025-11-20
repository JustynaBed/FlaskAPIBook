<template>
  <li>
    {{ author.id }}, {{ author.first_name }}, {{author.last_name}}, {{ author.birth_date }}
    <button @click="$emit('delete', author.id)">Delete</button>
  </li>
</template>

<script setup>
defineProps({
  author: {
    type: Object,
    required: true
  }
})
</script>
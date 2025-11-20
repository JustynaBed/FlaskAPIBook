<template>
  <li>
    {{ author.first_name }}
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
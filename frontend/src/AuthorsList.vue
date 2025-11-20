<template>
  <AuthorItem
    v-for="author in authors"
    :key="author.id"
    :author="author"
    @delete="onDelete"
  />
</template> 

<script setup>
import AuthorItem from './AuthorItem.vue'   
import {defineEmits, defineProps} from 'vue';

defineProps({
  authors: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['delete-author'])

function onDelete(id) {
  emit('delete-author', id)
}
</script>
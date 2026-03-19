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
import { AuthorsListEvent } from './constants.js';

defineProps({
  authors: {
    type: Array,
    required: true
  }
})

const emit = defineEmits([AuthorsListEvent.DELETE_AUTHOR])

function onDelete(id) {
  emit(AuthorsListEvent.DELETE_AUTHOR, id)
  // emit('delete-author', id)
}
</script>
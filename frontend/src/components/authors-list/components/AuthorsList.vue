<template>
  <p>Liczba autorów: {{ count }}</p>
  <AuthorItem
    v-for="author in authors"
    :key="author.id"
    :author="author"
    @delete="onDelete"
  />
  <AuthorForm @author-added="onAuthorAdded" />
</template> 

<script setup>
import AuthorItem from './AuthorItem.vue'   
import AuthorForm from './AuthorForm.vue'
import { computed, onMounted } from 'vue';
import { useStore } from "vuex";

const store = useStore()
const authors = computed(() => store.getters["authors/allAuthors"])
const count = computed(() => store.getters["authors/authorsCount"])

onMounted(() => {
  store.dispatch("authors/fetchAuthors");       
})

</script>
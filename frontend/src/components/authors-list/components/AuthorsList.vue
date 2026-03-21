<template>
  <p>Liczba autorów: {{ count }}</p>
  <AuthorItem
    v-for="author in authors"
    :key="author.id"
    :author="author"
    :selectedAuthor="selectedAuthor"
    @selected-author="onSelectedAuthor"
  />
  <AuthorForm 
    :author="selectedAuthor"
    @cancel="selectedAuthor = null"
    @saved="selectedAuthor = null"
  />
  <pre>{{selectedAuthor}}</pre>
</template>

<script setup>
import AuthorItem from './AuthorItem.vue'   
import AuthorForm from './AuthorForm.vue'
import { computed, onMounted, ref } from 'vue';
import { useStore } from "vuex";

const store = useStore()
const authors = computed(() => store.getters["authors/allAuthors"])
const count = computed(() => store.getters["authors/authorsCount"])
const selectedAuthor = ref(null)

onMounted(() => {
  store.dispatch("authors/fetchAuthors")       
})

function onSelectedAuthor(author) {
  selectedAuthor.value = author
}
</script>
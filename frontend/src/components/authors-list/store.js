import * as API from './api.js'

export default {
  namespaced: true,
  state: {
    authors: []
  },
  mutations: {
    SET_AUTHORS(state, authors) {
      state.authors = authors
    },
    REMOVE_AUTHOR(state, authorId) {
      state.authors = state.authors.filter(author => author.id !== authorId);
    },
    ADD_AUTHOR(state, author) {
      state.authors.push(author);
    },
    UPDATE_AUTHOR(state, updatedAuthor) {
      const index = state.authors.findIndex(author => author.id === updatedAuthor.id);
      if (index !== -1) {
        state.authors.splice(index, 1, updatedAuthor);
      }
    }
  },
  actions: {
    fetchAuthors({ commit }) {
      return API.fetchAuthors()
        .then(data => {
          commit('SET_AUTHORS', data.data)
        })
    },
    deleteAuthor({ commit }, authorId) {
      return API.deleteAuthor(authorId)
        .then(() => {
          commit('REMOVE_AUTHOR', authorId)
        })
    },
    createAuthor({ commit }, authorData) {
      return API.createAuthor(authorData)
        .then(response => {
          commit('ADD_AUTHOR', response.data)
          return response
        })
    },
    updateAuthor({ commit }, authorData) {
      return API.updateAuthor(authorData)
        .then(response => {
          commit('UPDATE_AUTHOR', response.data)
          return response
        })
    }
  },
  getters: {
    allAuthors(state) {
      return state.authors
    },
    authorsCount(state) {
      return state.authors.length
    }
  }
}
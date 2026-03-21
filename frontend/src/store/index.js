import { createStore } from "vuex";

import authors from "../components/authors-list/store.js";

export default createStore({
  modules: {
    authors
  }
})
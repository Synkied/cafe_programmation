import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    'projects': null,
    'searchFilter': '' || 'tout',
    'filteredProjects': []
  },
  getters: {
    getSearchFilter: state => {
      return state.searchFilter
    },
    getFilterdProjects: state => {
      return state.filteredProjects
    }
  },
  mutations: {
    setSearchFilter: (state, payload) => {
      state.searchFilter = payload
    },
    setFilteredProjects: (state, payload) => {
      state.filteredProjects = payload
    }
  }
})

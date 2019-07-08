import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    'projects': null,
    'searchFilter': '' || 'sans filtre',
    'filteredProjects': [],
    'FPSectionInfos': {
      index: -1
    }
  },
  getters: {
    getSearchFilter: state => {
      return state.searchFilter
    },
    getFilterdProjects: state => {
      return state.filteredProjects
    },
    getFPSectionInfos: state => {
      return state.FPSectionInfos
    }
  },
  mutations: {
    setSearchFilter: (state, payload) => {
      state.searchFilter = payload
    },
    setFilteredProjects: (state, payload) => {
      state.filteredProjects = payload
    },
    setFPSectionInfos: (state, payload) => {
      state.FPSectionInfos = payload
    }
  }
})

<template>
  <section id="realisations" class="v-align-center" v-if="projects.length > 0">
    <div class="container">
      <div class="row v-align-left-center">
        <div class="col-xl-1 col-12">
          <ul class="search-terms">
            <li v-for="searchFilter in searchFilters" v-bind:key="searchFilter.id">
              <a href="#" @click.prevent="setActiveSearchFilter(searchFilter.name); filterProjects()">{{ capitalizeFirstLetter(searchFilter.name) }}</a>
            </li>
          </ul>
        </div>
        <div class="col-xl-6 col-lg-12 col-md-12 col-sm-12 col-12">
          <div v-if="getSearchFilter">
            <div v-for="searchFilter in searchFilters" :key="searchFilter.id">
              <div v-if="searchFilter.name === getSearchFilter" v-for="subFilter in searchFilter.subFilters" :key="subFilter.id">
                <div class="sub-filters" @click="showFilteredProjects(subFilter)">
                  {{ subFilter.name }}
                </div>
                <div v-for="project in filteredProjects" v-if="showProjects" :key="project.id">
                  <app-project :project="project"></app-project>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
/* Imports */
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
import axios from 'axios'
import { loadProgressBar } from 'axios-progress-bar'
import 'axios-progress-bar/dist/nprogress.css'

import Project from './Project.vue'
import ProjectsFiltered from './ProjectsFiltered.vue'
import { mapGetters } from 'vuex'

// this is to use: https://docs.djangoproject.com/fr/2.0/ref/request-response/#django.http.HttpRequest.is_ajax
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest' // for all requests

/* data, methods, components... declaration */
export default {
  components: {
    'rise-loader': RiseLoader,
    'app-project': Project,
    ProjectsFiltered
  },

  data () {
    return {
      nextPage: '',
      projects: [],
      filteredProjects: [],
      searchFilters: [
        {name: 'fonction', subFilters: []},
        {name: 'contexte', subFilters: []},
        {name: 'avancement', subFilters: []},
        {name: 'dimension', subFilters: []}
      ],
      search: '',
      showProjects: false
    }
  },

  computed: {
    ...mapGetters([
      'getSearchFilter'
    ])
  },

  methods: {
    capitalizeFirstLetter (string) {
      return string[0].toUpperCase() + string.slice(1)
    },

    viewProjects () {
      var thisVm = this
      loadProgressBar()
      axios.get('/api/projects/').then(response => {
        console.log(response.data)
        var jsonProject = response.data
        for (var i = 0; i < jsonProject.length; i++) {
          thisVm.projects.push(jsonProject[i])
        }
      })
        .catch(function (error) {
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.log(error.response.data)
            console.log(error.response.status)
            console.log(error.response.headers)
          } else if (error.request) {
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the browser
            // and an instance of http.ClientRequest in node.js
            console.log(error.request)
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log('Error', error.message)
          }
          console.log(error.config)
        })
    },

    setActiveSearchFilter (name) {
      this.$store.commit('setSearchFilter', name)
    },

    displayContents (name) {
      var thisVm = this
      return thisVm.activeSearchFilter
    },

    appendSubFilters () {
      let apiUrl = '/api/'
      this.searchFilters.map((searchFilter, index) => {
        axios.get(apiUrl + searchFilter.name + 's').then(response => {
          console.log(response.data)
          searchFilter.subFilters = response.data
        })
          .catch(function (error) {
            if (error.response) {
              // The request was made and the server responded with a status code
              // that falls out of the range of 2xx
              console.log(error.response.data)
              console.log(error.response.status)
              console.log(error.response.headers)
            } else if (error.request) {
              // The request was made but no response was received
              // `error.request` is an instance of XMLHttpRequest in the browser
              // and an instance of http.ClientRequest in node.js
              console.log(error.request)
            } else {
              // Something happened in setting up the request that triggered an Error
              console.log('Error', error.message)
            }
            console.log(error.config)
          })
      })
    },

    filterProjects () {
      let filteredProjects = []
      this.projects.map(project => {
        filteredProjects.push(project)
      })
      this.filteredProjects = filteredProjects
    },

    showFilteredProjects () {
      var thisVm = this
      thisVm.showProjects = !thisVm.showProjects
    }

  },

  beforeMount () {
    this.appendSubFilters()
  },

  mounted () {
    var thisVm = this
    thisVm.viewProjects()
  }
}
</script>

<!-- scoped styles for this component -->
<style scoped>

  #projects {
    color: #000;
  }

  .sub-filters {
    background-color: #000;
    color: #fff;
    text-align: left;
    padding: 0 15px;
    margin: 0 15px;
    font-weight: 900;
  }

</style>

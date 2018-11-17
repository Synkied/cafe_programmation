<template>
  <section id="realisations" class="v-align-center" v-if="projects.length > 0">
    <div class="container">
      <div class="row v-align-left-center">
        <div class="col-xl-2 col-12">
          <ul class="search-terms">
            <li v-for="searchFilter in searchFilters" v-bind:key="searchFilter.id" class="search-filter-item" @click="selected = searchFilter.name">
              <div class="shallow-circle" :class="{active:searchFilter.name === selected}">
              </div>
              <a href="#" @click.prevent="setActiveSearchFilter(searchFilter.name)">{{ capitalizeFirstLetter(searchFilter.name) }}</a>
            </li>
          </ul>
        </div>
        <div class="col-xl-8 col-lg-12 col-md-12 col-sm-12 col-12">

        <div v-if="getSearchFilter !== 'tout' ">
            <v-expansion-panel
              v-model="panel"
              v-for="searchFilter in searchFilters" :key="searchFilter.id"
              expand>
              <v-expansion-panel-content class="black"
                v-if="searchFilter.name === getSearchFilter"
                v-for="subFilter in searchFilter.subFilters"
                :key="subFilter.id"
                expand-icon="mdi-menu-down">
                <div slot="header" class="projects-expansion-panel-header text-white">{{ subFilter.name }}</div>
                <v-card v-for="project in projects" :key="project.id">
                  <v-card-text><app-project :project="project" :searchFilter="searchFilter" :subFilter="subFilter"></app-project></v-card-text>
                </v-card>
              </v-expansion-panel-content>
            </v-expansion-panel>
        </div>

        <div v-else>
          <div v-for="project in projects" :key="project.id">
            <app-project :project="project"></app-project>
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
import { mapGetters } from 'vuex'

// this is to use: https://docs.djangoproject.com/fr/2.0/ref/request-response/#django.http.HttpRequest.is_ajax
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest' // for all requests

/* data, methods, components... declaration */
export default {
  components: {
    'rise-loader': RiseLoader,
    'app-project': Project
  },

  data () {
    return {
      nextPage: '',
      projects: [],
      searchFilters: [
        {name: 'tout'},
        {name: 'fonction', subFilters: []},
        {name: 'contexte', subFilters: []},
        {name: 'dimension', subFilters: []},
        {name: 'avancement', subFilters: []}
      ],
      panel: [],
      search: '',
      selected: ''
    }
  },

  computed: {
    ...mapGetters([
      'getSearchFilter'
    ])
  },

  methods: {
    capitalizeFirstLetter (string) {
      if (string) {
        return string[0].toUpperCase() + string.slice(1)
      }
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

    appendSubFilters () {
      let apiUrl = '/api/'
      let promises = this.searchFilters.map(searchFilter => {
        if (searchFilter.name !== 'tout') {
          return axios.get(apiUrl + searchFilter.name + 's')
            .then(response => {
              console.log('data', response.data)
              searchFilter.subFilters = response.data
              return searchFilter
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
        }
      })
      Promise.all(promises)
        .then(response => {
          console.log(response)
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

.projects-expansion-panel-header {
  padding: 0 0 0 10px;
}

.v-card__text {
  padding: 0;
}

</style>

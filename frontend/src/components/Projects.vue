<template>
  <div class="section" id="realisations_section">
    <div class="container">
      <div class="row v-align-left-center">
        <div class="col-xl-1 col-12">
          <ul class="search-terms">
            <li v-for="searchFilter in searchFilters" v-bind:key="searchFilter.id" class="search-filter-item">
              <div class="shallow-circle" :class="{active:searchFilter.name === selected}">
              </div>
              <a href="#" @click.prevent="setActiveSearchFilter(searchFilter.name); selected = searchFilter.name; setPanelsVisibility(searchFilter)">{{ capitalizeFirstLetter(searchFilter.name) }}</a>
            </li>
          </ul>
        </div>
        <div class="col-xl-7 col-lg-12 col-md-12 col-sm-12 col-12">

        <div class="v-panel-wrapper" v-if="getSearchFilter !== 'tout' ">
            <v-expansion-panel
              v-for="searchFilter in searchFilters" :key="searchFilter.id"
              v-if="searchFilter.name === getSearchFilter"
              v-model="searchFilter.panels"
              expand>
              <v-expansion-panel-content class='black'
                v-for="subFilter in searchFilter.subFilters"
                :key="subFilter.id"
                expand-icon="mdi-menu-down">
                <div slot="header" class="projects-expansion-panel-header black-header text-white">{{ subFilter.name }}</div>

                  <v-expansion-panel>
                    <div class="container-fluid" v-for="project in projects" :key="project.id">
                      <div><app-project :project="project" :searchFilter="searchFilter" :subFilter="subFilter"></app-project></div>
                    </div>
                  </v-expansion-panel>

              </v-expansion-panel-content>
            </v-expansion-panel>
        </div>

        <div v-else-if="getSearchFilter === 'tout' ">
          <v-expansion-panel>
            <div class="container-fluid" v-for="project in projects" :key="project.id">
              <app-project :project="project"></app-project>
            </div>
          </v-expansion-panel>
        </div>

        </div>
      </div>
    </div>
  </div>
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
        {name: 'fonction', subFilters: [], panels: []},
        {name: 'contexte', subFilters: [], panels: []},
        {name: 'dimension', subFilters: [], panels: []},
        {name: 'avancement', subFilters: [], panels: []}
      ],
      search: '',
      selected: 'tout'
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
    },

    setPanelsVisibility (obj) {
      console.log(obj)
      obj.panels = []
      setTimeout(function () {
        if (obj.panels && obj.subFilters) {
          for (let _ of obj.subFilters) {
            obj.panels.push(true)
          }
        }
      }, 1000)
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
  background-color: #000;
}

</style>

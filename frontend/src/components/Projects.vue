<template>
  <div class="section fp-auto-height" id="realisations_section">
    <div class="container projects-container">
      <div class="row v-align-left-center">

        <!-- Side Menu -->
        <div class="col-xl-1 col-12 ml-4" :class="{fadeIn: animatedProjects}" style="animation-delay: 3s">
          <ul :class="{'search-terms': windowWidth > 1200, 'list-inline': windowWidth < 1200}">
            <li
              v-for="searchFilter in searchFilters"
              v-bind:key="searchFilter.id"
              :class="{'search-filter-item': windowWidth > 1200, 'list-inline-item': windowWidth < 1200, active: searchFilter.name === selected}">
              <div
                :class="{active: searchFilter.name === selected, 'shallow-circle': windowWidth > 1200}">
              </div>
              <a
                href="#"
                @click.prevent="setActiveSearchFilter(searchFilter.name); selected = searchFilter.name; setPanelsVisibility(searchFilter)">
                {{ capitalizeFirstLetter(searchFilter.name) }}
              </a>
            </li>
          </ul>
        </div>

        <!-- Projects lines -->
        <div class="col-xl-5 col-lg-12 col-md-12 col-sm-12 col-12">

          <div class="v-panel-wrapper" v-if="getSearchFilter !== 'sans filtre' ">
              <v-expansion-panel
                @click.native="$emit('rebuild')"
                v-for="searchFilter in searchFilters"
                :key="searchFilter.id"
                v-if="searchFilter.name === getSearchFilter"
                v-model="searchFilter.panels"
                expand>
                <v-expansion-panel-content
                  class="black"
                  v-for="subFilter in searchFilter.subFilters"
                  :key="subFilter.id"
                  expand-icon="mdi-menu-down">
                  <div slot="header" class="projects-expansion-panel-header black-header text-white">{{ subFilter.name }}</div>

                    <v-expansion-panel
                      @click.native="$emit('rebuild')">
                      <div class="container-fluid" v-for="project in projects" :key="project.id">
                        <div>
                          <app-project :project="project" :searchFilter="searchFilter" :subFilter="subFilter">
                          </app-project>
                        </div>
                      </div>
                    </v-expansion-panel>

                </v-expansion-panel-content>
              </v-expansion-panel>
          </div>

          <div v-else-if="getSearchFilter === 'sans filtre' ">
            <v-expansion-panel
              @click.native="$emit('rebuild')">
              <div class="container-fluid" v-for="(project, index) in projects" :key="project.id">
                <app-project
                  :animatedProjects="animatedProjects"
                  :project="project"
                  :index="index">
                </app-project>
              </div>
            </v-expansion-panel>
          </div>

        </div>
        <!-- !!END Projects lines -->

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
  props: ['animatedProjects'],

  components: {
    'rise-loader': RiseLoader,
    'app-project': Project
  },

  data () {
    return {
      nextPage: '',
      projects: [],
      searchFilters: [
        {name: 'sans filtre'},
        {name: 'fonction', subFilters: [], panels: []},
        {name: 'contexte', subFilters: [], panels: []},
        {name: 'dimension', subFilters: [], panels: []},
        {name: 'avancement', subFilters: [], panels: []}
      ],
      search: '',
      selected: 'sans filtre',
      windowWidth: 0,
      windowHeight: 0
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
        if (searchFilter.name !== 'sans filtre') {
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
    },

    setPanelsVisibility (obj) {
      let thisVm = this
      thisVm.searchFilters.map(searchFilter => {
        if (searchFilter.panels) {
          searchFilter.panels = [false, false, false, false]
        }
      })
      setTimeout(function () {
      /* thisVm.searchFilters.map(searchFilter => {
          if (searchFilter.panels) {
            searchFilter.panels = []
          }
        }) */
        if (obj.panels && obj.subFilters) {
          for (let _ of obj.subFilters) {
            obj.panels = [true, true, true, true]
          }
        }
      }, 1000)
    },

    getWindowWidth (event) {
      this.windowWidth = document.documentElement.clientWidth
    },

    getWindowHeight (event) {
      this.windowHeight = document.documentElement.clientHeight
    }

  },

  beforeMount () {
    this.appendSubFilters()
  },

  mounted () {
    var thisVm = this
    thisVm.viewProjects()

    this.$nextTick(() => {
      window.addEventListener('resize', this.getWindowWidth)
      window.addEventListener('resize', this.getWindowHeight)

      // Init
      this.getWindowWidth()
      this.getWindowHeight()
    })
  },

  beforeDestroy () {
    window.removeEventListener('resize', this.getWindowWidth)
    window.removeEventListener('resize', this.getWindowHeight)
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

.search-terms {
  text-align: left;
  list-style-type: none;
}

.search-filter-item {
  font-family: FuturaBT-CondMedium;
  display: flex;
  align-items: center;
  padding: 5px 0;
  font-weight: 600;
  font-size: 1.2rem;
}

</style>

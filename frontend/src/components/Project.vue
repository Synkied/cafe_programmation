<template>
  <div id="project">
    <div v-if="searchFilter">
    <hr class="hr-line">
      <div class="row" v-if="project[searchFilter.name] === subFilter.name ">
        <div class="col-12 project-row">
          <v-expansion-panel-content
            expand-icon="mdi-menu-down">
            <div slot="header" class="project-title">{{ project.titre }}</div>
            <v-card>
              <v-card-text class="card-text"><project-desc :project="project"></project-desc></v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </div>
      </div>
    </div>

    <div v-if="getSearchFilter === 'tout' ">
      <div
        :class="{fadeInLeft: animatedProjects}"
        :style="{visibility: this.animatedProjects ? 'visible' : 'hidden', animationDelay: 0.01 * this.index + 's'}">
      <hr class="hr-line">
      <div class="row">
        <div class="col-12 project-row">
            <v-expansion-panel-content
              class="all-projects"
              expand-icon="mdi-menu-down">
              <div slot="header" class="project-title">{{ project.titre }}</div>
              <v-card>
                <v-card-text class="card-text">
                  <project-desc :project="project"></project-desc>
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
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
import 'axios-progress-bar/dist/nprogress.css'
import { mapGetters } from 'vuex'

import ProjectDesc from './ProjectDesc.vue'

// this is to use: https://docs.djangoproject.com/fr/2.0/ref/request-response/#django.http.HttpRequest.is_ajax
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest' // for all requests

/* data, methods, components... declaration */
export default {
  props: ['project', 'index', 'searchFilter', 'subFilter', 'animatedProjects'],
  data () {
    return {
      nextPage: '',
      showDesc: false
    }
  },
  computed: {
    ...mapGetters([
      'getSearchFilter'
    ])
  },
  methods: {
    showDescription (project) {
      var thisVm = this
      thisVm.showDesc = !thisVm.showDesc
    }
  },
  components: {
    'rise-loader': RiseLoader,
    'project-desc': ProjectDesc
  },
  mounted () {
  }
}
</script>

<!-- scoped styles for this component -->
<style lang="scss" scoped>

</style>

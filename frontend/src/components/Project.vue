<template>
  <div id="project">

    <!-- Projects filtered -->
    <div v-if="searchFilter">
    <hr class="hr-line">
      <div class="row" v-if="project[searchFilter.name] === subFilter.name ">
        <div class="col-12 project-row">
          <v-expansion-panel-content
            class="filtered-projects"
            expand-icon="mdi-menu-down">
            <div slot="header" class="project-title">{{ project.titre }}</div>
            <v-card>
              <v-card-text class="card-text"><project-desc :project="project"></project-desc></v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </div>
      </div>
    </div>

    <!-- Projects without filters -->
    <div v-if="getSearchFilter === 'sans filtre' ">
      <div>
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
  }
}
</script>

<!-- scoped styles for this component -->
<style scoped>

.project-title {
  font-family: FuturaBT-CondMedium;
  text-transform: uppercase;
  font-size: 1.2rem;
  font-weight: 800;
}

</style>

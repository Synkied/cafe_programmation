<template>
  <div id="project">
    <div class="container-fluid" v-if="project">
      <div class="row">
        <div class="col-12">
          <transition appear name="fadeLeft" tag="div">
            <div class="project-row">
                <hr>
                <h4 class="project-title" @click="showDescription(project)">
                  {{ project.titre }}
                </h4>
                  <p v-if="project.short_description" v-html="project.short_description"></p>
                  <!-- Hidden description, image... -->
                  <div v-if="showDesc && project.description" class="">
                    <project-desc :project="project"></project-desc>
                  </div>

                  <div class="text-right more-button">
                    <div v-if="showDesc === false && project.description">
                      <button class="btn btn-primary-outline btn-bottom-right" @click="showDescription(project)">
                        +
                      </button>
                    </div>
                    <div v-if="showDesc === true && project.description">
                      <button class="btn btn-primary-outline btn-bottom-right" @click="showDescription(project)">
                        -
                      </button>
                    </div>
                  </div>
            </div>
          </transition>
        </div>
      </div>
      <div v-if="nextPage">
        <button class="btn btn-info mt-5" @click="[viewMore()]">View more</button>
      </div>
    </div>
  </div>
</template>

<script>
/* Imports */
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
import axios from 'axios'
import 'axios-progress-bar/dist/nprogress.css'

import ProjectDesc from './ProjectDesc.vue'

// this is to use: https://docs.djangoproject.com/fr/2.0/ref/request-response/#django.http.HttpRequest.is_ajax
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest' // for all requests

/* data, methods, components... declaration */
export default {
  props: ['project'],
  data () {
    return {
      nextPage: '',
      projectId: '',
      showDesc: false
    }
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
<style scoped>

</style>

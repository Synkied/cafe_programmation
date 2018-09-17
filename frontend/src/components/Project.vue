<template>
  <div id="project">
    <div class="container-fluid" v-if="project">
      <div class="row">
        <div class="col-12">
          <transition appear name="fadeLeft" tag="div">
            <div class="project-row">
                <hr>
                <h4 class="project-title" @click="showDescription(project)">
                  {{ project.fields.titre }}
                </h4>
                  <p v-html="project.fields.short_description"></p>

                  <!-- Hidden description, image... -->
                  <div v-if="showDesc && project.fields.description" class="">
                    <div class="img-wrapper mb-3 img-desc-project">
                      <img class="mb-2" :src="project.fields.image" width="200px" :alt="project.fields.titre">
                      <div class="desc-project">
                        <p> {{ project.fields.description }} </p>
                      </div>
                    </div>
                    <div class="info-project">
                      <p> Commanditaire : {{ project.fields.commanditaire }}</p>
                      <p> Mission : {{ project.fields.mission }}</p>
                      <p> Concepteur : {{ project.fields.concepteur }} </p>
                    </div>
                  </div>

                  <div class="text-right more-button">
                    <div v-if="showDesc === false && project.fields.description">
                      <button class="btn btn-primary-outline btn-bottom-right" @click="showDescription(project)">
                        +
                      </button>
                    </div>
                    <div v-if="showDesc === true && project.fields.description">
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
      console.log(project.id)
    }
  },
  components: {
    'rise-loader': RiseLoader
  },
  mounted () {
  }
}
</script>

<!-- scoped styles for this component -->
<style scoped>

</style>

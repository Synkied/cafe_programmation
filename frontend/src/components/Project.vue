<template>
  <div id="project" class="mt-5">
    <h2>Projects I've built</h2>
    <div>
      <div class="container-fluid" v-if="project">
        <div class="row">
          <div class="col-12 mt-3">
            <transition appear name="fadeLeft" tag="div">
              <div class="card h-100">
                  <div class="img-wrapper mb-3">
                  <img class="card-img-top" :src="project.fields.image_url" :alt="project.fields.name">
                  <div class="card-body">
                    <p><a :href="project.fields.link_to">{{ project.fields.name }} <font-awesome-icon icon="link" size="xs" /></a></p>
                    <p v-html="project.fields.description"></p>
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
  </div>
</template>

<script>
/* Imports */
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
import axios from 'axios'
import { loadProgressBar } from 'axios-progress-bar'
import 'axios-progress-bar/dist/nprogress.css'

// this is to use: https://docs.djangoproject.com/fr/2.0/ref/request-response/#django.http.HttpRequest.is_ajax
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest' // for all requests

/* data, methods, components... declaration */
export default {
  data () {
    return {
      moduleTitle: 'Home',
      nextPage: '',
      projectId: '',
      project: ''
    }
  },
  title () {
    return `Evopy — ${this.moduleTitle}`
  },
  methods: {
    viewProject () {
      var thisVm = this
      if (thisVm.$route.params) {
        thisVm.projectId = thisVm.$route.params.id
      }
      const projectPath = '/projects/' + encodeURI(thisVm.projectId)
      loadProgressBar()

      axios.get(projectPath).then(response => {
        console.log(response.data)
        var jsonProject = JSON.parse(response.data.project)
        thisVm.project = jsonProject[0]
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
  components: {
    'rise-loader': RiseLoader
  },
  mounted () {
    var thisVm = this
    thisVm.viewProject()
  }
}
</script>

<!-- scoped styles for this component -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Oxygen');
  @import url('https://fonts.googleapis.com/css?family=Raleway');

  .about-us {
    background-color: white;
    padding: 4rem;
  }

</style>

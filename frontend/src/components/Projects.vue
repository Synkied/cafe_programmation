<template>
  <section id="realisations" class="s-100 v-align-center" v-if="projects.length > 0">
    <div class="container">
      <div class="row v-align-left-center">
        <div class="col-xl-1 col-12 text-left">
          <p>Fonction</p>
          <p>Contexte</p>
          <p>Dimension</p>
          <p>Avancement</p>
        </div>
        <div class="col-xl-8 col-lg-8 col-md-8 col-sm-12 col-12">
          <div v-for="project in projects" :key="project.id">
            <app-project :project="project"></app-project>
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

// this is to use: https://docs.djangoproject.com/fr/2.0/ref/request-response/#django.http.HttpRequest.is_ajax
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest' // for all requests

/* data, methods, components... declaration */
export default {
  data () {
    return {
      moduleTitle: 'Projects',
      nextPage: '',
      projects: []
    }
  },
  title () {
    return `Evopy — ${this.moduleTitle}`
  },
  methods: {
    viewProjects () {
      var thisVm = this
      loadProgressBar()
      axios.get('/realisations/').then(response => {
        var jsonProject = JSON.parse(response.data.projects)
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
    }
  },
  components: {
    'rise-loader': RiseLoader,
    'app-project': Project
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

</style>

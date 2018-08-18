<template>
  <section id="projects" class="container" v-if="projects.length > 0">
    <h1 class="mb-5">Projets réalisés</h1>
    <div>
      <div class="container-fluid">
        <div class="row">
          <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12 mt-5" v-for="project in projects" :key="project.id">
            <transition appear name="fadeLeft" tag="div">
              <div class="card h-100">
                <div class="img-wrapper mb-3">
                  <a :href="'/projects/' + project.pk"><img class="card-img-top" :src="project.fields.image_url" :alt="project.fields.name"></a>
                </div>
                <div class="pad card-body">
                  <p>
                    <a :href="project.fields.link_to"> {{ project.fields.name }} <font-awesome-icon icon="link" size="xs" /> </a>
                  </p>
                  <hr class="hr" align="left"/>
                    <p v-if="project.fields.description.length < 255" v-html="project.fields.description">{{ project.fields.description }}</p>
                    <p v-else v-html="project.fields.description">{{ project.fields.description.substring(0,255)+"..." }}</p>
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
  </section>
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
      axios.get('/projects/').then(response => {
        console.log(JSON.parse(response.data.projects))
        console.log(response.data)
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
    'rise-loader': RiseLoader
  },
  mounted () {
    var thisVm = this
    thisVm.viewProjects()
  }
}
</script>

<!-- scoped styles for this component -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Oxygen');
  @import url('https://fonts.googleapis.com/css?family=Raleway');

  #projects {
    background-color: #a8d0e6;
    color: #000;
  }

</style>

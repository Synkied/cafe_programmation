<template>
  <section id="skills" v-if="skills.length > 0">
    <h1 class="mb-5">Compétences</h1>
    <div>
      <div class="row">
        <div class="col-xl-2 col-lg-6 col-md-6 col-sm-4 col-6" v-for="skill in skills" :key="skill.id">
          <transition appear name="slideDown" tag="ul">
            <li class="ns-li">
              <div class="img-wrapper mb-3">
                <img class="skill-img" :src="skill.fields.image_url" alt="">
              </div>
              <p>{{ skill.fields.name }}</p>
              <p>{{ skill.fields.description }}</p>
            </li>
          </transition>
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
      skills: []
    }
  },
  title () {
    return `Evopy — ${this.moduleTitle}`
  },
  methods: {
    viewProjects () {
      var thisVm = this
      loadProgressBar()
      axios.get('/skills/').then(response => {
        console.log(JSON.parse(response.data.skills))
        console.log(response.data)
        var jsonProject = JSON.parse(response.data.skills)
        for (var i = 0; i < jsonProject.length; i++) {
          thisVm.skills.push(jsonProject[i])
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

  #skills {
    background-color: #24305e;
    color: #fff;
  }

</style>

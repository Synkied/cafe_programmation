<template>
  <div id="home">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-4 col-lg-4 col-md-4 col-12 no-pad">
          <about-me></about-me>
        </div>
        <div class="col-xl-8 col-lg-8 col-md-8 col-12 no-pad">
          <app-skills></app-skills>
        </div>
      </div>
    </div>
    <app-projects></app-projects>
  </div>
</template>

<script>
/* Imports */
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
import About from './About'
import Projects from './Projects'
import Skills from './Skills'
/* import { loadProgressBar } from 'axios-progress-bar'
import 'axios-progress-bar/dist/nprogress.css' */

/* data, methods, components... declaration */
export default {
  data () {
    return {
      moduleTitle: 'Home'
    }
  },
  title () {
    return `Evopy — ${this.moduleTitle}`
  },
  methods: {
  },
  components: {
    'rise-loader': RiseLoader,
    'app-projects': Projects,
    'app-skills': Skills,
    'about-me': About
  },
  mounted () {
  }
}
</script>

<!-- scoped styles for this component -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Oxygen');
  @import url('https://fonts.googleapis.com/css?family=Raleway');

</style>

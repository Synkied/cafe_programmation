<template>
  <div id="404">
    <p>Are you lost?</p>
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

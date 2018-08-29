<template>
  <div id="home">
    <div class="container-fluid">
      <section class="text-left ">
        <img class=logo_home src="../assets/cafe_logo.png" alt="">
        <p class="logo-moto">programmation d'architectures culturelles</p>
      </section>
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
import Intentions from './Intentions'
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
    'about-me': About,
    'intentions-app': Intentions
  },
  mounted () {
  }
}
</script>

<!-- scoped styles for this component -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Oxygen');
  @import url('https://fonts.googleapis.com/css?family=Raleway');
  @import url('https://fonts.googleapis.com/css?family=Poppins');

  @font-face {
    font-family: 'futuristregular';
    src: url('../assets/fonts/futr-webfont.woff2') format('woff2'),
         url('../assets/fonts/futr-webfont.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }

  .logo-home {
    font-size: 4rem;
    font-family: 'Raleway', Futura, sans-serif;
  }

  .logo-moto {
    font-size:2rem;
  }

</style>

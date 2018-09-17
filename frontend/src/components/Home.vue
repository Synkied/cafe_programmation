<template>
  <div id="home">
      <section class="text-center s-100 v-align-center" id="home-section">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xl-12 col-12 mx-auto">
              <img class="logo-img" src="../assets/cafe_logo_full.png" alt="cafe logo">
            </div>
          </div>
        </div>
      </section>
    <intentions-app></intentions-app>
    <projects-app></projects-app>
  </div>
</template>

<script>
/* Imports */
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
import About from './About'
import Projects from './Projects'
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
    return `Café Programmation — ${this.moduleTitle}`
  },
  methods: {
  },
  components: {
    'rise-loader': RiseLoader,
    'projects-app': Projects,
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

<template>
    <full-page ref="fullpage" :options="options" id="fullpage">
      <div class="section" id="home_section">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xl-12 col-12 mx-auto">
              <img class="logo-img" src="../assets/cafe_logo_full.png" alt="cafe logo">
            </div>
          </div>
        </div>
      </div>
    <intentions-app></intentions-app>
    <projects-app @rebuild="rebuildFullPage()"></projects-app>
  </full-page>
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
      moduleTitle: 'Home',
      options: {
        licenseKey: 'C6820AA9-BC954443-A4F97A82-86A455D2',
        menu: '#header',
        anchors: ['home', 'intentions', 'realisations'],
        scrollOverflow: true,
        responsiveWidth: 1200 // disable autoscroll on responsive
      }
    }
  },
  title () {
    return `Café Programmation — ${this.moduleTitle}`
  },
  components: {
    'rise-loader': RiseLoader,
    'projects-app': Projects,
    'about-me': About,
    'intentions-app': Intentions
  },

  methods: {
    rebuildFullPage () {
      setTimeout(() => {
        console.log('test')
        console.log(this.$refs)
        this.$refs.fullpage.api.reBuild()
      }, 600)
    }
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

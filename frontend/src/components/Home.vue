<template>
    <full-page ref="fullpage" :options="options" id="fullpage">
      <div class="section" id="home_section">
        <div class="container-fluid">
          <div class="row row-home justify-content-center">
            <v-spacer></v-spacer>
            <div class="col-xl-9 col-lg-8 col-md-10 col-sm-9 col-12">
              <p class="cafe-title align-left">
                <span class="intention-word-left">
                  <img class="logo-img" src="../assets/cafe_logo_solo.png" alt="cafe logo">
                </span>
              </p>
              <p
                :class="{fadeOut: !animatedHome, fadeIn: animatedHome}"
                v-show="animatedHome" style="animation-delay: 1.6s;"
                class="cafe-logo-line">
              </p>
              <transition name="shiftx">
                <p
                  v-show="animatedHome"
                  style="transition-delay: 1.4s;"
                  class="cafe-sub-title align-left">
                  programmation d'architectures culturelles
                </p>
              </transition>
            </div>
          </div>
        </div>
      </div>
    <intentions-app
      :animatedIntentions="animatedIntentions">
    </intentions-app>
    <projects-app
      :filter="filter"
      :animatedProjects="animatedProjects"
      :animatedProjectsMenu="animatedProjectsMenu"
      @rebuild="rebuildFullPage()">
    </projects-app>
    <app-footer></app-footer>
  </full-page>
</template>

<script>
/* Imports */
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
import About from './About'
import Projects from './Projects'
import Intentions from './Intentions'
import Footer from './Shared/Footer.vue'
/* import { loadProgressBar } from 'axios-progress-bar'
import 'axios-progress-bar/dist/nprogress.css' */

/* data, methods, components... declaration */
export default {
  data () {
    return {
      moduleTitle: 'Home',
      animatedHome: false,
      animatedIntentions: false,
      animatedProjects: false,
      animatedProjectsMenu: false,
      showIntentions: false,
      autoScrolling:false,
      filter: '',
      options: {
        licenseKey: 'C6820AA9-BC954443-A4F97A82-86A455D2',
        menu: '#header',
        anchors: ['home', 'intentions', 'realisations', 'contact'],
        scrollOverflow: true,
        afterLoad: this.afterLoad,
        onLeave: this.onLeave,
        responsiveWidth: 1024, // disable autoscroll on responsive
        paddingTop: '50px',
        paddingBottom: '50px'
      }
    }
  },
  title () {
    return `Café Programmation — ${this.moduleTitle}`
  },
  components: {
    'rise-loader': RiseLoader,
    'projects-app': Projects,
    'intentions-app': Intentions,
    'app-footer': Footer
  },

  methods: {
    afterLoad (origin, destination, direction) {
      // do something after a section is loaded
      // in correlation with fullPage.js
      if (destination.index === 0) {
        this.animatedHome = true
        this.filter = 'sans filtre'
      }
      if (destination.index === 1) {
        this.animatedIntentions = true
        this.filter = 'sans filtre'
      }
      if (destination.index === 2) {
        this.animatedProjects = true
        this.filter = 'sans filtre'
        /*this.$refs.fullpage.api.setAutoScrolling(false)*/
      }
    },
    onLeave (origin, destination, direction) {
      // do something after a section is left
      // in correlation with fullPage.js
      this.$store.commit('setFPSectionInfos', destination)
      if (origin) {
        if (origin.index === 0) {
          this.animatedHome = false
          this.filter = 'sans filtre'
        }
        if (origin.index === 1) {
          this.animatedIntentions = false
          this.filter = 'sans filtre'
        }
        if (origin.index === 2) {
          this.animatedProjects = false
          this.filter = 'sans filtre'
          /*this.$refs.fullpage.api.setAutoScrolling(true)*/
        }
      }
    },
    rebuildFullPage () {
      setTimeout(() => {
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

  .logo-home {
    font-size: 4rem;
    font-family: 'Raleway', Futura, sans-serif;
  }

  .logo-moto {
    font-size:2rem;
  }

</style>

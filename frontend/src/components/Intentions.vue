<template>
  <section class="s-100 v-align-center" id="intentions">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-3"></div>
        <div class="col-xl-6 col-12">
          <p class="h5 align-right"><span>culturelles</span></p>
          <p class="justif">
            Nous sommes convaincus de l’utilité des projets à vocation culturelle. Aujourd’hui peut-être plus encore, des projets inventifs, qui soient à la fois plus pragmatiques et plus ambitieux. Café conçoit, avec les porteurs de ceux-ci, des projets qui font sens.
          </p>
          <p class="h5 text-center"><span>d'architectures</span></p>
          <p class="justif">
            Nous sommes également passionnés d’architecture. Où l’architecture est vue comme un art de commande, la qualité de l’une étant conditionnée par celle de l’autre. Café installe, auprès des commanditaires, les conditions d’une architecture créative et juste.
          </p>
          <p class="h5 align-left"><span>programmation</span></p>
          <p class="justif">
            Nous ne nous reconnaissons que relativement sous le terme de programmation, tel qu’il désigne notre métier. Il y a une part illusoire dans son ambition catégorique. Café étudie la relation dialectique - c’est elle qui fera véritablement projet - entre des usages évolutifs et des espaces structurants.
          </p>
        </div>
        <div class="col-xl-3"></div>
      </div>
    </div>
  </section>
</template>

<script>
/* Imports */
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
/* import { loadProgressBar } from 'axios-progress-bar'
import 'axios-progress-bar/dist/nprogress.css' */

/* data, methods, components... declaration */
export default {
  data () {
    return {
      moduleTitle: 'Intentions'
    }
  },
  title () {
    return `Café Programmation — ${this.moduleTitle}`
  },
  methods: {
  },
  components: {
    'rise-loader': RiseLoader
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

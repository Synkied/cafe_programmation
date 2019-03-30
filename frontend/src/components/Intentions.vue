<template>
  <div class="section" id="intentions_section">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-3"></div>
        <div class="col-xl-3 col-12">
          <p class="intentions-title align-right" :class="{fadeInDownBig: animatedIntentions}" :style="{visibility: animatedIntentions ? 'visible' : 'hidden'}"><span class="intention-word-right">culturelles</span></p>
          <p class="justif intentions">
            Nous sommes convaincus de l’utilité des projets à vocation culturelle. Aujourd’hui peut-être plus encore, des projets inventifs, qui soient à la fois plus pragmatiques et plus ambitieux. Café conçoit, avec les porteurs de ceux-ci, des projets qui font sens.
          </p>
          <p class="intentions-title text-center" :class="{fadeInDownBig: animatedIntentions}" :style="{visibility: animatedIntentions ? 'visible' : 'hidden'}"><span class="intention-word-center">d'architectures</span></p>
          <p class="justif intentions">
            Nous sommes également passionnés d’architecture. Où l’architecture est vue comme un art de commande, la qualité de l’une étant conditionnée par celle de l’autre. Café installe, auprès des commanditaires, les conditions d’une architecture créative et juste.
          </p>
          <p class="intentions-title align-left" :class="{fadeInDownBig: animatedIntentions}" :style="{visibility: animatedIntentions ? 'visible' : 'hidden'}" ><span class="intention-word-left">programmation</span></p>
          <p class="justif intentions">
            Nous ne nous reconnaissons que relativement sous le terme de programmation, tel qu’il désigne notre métier. Il y a une part illusoire dans son ambition catégorique. Café étudie la relation dialectique - c’est elle qui fera véritablement projet - entre des usages évolutifs et des espaces structurants.
          </p>
        </div>
        <div class="col-xl-3 col-12">
          <p class="intentions-title bounce align-right" :class="{bounceInDown: animatedIntentions}" :style="{visibility: animatedIntentions ? 'visible' : 'hidden'}"><span class="intention-word-right">culturelles</span></p>
          <p class="justif intentions">
            Nous sommes convaincus de l’utilité des projets à vocation culturelle. Aujourd’hui peut-être plus encore, des projets inventifs, qui soient à la fois plus pragmatiques et plus ambitieux. Café conçoit, avec les porteurs de ceux-ci, des projets qui font sens.
          </p>
          <p class="intentions-title bounce text-center" :class="{bounceInDown: animatedIntentions}" :style="{visibility: animatedIntentions ? 'visible' : 'hidden'}"><span class="intention-word-center">d'architectures</span></p>
          <p class="justif intentions">
            Nous sommes également passionnés d’architecture. Où l’architecture est vue comme un art de commande, la qualité de l’une étant conditionnée par celle de l’autre. Café installe, auprès des commanditaires, les conditions d’une architecture créative et juste.
          </p>
          <p class="intentions-title bounce align-left" :class="{bounceInDown: animatedIntentions}" :style="{visibility: animatedIntentions ? 'visible' : 'hidden'}" ><span class="intention-word-left">programmation</span></p>
          <p class="justif intentions">
            Nous ne nous reconnaissons que relativement sous le terme de programmation, tel qu’il désigne notre métier. Il y a une part illusoire dans son ambition catégorique. Café étudie la relation dialectique - c’est elle qui fera véritablement projet - entre des usages évolutifs et des espaces structurants.
          </p>
        </div>
        <div class="col-xl-3"></div>
      </div>
    </div>
  </div>
</template>

<script>
/* Imports */
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
/* import { loadProgressBar } from 'axios-progress-bar'
import 'axios-progress-bar/dist/nprogress.css' */

/* data, methods, components... declaration */
export default {
  props: ['animatedIntentions'],
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
.intentions-title {
  overflow: hidden;
  font-size: 1.1rem;
  animation-duration: 1.3s
}

.intentions-title.align-right {
  animation-delay: .8s
}

.intentions-title.text-center {
  animation-delay: .4s
}

.intentions-title.bounce {
  animation-delay: 2s;
}

.intentions-title.bounce.align-right {
  animation-delay: 2.8s
}

.intentions-title.bounce.text-center {
  animation-delay: 2.4s
}

.intentions-title:after {
  content:"";
  display: inline-block;
  height: 0.5em;
  vertical-align: bottom;
  width: 100%;
  margin-right: -100%;
  border-top: 1px solid black;
}

.intentions-title:before {
  content:"";
  display: inline-block;
  height: 0.5em;
  vertical-align: bottom;
  width: 100%;
  margin-left: -100%;
  border-top: 1px solid black;
}

.intention-word-left {
  margin: 0 10px 0 0;
}

.intention-word-center {
  margin: 0 10px;
}

.intention-word-right {
  margin: 0 0 0 10px;
}

.intentions {
  font-family: AvantGardeGothicITCW02Md;
  font-size: 1.11rem;
}

</style>

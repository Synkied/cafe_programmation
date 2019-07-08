<template>
  <section id="about">
    <div>
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
      moduleTitle: 'About me'
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

</style>

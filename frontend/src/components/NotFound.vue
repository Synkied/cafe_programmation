<template>
  <div id="404">
    <p>Are you lost?</p>
  </div>
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
      moduleTitle: 'Home'
    }
  },
  title () {
    return `Evopy — ${this.moduleTitle}`
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

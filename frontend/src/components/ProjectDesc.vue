<template>
  <div>
    <div class="img-wrapper mb-3 img-desc-project">
      <img class="mb-2 img-project" :src="project.image" :alt="project.titre">
      <div class="desc-project">
        <p> {{ project.description }} </p>
      </div>
    </div>
    <div class="info-project">
      <p> Commanditaire : {{ project.commanditaire }}</p>
      <p> Mission : {{ project.mission }}</p>
      <p> Concepteur : {{ project.concepteur }} </p>
      <p> Fonction : {{ project.fonction }} </p>
      <p> Contexte : {{ project.contexte }} </p>
      <p> Dimension : {{ project.dimension }} </p>
      <p> Avancement : {{ project.avancement }} </p>
      <p>{{ getSearchFilter }}</p>
    </div>
  </div>
</template>

<script>
// imports
import { mapGetters } from 'vuex'

export default {
  props: ['project'],
  computed: {
    counter () {
      return this.$store.state.counter
    },
    ...mapGetters([
      'getSearchFilter'
    ])
  },
  methods: {
  }
}
</script>

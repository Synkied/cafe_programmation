<template>
  <div>
    <v-layout wrap class="img-desc-project" :class="{fadeIn: true}" style="animation-delay: .1s">
      <v-flex xs11 sm4 md2 lg3 xl3 :class="{'mr-5': $vuetify.breakpoint.lg, 'mr-4': $vuetify.breakpoint.md}">
        <img class="mb-2 img-project" :src="project.image" :alt="project.titre">
      </v-flex>
      <v-flex xs11 sm7 md9 lg8 xl9 >
        <div class="desc-project">
          <p> {{ project.description }} </p>
        </div>
      </v-flex>
    </v-layout>
    <div class="info-project">
      <p> Commanditaire : {{ project.commanditaire }}</p>
      <p> Mission : {{ project.mission }}</p>
      <p> Concepteur : {{ project.concepteur }} </p>
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

<style scoped>
.desc-project {
  font-family: AvantGardeGothicITCW02Md;
  font-size: 1rem;
}
.info-project {
  font-family: FuturaCon-Lig;
  font-size: 1.22rem;
}
.info-project p {
  margin: 0;
}
.info-project p:last-child {
  margin: 0 0 15px 0;
}
</style>

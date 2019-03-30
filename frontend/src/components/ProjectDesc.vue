<template>
<!--   <div>
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
  </div>
</div> -->
  <div>
    <v-layout wrap class="img-desc-project" :class="{fadeIn: true}" style="animation-delay: .2s">
      <v-flex xs5 s2 md4 lg3 xl3 :class="{'mr-5': $vuetify.breakpoint.lg}">
        <img class="mb-2 img-project" :src="project.image" :alt="project.titre">
      </v-flex>
      <v-flex xs7 s10 md8 lg8 xl9 >
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

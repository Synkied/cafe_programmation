<template>
<div>

  <div v-for="searchFilter in searchFilters" :key="searchFilter.id">
    <div v-if="searchFilter.name === getSearchFilter" v-for="subFilter in searchFilter.subFilters" :key="subFilter.id">
      <div class="sub-filters" @click="showFilteredProjects(subFilter)">
        {{ subFilter.name }}
      </div>
      <div v-for="project in filteredProjects" v-if="showProjects" :key="project.id">
        <app-project :project="project"></app-project>
      </div>
    </div>
  </div>

</div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {

  data () {
    return {
      filteredProjects: [],
      searchFilters: [
        {name: 'fonction', subFilters: []},
        {name: 'contexte', subFilters: []},
        {name: 'avancement', subFilters: []},
        {name: 'dimension', subFilters: []}
      ],
      showProjects: false
    }
  }
}


</script>

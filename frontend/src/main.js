// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'

/* boostrap's css import, needed for bootstrap to work */
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import titleMixin from './mixins/titleMixin'
import vueSmoothScroll from 'vue2-smooth-scroll'

// Font awesome icon import and adding

import { faLink } from '@fortawesome/free-solid-svg-icons'
library.add(faLink)

// mixins
Vue.mixin(titleMixin)

// components
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(BootstrapVue)
Vue.use(vueSmoothScroll)

// config
Vue.config.productionTip = false

require('vue2-animate/dist/vue2-animate.min.css')

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    App,
    BootstrapVue
  },
  template: '<App/>'
})

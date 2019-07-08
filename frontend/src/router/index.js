import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  /* what to render depending on the url passed */
  { path: '/', component: 'Home', name: 'home' },
  { path: '/projects/', component: 'Projects', name: 'allProjects' },
  { path: '/projects/:id', component: 'Project', name: 'projectDetail' },
  { path: '*', component: 'NotFound', name: 'notFound' }
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
    /* searches for the component to render depending on the url passed */
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})

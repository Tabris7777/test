import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: require('@/components/home').default
    },
    {
      path: '*',
      redirect: '/'
    },
    {
      path: '/secondHome',
      name: 'secondHome',
      component: require('@/components/secondHome').default
    },
    {
      path: '/showChart',
      name: 'showChart',
      component: require('@/components/showChart').default
    },
  ]
})

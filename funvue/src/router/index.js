import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/pages/HomePage'
import ToothPage from '@/pages/ToothPage'
import CreateAccount from '@/components/CreateAccount'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/toothpage',
      name: 'ToothPage',
      component: ToothPage
    },
    {
      path: '/createaccount',
      name: 'CreateAccount',
      component: CreateAccount
    }
  ]
})

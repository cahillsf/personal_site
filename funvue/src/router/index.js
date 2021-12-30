import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/pages/HomePage'
import ToothPage from '@/pages/ToothPage'
import CreateAccount from '@/components/CreateAccount'
import ThreeScene from '@/pages/ThreeScene'
import RileyProject from '@/pages/RileyProject'
import RileyCanvas from '@/pages/RileyCanvas'
import DecTree from '@/pages/DecTree'
import JupyterNb from '@/pages/JupyterNb'
import NetworkGraph from '@/pages/NetworkGraph'
import NetworkJupyterNb from '@/pages/NetworkJupyterNb'

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
    },
    {
      path: '/threescene',
      name: 'ThreeScene',
      component: ThreeScene
    },
    {
      path: '/rileyproject',
      name: 'RileyProject',
      component: RileyProject
    },
    {
      path: '/rileycanvas',
      name: 'RileyCanvas',
      component: RileyCanvas
    },
    {
      path: '/dectree',
      name: 'DecTree',
      component: DecTree
    },
    {
      path: '/jupyternb',
      name: 'JupyterNb',
      component: JupyterNb
    },
    {
      path: '/graphalgo',
      name: 'NetworkGraph',
      component: NetworkGraph
    },
    {
      path: '/networkjupyternb',
      name: 'NetworkJupyterNb',
      component: NetworkJupyterNb
    }
  ]
})

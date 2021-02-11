import Vue from 'vue'
import VueRouter from 'vue-router'
import Call from '../views/Call.vue'
import Home from "@/views/Home";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component:Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
  ,{
  path:'/call',
    name:'call',
    component: Call
  },
  {
    path:'/call/test',
    name:'te',
    component: Home
  }
]

const router = new VueRouter({
  routes
})

export default router

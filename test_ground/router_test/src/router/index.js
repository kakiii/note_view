import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "@/views/Home";
import About from "@/views/About.vue"
import page_404 from "@/views/404.vue"
import Editor from "@/views/Editor";
import Discussion from "@/views/Discussion";
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component:Home
  },
  {
    path:'/editor',
    name:'editor',
    component: Editor
  },{
  path:'/discussion',
    name:'discussion',
    component: Discussion
  },
  {
    path:'/about',
    name:'about',
    component: About
  },
  {
    path:'/404',
    name:'404',
    component: page_404
  }
]

const router = new VueRouter({
  routes
})

export default router

// 这是路由部分的核心规则,所有需要前往的URL路径都需要在这里进行注册.
// 下面的import语句用于引入需要的"核心"组件,下一级的组件无需在此注册.
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "@/components/Home";
import About from "@/components/About.vue"
import Editor from "@/components/Editor";
import Discussion from "@/components/Discussion";
import Login from "@/components/Login";
Vue.use(VueRouter)

const routes = [
  {
    // 这个URL表示根目录
    path: '/',
    // 名字是只是标识符,没有特殊的含义,只需要方便记忆即可
    name: 'Index',
    // Component表示挂载在这个URL下的Vue组件名称,只能填入一个.
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
    path:'/login',
    name:'login',
    component: Login
  }
]

const router = new VueRouter({
  routes
})

export default router

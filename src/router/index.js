// 这是路由部分的核心规则,所有需要前往的URL路径都需要在这里进行注册.
// 下面的import语句用于引入需要的"核心"组件,下一级的组件无需在此注册.
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home.vue";
import About from "../components/About.vue";
import Editor from "../components/Editor.vue";
import Discussion from "../components/Discussion.vue";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import FindArticle from "../components/FindArticle.vue";
import CodeEditor from "../components/CodeEditor.vue";
import todo from "../components/todo.vue";
import UserPage from "../components/UserPage.vue";
import page_404 from "../components/404.vue";
import management from "../components/Management.vue";
import Preview from "../components/Preview.vue";

Vue.use(VueRouter);

const routes = [
  {
    // 这个URL表示根目录
    path: "/",
    // 名字是只是标识符,没有特殊的含义,只需要方便记忆即可
    name: "Index",
    // Component表示挂载在这个URL下的Vue组件名称,只能填入一个.
    component: Home,
  },
  {
    path: "/editor",
    name: "editor",
    component: Editor
  },
  {
    path: "/discussion",
    name: "discussion",
    component: Discussion
  },
  {
    path: "/about",
    name: "about",
    component: About
  },
  {
    path: "/login",
    name: "login",
    component: Login
  },
  {
    path: "/register",
    name: "register",
    component: Register,
  },
  {
    path: "/find",
    name: "find",
    component: FindArticle,

  },
  {
    path: "/code",
    name: "code",
    component: CodeEditor,
  },
  {
    path: "/todo",
    name: "todo",
    component: todo,
  },
  {
    path: "/user/:username",
    name: "userpage",
    component: UserPage,
  },
  {
    path:"/management",
    name:"management",
    component:management,
  },
  {
    path:'*',
    name:"not found",
    component:page_404
  },{
    path:"/article/:id",
    name: "article",
    component: Preview,
  }
];
const router = new VueRouter({
  routes,
});

export default router;

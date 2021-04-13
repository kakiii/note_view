// 这是路由部分的核心规则,所有需要前往的URL路径都需要在这里进行注册.
// 下面的import语句用于引入需要的"核心"组件,下一级的组件无需在此注册.
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/components/Home";
import About from "@/components/About.vue";
import Editor from "@/components/Editor";
import Discussion from "@/components/Discussion";
import Login from "@/components/Login.vue";
import Register from "@/components/Register";
import FindArticle from "@/components/FindArticle";
import CodeEditor from "@/components/CodeEditor";

import store from "../store";
//import { TodoList } from "element-tiptap"; //Gan：不知道这个是干啥的我先把它注释掉了不然我新todo要报错
import todo from"@/components/todo";

Vue.use(VueRouter);

const routes = [
  {
    // 这个URL表示根目录
    path: "/",
    // 名字是只是标识符,没有特殊的含义,只需要方便记忆即可
    name: "Index",
    // Component表示挂载在这个URL下的Vue组件名称,只能填入一个.
    component: Home,
    meta: {
      isLogin: false,
    },
  },
  {
    path: "/editor",
    name: "editor",
    component: Editor,
  },
  {
    path: "/discussion",
    name: "discussion",
    component: Discussion,
  },
  {
    path: "/about",
    name: "about",
    component: About,
  },
  {
    path: "/login",
    name: "login",
    component: Login,
    meta: {
      isLogin: false,
    },
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
  }

];

const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  var getFlag = store.isLogin;
  if (!getFlag && to.name != "login") {
    next("/login");
  } else {
    next();
  }
});
export default router;

// 这是整个项目的规则定义文件,尽量不要修改
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Vuex from "vuex";
import "./editor_config";
import "./plugins/element.js";
import "element-tiptap/lib/index.css";
import { ElementTiptapPlugin } from "element-tiptap";
Vue.config.productionTip = true;
Vue.use(Vuex);
Vue.use(ElementTiptapPlugin, { lang: "en", spellcheck: true });
new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");

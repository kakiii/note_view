// 这是整个项目的规则定义文件,尽量不要修改
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "./plugins/element.js";
// import Vuex from "vuex"
import store from "./store";

Vue.config.productionTip = true;
new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app");
// 这是整个项目的规则定义文件,尽量不要修改
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuex from 'vuex'
import './editor_config'
import vuetify from './plugins/vuetify';
Vue.config.productionTip = true
Vue.use(Vuex)
new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')

// 这是整个项目的规则定义文件,尽量不要修改
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuex from 'vuex'
import {Button,Container} from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
Vue.config.productionTip = true
Vue.use(Button)
Vue.use(mavonEditor)
Vue.use(Container)
Vue.use(Vuex)
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

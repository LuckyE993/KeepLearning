import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'font-awesome/css/font-awesome.css'
import axios from 'axios'; 
axios.defaults.baseURL = "http://localhost:8084";
Vue.prototype.$http=axios

Vue.use(ElementUI);
new Vue({
  render: h => h(App),
}).$mount('#app')

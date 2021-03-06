// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from "./store";
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import vueMoment from 'vue-moment'

Vue.use(vueMoment);
Vue.use(Vuetify);
require('../node_modules/bootstrap/dist/css/bootstrap.css')

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  icons: {
    iconfont: 'mdi', // 'mdi' || 'mdiSvg' || 'md' || 'fa' || 'fa4' || 'faSvg'
  },
  router,
  store,
  components: { App },
  vuetify: new Vuetify(),
  template: '<App/>'
})

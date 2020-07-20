import Vue from 'vue'
import Router from 'vue-router'
import List from '@/Views/List'
import placeCard from '@/components/placeCard'
import Map from '@/Views/Map'
import Lend from '@/Views/Lend'
import NewItem from '@/Views/NewItem'
import itemForm from '@/components/itemForm'
import Login from '@/Views/Login'
import {mapState, mapActions} from "vuex"
Vue.use(Router)
const requireAuth = () => (from, to, next) => {
  const isAuthenticated = this.mapState.state.isLogin;
  console.log(isAuthenticated);
  if (isAuthenticated) return next();
  window.alert('먼저 로그인 해주세요.');
  next('/Login');
};
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/Lend',
      name: 'Lend',
      component: Lend,
      //beforeEnter: requireAuth()
    },
    {
      path: '/admin',
      name: 'admin',
      // route level code-splitting
      // this generates a separate chunk (chunkName.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "Admin" */ '../components/admin.vue')
    },
    {
      path:'/NewItem',
      name: 'NewItem',
      component: NewItem
    }
  ]
})

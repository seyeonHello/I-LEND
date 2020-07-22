import Vue from 'vue'
import Router from 'vue-router'
import Lend from '@/Views/Lend'
import NewItem from '@/Views/NewItem'
import itemForm from '@/components/itemForm'
import Login from '@/Views/Login'
import Seek from '@/Views/Seek'
import SeekForm from '@/components/SeekForm'
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
      path:'/NewItem',
      name: 'NewItem',
      component: NewItem
    },
    {
      path:'/Seek',
      name: 'Seek',
      component: Seek
    }
  ]
})

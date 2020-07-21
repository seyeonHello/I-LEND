import Vue from "vue"
import Vuex from "vuex"
import router from "@/router/index"
Vue.use(Vuex);

export default new Vuex.Store({
  state:{
    allUsers: [
      {id:1, name:"seyeon",email:"seyeon@ajou.ac.kr",password:"1234"},
      {id:2, name:"seyeon2",email:"seyeon2@ajou.ac.kr",password:"1234"}
    ],
    userList:[],
    isLogin: false,
    isLoginError: false,
    currentMember:null,
    nickName:''
  },
   getters: {
    getID: function (state) {
      console.log(state.nickName);
      return state.nickName;
    }
  },
  mutations:{
    //로그인 성공
    loginSuccess(state){
      state.isLogin=true;
    },
    changeName(state, account){
      state.nickName=account;
      state.isLogin=true;
      console.log(state.nickName)
    }
  },
  actions:{
    //로그인 시도
    login({state,commit},signObj){
      state.userList=signObj.userList;
      state.userList.forEach(user=>{
        if(user.id===signObj.id) state.currentMember=user;
      });
      state.currentMember===null
      ? (state.isLoginError=true)
        :state.currentMember.pwd!==signObj.password
      ? alert("이메일과 비밀번호가 일치하지 않습니다.")
        : state.isLogin=true;

      if(state.isLogin===true) {
        commit('changeName',state.currentMember.id);
        alert(state.currentMember.id+'님 환영합니다.');
        //window.location.href = '/NewItem';
        router.push({name:"Lend"})
      }
    }
  }
})

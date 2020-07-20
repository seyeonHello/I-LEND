<template>
  <v-container fill-height style="max-width:450px;">
    <v-layout align-center row wrap>
      <v-flex xs12>
        <v-card>
          <div class="pa-3">
            <v-text-field
              v-model="id"
              label="id">
              </v-text-field>
              <v-text-field
                v-model="password"
                type="password"
                label="password">
                </v-text-field>
           </div>
           <div class="pa-2">
            <v-btn
             @click="login({id, password,
             userList})"
             >
             로그인
            </v-btn>
               <v-btn
              @click.stop="dialog = true"
              >
              회원가입
            </v-btn>
           </div>
        </v-card>
      </v-flex>
    </v-layout>
    <v-dialog
      v-model="dialog"
      max-width="350"
    >
      <v-card>
        <v-card-title class="headline">회원가입</v-card-title>

        <v-card-text>
        <v-text-field
              v-model="email"
              label="email">
              </v-text-field>
              <v-text-field
                v-model="phoneNum"
                label="phoneNum">
                </v-text-field>
          <v-text-field
              v-model="signUpID"
              label="id">
              </v-text-field>
              <v-text-field
                v-model="signUpPWD"
                type="password"
                label="password">
                </v-text-field>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="addNewUser"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>
<script>
import axios from 'axios'
import {mapState, mapActions} from "vuex"
export default {
  name: 'Login',
  data () {
    return {
      id:'',
      password:'',
      email:'',
      phoneNum:'',
      signUpID:'',
      signUpPWD:'',
      dialog:false,
      userList:[]
      }
  },
  mounted () {
    this.getUsers()
    this.gotoLend()
  },
  methods:{
    ...mapActions(['login']),
    getUsers () {
      axios({ method: 'GET', url: '/api/signup' }).then(
        result => {
          this.userList = result.data
        },
        error => {
          console.error(error)
        }
      )
    },
    addNewUser () {
      axios.post('/api/signup',
        { signUpID: this.signUpID, signUpPWD: this.signUpPWD, phoneNum:this.phoneNum, email:this.email})
        .then((res) => {
          this.dialog=false
          this.signUpID = ''
          this.signUpPWD=''
          this.phoneNum=''
          this.email=''
          alert('회원 가입이 되었습니다.');
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    gotoLend(){
    console.log('bye');
    if(this.$store.state.isLogin===true){
    alert("hello");
      window.location.href = '/Lend';
    }
    }
}
}
</script>

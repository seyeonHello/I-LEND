<style>
 #content {
    margin-top: 10px;
  }
</style>
<template>
  <v-card
    max-width="500"
    class="mx-auto"
    id="content"
  >
  <v-card>
  <v-list subheader>
      <v-toolbar
      color="teal lighten-2"
      dark
    >
      <v-toolbar-title>{{this.$store.getters.getID}}님의 Member</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

      <v-list-item
        v-for="item in memberNameList"
        :key="item"
        @click="dialog=true"
      >
      <v-list-item-avatar>
          <v-img :src=imgURL></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title v-text="item"></v-list-item-title>
        </v-list-item-content>
        </v-list-item>
        </v-list>

  </v-card>
    <v-toolbar
      color="teal lighten-2"
      dark
    >
      <v-toolbar-title>Message</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-list subheader>
      <v-subheader>Recent chat</v-subheader>

      <v-list-item
        v-for="item in memberList"
        :key="item.sender"
      >

        <v-list-item-content>
          <v-list-item-title v-text="item.sender"></v-list-item-title>
          [{{item.title}}] {{item.message}}
        </v-list-item-content>
    <v-dialog
      v-model="dialog"
      max-width="400"
    >
      <v-card>
        <v-card-title class="headline">Message</v-card-title>

        <v-card-text>
        <v-text-field
              v-model="title"
              label="책이름"
              >
              </v-text-field>
         <v-text-field
              v-model="toMessage"
              label="메시지를 입력하세요."
              >
              </v-text-field>
        </v-card-text>
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
            @click="onClickMemoUpdateBtn(item.sender)"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
      </v-list-item>
    </v-list>
    <v-divider></v-divider>
  </v-card>
</template>
<script>
import axios from 'axios'
import {mapState, mapActions, mapGetters} from "vuex"
export default {
    name: 'MyPage',
    data () {
    return {
      memberName:'',
      dialog:false,
      memberList:[],
      memberNameList:[],
      toMessage:'',
      imgURL:'/static/human.png',
      title:''
      }
    },
    computed: mapGetters([
      'getID'
    ]),
    mounted () {
      this.getMessage()
    },
    methods: {
    onClickMemoUpdateBtn(sender){
      axios.post('/api/users',
        { receiver :sender, sender: this.$store.getters.getID, message: this.toMessage, title:this.title})
        .then((res) => {
          alert('메시지가 전송 되었습니다.');
          this.dialog=false;
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMessage () {
    const ctx=this;
    console.log(this.$store.getters.getID);
      axios.get('/api/users', {
        params: {
        hostName: this.$store.getters.getID
        }
      }).then(
        result => {
         // console.log(result.data)
          this.memberList = result.data
          result.data.forEach(function (rr, idx) {
            ctx.memberNameList.push(rr.sender);
          });
         ctx.memberNameList = Array.from(new Set(ctx.memberNameList));
        },
        error => {
          console.error(error)
        })
    }
  }
}
</script>

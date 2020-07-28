<template>
<v-app>
<v-container>
<v-card class="grey lighten-5">
<v-row>
  <v-col cols="12" md="6">
  <v-card
    max-width="500"
    class="mx-auto"
    id="content"
  >
  <v-list subheader>
  <v-card-title class="teal lighten-5">{{this.$store.getters.getID}}님의 친구목록</v-card-title>

      <v-list-item
        v-for="item in memberNameList"
        :key="item"
      >
      <v-list-item-avatar>
          <v-img :src=imgURL></v-img>
        </v-list-item-avatar>
        <v-list-item-content @click="dialog=true">
          <v-list-item-title v-text="item"></v-list-item-title>
        </v-list-item-content>
        <v-btn color="deep-orange lighten-2" text @click="onClickReviewBtn(item)">❤ 후기</v-btn>
        <v-btn text color="teal lighten-1" @click="dialog=true">Message</v-btn>
        <v-btn text color="teal lighten-1" @click="dialog2=true">rent</v-btn>
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
            @click="onClickMemoUpdateBtn(item)"
          >
            Agree
          </v-btn>
      </v-card>
    </v-dialog>
   <v-dialog
      v-model="dialog2"
      max-width="400"
    >
      <v-card>
        <v-card-title class="headline">Rent</v-card-title>

        <v-card-text>
        <v-text-field
              v-model="rentTitle"
              label="책이름"
              >
              </v-text-field>
        <v-text-field
              v-model="dueDate"
              label="반납날짜(YYYY-MM-DD)">
              </v-text-field>
        <v-text-field
              v-model="dueTime"
              label="반납시간(HH:MM)">
              </v-text-field>
        <v-text-field
              v-model="meetPlace"
              label="만나는장소">
              </v-text-field>
        </v-card-text>
          <v-btn
            color="green darken-1"
            text
            @click="dialog2 = false"
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="onClickRentBtn(item)"
          >
            Agree
          </v-btn>
      </v-card>
    </v-dialog>
    <v-dialog
      v-model="dialog3"
      max-width="400"
    >
    <v-card>
        <v-card-title class="headline">Review</v-card-title>
        <v-card-text>
          <li v-for="reviews in reviewList"> {{ reviews.comment }} </li>
          <br>
          <v-text-field
            v-model="giveScore"
            label="후기를 작성해주세요:)">
          </v-text-field>
        </v-card-text>
        <v-btn
            color="deep-orange lighten-2"
            text
            @click="dialog3 = false"
          >
            Disagree
          </v-btn>

          <v-btn
            color="deep-orange lighten-2"
            text
            @click="dialog3 = false"
          >
            Agree
          </v-btn>
    </v-card>
    </v-dialog>
        </v-list-item>
        </v-list>
  <v-card-title class="teal lighten-5">메시지함</v-card-title>

    <v-list subheader>
      <v-subheader>Recent chat</v-subheader>

      <v-list-item
        v-for="item in memberList"
        :key="item.index"
      >

        <v-list-item-content>
          <v-list-item-title v-text="item.sender"></v-list-item-title>
          [{{item.title}}] {{item.message}}
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-divider></v-divider>
  </v-card>
  </v-col>
<v-col cols="12" md="6">
  <Timer/>
  </v-col>
  </v-row>
</v-card>
</v-container>
</v-app>
</template>
<script>
import axios from 'axios'
import Timer from '@/components/Timer.vue'
import {mapState, mapActions, mapGetters} from "vuex"
export default {
    name: 'MyPage',
    components: {
    Timer
    },
    data () {
    return {
      memberName:'',
      dialog:false,
      dialog2:false,
      dialog3:false,
      memberList:[],
      memberNameList:[],
      toMessage:'',
      imgURL:'/static/human.png',
      title:'',
      dueDate:'',
      dueTime:'',
      rentTitle:'',
      meetPlace:'',
      giveScore:'',
      reviewList:[]
      }
    },
    computed: mapGetters([
      'getID'
    ]),
    mounted () {
      this.getMessage()
    },
    methods: {
    onClickRentBtn(borrower){
      axios.post('/api/rent',
        { lender : this.$store.getters.getID, borrower: borrower, rentTitle: this.rentTitle, dueDate:this.dueDate,dueTime:this.dueTime, meetPlace:this.meetPlace})
        .then((res) => {
          alert('메시지가 전송 되었습니다.');
          this.dialog2=false;
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
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
    },
    onClickReviewBtn(name){
    this.dialog3=true;
    const ctx=this;
    axios.get('/api/reviews', {
        params: {
        ID: name
        }
      }).then(
        result => {
          this.reviewList = result.data
        },
        error => {
          console.error(error)
        })
        }
  }
}
</script>
<style>
 #content {
  }
</style>

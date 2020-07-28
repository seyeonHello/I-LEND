<template>
  <v-card
    max-width="500"
    class="mx-auto"
    id="content2"
  >
  <v-card-title class="teal lighten-5">결제하기</v-card-title>
  <v-list subheader>
    <v-list-item
        v-for="item in rentItems"
        :key="item.index"
        @click="dialog=true"
      >
        <v-list-item-content>
          <v-list-item-title v-text="item.rentTitle"></v-list-item-title>
        </v-list-item-content>
        <v-btn text color="teal lighten-1" @click="dialog2=true">결제완료</v-btn>
    </v-list-item>
  </v-list>
  <v-card-title class="teal lighten-5">대여목록</v-card-title>
  <v-list subheader>
    <v-list-item
        v-for="item in rentItems"
        :key="item.index"
      >
        <v-list-item-content>
          <v-list-item-title v-text="item.rentTitle"></v-list-item-title>
          <v-list-item-subtitle v-text="item.meetTime"></v-list-item-subtitle>
          <v-list-item-subtitle v-text="item.remainTime"></v-list-item-subtitle>
        </v-list-item-content>
    </v-list-item>
  </v-list>
  </v-card>
</template>
<script>
import axios from 'axios'
import {mapState, mapActions, mapGetters} from "vuex"
export default {
    name: 'Timer',
    data(){
    return{
        leftStr:'남은시간 ',
        leftDate:'',
        leftHour:'',
        leftMin:'',
        leftSec:'',
        rentItems:[],
        rentItem:[],
        dueDate:'',
        dueTime:'',
        showMeetDay:''
    }
    },
    computed: mapGetters([
      'getID'
    ]),
   mounted () {
    //this.showtime();
    this.getRent();
    },
    methods:{
      getRent () {
      axios({ method: 'GET', url: '/api/rent' }).then(
        result => {
          console.log(result.data);
          console.log(result.data[0]);
          for (let i = 0; i < result.data.length; i++) {
            if (result.data[i].borrower===this.$store.getters.getID) {
            result.data[i].remainTime=this.showtime(result.data[i].dueDate,result.data[i].dueTime);
            result.data[i].meetTime=result.data[i].dueDate+" "+result.data[i].dueTime;
            this.rentItems.push(result.data[i]);
            }
          }
          console.log(this.rentItems);
        },
        error => {
          console.error(error)
        }
      )
    },
      showtime(dueDate,dueTime) {
      const ctx = this;
      var now=new Date();
      var dayStr=dueDate+"T"+dueTime+":00"
      ctx.showMeetDay=dueDate+" "+dueTime;
      var event_day = new Date(dayStr)
      console.log(event_day)
      var date=Math.floor((event_day-now)/1000/60/60/24);
      var hour=Math.floor((event_day-now)/1000/60/60);
      var min=Math.floor((event_day-now)/1000/60);
      var sec=Math.floor((event_day-now)/1000);
       if(sec>=60)
        sec-=60*min;
       if(min>=60)
        min-=60*hour;
       if(hour>=24)
        hour-=24*date;
      if ((event_day.getTime() - now.getTime()) > 0) {
        this.leftDate = date;
        this.leftHour = hour;
        this.leftMin = min;
        this.leftSec = sec;
      } else {
        console.log("기간이 지났습니다.");
      }
      return "남은시간: "+this.leftDate+"일 "+this.leftHour+"시 "+this.leftMin+"분 ";
      }
    }
}
</script>

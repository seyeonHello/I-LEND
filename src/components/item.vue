<template>
<v-container>
  <v-card
    class="mx-auto"
    max-width="400"
    color="grey lighten-5"
    id="content"
  >
    <v-img
      :aspect-ratio="4/3"
      class="white--text align-end"
      height="300px"
      :src="data.image"
    >
    </v-img>
    <v-card-title>{{ data.title }}</v-card-title>
    <v-card-subtitle class="pb-0">{{ data.price }}원</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>{{ data.startDate }}~{{ data.endDate }}</div>

      <div>{{ data.des }}</div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
        @click="dialog = true"
      >
        Share
      </v-btn>

      <v-btn
        color="orange"
        text
      >
        Explore
      </v-btn>
    </v-card-actions>
  </v-card>
  <v-dialog
      v-model="dialog"
      max-width="400"
    >
    <v-card>
          <v-card-title>"{{data.memberID}}"님에게 보내는 메시지</v-card-title>
          <v-textarea
            background-color="teal lighten-4"
            color="black"
            v-model="memoDetail"
            rows="10"
          ></v-textarea>
          <v-btn color="teal darken-1" text v-on:click="onClickMemoUpdateBtn(memoDetail)">save</v-btn>
    </v-card>
    </v-dialog>
    </v-container>
</template>
<script>
import axios from 'axios'
import {mapState, mapActions, mapGetters} from "vuex"
export default {
    name: 'item',
    props: {
        data: {
          id: String,
          title: String,
          price: String,
          startDate: String,
          endDate: String,
          des: String,
          image: String,
          memberID: String
        }
    },
    data () {
    return {
      memoDetail:'',
      dialog:false
    }
    },
  computed: mapGetters([
  'getID'
  ]),
  methods: {
    onClickMemoUpdateBtn(memo){
    console.log(this.data.memberID);
    console.log('ple');
      axios.post('/api/users',
        { receiver :this.data.memberID, sender: this.$store.getters.getID, message: memo})
        .then((res) => {
          alert('메시지가 전송 되었습니다.');
          this.dialog=false;
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
<style>
 #content {
    margin-bottom: 3px;
  }
</style>

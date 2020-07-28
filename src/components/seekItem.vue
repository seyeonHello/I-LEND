<template>
<v-container>
  <v-card
    class="mx-auto"
    max-width="400"
    color="grey lighten-5"
  >
    <v-card-title>{{ data.seekName }}</v-card-title>

    <v-card-text class="text--primary">
      <div>게시일:{{data.today}}</div>
      <div>{{ data.seekStartDate }}~{{ data.seekEndDate }}</div>

      <div>{{ data.seekDes }}</div>
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
          <v-card-title>"{{data.memberID}}"님에게 요청해보세요</v-card-title>
          <v-textarea
            background-color="lime lighten-4"
            color="black"
            v-model="memoDetail"
            rows="5"
          ></v-textarea>
          <v-btn color="teal darken-1" text v-on:click="onClickMemoUpdateBtn(data.seekName)">save</v-btn>
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
          seekName: String,
          seekDes: String,
          seekStartDate: String,
          seekEndDate: String,
          today: String,
          memberID: String
        }
    },
    data () {
    return {
      memoDetail:'책 빌려줄게요',
      dialog:false
    }
    },
  computed: mapGetters([
  'getID'
  ]),
  methods: {
    onClickMemoUpdateBtn(title){
    console.log(this.data.memberID);
      axios.post('/api/users',
        { receiver :this.data.memberID, sender: this.$store.getters.getID, message: this.memoDetail, title:title})
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

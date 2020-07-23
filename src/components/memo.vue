<template>
  <v-dialog
      v-model="dialog"
      max-width="400"
    >
        <v-icon id="account">mdi-account</v-icon>
          <h4>"{{memberID}}"님에게 보내는 메시지</h4>
          <v-textarea
            background-color="grey lighten-3"
            color="black"
            v-model="memoDetail"
            rows="10"
          ></v-textarea>
          <v-btn color="blue darken-1" text v-on:click="onClickMemoUpdateBtn(memoDetail)">save</v-btn>
    </v-dialog>
</template>
<script>
export default {
    name: 'memo',
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
  methods: {
    onClickMemoUpdateBtn(memo){

    }
  }
}
</script>

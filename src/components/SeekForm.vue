<template>
<v-app>
<v-container>
        <v-form v-model="valid">
        <v-card >
        <v-card-text>
            <v-row>
                <v-col cols="12" md="4">
                    <v-text-field label="물품명" v-model="seekName"></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                    <v-text-field label="설명" v-model="seekDes"></v-text-field>
                </v-col>
                <v-col cols="12" md="3">
                  <v-menu
                    :close-on-content-click="false"
                    ref="menu"
                    v-model="modal"
                    :return-value.sync="seekStartDate"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                   >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                      v-model="seekStartDate"
                      label="시작 날짜"
                      readonly
                      outlined
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="seekStartDate" no-title scrollable>
                  <v-btn text color="indigo" @click="modal = false">취소</v-btn>
                  <v-btn text color="indigo" @click="$refs.menu.save(seekStartDate)">확인</v-btn>
                  </v-date-picker>
                  </v-menu>
                </v-col>
                <v-col cols="12" md="3">
                  <v-menu
                    :close-on-content-click="false"
                    ref="menu2"
                    v-model="modal2"
                    :return-value.sync="seekEndDate"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                   >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                      v-model="seekEndDate"
                      label="마지막 날짜"
                      readonly
                      outlined
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="seekEndDate" no-title scrollable>
                  <v-btn text color="indigo" @click="modal2 = false">취소</v-btn>
                  <v-btn text color="indigo" @click="$refs.menu2.save(seekEndDate)">확인</v-btn>
                  </v-date-picker>
                  </v-menu>
                </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-row>
                <v-btn
                    color="primary"
                    text
                    @click="addNewSeek"
                >
                    SUBMIT
                </v-btn>
                <v-btn
                    color="orange"
                    text
                    @click="goBack"
                >
                    BACK
                </v-btn>
            </v-row>
        </v-card-text>
        </v-card>
    </v-form>
    </v-container>
</v-app>
</template>
<script>
import axios from 'axios'
import {mapState, mapActions} from "vuex"
export default {
  name: 'SeekForm',
  data () {
    return {
      seekName:'',
      seekStartDate:'',
      seekEndDate:'',
      seekDes:'',
      menu: '',
      menu2: '',
      modal: '',
      modal2: '',
      valid: false,
    }
  },
  methods: {
    goBack(){
    },
    addNewSeek () {
      axios.post('/api/seeks',
        { seekName: this.seekName, seekDes:this.seekDes, seekStartDate:this.seekStartDate, seekEndDate:this.seekEndDate})
        .then((res) => {
          this.seekName = ''
          this.seekDes=''
          this.seekStartDate=''
          this.seekEndDate=''
          alert('상품이 게시되었습니다.');
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}

</script>

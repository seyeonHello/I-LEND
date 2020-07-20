<template>
<v-app>
<v-container>
        <v-form v-model="valid">
        <v-card >
        <v-card-text>
            <v-row>
                <v-col cols="12" md="4">
                    <v-text-field label="물품명" v-model="name"></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                    <v-text-field label="대여가격" v-model="price"></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-text-field label="물품사진" v-model="image"></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                    <v-text-field label="설명" v-model="description"></v-text-field>
                </v-col>
                <v-col cols="12" md="3">
                  <v-menu
                    :close-on-content-click="false"
                    ref="menu"
                    v-model="modal"
                    :return-value.sync="startDate"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                   >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                      v-model="startDate"
                      label="시작 날짜"
                      readonly
                      outlined
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="startDate" no-title scrollable>
                  <v-btn text color="indigo" @click="modal = false">취소</v-btn>
                  <v-btn text color="indigo" @click="$refs.menu.save(startDate)">확인</v-btn>
                  </v-date-picker>
                  </v-menu>
                </v-col>
                <v-col cols="12" md="3">
                  <v-menu
                    :close-on-content-click="false"
                    ref="menu2"
                    v-model="modal2"
                    :return-value.sync="endDate"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                   >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                      v-model="endDate"
                      label="마지막 날짜"
                      readonly
                      outlined
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="endDate" no-title scrollable>
                  <v-btn text color="indigo" @click="modal2 = false">취소</v-btn>
                  <v-btn text color="indigo" @click="$refs.menu2.save(endDate)">확인</v-btn>
                  </v-date-picker>
                  </v-menu>
                </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-row>
                <v-btn
                    color="primary"
                    text
                    @click="addNewItem"
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
import {mapState, mapActions} from "vuex"
import axios from 'axios'
export default {
  name: 'NewPost',
  data () {
    return {
      name:'',
      price:'',
      startDate:'',
      endDate:'',
      date:null,
      description:'',
      image:'',
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
    addNewItem () {
      console.log('hello');
      axios.post('/api/task',
        { title: this.name, price: this.price, startDate:this.startDate, endDate:this.endDate, description:this.description, image:this.image, memberID: this.$store.state.currentMember.id })
        .then((res) => {
          this.name = ''
          this.price=''
          this.startDate=''
          this.endDate=''
          this.description=''
          this.image=''
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

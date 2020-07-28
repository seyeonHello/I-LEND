<template>
<v-card>
<v-card>
<v-row>
                <v-col cols="12" md="2" id="majorbar">
                  <v-select
                  v-model="selectedMajor"
                  :items="major"
                  menu-props="auto"
                  chips
                  hide-details
                  append-outer-icon="search"
                  label="major"
                  hint="전공/영역을 선택해주세요"
                  single-line
                ></v-select>
                </v-col>
</v-row>
<v-card-title class="headline font-weight-bold">빌려주세요!</v-card-title>
<div class="col-md-12 mx-auto">
  <v-row dense>
            <v-col cols="3" v-for="(m, index) of seeks" :key="index">
              <seekItem :data="m" />
            </v-col>
   </v-row>
</div>
</v-card>
<v-card id="content">
<v-card-title class="headline font-weight-bold">빌려가세요!</v-card-title>
<div class="col-md-12 mx-auto">
  <v-row dense>
            <v-col cols="3" v-for="(m, index) of todos" :key="index">
              <item :data="m" />
            </v-col>
  </v-row>
</div>
</v-card>
</v-card>
</template>

<script>
import axios from 'axios'
import item from '@/components/item.vue'
import seekItem from '@/components/seekItem.vue'
export default {
  name: 'Lend',
  components: {
    item,
    seekItem
  },
  data () {
    return {
      todos: [],
      seeks: [],
      selectedMajor:'전체',
      major:['전체','기초과목','교양과목','경영학과','기계공학과','산업공학과','화학과','수학과','전자공학과','소프트웨어학과','정치외교학과','e-비즈니스학과']
    }
  },
  mounted () {
    this.getTasks(),
    this.getSeeks()
  },
  watch: {
    'selectedMajor' (newVal) {
      this.getTasks(newVal);
      this.getSeeks(newVal);
    }
  },
  methods: {
  getTasks () {
      axios.get('/api/tasks', {
        params: {
        major: this.selectedMajor
        }
      }).then(
        result => {
          console.log(result.data)
          this.todos = result.data
        },
        error => {
          console.error(error)
        })
    },
    getSeeks () {
      axios.get('/api/seeks', {
        params: {
        major: this.selectedMajor
        }
      }).then(
        result => {
          console.log(result.data)
          this.seeks = result.data
        },
        error => {
          console.error(error)
        })
    }
 }
 }
</script>

<style>
#map {
    width: 400px;
    height: 300px;
}
 #content {
    margin-top: 0px;
  }
  #majorbar{
  float: right;
  margin-left: 1300px;
  }
</style>

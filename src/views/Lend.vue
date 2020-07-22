<template>
<v-card>
<v-card>
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
      seeks: []
    }
  },
  mounted () {
    this.getTasks(),
    this.getSeeks()
  },
  methods: {
    getTasks () {
      axios({ method: 'GET', url: '/api/tasks' }).then(
        result => {
          console.log(result.data)
          this.todos = result.data
        },
        error => {
          console.error(error)
        }
      )
    },
    getSeeks () {
      axios({ method: 'GET', url: '/api/seeks' }).then(
        result => {
          console.log(result.data)
          this.seeks = result.data
        },
        error => {
          console.error(error)
        }
      )
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
</style>

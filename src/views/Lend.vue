<template>
<div class="col-md-12 mx-auto">
  <v-row dense>
            <v-col cols="3" v-for="(m, index) of todos" :key="index">
              <item :data="m" />
            </v-col>
          </v-row>
  <item/>
</div>
</template>

<script>
import axios from 'axios'
import item from '@/components/item.vue'
export default {
  name: 'Lend',
  components: {
    item
  },
  data () {
    return {
      todos: [],
    }
  },
  mounted () {
    this.getTasks()
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
 }
 }
</script>

<style>
#map {
    width: 400px;
    height: 300px;
}
</style>

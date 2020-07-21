<template>
<div class="col-md-12 mx-auto">
  <v-row dense>
            <v-col cols="3" v-for="(m, index) of seeks" :key="index">
              <seekItem :data="m" />
            </v-col>
          </v-row>
</div>
</template>

<script>
import axios from 'axios'
import seekItem from '@/components/seekItem.vue'
export default {
  name: 'SeekList',
  components: {
    seekItem
  },
  data () {
    return {
      seeks: []
    }
  },
  mounted () {
    this.getSeeks()
  },
  methods: {
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

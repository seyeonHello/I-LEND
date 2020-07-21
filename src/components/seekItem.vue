<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-card-title>{{ data.seekName }}</v-card-title>

    <v-card-text class="text--primary">
      <div>{{ data.seekStartDate }}~{{ data.seekEndDate }}</div>

      <div>{{ data.seekDes }}</div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
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
</template>
<script>
export default {
    name: 'item',
    props: {
        data: {
          seekName: String,
          seekDes: String,
          seekStartDate: String,
          seekEndDate: String
        }
    },
  methods: {

  }
}
</script>

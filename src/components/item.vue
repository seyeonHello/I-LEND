<template>
  <v-card
    class="mx-auto"
    max-width="400"
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
          id: String,
          title: String,
          price: String,
          startDate: String,
          endDate: String,
          des: String,
          image: String
        }
    },
  methods: {

  }
}
</script>

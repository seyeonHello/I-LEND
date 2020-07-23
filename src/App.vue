<template>
<!--  <div id="app">-->
<!--    <router-view />-->
<!--  </div>-->
  <v-app>
    <v-app id="app">
      <div>
        <v-toolbar color="teal lighten-4" dark>
          <v-toolbar-side-icon>
            <v-img class="mr-3" src="/static/island.PNG" height="40px" width="50px">
            </v-img>
          </v-toolbar-side-icon>
          <v-toolbar-title>아일랜드</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items class="hidden-sm-and-down">
            <v-btn color="teal lighten-3" to="/Lend">SHOW</v-btn>
            <v-btn color="teal lighten-3" to="/NewItem">POST</v-btn>
            <v-btn color="teal lighten-3" to="/Seek">SEEK</v-btn>
            <v-btn color="teal lighten-3" to="/MyPage">ME</v-btn>
          </v-toolbar-items>
        </v-toolbar>
      </div>
        <div id="content">
          <router-view/>
        </div>
    </v-app>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>
<style>

</style>

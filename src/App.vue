<template>
  <div id="app">
    <v-container>
      <!-- <router-view></router-view> -->
      <the-header></the-header>
      <router-view></router-view>
    </v-container>
  </div>
</template>

<script>
import TheHeader from "./components/TheHeader";
export default {
  
  name: "app",
  components: {TheHeader},
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

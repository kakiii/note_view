<template>
  <div id="app">
    <v-container>
      <router-link v-if="$route.name !== `login`" to="/login">To Login</router-link>
      <router-view></router-view>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {},
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

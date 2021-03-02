<template>
  <div id="app">
    <the-header/>
    <router-view></router-view>
    <the-footer/>

  </div>
</template>

<script>
export default {
  name: "app",
  components: {TheHeader, TheFooter},
};
import TheFooter from './components/TheFooter.vue'
import TheHeader from './components/TheHeader.vue';
</script>

<template>
  <div>
    <router-link to="/">HOME </router-link>
    <router-link to="/editor">EDITOR </router-link>
    <router-link to="/discussion">DISCUSSION BOARD </router-link>
    <router-link v-if="$route.name !== `login`"  to="/login">LOGIN </router-link>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>
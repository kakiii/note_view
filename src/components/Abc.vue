<template>
  <div class="Abc">
    <h1>{{ message }}</h1>
    <h2>{{ h2_s_message }}</h2>

  </div>
</template>

<script>

export default {
  name: "Abc",
  props: {
    message: String,
    h2_s_message: String
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
h1 {
  color: aqua;
}
h2 {
  color: darkgreen;
}
</style>

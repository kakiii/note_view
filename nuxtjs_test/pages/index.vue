<template>
  <div>
    <div class="container">
      <h1>INDEX PAGE 👋</h1>

      <!--
    <NuxtLInk to="/editor">
      GO TO editor
    </NuxtLInk> -->
    </div>
    <div class="container">
      <hr>
      <p>下面的链接提供了通向编辑器的路由功能</p>
      <p>当前只注册了一个链接路由</p>

      <NuxtLink to="/editor">
        GO TP EDITOR
      </NuxtLink>
    </div>
  </div>
</template>
<script>
export default {
  methods: {}
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 10vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>

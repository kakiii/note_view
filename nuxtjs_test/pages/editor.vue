<template>
  <div>
    <h1>Editor Page</h1>
    <p>这是编辑器的界面</p>
    <NuxtLink to="/">
      Home page
    </NuxtLink>
    <vue-simplemde ref="markdownEditor" v-model="content" />
  </div>
</template>

<script>
import VueSimplemde from 'vue-simplemde'

export default {
  components: {
    VueSimplemde
  },
  data () {
    return {
      configs: {
        toolbar: ['italic', 'heading', '|']
      }
    }
  }
}
</script>

<style>
@import 'simplemde/dist/simplemde.min.css';
</style>

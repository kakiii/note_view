<template>
  <div>
    This is Editor Page.
    <br />
    之后会在这里放入编辑器的组件
    <p>{{ greets }}</p>

    <input v-model="message" placeholder="edit me" />
    <p>Message is {{ message }}</p>
    <compo1/>
  </div>
</template>

<script>
import compo1 from '../components/compo1.vue'
export default {
  name: "Editor",
  data() {
    return {
      greets: "hih",
      message:"hh"
    };
  },
  components:{compo1}
};
</script>

<style scoped></style>

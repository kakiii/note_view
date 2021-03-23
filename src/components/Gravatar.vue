<template>
    <p style="width: 4em" v-html="svgs"/>
</template>

<script>
import multiavatar from '@multiavatar/multiavatar'
export default {
  name: "Gravatar",
  props:{gen_key:Object},
  data(){
    return{
      svgs:multiavatar(this.gen_key)
    }
  }
}
</script>

<style scoped>
.p{
  width: 10px;
  height: 10px
}
</style>
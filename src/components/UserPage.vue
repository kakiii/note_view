<!-- todolist试做,需要优化ui。checkbox问题解决，本地存储todolist-->

<template>
  <div>
    <p>Hello, {{this.$store.state.username}}!</p>
    <Gravatar :gen_key=this.$store.state.username
    />
  </div>
</template>

<script>
import Gravatar from "./Gravatar";
export default{
  components: {Gravatar},
}
</script>
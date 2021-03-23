<template>
  <div class="about">
    <h1>This is an about page</h1>
    <Gravatar gen_key="boaSDS"/>
  </div>
</template>

<script>
import Gravatar from "@/components/Gravatar";
export default {
  name: "About",
  components:{Gravatar}

};
</script>

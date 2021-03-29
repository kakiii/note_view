<template>
  <div class="about">
    <h1>This is an about page</h1>
    <Gravatar :gen_key="inputs" />
    <input placeholder="INPUT USER NAME" v-model="inputs" />
  </div>
</template>

<script>
import Gravatar from "@/components/Gravatar2";

export default {
  name: "About",
  components: { Gravatar },
  data() {
    return {
      inputs: "users",
    };
  },
};
</script>

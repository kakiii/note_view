<template>
  <div class="about">
    <h1>This is an about page</h1>
    <Gravatar :gen_key="inputs" />
    <GravatarsSVG :gen_key="inputs" />
    <input placeholder="INPUT USER NAME" v-model="inputs" />
  </div>
</template>

<script>
import GravatarsSVG from "./Gravatar_SVG";
import Gravatar from "./Gravatar";

export default {
  name: "About",
  components: { Gravatar, GravatarsSVG },
  data() {
    return {
      inputs: "users",
    };
  },
};
</script>

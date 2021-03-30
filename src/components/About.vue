<template>
  <div class="about">
    <h1>This is an about page</h1>
    <GravatarsSVG :gen_key="inputs" />
    <input placeholder="INPUT USER NAME" v-model="inputs" />
  </div>
</template>

<script>
import GravatarsSVG from "./Gravatar_SVG";

export default {
  name: "About",
  components: { GravatarsSVG },
  data() {
    return {
      inputs: "users",
    };
  },
};
</script>



<template>
  <div v-if="mode === 'header'">
    <span style="width:16em;height:16em;" v-html="svgs" />
  </div>
  <div v-else-if="mode === 'userpage'">
    <p style="width: 16em; height: 16em;" v-html="svgs" />
  </div>
</template>

<script>
import multiavatar from "@multiavatar/multiavatar";

export default {
  name: "Gravatar",
  props: { gen_key: String, mode: String },
  data() {
    return {
      svgs: multiavatar(this.gen_key),
    };
  },
  watch: {
    gen_key(newVal) {
      this.svgs = multiavatar(newVal);
      // Below is only for Debug use.
      // console.log("Prop changed", newVal, '| was : ',oldVal)
    },
    svgs(newVal, oldVal) {
      console.log("Prop changed", newVal, "| was : ", oldVal);
    },
  },
};
</script>

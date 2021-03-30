<template>
  <p style="width: 4em" v-html="svgs" />
</template>

<script>
import multiavatar from "@multiavatar/multiavatar";

export default {
  name: "Gravatar",
  props: { gen_key: String },
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

<template>
  <div v-if="size == 4">
    <p
      style="width: 2em; height: 2em; border-radius: 50%; overflow: hidden"
      v-html="svgs"
    />
  </div>
  <div v-else-if="size == 6">
    <p
      style="width: 3em; height: 3em; border-radius: 50%; overflow: hidden"
      v-html="svgs"
    />
  </div>
  <div v-else-if="size == 8">
    <p
      style="width: 4em; height: 4em; border-radius: 50%; overflow: hidden"
      v-html="svgs"
    />
  </div>
</template>

<script>
import md5 from "js-md5";

export default {
  name: "GravatarsSVG",
  props: { gen_key: String, size: Number },
  data() {
    return {
      svgs: avatar(this.gen_key, this.size),
    };
  },
  watch: {
    gen_key(newVal) {
      this.svgs = avatar(newVal, this.size);
      // Below is only for Debug use.
      // console.log("Prop changed", newVal, '| was : ',oldVal)
    },
    svgs(newVal, oldVal) {
      console.log("Prop changed", newVal, "| was : ", oldVal);
    },
  },
};

function avatar(gen_key, size) {
  if (gen_key.length == 0) {
    return null;
  }
  var hash = md5(gen_key);
  var str = hash.toString(16);
  var color = "#" + str.substring(0, 6);
  var svg = "<svg>";
  for (var i = 0; i < 8; i++) {
    for (var j = 0; j < 4; j++) {
      if (str.charAt(4 * i + j) < 8) {
        svg +=
          "<rect x='" +
          size * j +
          "' y='" +
          size * i +
          "' width='" +
          size +
          "' height='" +
          size +
          "' style='fill:white'/>";
        svg +=
          "<rect x='" +
          size * (7 - j) +
          "' y='" +
          size * i +
          "' width='" +
          size +
          "' height='" +
          size +
          "' style='fill:white'/>";
      } else {
        svg +=
          "<rect x='" +
          size * j +
          "' y='" +
          size * i +
          "' width='" +
          size +
          "' height='" +
          size +
          "' style='fill:" +
          color +
          "'/>";
        svg +=
          "<rect x='" +
          size * (7 - j) +
          "' y='" +
          size * i +
          "' width='" +
          size +
          "' height='" +
          size +
          "' style='fill:" +
          color +
          "'/>";
      }
    }
  }
  svg += "</svg>";
  return svg;
}
</script>

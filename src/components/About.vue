<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>
      <Gravatar :gen_key="inputs" mode="userpage" />
    </p>
    <p>
      <GravatarsSVG :gen_key="inputs" mode="userpage" />
    </p>
    <input placeholder="INPUT USER NAME" v-model="inputs" />
    <!--这里放一个Log Out的功能，能够去除Login的状态。-->
    <input type="button" v-on:click="logout" value="LOGOUT" />
  </div>
</template>

<script>
import Gravatar from "./Gravatar.vue";
import GravatarsSVG from "./Gravatar_SVG.vue";

export default {
  name: "About",
  components: { Gravatar, GravatarsSVG },
  data() {
    return {
      inputs: "users",
    };
  },
  methods: {
    logout() {
      this.$store.state.isLogin = false;
      this.$store.state.username = "";
      this.$alert("You have logged out!");
      setTimeout(function () {
        this.$router.push("/");
      }, 2000);
    },
  },
};
</script>

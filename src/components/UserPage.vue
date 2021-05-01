<template>
  <div>
    <!-- <p>Hello, {{ this.$store.state.username }}!</p> -->

    <!-- <Gravatar :gen_key="this.$store.state.username" style="margin: auto" /> -->
    <el-container>
      <p style="float: left ; font-size: 30px">
        {{ "username: " + this.$store.state.username }}
      </p>
    </el-container>

    <el-container style="margin-left: 40px; margin-top: 20px">
      <el-aside width="300px">
        <p v-if="!this.$store.state.gravatar">
          <GravatarsSVG :gen_key="this.$store.state.username" mode="userpage" />
        </p>
        <p v-else>
          <Gravatar :gen_key="this.$store.state.username" mode="userpage" />
        </p>

        <br />

        <el-button
            class="gravatarButton"
            v-if="this.$store.state.gravatar"
            v-on:click="changeGravatar"
            size="mini"
        >
          Switch to Pixel Style
        </el-button>

        <el-button
            class="pixelButton"
            v-if="!this.$store.state.gravatar"
            size="mini"
            v-on:click="changeGravatar"
        >
          Switch to Gravatar Style(suggests on firefox)
        </el-button>

      </el-aside>

    </el-container>
    <el-container style="margin-left: 90px; margin-top: 10px">
      <el-button
          class="logoutButton"
          size="mini"
          v-on:click="logout"
          value="LOGOUT"
      >Log out</el-button>
    </el-container>

  </div>
</template>

<script>
import Gravatar from "./Gravatar.vue";
import GravatarsSVG from "./Gravatar_SVG.vue";
import axios from "axios";

export default {
  components: { Gravatar, GravatarsSVG },
  data() {
    return {
      article_list: [],
    };
  },
  methods: {
    get_my_article() {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://localhost:5000/article/user/";
      } else {
        url = "article/user/";
      }
      axios
        .get(url + this.$store.state.username)
        .then((res) => {
          let arr = res.data["article_collection"];
          console.log(arr);
          this.article_list = arr;
        })
        .catch((err) => console.log(err));
    },
    changeGravatar() {
      if (this.$store.state.gravatar) {
        this.$store.state.gravatar = false;
      } else {
        this.$store.state.gravatar = true;
      }
      console.log("change gravatar");
    },


    mounted() {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://localhost:5000/article/user/";
      } else {
        url = "article/user/";
      }
      axios
          .get(url + this.$store.state.username)
          .then((res) => {
            let arr = res.data["article_collection"];
            console.log(arr);
            this.article_list = arr;
          })
          .catch((err) => console.log(err));
    },

    logout() {
      this.$store.state.isLogin = false;
      this.$store.state.username = "";
      this.$alert("You have logged out!");
      setTimeout(function () {
        this.$router.push("/discussion");
      }, 2000);
    },

  },




};

</script>

<style scoped>
.pixelButton,
.gravatarButton，
.pixelButton:focus,
.gravatarButton:focus{
  width: 200px;
  margin-top: 0px;
  background: #93E0FF;
  color: #253B6E;
  border-color: #C4E2D8;
  font-size: small;
}

.logoutButton{
  width: 200px;
  margin-top: 0px;
  text-align: center;
  background: #93E0FF;
  color: #253B6E;
  border-color: #C4E2D8;
  font-size: small;
}


</style>

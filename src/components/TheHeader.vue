<template>
  <div>
    <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        router
        @select="handleSelect"
        background-color="#93E0FF"
        text-color="#253B6E"
        active-text-color="#FFFFD2"
    >
      <el-menu-item index="/login">LOGIN</el-menu-item>
      <el-menu-item index="/register">REGISTER</el-menu-item>
      <el-menu-item index="/editor">EDITOR</el-menu-item>
      <el-menu-item index="/find">FIND</el-menu-item>
      <el-menu-item index="/code">CODE</el-menu-item>
      <el-menu-item index="/about">ABOUT</el-menu-item>
      <el-menu-item index="/discussion">DISCUSSION</el-menu-item>
      <el-menu-item index="/todo">TODOLIST</el-menu-item>
      <el-menu-item v-if="this.$store.state.username==='admin'" index="/management">MANAGEMENT</el-menu-item>
      <el-menu-item
        :disabled="!this.$store.state.isLogin"
        style="float: right"
        :index="{
          name: 'userpage',
          params: { username: this.$store.state.username },
        }"
      >
        <div v-if="!this.$store.state.gravatar">
          <Gravatar :gen_key="this.$store.state.username" mode="header" />
        </div>
        <div v-else>
          <GravatarsSVG :gen_key="this.$store.state.username" mode="header" />
        </div>
      </el-menu-item>
      <!-- <el-menu-item :disabled="!this.$store.state.isLogin" style="float: right"
                    :index="{name:'userpage',params:{username:this.$store.state.username}}">My Page
      </el-menu-item> -->
    </el-menu>
  </div>
</template>

<script>
import Gravatar from "./Gravatar.vue";
import GravatarsSVG from "./Gravatar_SVG.vue";

export default {
  name: "Header",
  components: { Gravatar, GravatarsSVG },
  data() {
    return {
      isCollapse: false,
      activeIndex: "/login",
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  },
};
</script>

<template>
  <div>
    <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        router
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
      <el-menu-item index="/login">LOGIN</el-menu-item>
          <el-menu-item index="/editor">EDITOR</el-menu-item>
    </el-menu>
<!--    <router-link to="/login">LOGIN</router-link>-->
<!--    <router-link to="/editor">EDITOR</router-link>-->
<!--    <router-link to="/">HOME</router-link>-->
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      isCollapse: false
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  },
};
</script>
<template>
  <div>
    <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      router
      @select="handleSelect"
      background-color="#020080"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item index="/login">LOGIN</el-menu-item>
      <el-menu-item index="/register">REGISTER</el-menu-item>
      <el-menu-item index="/editor">EDITOR</el-menu-item>
      <el-menu-item index="/find">FIND</el-menu-item>
      <el-menu-item index="/code">CODE</el-menu-item>
      <el-menu-item index="/about">ABOUT</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      isCollapse: false,
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

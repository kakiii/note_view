<template>
  <div>
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">OPEN</el-radio-button>
      <el-radio-button :label="true">CLOSE</el-radio-button>
    </el-radio-group>
    <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
      <el-menu-item index="1">
        <i class="el-icon-menu"></i>
          <span slot="title"><router-link to="/login">LOGIN</router-link></span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title"><router-link to="/editor">EDITOR</router-link> </span>
      </el-menu-item>
      <el-menu-item index="3" >
        <i class="el-icon-menu"></i>
        <span slot="title"><router-link to="/">HOME</router-link> </span>
      </el-menu-item>
    </el-menu>
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
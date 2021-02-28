// 这是根组件,所有的其他组件都在它之上构建 //
下面的tempalte内容就是HTML内容,使用的语言也是HTML
<template>
  <div id="app">
    <q-btn color="white" text-color="black" label="HOME" to="/"/>
    <q-btn color="primary" label="ABOUT" to="/about"/>
    <!--在这里的router-link能够直接通向指定的URL地址，但如果没有实现注册对应的组件，也只能显示空白-->
    <q-btn color="secondary" label="EDITOR" to="/editor"/>
    <q-btn color="amber" glossy label="DISCUSSION" to="/discussion"/>
    <q-btn color="deep-orange" glossy label="404" to="/404"/>
    
    
    <el-button type="primary" icon="el-icon-search">Search</el-button>
    <hr
      align="center"
      width="80%"
      color="#987cb9"
      size="3"
      style="filter: alpha(opacity=100, finishOpacity=0, style=3)"
    />
    <router-view></router-view>
    <hr
      align="center"
      width="80%"
      color="#987cb9"
      size="3"
      style="filter: alpha(opacity=100, finishOpacity=0, style=3)"
    />
  </div>
</template>

<script>
export default {
  name: "app",
  components: {},
};
</script>
// 下面的style部分就是CSS内容,使用的语言就是CSS
<style>
@import "~element-ui/lib/theme-chalk/index.css";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

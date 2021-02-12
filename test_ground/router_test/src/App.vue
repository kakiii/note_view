<template>
  <div id="app">
        <el-main>
          <el-row :gutter="20">
            <el-button>
              <router-link to="/">Home</router-link>
            </el-button>
            <el-button>
              <router-link to="/about">About</router-link>
            </el-button>
            <!--      在这里的router-link能够直接通向指定的URL地址，但如果没有实现注册对应的组件，也只能显示空白-->
            <el-button>
              <router-link to="/editor">EDITOR</router-link>
            </el-button>
            <el-button>
              <router-link to="/discussion">Discussion Board</router-link>
            </el-button>
            <el-button>
              <router-link to="/404">通向404界面</router-link>
            </el-button>
            <el-button type="primary" icon="el-icon-search">Search</el-button>
          </el-row>
          <p>向上是不变的路由区</p>
          <p>这里的内容在App.vue文件中定义</p>
          <p>下方是Router-View的区域</p>
          <hr align="center" width="80%" color="#987cb9" size="3"
              style="filter: alpha(opacity=100,finishOpacity=0,style=3)">
          <router-view></router-view>
          <hr align="center" width="80%" color="#987cb9" size="3"
              style="filter: alpha(opacity=100,finishOpacity=0,style=3)">
          <p>上面是Router-View的区域</p>
          <p>下面也是不变的路由区</p>
          <br><br><br><br>
          <p>需要现在router/index.js里面注册</p>
        </el-main>
  </div>

</template>

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

<template>
  <div>
    <h1>SEARCH</h1>
    <el-input
        class="search"
        type="search"
        v-model="id"
        placeholder="Search for an article"
        prefix-icon="el-icon-tickets"
    ></el-input>

    <el-button
        icon="el-icon-search"
        class="search-button"
        type="button"
        @click="get_article()"
        block
    ></el-button
    >
    <MarkdownItVue :content="content"/>
  </div>
</template>

<script>
import axios from "axios";
import store from "../store";
import "markdown-it-vue/dist/markdown-it-vue.css";
import MarkdownItVue from "markdown-it-vue";
export default {
  beforeRouteEnter(to,from,next){
    if(store.state.isLogin == true){
      next();
    }else{
      next("/login");
    }
  },
  name: "FindArticle",
  components:{MarkdownItVue},
  data() {
    return {
      id: "",
      content: "",
      title:""
    };
  },
  methods: {
    get_article() {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://127.0.0.1:5000/"
      }
      else{
        url = "/"
      } 

      axios.post(url+"article/find",{
        title:this.id
      }).then((res) => {
        console.log(res.data["title"]);
        this.title = res.data["title"];
        this.content = res.data["content"];
      })
    },
  },
};
</script>

<style scoped>
.search{
  width: 200px;
}
</style>

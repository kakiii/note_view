<template>
  <div>
    <input v-model="id"/>
    <button v-on:click="get_article()">HIT TO GET VALUE</button>
    <table>
      <thead>
      <tr>
        <th>ID</th>
        <th>Content</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td>{{ this.id }}</td>
<!--        <td>{{ content }}</td>-->
      </tr>
      </tbody>
    </table>
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
              axios
            .get(url + "article/" + this.id)
            .then((res) => {
              console.log(res.data["Content"]);
              this.content = res.data["Content"];
            })
            .catch(() => (this.content = "NO CONTENT"));
    },
  },
};
</script>

<style scoped></style>

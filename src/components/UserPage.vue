<!-- todolist试做,需要优化ui。checkbox问题解决，本地存储todolist-->

<template>
  <div>
    <p>Hello, {{ this.$store.state.username }}!</p>

    <Gravatar :gen_key=this.$store.state.username
              style="margin: auto"/>

    <input type="button" value="GET ARTCILE" v-on:click="get_my_article"/>
    <p>User's article collection in array form.</p>
<!--    之后其他人把这个东西改成v-for的形式-->
<!--    等待增加具体的美化-->
<!--    使用mounted，在user page加载的时候就能自动获取后端用户的数据-->

    <p>{{article_list}}</p>
  </div>
</template>

<script>
import Gravatar from "./Gravatar.vue";
import axios from "axios";
export default {
  components: {Gravatar},
  data(){
    return{
      article_list:[],
    }
  },
  methods: {
    get_my_article() {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://localhost:5000/article/user/";
      } else {
        url = "article/user/";
      }
      axios.get(url + this.$store.state.username).then((res) => {
        let arr = res.data["article_collection"]
        console.log(arr);
        this.article_list = arr;
      }).catch((err) => console.log(err));
    }
  },
  mounted() {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://localhost:5000/article/user/";
      } else {
        url = "article/user/";
      }
      axios.get(url + this.$store.state.username).then((res) => {
        let arr = res.data["article_collection"]
        console.log(arr);
        this.article_list = arr;
      }).catch((err) => console.log(err));
    }
}
</script>
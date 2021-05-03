<template>
  <div>
    <h1>HOME PAGE</h1>
    <!-- <ul>
      <li v-for="article in articles" :key="article">{{article.Title}}</li>
    </ul> -->
    <el-container>
    <MarkdownItVue style="width:25%"
    v-for="article in articles" :key="article"
    :content="article.Content" :options="options" class="md-body" />
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
import MarkdownItVue from "markdown-it-vue";
export default {
  name: "Home",
  components: { MarkdownItVue },
  mounted() {
    let url = "";
    if (process.env.NODE_ENV === "development") {
      url = "http://localhost:5000/article/";
    } else {
      url = "/article/";
    }
    this.random_article_ids = axios
      .get(url + "random")
      .then((res) => {
        this.random_article_ids = res.data["id"];
        let articles_get = [];
        this.random_article_ids.forEach((id) => {
          articles_get.push(axios.get(url + id));
        });
        axios.all(articles_get).then((res) => {
          this.articles = res.map((r) => r.data);
          console.log(this.articles);
        });
        //console.log(this.random_article_ids);
      })
      .catch((err) => console.log(err));
  },
  methods: {},
  data() {
    return {
      random_article_ids: [],
      articles: [],
    };
  },
};
</script>

<style scoped></style>

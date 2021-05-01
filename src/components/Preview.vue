<template>
<div>
  <h1 style="text-align:left">Title: {{title}}</h1>
  <MarkdownItVue :content="content" :options="options" class="md-body" />
</div>
</template>

<script>
import MarkdownItVue from "markdown-it-vue";
import axios from "axios";
export default {
  components: { MarkdownItVue },
  name: "Preview",
  mounted() {
    this.id = window.location.href.split("/").pop().toString();
    console.log(this.id);
    if (this.id !== "") {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://localhost:5000/article/";
      } else {
        url = "/article/";
      }
      axios
        .get(url + this.id)
        .then((res) => {
          this.content = res.data["Content"];
          this.title = res.data["Title"];
          console.log(this.title);
        })
        .catch((err) => console.log(err));
    }else{
      this.$router.push("/404");
    }
  },

  data() {
    return {
      id: "",
      title:"",
      content: "",
    };
  },
};
</script>

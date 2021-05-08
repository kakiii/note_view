<template>
<div>
  <el-button v-on:click="print">Print</el-button>
  <h1 style="text-align:left">Author: <i>{{author}}</i></h1>
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
          this.author = res.data['author'];

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
      author:"",
    };
  },
  methods:{
    print(){
      window.print();
    }
  }
};
</script>

<style scopde>
.el-button {
  width: 80px;
  height: 40px;
  margin-top: 10px;
  background: #93E0FF;
  color: white;
  border-color: #C4E2D8;
  font-size: medium;
}
</style>

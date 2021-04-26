
<template>
  <div>
    <el-container>
      <el-header>This is discussion borad. 这是讨论版</el-header>

      <el-main>
      <ul v-for="(item, index) in list" :key="index">
        <span>{{ item.author + " " + item.content }}</span>
      </ul>
      </el-main>

      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-size="pagesize"
        :page-sizes="[8, 10, 20, 40]"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>

      <el-input
        type="textarea"
        :autosize="{ minRows: 2, maxRows: 4 }"
        placeholder="请输入内容"
        v-model="textarea"
      >
      </el-input>

      <el-button type="send" @click="clickSending()">发送</el-button>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Discussion",
  data() {
    return {
      currentPage: 1,
      pagesize: 8,
      total: 800,
      textarea: "",
      discussionContent: "",
      list: [],
    };
  },

  methods: {
    handleSizeChange(size) {
      this.pagesize = size;
      console.log(this.pagesize);
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;
      console.log(this.currentPage);
    },
    clickSending() {
      var that = this;
      console.log("Hello " + that.textarea);
      this.textarea = "";
    },
  },
  watch: {
    pagesize: function () {
      let url = "";
      if(process.env.NODE_ENV === "development"){
        url = "http://127.0.0.1:5000/";
      }else{
        url = "/"
      }
      this.list = [];
      var axiosList = [];
      var i;
      for (i = 1; i <= this.pagesize; i++) {
        axiosList.push(
          axios.get(url + "content/discussion/" + i)
        );
      }
      axios
        .all(axiosList)
        .then((results) => {
          let temp = results.map((r) => r.data);
          // console.log("hello" + temp[1]);
          // console.log(temp[0].author);
          for (let j = 0; j < temp.length; j++) {
            if (temp[j] == undefined || temp[j].author == null) {
            } else {
              this.list.push({
                author: temp[j].author,
                content: temp[j].content,
              });
            }
          }
        })
        .catch((err) => console.log(err));
    },
  },
  mounted() {
          let url = "";
      if(process.env.NODE_ENV === "development"){
        url = "http://127.0.0.1:5000/";
      }else{
        url = "/"
      }
    var axiosList = [];
    var i;
    for (i = 1; i <= this.pagesize; i++) {
      axiosList.push(
        axios.get(url + "content/discussion/" + i)
      );
    }
    axios
      .all(axiosList)
      .then((results) => {
        let temp = results.map((r) => r.data);
        // console.log("hello" + temp[1]);
        // console.log(temp[0].author);
        for (let j = 0; j < temp.length; j++) {
          if (temp[j] == undefined || temp[j].author == null) {
          } else {
            this.list.push({
              author: temp[j].author,
              content: temp[j].content,
            });
          }
        }
      })
      .catch((err) => console.log(err));
  },
};
</script>

<style>
.el-header {
  background-color: #161515;
  color: rgb(255, 0, 0);
  text-align: center;
  line-height: 60px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

.el-footer {
  background-color: #92be1a;
  color: rgb(194, 233, 87);
  text-align: center;
  line-height: 60px;
}
</style>

<style scoped>
</style>


<template>
  <div>
    <el-container>
      <el-header>This is discussion borad. 这是讨论版</el-header>

      <el-main>
        <ul v-for="(item, index) in list" :key="index">
          <span>{{ item.id + " ::" + item.author + " " + item.content }}</span>
        </ul>
      </el-main>

      <el-pagination
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-size="pagesize"
        layout="total, prev, pager, next, jumper"
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
      total: 0,
      textarea: "",
      discussionContent: "",
      list: [],
    };
  },

  methods: {
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;
      console.log(this.currentPage);
    },

    clickSending() {
      if (this.textarea == "") {
        alert("not null");
      } else {
        let data = {
          author: "name", //need get author name api
          content: this.textarea,
        };
        axios
          .post(
            "http://127.0.0.1:5000/content/discussion",
            data
            // , {header: {
            //   "Content-Type": "application/json", //如果写成contentType会报错
            // }}
          )
          .then((res) => {
            console.log("res=>", res);
          });
        this.textarea = "";
      }
      this.currentPage=1;
    },
  },

  watch: {
    currentPage: function () {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://127.0.0.1:5000/";
      } else {
        url = "/";
      }

      this.list = [];
      var axiosList = [];

      let currentPos = this.total - (this.currentPage-1) * 8;
      if (currentPos > 8) {
        for (let i = currentPos; i >= currentPos-7; i--) {
          axiosList.push(axios.get(url + "content/discussion/" + i));
        }
      }else{
        // currentPos=currentPos+8;
        for (let i = currentPos; i >= 1; i--) {
          axiosList.push(axios.get(url + "content/discussion/" + i));
        }
      }

      axios
        .all(axiosList)
        .then((results) => {
          let temp = results.map((r) => r.data);
          for (let j = 0; j < temp.length; j++) {
            this.list.push({
              author: temp[j].author,
              content: temp[j].content,
              id: temp[j].id,
            });
          }
        })
        .catch((err) => console.log(err));
    },
  },

  mounted() {
    let url = "";
    if (process.env.NODE_ENV === "development") {
      url = "http://127.0.0.1:5000/";
    } else {
      url = "/";
    }

    axios
      .get(url + "content/discussion")
      .then((res) => {
        console.log("hello" + res.data["discussion_size"]);
        this.total = res.data["discussion_size"];
        // i = this.total;
        console.log("total is" + this.total);

        if (this.total !== 0) {
          let i = 0;
          i = this.total;
          var axiosList = [];

          console.log("already loading " + i);

          if (i > 8) {
            for (; i >= this.total - 7; i--) {
              axiosList.push(axios.get(url + "content/discussion/" + i));
            }
          } else {
            for (; i >= 1; i--) {
              axiosList.push(axios.get(url + "content/discussion/" + i));
            }
          }

          axios
            .all(axiosList)
            .then()
            .then((results) => {
              let temp = results.map((r) => r.data);
              console.log("hello" + temp[1]);
              // console.log(temp[0].author);
              for (let j = 0; j < temp.length; j++) {
                this.list.push({
                  author: temp[j].author,
                  content: temp[j].content,
                  id: temp[j].id,
                });
              }
            })
            .catch((err) => console.log(err));
        }
      })
      .catch((err) => console.log(err));
  },
};
</script>

<style scoped>
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

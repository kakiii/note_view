
<template>
  <div>
    <el-container>
      <el-header>DISCUSSION</el-header>

      <ul v-for="(item, index) in list" :key="index">
        <el-main>
          <span class="dis">{{
            item.time + "   " + item.author + ": " + item.content
          }}</span></el-main
        >
      </ul>

      <el-pagination
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-size="pagesize"
        :page-sizes="[8, 10, 20, 40]"
        layout="total, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>

      <el-input
        type="textarea"
        :autosize="{ minRows: 2, maxRows: 4 }"
        placeholder="Please post here"
        v-model="textarea"
      >
      </el-input>

      <el-button
        class="sendButton"
        type="send"
        @click="clickSending()"
        icon="el-icon-check"
        :disabled="textarea.length<=3"
        >Send</el-button
      >
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
import store from "../store";
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
      //console.log(this.currentPage);
    },

    clickSending() {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://127.0.0.1:5000/content/discussion/";
      } else {
        url = "/content/discussion/";
      }

      if (store.state.isLogin == true) {
        if (this.textarea == "") {
          alert("not null");
        } else {
          let data = {
            author: this.$store.state.username,
            content: this.textarea,
          };
          console.log(data);

          axios
            .post(url, {
              author: this.$store.state.username,
              content: this.textarea,
            })
            .then((res) => {
              console.log("res=>", res);
            })
            .catch((err) => {
              console.log(err);
            });
        }

        //this.total=this.total+1;

        if (this.currentPage == 1) {
          var temp = [];
          var d = new Date();
          let time = d.getFullYear()+"-"+(d.getMonth()+1)+"-"+d.getDate()+" "+d.getHours()+":"+d.getMinutes()+":"+d.getSeconds()+"."+d.getMilliseconds()+"000";
          temp.push({
            author: this.$store.state.username,
            content: this.textarea,
            time: time,
          });
          var listtemp = this.list;
          for (let i in listtemp) {
            //console.log(listtemp[i]);
            temp.push(listtemp[i]);
          }
          if (this.total > 8) {
            temp.pop();
          }
          this.list = temp;
        }
        this.textarea = "";
      } else {
        alert("Must log in first");
      }
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

      axios.get(url + "content/discussion").then((res) => {
        //console.log("hello" + res.data["discussion_size"]);
        this.total = res.data["discussion_size"];
        // i = this.total;
        //console.log("total is" + this.total);

        this.list = [];
        var axiosList = [];

        let currentPos = this.total - (this.currentPage - 1) * 8;
        if (currentPos > 8) {
          for (let i = currentPos; i >= currentPos - 7; i--) {
            axiosList.push(axios.get(url + "content/discussion/" + i));
          }
        } else {
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

                time: temp[j].time,
              });
            }
          })
          .catch((err) => console.log(err));
      });
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
        //console.log("hello" + res.data["discussion_size"]);
        this.total = res.data["discussion_size"];
        // i = this.total;
        //console.log("total is" + this.total);

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
              //console.log("hello" + temp[1]);
              // console.log(temp[0].author);
              for (let j = 0; j < temp.length; j++) {
                this.list.push({
                  author: temp[j].author,
                  content: temp[j].content,

                  time: temp[j].time,
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
  background-color: white;
  color: black;
  text-align: center;
  line-height: 60px;
  font-size: xx-large;
  font-weight: bolder;
}

.el-main {
  background-color: white;
  color: black;
  text-align: left;
  line-height: 35px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.sendButton {
  background-color: #93e0ff;
  color: #253b6e;
  text-align: center;
  line-height: 15px;
}
</style>


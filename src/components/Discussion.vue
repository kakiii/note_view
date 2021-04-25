
<template>
  <div>
    <el-container>
      <el-header>This is discussion borad. 这是讨论版</el-header>

      <el-main>

        <ul v-for="(item, index) in list" :key="index">
          <span>{{ item.text }}</span>
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
import axios from 'axios';


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
      this.list=[];
      var i;
      for (i = 1; i <= this.pagesize; i++) {
        axios
          .get("http://127.0.0.1:5000/content/discussion/" + i)
          .then((res) => {
            console.log("数据：", res.data["author"]);
            this.discussionContent = res.data["author"];
            this.list.push({ text: this.discussionContent });
          });

          setTimeout("function",50000);
      }
    }
  },
  mounted() {
    var i;
    for (i = 1; i <= this.pagesize; i++) {
      axios.get("http://127.0.0.1:5000/content/discussion/" + i).then((res) => {
        console.log("数据：", res.data["author"]);
        this.discussionContent = res.data["author"];
        this.list.push({ text: this.discussionContent });
      });
    }
    },
};
</script>

<style>
.el-header {
  background-color: #d1b3b3;
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

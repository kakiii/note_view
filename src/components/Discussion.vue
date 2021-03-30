<!-- 讨论版试做v0.1,后期需要对放数据 翻页 输入进一步增加内容-->

<template>
  <div>
    <el-container>
      <el-header>This is discussion borad. 这是讨论版</el-header>

      <!-- 
    <el-container>
      <el-main
        ><ul
          class="infinite-list"
          ref="scroll"
          v-infinite-scroll="handleScroll"
          infinite-scroll-disabled="disabled"
          style="overflow: auto"
        >
          <li v-for="i in count" :key="i" class="infinite-list-item">
            {{ i }}
          </li>
        </ul>

          <p v-if="loading">Loading...</p>
       <p v-if="noMore">No more...</p>

      </el-main>-->

      <el-main>
        <li class="content" v-for="i in 8" :key="i" style="overflow: auto">
          {{ "this is " + i + "th comment" }}
        </li></el-main
      >

      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage3"
        :page-size="100"
        layout="prev, pager, next, jumper"
        :total="1000"
      >
      </el-pagination>

      <el-footer
        ><el-input v-model="input" placeholder="input something"></el-input
      ></el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Discussion",
  data() {
    return {
      input: "",
    };
  },
  methods: {},
};
</script>

<!-- 
<script>
export default {
  name: "Discussion",
  data() {
    return {
      count: 5,
      loading: false,
    };
  },
  computed: {
    /*noMore() {
      return this.count >= 30;
    },*/
    disabled() {
      //return this.loading || this.noMore;
      return false || this.loading;
    },
  },
  mounted() {
    var that = this;
    document
      .getElementsByClassName("content")[0]
      .addEventListener("scroll", that.handleScroll, true);
  },
  methods: {
    handleScroll() {
      var that = this;
      var scrollHeight = that.$refs["scrolling"].scrollHeight;
      var scrollTop = that.$refs["scrolling"].scrollTop;
      var clientHeight = that.$refs["scrolling"].clientHeight;

      console.log("Scrollheight is " + scrollHeight);
      console.log("scrollTop is " + scrollTop);
      console.log("client height is " + clientHeight);

      if (scrollTop + clientHeight >= scrollHeight) {
        this.count += 5;
      }
    },

    /*load() {
      this.loading = true;
      setTimeout(() => {
        this.count += 2;
        this.loading = false;
      }, 100);
    },*/
  },
};
</script>
-->

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
  background-color: #d1b3b3;
  color: rgb(255, 0, 0);
  text-align: center;
  line-height: 60px;
}
</style>

<!--<script>
import Login from "@/components/Login";
export default {
  name: "Discussion",
  components: { Login },
};
</script>-->

<style scoped></style>

<!-- todolist试做,需要优化ui。checkbox问题解决，本地存储todolist-->

<template>
  <div>
    <!-- 测试用
    <p>Local Data = {{ st }}</p>
    <button @click="myGetFunction()">Get Local Storage Data</button><br /> -->

    <el-container>
      <!-- <el-header height="20">
        <h1>To Do List</h1>
      </el-header> -->
      <el-main>
        <h1>To Do List</h1>
        <el-input
          type="text"
          v-model="inputValue"
          placeholder="Enter your plan"
          @keyup.enter.native="add()"
          style="width: 400px"
        ></el-input>
        <el-button icon="el-icon-plus" type="send" @click="add()"></el-button>

        <el-row gutter="20">
          <el-col :span="12">
            <div class="grid-content bg-purple">
              <h3>To Do</h3>
              <ul v-for="(item, index) in list" :key="'info-' + index">
                <!-- 这里的info没什么意义就是防俩v-for并行报错 -->
                <li v-if="item.done === false">
                  <div style="float: left">
                    <el-checkbox type="checkbox" @change="change(index, true)">
                    </el-checkbox>
                    <span>{{ item.text }}</span>
                  </div>
                  <div style="float: right; margin-right: 40px">
                    <el-button
                      icon="el-icon-delete"
                      size="mini"
                      circle
                      @click="remove(index)"
                    ></el-button>
                  </div>
                  <br />
                </li>
              </ul>
            </div>
          </el-col>

          <el-col :span="12">
            <div class="grid-content bg-purple">
              <h3>Done</h3>
              <div>
                <ul v-for="(item, index) in list" :key="index">
                  <li v-if="item.done === true">
                    <div style="float: left">
                      <el-checkbox
                        type="checkbox"
                        @change="change(index, false)"
                        checked="checked"
                      ></el-checkbox>
                      <span>{{ item.text }}</span>
                    </div>
                    <div style="float: right; margin-right: 40px">
                      <el-button
                        icon="el-icon-delete"
                        size="mini"
                        circle
                        @click="remove(index)"
                      ></el-button>
                    </div>
                    <br />
                  </li>
                </ul>
              </div>
            </div>
          </el-col>
        </el-row>

        <!-- 折叠
        <el-row type="flex" justify="center">
          <el-col :span="12">
            <el-collapse>
              <el-collapse-item title="Todo">
                <ul v-for="(item, index) in list" :key="'info-' + index">
                  <li v-if="item.done === false">
                    <div style="float: left">
                      <el-checkbox
                        type="checkbox"
                        @change="change(index, true)"
                      >
                      </el-checkbox>
                      <span>{{ item.text }}</span>
                    </div>
                    <div style="float: right; margin-right: 40px">
                      <el-button
                        icon="el-icon-delete"
                        size="mini"
                        circle
                        @click="remove(index)"
                      ></el-button>
                    </div>
                    <br />
                  </li>
                </ul>
              </el-collapse-item>
              <el-collapse-item title="Done">
                <div>
                  <ul v-for="(item, index) in list" :key="index">
                    <li v-if="item.done === true">
                      <div style="float: left">
                        <el-checkbox
                          type="checkbox"
                          @change="change(index, false)"
                          checked="checked"
                        ></el-checkbox>
                        <span>{{ item.text }}</span>
                      </div>
                      <div style="float: right; margin-right: 40px">
                        <el-button
                          icon="el-icon-delete"
                          size="mini"
                          circle
                          @click="remove(index)"
                        ></el-button>
                      </div>
                      <br />
                    </li>
                  </ul>
                </div>
              </el-collapse-item>
            </el-collapse>
          </el-col>
        </el-row> -->
      </el-main>
    </el-container>
  </div>
</template>

<script>
import store from "../store";

function set(key, val) {
  localStorage.setItem(key, JSON.stringify(val));
}

function get(key) {
  return JSON.parse(localStorage.getItem(key));
}

var myStorage = {
  set: set,
  get: get,
};

export default {
  name: "todo",
  beforeRouteEnter(to, from, next) {
    if (store.state.isLogin != true) {
      next("/login");
    } else {
      next();
    }
  },
  data() {
    return {
      inputValue: "",
      list: [],
      st: "",

      //mylist: localStorage.getItem("myitem"),
    };
  },
  methods: {
    add() {
      if (this.inputValue == null) {
        alert("Can not be null!");
      } else {
        //this.list.push({ text: this.inputValue, done: false });
        this.list.push({ text: this.inputValue, done: false });

        this.inputValue = null;
      }
    },
    change(index, done) {
      if (done) {
        this.list[index].done = true;
      } else {
        this.list[index].done = false;
      }
    },
    remove(index) {
      this.list.splice(index, 1);
    },
    /*测试用
    myGetFunction: function () {
      this.st = myStorage.get("list");
      console.log("hello" + this.st);
    },*/
  },
  watch: {
    list: {
      deep: true,
      handler: function (newVal, oldVal) {
        if (newVal) {
          myStorage.set("list", newVal);
        } else {
          myStorage.set("list", oldVal);
        }
      },
    },
  },
  mounted: function () {
    this.list = myStorage.get("list") || [];
  },
};
</script>

<style scoped>
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 30px;
}

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 5px;
  min-height: 36px;
}

.bg-purple {
  background: #93E0FF;
  color: #253B6E;
  font-size: small;
}

/* .bg-purple-dark {
  background: #99a9bf;
}

.bg-purple-light {
  background: #e5e9f2;
} */

ul {
  list-style: none;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

/* .left {
  position: absolute;
  left: 0;
  width: 100px;
  padding: 10px;
}
.right {
  position: absolute;
  right: 0px;
  width: 100px;
  padding: 10px;
} */
</style>
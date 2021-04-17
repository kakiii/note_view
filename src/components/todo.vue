<!-- todolist试做,需要优化ui。checkbox问题解决，本地存储todolist-->

<template>
  <div>
    <!--测试用
    <p>Local Data = {{ st }}</p>
    <button @click="myGetFunction()">Get Local Storage Data</button><br />
-->
    <el-container>
      <el-main>
        <h2>To Do List</h2>
        <el-input
            type="text"
            v-model="inputValue"
            placeholder="Add ToDo"
            @keyup.enter="add()"
        ></el-input>

        <el-button type="send" @click="add()">add</el-button>
      </el-main>
    </el-container>

    <el-container>
      <el-col :span="12"
      >
        <div class="grid-content bg-purple">

          <h3>ToDo</h3>
          <ul v-for="(item, index) in list" :key="'info-' + index">
            <!-- 这里的info没什么意义就是防俩v-for并行报错-->

            <li v-if="item.done === false">
              <el-checkbox
                  type="checkbox"
                  @change="change(index, true)"
              ></el-checkbox>

              <span>{{ item.text }}</span>
              <el-button type="danger" icon="el-icon-delete" circle @click="remove(index)"></el-button>

            </li>
          </ul>
        </div>
      </el-col
      >

      <el-col :span="12"
      >
        <div class="grid-content bg-purple-light">
          <h3>Done</h3>
          <ul v-for="(item, index) in list" :key="index">
            <li v-if="item.done === true">
              <el-checkbox
                  type="checkbox"
                  @change="change(index, false)"
                  checked="checked"

              ></el-checkbox>

              <span>{{ item.text }}</span>

              <el-button type="danger" icon="el-icon-delete" circle @click="remove(index)"></el-button>
            </li>
          </ul>
        </div>
      </el-col
      >
    </el-container>
  </div>
</template>

<script>
import store from "../store"
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
  beforeRouteEnter(to,from,next){
    if(store.state.isLogin != true){
      next('/login')
    }else{
      next();
    }
  },
data()
{
  return {
    inputValue: "",
    list: [],
    st: "",

    //mylist: localStorage.getItem("myitem"),
  };
}
,
methods: {
  add()
  {
    if (this.inputValue == null) {
      alert("不能爲空");
    } else {
      //this.list.push({ text: this.inputValue, done: false });
      this.list.push({text: this.inputValue, done: false});

      this.inputValue = null;
    }
  }
,
  change(index, done)
  {
    if (done) {
      this.list[index].done = true;
    } else {
      this.list[index].done = false;
    }
  }
,
  remove(index)
  {
    this.list.splice(index, 1);
  }
,

  /*测试用
  myGetFunction: function () {
    this.st = myStorage.get("list");
    console.log("hello" + this.st);
  },*/
}
,

watch: {
  list: {
    deep: true,
        handler
  :

    function (newVal, oldVal) {
      if (newVal) {
        myStorage.set("list", newVal);
      } else {
        myStorage.set("list", oldVal);
      }
    }

  ,
  }
,
}
,
mounted: function () {
  this.list = myStorage.get("list") || [];
}
,
}
;
</script>

<style>
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 30px;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-row {
  margin-bottom: 20px;

&
:last-child {
  margin-bottom: 0;
}

}
.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
<!-- todolist试做,需要优化ui。checkbox问题解决，本地存储todolist-->

<template>
  <div>

    <!--测试用
    <p>Local Data = {{ st }}</p>
    <button @click="myGetFunction()">Get Local Storage Data</button><br />
-->
    <h2>To Do List</h2>
    <input
      type="text"
      v-model="inputValue"
      placeholder="Add ToDo"
      @keyup.enter="add()"
    />
    <button @click="add()">add</button>

    <!-- ToDo -->
    <h3>ToDo</h3>
    <ul v-for="(item, index) in list" :key="'info-' + index">
      <!-- 这里的info没什么意义就是防俩v-for并行报错-->
      <li v-if="item.done === false">
        <input type="checkbox" @change="change(index, true)" />
        <span>{{ item.text }}</span>
        <button @click="remove(index)">delete</button>
      </li>
    </ul>

    <!-- Done -->
    <h3>Done</h3>
    <ul v-for="(item, index) in list" :key="index">
      <li v-if="item.done === true">
        <input
          type="checkbox"
          @change="change(index, false)"
          checked="checked"
        />
        <span>{{ item.text }}</span>
        <button @click="remove(index)">delete</button>
      </li>
    </ul>


  </div>
</template>

<script>
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
        alert("不能爲空");
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
    this.list = myStorage.get("list")|| [];
  },
};
</script>
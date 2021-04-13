<!-- todolist试做,需要优化ui。clickbox做的有问题，本地存储todolist-->

<template>
  <div>
    <el-header>This is to do list. 拉清单</el-header>
    <input type="text" v-model="inputValue" @keyup.enter="add" />
    <button @click="add">add</button>
    <ul>
      <li v-for="(i, index) in list" :key="index">
        <input type="checkbox" />
        <span>{{ i.text }}</span>
        <button @click="remove(i)">delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "todo",
  data() {
    return {
      inputValue: "",
      list: [

      ],
    };
  },
  methods: {
    add() {
     
      this.list.push({ text: this.inputValue });
      this.inputValue = null;
    },
    remove(i) {
      this.list.splice(this.list.indexOf(i), 1);
    },
  },
};
</script>

<style>

.el-header {
  background-color: #ff0000;
  color: rgb(255, 255, 255);
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
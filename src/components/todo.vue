<!-- todolist试做,需要优化ui。checkbox问题解决，本地存储todolist-->

<template>
  <div>
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
    <ul v-for="(item, index) in list" :key="index">
      <li v-if="item.done == false">
        <input type="checkbox" @change="change(index, true)" />
        <span>{{ item.text }}</span>
        <button @click="remove(index)">delete</button>
      </li>
    </ul>

    <!-- Done -->
    <h3>Done</h3>
    <ul v-for="(item, index) in list" :key="index">
      <li v-if="item.done == true">
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
export default {
  name: "todo",
  data() {
    return {
      inputValue: "",
      list: [],
    };
  },
  methods: {
    add() {
      this.list.push({ text: this.inputValue, done: false });
      this.inputValue = null;
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
  },
};
</script>
<template>
  <div class="container">
    <Monaco
        :options="options"
        :value="content"
        @contentChange="contentChange"
        style="height: 400px; width: 600px;"
    ></Monaco>
  </div>
</template>

<script>
import Monaco from "@/components/Monaco";
export default {
  name: "CodeEditor",
  components: {
    Monaco,
  },
  data() {
    return {
      content: "",
      options: {
        language: "sql",
        theme: 'vs',
        readOnly: false
      }
    };
  },
  created() {
  },
  methods: {
    // 绑定编辑器value值的变化
    contentChange(val) {
      this.content = val;
    }
  }
}
</script>

<style scoped lang="scss">
  .container {
    text-align: left;
    padding: 10px;
  }
</style>
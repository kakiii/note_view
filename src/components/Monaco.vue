<template>
  <div>
    <input v-model="cc" type="text" />
    <div>
      <MonacoEditor class="editor" v-model="code" language="cpp" v-if="cc == 'cpp'" />
      <MonacoEditor class="editor" v-model="code" language="javascript" v-if="cc == 'javascript'" />
      <MonacoEditor class="editor" v-model="code" language="typescript" v-if="cc == 'typescript'" />
      <MonacoEditor class="editor" v-model="code" language="python" v-if="cc == 'python'" />
      <MonacoEditor class="editor" v-model="code" language="php" v-if="cc == 'php'" />
      <MonacoEditor class="editor" v-model="code" language="java" v-if="cc == 'java'" />
      <MonacoEditor class="editor" v-model="code" language="sql" v-if="cc == 'sql'" />
      <!-- <MonacoEditor class="editor" v-model="code" language="cpp" v-if="cc == 'cpp'"/>
  <MonacoEditor class="editor" v-model="code" language="cpp" v-if="cc == 'cpp'"/>
  <MonacoEditor class="editor" v-model="code" language="cpp" v-if="cc == 'cpp'"/>
  <MonacoEditor class="editor" v-model="code" language="cpp" v-if="cc == 'cpp'"/>
  <MonacoEditor class="editor" v-model="code" language="cpp" v-if="cc == 'cpp'"/>
  <MonacoEditor class="editor" v-model="code" language="cpp" v-if="cc == 'cpp'"/>
  <MonacoEditor class="editor" v-model="code" language="cpp" v-if="cc == 'cpp'"/>
  <MonacoEditor class="editor" v-model="code" language="cpp" v-if="cc == 'cpp'"/> -->
    </div>
  </div>
</template>

<script>
import MonacoEditor from 'vue-monaco';

export default {
  components: {
    MonacoEditor,
  },
  methods: {
    change_to_cpp() {
      this.cc = 'cpp';
    },
    change_to_py() {
      this.cc = 'python';
    },
    change_to_ts() {
      this.cc = 'typescript';
    },
    change_to_php() {
      this.cc = 'php';
    },
  },

  data() {
    return {
      code: 'abc',
      cc: 'cpp',
    };
  },
};
</script>

<style scoped>
.editor {
  width: 600px;
  height: 800px;
}
</style>

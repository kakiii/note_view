<template>
  <div>
    <el-container>
      <el-tiptap

          :extensions="extensions"
          output="json"
          :content="content"
          @onUpdate="onUpdate"
      />
    </el-container>

    <el-container>
      <el-container>
        <div v-html="output.html"></div>
      </el-container>
      <el-container>
        <pre><code>{{ output.html }}</code></pre>
      </el-container>

      <el-container>
        <pre><code>{{ output.json }}</code></pre>
      </el-container>

    </el-container>
  </div>

</template>

<script>
import {
  Bold,
  BulletList,
  Doc,
  Fullscreen,
  HardBreak,
  Heading,
  History,
  HorizontalRule,
  Indent,
  Italic,
  ListItem,
  OrderedList,
  Paragraph,
  Strike,
  Text,
  TextAlign,
  TodoItem,
  TodoList,
  Underline,
} from 'element-tiptap';

export default {

  name: "Editor",
  methods: {
    onUpdate(output, options) {
      const {getJSON, getHTML} = options;
      this.output.json = getJSON();
      this.output.html = getHTML();
    },
  },
  data() {
    return {
      output: {
        json: `json content`,
        html: `html content`
      },
      extensions: [
        new Doc(),
        new Text(),
        new Paragraph(),
        new Heading({level: 5}),
        new Bold({bubble: true}), // render command-button in bubble menu.
        new Underline({bubble: true, menubar: false}), // render command-button in bubble menu but not in menubar.
        new Italic(),
        new Strike(),
        new TextAlign(),
        new ListItem(),
        new BulletList(),
        new OrderedList(),
        new TodoItem(),
        new TodoList(),
        new Indent(),
        new HardBreak(),
        new HorizontalRule({bubble: true}),
        new Fullscreen(),
        new History(),
      ],
      // editor's content
      content: `Enter your notes here.`,
    };
  }
};
</script>

<style scoped></style>

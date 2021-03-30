<template>
  <div>
    <div>
      <textarea v-model="content"/>
    </div>
    <div>
      <MarkdownItVue :content="content" :options="options" class="md-body" />
    </div>
  </div>
</template>

<script>
import MarkdownItVue from "markdown-it-vue";
import 'markdown-it-vue/dist/markdown-it-vue.css'
export default {
  components: { MarkdownItVue },
  name: "Editor",
  methods: {
    onUpdate(output, options) {
      const { getJSON, getHTML } = options;
      this.output.json = getJSON();
      this.output.html = getHTML();
    }
  },
  data() {
    return {
      output: {
        json: `json content`,
        html: `html content`
      },
      content: "CONTENT",
      options: {
        linkAttributes: {
          attrs: {
            target: "_blank",
            rel: "noopener"
          }
        },
        katex: {
          throwOnError: false,
          errorColor: "#cc0000"
        },
        icons: "font-awesome",
        githubToc: {
          tocFirstLevel: 2,
          tocLastLevel: 3,
          tocClassName: "toc",
          anchorLinkSymbol: "",
          anchorLinkSpace: false,
          anchorClassName: "anchor",
          anchorLinkSymbolClassName: "octicon octicon-link"
        },
        mermaid: {
          theme: "default"
        },
        image: {
          hAlign: "left",
          viewer: true
        }
      }

    };
  }
};
</script>

<style scoped></style>

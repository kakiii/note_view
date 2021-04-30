<template>
  <div>

    <br /><br />
    <el-container>
      <el-radio-group
        v-model="isCollapse"
        style="margin-bottom: 20px; alignment: left"
      >
        <el-radio-button :label="true">-</el-radio-button>
        <el-radio-button :label="false">+</el-radio-button>

      </el-radio-group>
      <el-select
        v-model="headerValue"
        placeholder="Select header"
        @change="insertHeader(headerValue)"
      >
        <el-option
          v-for="header in headers"
          :key="header.value"
          :label="header.label"
          :value="header.value"
        >
        </el-option>
      </el-select>
      <el-button v-on:click="markup('italic')"><i>Italic</i></el-button>
      <el-button v-on:click="markup('bold')"><b>Bold</b></el-button>
      <el-button v-on:click="markup('code')">Code Block</el-button>
      <el-button v-on:click="markup('blockquotes')">Block Quotes</el-button>
      <el-button v-on:click="markup('image')">Image</el-button>
      <el-button v-on:click="markup('link')">Link</el-button>
      <el-button v-on:click="markup('indent')">Tab</el-button>
      <el-button v-on:click="clear">Clear</el-button>
      <el-button>Save</el-button>
      <el-button v-on:click="upload">Upload</el-button>
      <!--      <el-button v-on:click="refresh">Refresh</el-button>-->
      <el-input
        v-model="article_id"
        placeholder="choose a id"
        type="text"
        style="width: 200px"
        clearable
      />
    </el-container>
    <el-container> </el-container>

    <el-container>
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        :collapse="isCollapse"
      >
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-document"></i>
            <span slot="title">My Articles</span>
          </template>
          <el-menu-item-group title="Folder 1">
            <el-menu-item
              v-for="id in article_list"
              :key="id"
              v-on:click="load(id)"
              >Article {{ id }}</el-menu-item
            >
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
      <textarea
        ref="textarea"
        v-model="content"
        :rows="100"
        type="textarea"
      ></textarea>

      <MarkdownItVue
        :content="content"
        :options="options"
        class="md-body"
      />
    </el-container>
  </div>
</template>

<script>
import MarkdownItVue from "markdown-it-vue";
import "markdown-it-vue/dist/markdown-it-vue.css";
import axios from "axios";

export default {
  components: { MarkdownItVue },
  name: "Editor",
  mounted() {
    if (this.$store.state.isLogin) {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://localhost:5000/article/user/";
      } else {
        url = "article/user/";
      }
      axios
        .get(url + this.$store.state.username)
        .then((res) => {
          this.article_list = res.data["article_collection"];
          console.log(this.article_list);
        })
        .catch((err) => console.log(err));
      /* if (this.article_list.length>0) {
        
      } */
    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    load(id) {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://localhost:5000/article/";
      } else {
        url = "/article/";
      }
      if (id !== undefined) {
        axios
          .get(url + id)
          .then((res) => {
            this.content = res.data["Content"];
          })
          .catch((err) => console.log(err));
      }
    },
    upload() {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://localhost:5000/article";
      } else {
        url = "/article";
      }
      axios
        .post(url, {
          id: this.article_id,
          content: this.content,
        })
        .catch((err) => {
          console.log(err);
        });
    },
    markup(val) {
      let textArea = this.$refs.textarea;
      let startPos = textArea.selectionStart;
      let endPos = textArea.selectionEnd;
      let tmpStr = textArea.value;
      //this.$alert(tmpStr);
      switch (val) {
        case "h1":
          this.content =
            tmpStr.substring(0, startPos) + "# \n" + tmpStr.substring(startPos);
          break;
        case "h2":
          this.content =
            tmpStr.substring(0, startPos) +
            "## \n" +
            tmpStr.substring(startPos);
          break;
        case "h3":
          this.content =
            tmpStr.substring(0, startPos) +
            "### \n" +
            tmpStr.substring(startPos);
          break;
        case "h4":
          this.content =
            tmpStr.substring(0, startPos) +
            "#### " +
            tmpStr.substring(startPos);
          break;
        case "h5":
          this.content =
            tmpStr.substring(0, startPos) +
            "##### \n" +
            tmpStr.substring(startPos);
          break;
        case "h6":
          this.content =
            tmpStr.substring(0, startPos) +
            "###### \n" +
            tmpStr.substring(startPos);
          break;
        case "bold":
          this.content =
            tmpStr.substring(0, startPos) +
            "**" +
            tmpStr.substring(startPos, endPos) +
            "**" +
            tmpStr.substring(endPos);
          break;
        case "italic":
          this.content =
            tmpStr.substring(0, startPos) +
            "*" +
            tmpStr.substring(startPos, endPos) +
            "*" +
            tmpStr.substring(endPos);
          break;
        case "blockquotes": {
          let temp = tmpStr.substring(startPos, endPos).split("\n");
          let res = "";
          for (let i = 0; i < temp.length; ++i) {
            res += "> " + temp[i] + "\n";
          }
          this.content =
            tmpStr.substring(0, startPos) + res + tmpStr.substring(endPos);
          break;
        }
        case "code":
          this.content =
            tmpStr.substring(0, startPos) +
            "```\n" +
            tmpStr.substring(startPos, endPos) +
            "\n```\n" +
            tmpStr.substring(endPos);
          break;
        case "image":
          this.content =
            tmpStr.substring(0, startPos) +
            "![]()\n" +
            tmpStr.substring(startPos);
          break;
        case "link":
          this.content =
            tmpStr.substring(0, startPos) +
            "[]()\n" +
            tmpStr.substring(startPos);
          break;
        case "indent":
          this.content =
            tmpStr.substring(0, startPos) + "   " + tmpStr.substring(startPos);
          break;
      }
    },
    clear() {
      this.content = "";
      this.$alert("You have reset the content!");
    },
    insertHeader(headerValue) {
      this.markup(headerValue);
      this.headerValue = "";
    },
  },
  data() {
    return {
      article_list: [],
      article_id: null,
      headerValue: "",
      isCollapse: true,
      headers: [
        {
          value: "h1",
          label: "Header 1",
        },
        {
          value: "h2",
          label: "Header 2",
        },
        {
          value: "h3",
          label: "Header 3",
        },
        {
          value: "h4",
          label: "Header 4",
        },
        {
          value: "h5",
          label: "Header 5",
        },
        {
          value: "h6",
          label: "Header 6",
        },
      ],
      output: {
        json: `json content`,
        html: `html content`,
      },
      options: {
        linkAttributes: {
          attrs: {
            target: "_blank",
            rel: "noopener",
          },
        },
        katex: {
          throwOnError: false,
          errorColor: "#cc0000",
        },
        icons: "font-awesome",
        githubToc: {
          tocFirstLevel: 2,
          tocLastLevel: 3,
          tocClassName: "toc",
          anchorLinkSymbol: "",
          anchorLinkSpace: false,
          anchorClassName: "anchor",
          anchorLinkSymbolClassName: "octicon octicon-link",
        },
        mermaid: {
          theme: "default",
        },
        image: {
          hAlign: "left",
          viewer: true,
        },
      },
      content: `# Manual for markdown editor

# This is H1
## This is H2
....
###### This is h6

## Table of content

[toc]

Note: Only \`h2\` and \`h3\` are shown in toc.

## Mermaid

You can bold **text** and use *italic style* or ***combine them***.

We also support mermaid diagrams, like this:

\`\`\`mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
\`\`\`

For more information, click here: [Flowchart Syntax](http://knsv.github.io/mermaid/#flowcharts-basic-syntax)

## Image

You are free to use regular grammar, but you can stretch them now.

 ![UK](https://wonderfulengineering.com/wp-content/uploads/2015/05/England-wallpaper-28.jpg =720x)

## Math Syntax

Inline: \`@(1/2[1-(1/2)^n])/(1-(1/2))=s_n@\`

Discrete: 

\`\`\`AsciiMath
oint_Cx^3 dx+4y^2 dy

2=(((3-x)xx2)/(3-x))

sum_(m=1)^oosum_(n=1)^oo(m^2 n)/(3^m(m3^n+n3^m)
\`\`\`

For more syntax, click here [AsciiMath Documentation](http://asciimath.org/)

## Emoji

:tiger: :panda_face: 

[Emoji Cheat Sheet](http://www.emoji-cheat-sheet.com/)

## Alert

::: success
This is success
:::

::: info
This is info
:::

::: warning
This is warning
:::

::: error
This is error
:::
`,
    };
  },
};
</script>

<style scoped>
.el-container {
  height: 100%;
  width: 100%;
}

.el-button{
  width: auto;
  height: 40px;
  margin: 5px;
  text-align: center;
  background: #020080;
  color: white;
}

.el-input,
.el-select,
.el-radio-button{
  width: auto;
  height: 40px;
  margin: 5px;
  text-align: center;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

textarea {
  width: 100%;
  height: auto;
  padding: 12px 20px;
  box-sizing: border-box;
  border: 2px solid #ccc;
  border-radius: 4px;
  background-color: #f8f8f8;
  resize: none;
  font-family: "system-ui";
}

textarea {
  width: 47%;
  border: 1px solid #ccc;
  border-radius: 15px;
  margin: 3px;
}

.md-body {
  width: 50%;
  margin: 3px;
}
</style>

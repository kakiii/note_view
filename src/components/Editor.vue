<template>
  <div>
    <h1>EDITOR</h1>
    <el-container>
      <el-radio-group
        v-model="isCollapse"
        style="margin-bottom: 20px; alignment: left"
        fill="#93E0FF"
        text-color="#253B6E"
      >
        <el-radio-button :label="true"> &lt; </el-radio-button>
        <el-radio-button :label="false"> &gt; </el-radio-button>
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
      <el-button v-on:click="getURL()">share article</el-button>
      <!-- <el-button v-on:click="getTitle">getTitle</el-button> -->
      <el-button
        v-on:click="upload"
        :disabled="content.length <= 5 || !this.$store.state.isLogin"
        >Upload
      </el-button>

      <!-- <el-button v-on:click="getTitle">Get Title</el-button> -->
      <!--      <el-button v-on:click="refresh">Refresh</el-button>-->
    </el-container>
    <el-input
      clearable
      size="large"
      class="titleInput"
      v-model="currentTitle"
      placeholder="Please enter your title"
      style="width: 46%; float: left"
    ></el-input>

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
              v-for="title_obj in title_id"
              :key="title_obj.id"
              v-on:click="load(title_obj.id)"
            >
              {{ title_obj.title }}
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>

      <textarea
        ref="textarea"
        v-model="content"
        :rows="100"
        type="textarea"
      ></textarea>

      <MarkdownItVue :content="content" :options="options" class="md-body" />
    </el-container>
  </div>
</template>

<script>
import MarkdownItVue from "markdown-it-vue";
import "markdown-it-vue/dist/markdown-it-vue.css";
import axios from "axios";
import CryptoJS from "crypto-js";
export default {
  components: { MarkdownItVue },
  name: "Editor",
  beforeMount() {
    if (this.$store.state.isLogin) {
      let url = "";
      if (process.env.NODE_ENV === "development") {
        url = "http://localhost:5000/article/user/";
      } else {
        url = "/article/user/";
      }
      axios
        .get(url + this.$store.state.username)
        .then((res) => {
          let article_list = res.data["article_collection"];
          let article_titles_list = res.data["article_titles_collection"];

          for (let i = 0; i < article_list.length; i++) {
            let article = {
              id: article_list[i],
              title: article_titles_list[i],
            };
            this.title_id[i] = article;
          }
          console.log(this.title_id);
        })
        .catch((err) => console.log(err));
      /* if (this.article_list.length>0) {
        
      } */
    }
  },
  methods: {
    getURL() {
      this.getTitle();
      let url = "https://note-view.herokuapp.com/#/article/";
      let link =
        url +
        CryptoJS.MD5(
          this.$store.state.username + " " + this.currentTitle
        ).toString();
        //console.log(link);
      this.$alert(link, "You can share this article with this link: \n");
    },
    getTitle() {
      if (this.currentTitle === "") {
        this.$alert("Please enter a title");
        return false;
      } else if (this.currentTitle.length < 3) {
        this.$alert("Length of title is less than 3!");
        return false;
      } else {
        console.log(this.$store.state.username + " " + this.currentTitle);
        console.log(
          CryptoJS.MD5(
            this.$store.state.username + " " + this.currentTitle
          ).toString()
        );
        return true;
      }
    },
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
            this.currentTitle = res.data["Title"];
          })
          .catch((err) => console.log(err));
      }
    },
    upload() {
      if (this.getTitle()) {
        let url = "";
        if (process.env.NODE_ENV === "development") {
          url = "http://localhost:5000/article";
        } else {
          url = "/article";
        }
        axios
          .post(url, {
            id: CryptoJS.MD5(
              this.$store.state.username + " " + this.currentTitle
            ).toString(),
            author: this.$store.state.username,
            content: this.content,
            title: this.currentTitle,
          })
          .catch((err) => {
            console.log(err);
          });
        this.$alert("You have successfully uploaded this article!");
      }
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
      test: {
        id1: "title1",
        id2: "title2",
        id3: "title3",
      },
      currentTitle: "",
      title_id: [],
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

For more information, click here: [Flowchart Syntax](https://mermaid-js.github.io/mermaid/#/flowchart)

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

.titleInput {
  width: auto;
  margin: auto;
  text-align: left;
}

.el-button,
.el-input,
.el-select,
.el-radio-button {
  width: auto;
  height: 40px;
  text-align: center;
  border-color: white;
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

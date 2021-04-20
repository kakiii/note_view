<template>
  <div>
    <el-container>
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
      <el-button v-on:click="clear">Clear</el-button>
      <el-button>Save</el-button>

      <el-button v-on:click="upload">Upload</el-button>
      <el-input v-model="article_id" placeholder="choose a id" type="text" style="width:200px" clearable/>
    </el-container>
    <el-container>
      <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;alignment: left">
        <el-radio-button :label="false">展开</el-radio-button>
        <el-radio-button :label="true">收起</el-radio-button>
      </el-radio-group>
    </el-container>

    <el-container>
      <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
               :collapse="isCollapse">
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-document"></i>
            <span slot="title">My Articles</span>
          </template>
          <el-menu-item-group>
            <span slot="title">Folder 1</span>
            <el-menu-item index="1-1" v-on:click="load('1')">Article 1</el-menu-item>
            <el-menu-item index="1-2" v-on:click="load('2')">Article 2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="Folder 2">
            <el-menu-item index="1-3" v-on:click="load('3')">Article 3</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
      <textarea
          ref="textarea"
          v-model="content"
          :rows="100"
          style="width: 47% ; border: 1px solid #ccc; border-radius:15px; margin:3px;"
          type="textarea"
      ></textarea>

      <MarkdownItVue
          v-model="htmloutput"
          :content="content"
          :options="options"
          class="md-body"
          style="width: 50% ; margin:3px;"
      />
    </el-container>
  </div>
</template>

<script>
import MarkdownItVue from "markdown-it-vue";
import "markdown-it-vue/dist/markdown-it-vue.css";
import axios from "axios";

export default {
  components: {MarkdownItVue},
  name: "Editor",
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
        url = "article/";
      }
      axios.get(url +id).then((res) => {
        this.content = res.data["Content"];
      }).catch((err) => console.log(err));

    },
    upload() {
      if (process.env.NODE_ENV === "development") {
        console.log("DEVELOPMENT")
        axios
            .post("http://localhost:5000/article", {
              id: this.article_id,
              content: this.content,
            })
            .catch((err) => {
              console.log(err);
            });
      } else {
        console.log(process.env)
        axios
            .post("/article", {
              id: this.article_id,
              content: this.content,
            })
            .catch((err) => {
              console.log(err);
            });
      }
    },
    /* onUpdate(output, options) {
      const { getJSON, getHTML } = options;
      this.output.json = getJSON();
      this.output.html = getHTML();
    }, */
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
              "![]()\n"+
              tmpStr.substring(startPos);
          break;
        case "link":
          this.content =
              tmpStr.substring(0, startPos) +
              "[]()\n"+
              tmpStr.substring(startPos);
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
      htmloutput: "",
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
      content: `

# markdown-it-vue

## Image size and Viewer

![GitHub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png =50x)


## GitHub Table of Contents

[toc]

Note: Only \`h2\` and \`h3\` are shown in toc.

## alter

Markup is similar to fenced code blocks. Valid container types are \`success\`, \`info\`, \`warning\` and \`error\`.

::: success
You have got it.
:::

::: info
You have new mail.
:::

::: warning
You have new mail.
:::

::: error
Staying up all night is bad for health.
:::

## mermaid charts

### mermaid Flowchart

[Flowchart Syntax](http://knsv.github.io/mermaid/#flowcharts-basic-syntax)

\`\`\`mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
\`\`\`

\`\`\`
sequenceDiagram
    participant Alice
    participant Bob
    Alice->John: Hello John, how are you?
    loop Healthcheck
        John->John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail...
    John-->Alice: Great!
    John->Bob: How about you?
    Bob-->John: Jolly good!
\`\`\`

## Definition list

Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b

[Definition List Syntax](http://pandoc.org/README.html#definition-lists)


## AsciiMath

Inline AsciiMath: \`@(1/2[1-(1/2)^n])/(1-(1/2))=s_n@\`

\`\`\`AsciiMath
oint_Cx^3 dx+4y^2 dy

2=(((3-x)xx2)/(3-x))

sum_(m=1)^oosum_(n=1)^oo(m^2 n)/(3^m(m3^n+n3^m)
\`\`\`

\`\`\`ASCIIMath
phi_n(kappa) = 1/(4pi^2 kappa^2)
 int_0^oo (sin(kappa R))/(kappa R)
 del/(del R)
[R^2 (del D_n (R))/(del R)] del R
\`\`\`

[AsciiMath Documentation](http://asciimath.org/)

## Subscript: H~2~O

You can also use inline math: \`$H_2O$\`


## Superscript: 29^th^

You can also use inline math: \`$29^{th}$\`


## Emoji: :panda_face: :sparkles: :camel: :boom: :pig:

[Emoji Cheat Sheet](http://www.emoji-cheat-sheet.com/)

## Fontawesome: :fa-car: :fa-flag: :fa-bicycle: :fa-leaf: :fa-heart:

[All the Font Awesome icons](http://fontawesome.io/icons/)

## Echarts

[Documentation for Echarts](http://echarts.baidu.com)

The width and height is the size for chart container.

\`\`\`echarts
{
  "width": 500,
  "height": 400,
  "series": [
    {
      "name": "访问来源",
      "type": "pie",
      "radius": "55%",
      "data": [
        {
          "value": 235,
          "name": "视频广告"
        },
        {
          "value": 274,
          "name": "联盟广告"
        },
        {
          "value": 310,
          "name": "邮件营销"
        },
        {
          "value": 335,
          "name": "直接访问"
        },
        {
          "value": 400,
          "name": "搜索引擎"
        }
      ]
    }
  ]
}
\`\`\`

## code

### c
\`\`\`c
#include <stdio.h>
int main(int argc char* argv[]) {
  printf("Hello, World!");
  return 0;
}
\`\`\`

### json

\`\`\`json
{
  "name": "markdown-it-vue"
}
\`\`\`

### javascript
\`\`\`json
import MarkdownItVue from 'markdown-it-vue'
export default {
  components: {
    MarkdownItVue
  }
}
\`\`\`

### bash
\`\`\`bash
npm install markdown-it-vue
\`\`\`

## table

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

## flowchart.js

\`\`\`flowchart.js
st=>start: Start|past:>http://www.google.com[blank]
e=>end: End:>http://www.google.com
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Yes
or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|request
para=>parallel: parallel tasks

st->op1(right)->cond
cond(yes, right)->c2
cond(no)->para
c2(true)->io->e
c2(false)->e

para(path1, bottom)->sub1(left)->op1
para(path2, right)->op2->e

st@>op1({"stroke":"Red"})@>cond({"stroke":"Red","stroke-width":6,"arrow-end":"classic-wide-long"})@>c2({"stroke":"Red"})@>op2({"stroke":"Red"})@>e({"stroke":"Red"})
\`\`\`


      `,
    };
  },
};
</script>

<style scoped>
.el-container {
  height: 100%;
  padding: 0;
  margin: 0;
  width: 100%;
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
</style>

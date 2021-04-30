<template>
  <MarkdownItVue :content="content" :options="options" class="md-body" />
</template>

<script>
import MarkdownItVue from "markdown-it-vue";
export default {
  components: { MarkdownItVue },
  name: "Preview",
  data() {
    return {
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

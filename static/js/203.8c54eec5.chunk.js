(this["webpackJsonpmy-app"]=this["webpackJsonpmy-app"]||[]).push([[203],{257:function(e,n){!function(e){var n="\\\\\\((?:[^()]|\\([^()]*\\))*\\)",t=RegExp('"(?:[^"\r\n\\\\]|\\\\[^\r\n(]|__)*"'.replace(/__/g,(function(){return n}))),i={interpolation:{pattern:RegExp("((?:^|[^\\\\])(?:\\\\{2})*)"+n),lookbehind:!0,inside:{content:{pattern:/^(\\\()[\s\S]+(?=\)$)/,lookbehind:!0,inside:null},punctuation:/^\\\(|\)$/}}},a=e.languages.jq={comment:/#.*/,property:{pattern:RegExp(t.source+"(?=\\s*:(?!:))"),greedy:!0,inside:i},string:{pattern:t,greedy:!0,inside:i},function:{pattern:/(\bdef\s+)[a-z_]\w+/i,lookbehind:!0},variable:/\B\$\w+/,"property-literal":{pattern:/\b[a-z_]\w*(?=\s*:(?!:))/i,alias:"property"},keyword:/\b(?:as|break|catch|def|elif|else|end|foreach|if|import|include|label|module|modulemeta|null|reduce|then|try|while)\b/,boolean:/\b(?:true|false)\b/,number:/(?:\b\d+\.|\B\.)?\b\d+(?:[eE][+-]?\d+)?\b/,operator:[{pattern:/\|=?/,alias:"pipe"},/\.\.|[!=<>]?=|\?\/\/|\/\/=?|[-+*/%]=?|[<>?]|\b(?:and|or|not)\b/],"c-style-function":{pattern:/\b[a-z_]\w*(?=\s*\()/i,alias:"function"},punctuation:/::|[()\[\]{},:;]|\.(?=\s*[\[\w$])/,dot:{pattern:/\./,alias:"important"}};i.interpolation.inside.content.inside=a}(Prism)}}]);
//# sourceMappingURL=203.8c54eec5.chunk.js.map
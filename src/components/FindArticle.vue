<template>
  <div>
    <input v-model="id" />
    <button v-on:click="get_article()">HIT TO GET VALUE</button>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Content</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ this.id }}</td>
          <td>{{ content }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FindArticle",
  data() {
    return {
      id: "",
      content: "",
    };
  },
  methods: {
    get_article() {
      axios
        .get("http://127.0.0.1:5000/articles/" + this.id)
        .then((res) => {
          console.log(res.data["Content"]);
          this.content = res.data["Content"];
        })
        .catch(() => (this.content = "NO CONTENT"));
    },
  },
};
</script>

<style scoped></style>

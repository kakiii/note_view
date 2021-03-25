<template>
  <form :action="url" method="GET">
    <h2>FIND</h2>
    <div class="form-group">
      <label>ID</label>
      <input
        type="text"
        id="username"
        name="username"
        v-model="id"
        v-on:change="change_url"
        required
      />
    </div>
    <div class="form-footer">
      <button type="submit" name="submit" class="btn">Submit</button>
      <router-link to="/" class="btn">Return Home</router-link>
    </div>
  </form>
</template>

<script>
// import api from "@/api"

export default {
  name: "FindArticle",
  data() {
    return {
      id: "",
      content: "",
      url: "/articles/",
    };
  },
  methods: {
    change_url() {
      this.url = "/articles/" + this.id;
    },
  },
};
</script>

<style scoped></style>

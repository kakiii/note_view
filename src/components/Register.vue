<template>
  <div>
    <form action="/auth/register" method="post" @submit="checkForm">
      <h2>Register</h2>
      <div class="form-group">
        <label for="username">Username</label>
        <input id="username" v-model="username" name="username" required type="text">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input id="password" v-model="password" name="password" required type="password">
      </div>
      <div class="form-footer">
        <button class="btn" name="submit" type="submit">Submit</button>
        <router-link class="btn" to="/">Return Home</router-link>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      username: "",
      password: "",
      remember: false
    }
  },
  methods: {},
}
</script>

<style scoped>

</style>
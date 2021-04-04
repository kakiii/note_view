<template>
  <div class="login">
    <form action="http://localhost:5000/auth/login" method="post" @submit="checkForm">
      <h2>Login</h2>
      <div class="form-group">
        <label for="username">Username</label>
        <input
          id="username"
          v-model="username"
          name="username"
          required
          type="text"
        />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
          id="password"
          v-model="password"
          name="password"
          required
          type="password"
        />
      </div>
      <div class="form-group">
        <label for="remember">
          <input
            id="remember"
            v-model="remember"
            name="remember"
            type="checkbox"
          />
          Remember Me
        </label>
      </div>
      <div class="form-footer">
        <button class="btn" name="submit" type="submit">Submit</button>
        <router-link class="btn" to="/">Return Home</router-link>
      </div>
    </form>
    <h3>Successful Login will take you back to HOME PAGE</h3>
  </div>
</template>

<script>
// import api from '../api'
export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      remember: false,
    };
  },
  methods: {},
};
</script>

<template>
  <div>
    <h1>LOGIN PAGE</h1>
    <el-form
      ref="loginForm"
      label-width="80px"
      class="login-box"
    >
      <h3 class="login-title">Welcome!</h3>
      <el-form-item label="Username" prop="username">
        <el-input
          type="text"
          placeholder="Please enter your username"
          v-model="username"
          value="username"
        /><br />
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input
          type="password"
          placeholder="Please enter your password"
          v-model="password"
          value="password"
        /><br />
      </el-form-item>
      <el-form-item>
        <el-button
          class="onSubmit"
          type="primary"
          v-on:click="exec_login"
          >Login</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";
import store from "../store";
export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      remember: false,
    };
  },
  methods: {
    exec_login() {
      /*
       * If the user exists & password confirmed, the console should output 200.
       * If the user exists but password wrong, the console should output 201.
       * If the user doesn't exist, the console should output 202.
       */
      axios
        .post("http://localhost:5000/auth/login", {
          username: this.username,
          password: this.password,
        })
        .then((res) => {
          console.log(res.data.status);
          store.isLogin = true;
          this.$router.push("/about");
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style lang="scss" scoped>
.login-box {
  border: 1px solid #020080;
  width: 350px;
  margin: 180px auto;
  padding: 35px 35px 15px 35px;
  border-radius: 5px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  box-shadow: 0 0 25px #909399;
}

.login-title {
  text-align: center;
  margin: 0 auto 40px auto;
  color: #020080;
}

.onSubmit {
  width: 80px;
  height: 36px;
  float: right;
  margin-top: 15px;
  margin-left: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #020080;
}
</style>

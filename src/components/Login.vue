<template>
  <div>
    <h1>LOGIN PAGE</h1>
    <el-form ref="loginForm" class="login-box" label-width="80px">
      <h3 class="login-title">Welcome!</h3>
      <el-form-item label="Username" prop="username">
        <el-input
            v-model="username"
            placeholder="Please enter your username"
            type="text"
            value="username"
        />
        <br/>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input
            v-model="password"
            placeholder="Please enter your password"
            type="password"
            value="password"
        />
        <br/>
      </el-form-item>
      <el-form-item>
        <el-button class="onSubmit" type="primary" v-on:click="exec_login">
          Login
        </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";
import validateUsername from "../utils/auth";

export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    exec_login() {
      if (validateUsername(this.username)) {
        /*
         * If the user exists & password confirmed, the console should output 200.
         * If the user exists but password wrong, the console should output 201.
         * If the user doesn't exist, the console should output 202.
         */
        let url;
        if (process.env.NODE_ENV === "development") {
          url = "http://localhost:5000/auth/login";
        } else {
          url = "auth/login";
        }
        axios
            .post(url, {
              username: this.username,
              password: this.password,
            })
            .then((res) => {
              if (res.data.status === 200) {
                console.log(res.data.status);
                this.$store.state.isLogin = true;
                this.$store.state.username = this.username;
                this.$router.push("/about");
              } else if (res.data.status === 201) {
                this.$alert("WRONG PASSWORD");
              } else {
                this.$alert("NO USER");
              }
            })
            .catch((err) => console.log(err));
      } else {
        this.$alert("Username not appropriate.");
      }
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

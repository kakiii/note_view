<template>
  <div>
    <h1>REGISTER</h1>
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
      <el-form-item label="Ensure" prop="password">
        <el-input
            v-model="password_again"
            placeholder="Please Enter password again"
            type="password"
            value="password_again"
        />
        <br/>
      </el-form-item>
      <el-form-item>
        <el-button class="onSubmit" type="primary" v-on:click="exec_register"
        >Login
        </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Register",
  data() {
    return {
      username: "",
      password: "",
      password_again: "",
    };
  },
  methods: {
    exec_register() {
      let path = "";
      if (process.env.NODE_ENV === "development") {
        path = "http://localhost:5000/auth/register";
      } else {
        path = "/auth/register";
      }
      if (this.password !== this.password_again) {
        this.$alert("Password not match, please try again.")
      } else {
        axios
            .post(path, {
              username: this.username,
              password: this.password,
            })
            .then((res) => {
              if (res.data.status === 200) {
                console.log(res.data.status);
                this.$alert("Registration Success, please login now.");
                this.$router.push("/login");
              } else {
                this.$alert("Registration Failed, Please try again.");
              }
            })
            .catch((err) => console.log(err));
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

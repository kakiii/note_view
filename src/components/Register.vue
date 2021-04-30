<template>
  <div class="login">
    <el-card>
      <h2>REGISTER</h2>
      <el-form
          class="login-box"
          ref="loginForm"
          @keyup.enter.native="exec_register"
      >
        <el-form-item>
          <el-input v-model="username"
                    placeholder="Username"
                    prefix-icon="el-icon-user-solid"
          ></el-input>
        </el-form-item>

        <el-form-item>
          <el-input
              v-model="password"
              placeholder="Password"
              type="password"
              prefix-icon="el-icon-lock"
          ></el-input>
        </el-form-item>

        <el-form-item>
          <el-input
              v-model="password_again"
              placeholder="Confirm"
              type="password"
              prefix-icon="el-icon-check"
          ></el-input>
        </el-form-item>

        <el-form-item>
          <el-button
              class="login-button"
              type="primary"
              @click="exec_register"
              block
          >Register</el-button>
        </el-form-item>

        <a class="home" href="">Home</a>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import axios from "axios";
import validateUsername from "../utils/auth";
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
      if(validateUsername(this.username)){


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
      }else{
        this.$alert("Your username is not appropriate, please try a longer username.")
      }
    },

  },
};
</script>

<style scoped>
.login {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-button {
  width: 100%;
  margin-top: 40px;
  background: #020080;
}
.login-box {
  width: 290px;
}
.home {
  margin-top: 10px;
}
</style>
<style lang="scss">
$teal: rgb(2, 0, 128);
.el-button--primary {
  background: $teal;
  border-color: $teal;

  &:hover,
  &.active,
  &:focus {
    background: lighten($teal, 7);
    border-color: lighten($teal, 7);
  }
}
.login .el-input__inner:hover {
  border-color: $teal;
}
.login .el-input__prefix {
  background: rgb(238, 237, 234);
  left: 0;
  height: calc(100% - 2px);
  left: 1px;
  top: 1px;
  border-radius: 3px;
  .el-input__icon {
    width: 30px;
  }
}
.login .el-input input {
  padding-left: 35px;
}
.login .el-card {
  margin-top: 100px ;
  padding-top: 10px;
  padding-bottom: 30px;
}
h2 {
  font-family: "Open Sans";
  letter-spacing: 1px;
  font-family: Roboto, sans-serif;
  padding-bottom: 20px;
}
a {
  color: $teal;
  text-decoration: none;
  &:hover,
  &:active,
  &:focus {
    color: lighten($teal, 7);
  }
}
.login .el-card {
  width: 340px;
  display: flex;
  justify-content: center;
}
</style>
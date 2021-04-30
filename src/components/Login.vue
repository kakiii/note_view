<template>
  <div class="login">
    <el-card>
      <h2>LOGIN</h2>
      <el-form
          class="login-box"
          ref="loginForm"
          @keyup.enter.native="exec_login"
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
          <el-button
              class="login-button"
              type="primary"
              @click="exec_login"
              block
          >Login</el-button>
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

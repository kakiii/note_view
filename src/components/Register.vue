<template>
  <div>
    <h1>REGISTER</h1>
    <input v-model="username" value="username"/><br/>
    <input v-model="password" value="password"/><br/>
    <input type="submit" @click="exec_register"/>
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
    };
  },
  methods: {
    exec_register() {
      if (process.env.NODE_ENV === "development") {
        axios
            .post("http://localhost:5000/auth/register", {
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
      } else{
        axios
            .post("/auth/register", {
              username: this.username,
              password: this.password,
            })
            .then((res) => {
              if (res.data.status === 200) {
                console.log(res.data.status);
                this.$alert("Registration Success, please login now.");
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

<style scoped></style>

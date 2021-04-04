<template>
  <div>
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
      password: ""
    };
  },
  methods: {
    exec_register() {
      axios.post("http://localhost:5000/auth/register", {
        username: this.username,
        password: this.password
      }).then(res => {
        if (res.data.status === 200) {
          console.log(res.data.status)
        } else {
          this.$alert("Registration Failed, Please try again.");
        }

      }).catch(err => console.log(err));
    }
  }
};
</script>

<style scoped></style>

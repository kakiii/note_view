<template>
  <div>
    <input v-model="username" value="username"/><br/>
    <input v-model="password" value="password"/><br/>
    <input type="submit" @click="exec_login"/>
  </div>
</template>

<script>
import axios from "axios";
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
    exec_login(){
      /*
      * If the user exists & password confirmed, the console should output 200.
      * If the user exists but password wrong, the console should output 201.
      * If the user doesn't exist, the console should output 202.
      */
      axios.post("http://localhost:5000/auth/login",{username:this.username,password:this.password}).then(res => console.log(res.data.status)).catch(err => console.log(err));
    }
  },
};
</script>

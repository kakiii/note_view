<template>
  <div>
    <h1>MANAGEMENT</h1>
    <p>Users: {{ total_users }} &nbsp; Articles: {{ total_artilces }} &nbsp; Discussions: {{ total_discussions }} </p>
    <el-button icon="el-icon-s-unfold" class="get-button" type="button" @click="getAllUser" value="GET All USERS" block
      >Get All Users</el-button
    >

    <!--<p>If you want to ban a user, just enter the user's name then hit <strong>BAN</strong> button</p>
    <input type="text" v-model="ban_user_name" />
    <input type="button" @click="banUser" value="BAN THE USER"/>-->
    <br><br>
    <!-- <input type="button" @click="getAllUser" value="GET ALL USERS" /> -->
    <el-input
              class="search"
              type="search"
              v-model="search_user_name"
              placeholder="Search for a user"
              prefix-icon="el-icon-user-solid"
    ></el-input>
    <el-button icon="el-icon-search" class="search-button" type="button" @click="searchUser" value="SEARCH FOR THAT USER" block
    ></el-button>
    <!-- <input type="button" @click="searchUser" value="SEARCH FOR THAT USER" /> -->
    <br /><br />
    <el-input
        class="ban"
        type="text"
        v-model="ban_user_name"
        placeholder="Ban a user"
        prefix-icon="el-icon-user-solid"
    ></el-input>
    <el-button icon="el-icon-circle-close" class="ban-button" type="button" @click="banUser" value="BAN THE USER" block
    ></el-button>
    <br /><br />
    <p>Found User: {{ found_user_name }}</p>
    <ul>
      <li v-for="item in registered_users" :key="item">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'management',
  data() {
    return {
      total_artilces: null,
      total_users: null,
      total_discussions: null,
      registered_users: [],
      search_user_name: '',
      found_user_name: '',
      ban_user_name: '',
    };
  },
  methods: {
    banUser() {
      let ban_url = '';
      if (process.env.NODE_ENV === 'development') {
        ban_url = 'http://127.0.0.1:5000/';
      } else {
        ban_url = '/';
      }
      axios({
        method:"put",
        url:ban_url + "auth/banUser",
        data:{
          username:this.ban_user_name
        }
      }).then((res) => {
        if(res.data.delete == "done"){
          this.$alert("User has been banned.");
        }else{
          this.$alert("There's no such user.");
        }
      })
    },
    getAllUser() {
      let url = '';
      if (process.env.NODE_ENV === 'development') {
        url = 'http://127.0.0.1:5000/';
      } else {
        url = '/';
      }
      axios.get(url + 'auth/getAllUser').then(res => {
        console.log(res.data);
        this.registered_users = res.data;
      });
    },
    searchUser() {
      let search_url = '';
      if (process.env.NODE_ENV === 'development') {
        search_url = 'http://127.0.0.1:5000/';
      } else {
        search_url = '/';
      }
      axios({
        method: 'post',
        url: search_url + 'auth/findUser',
        data: {
          username: this.search_user_name,
        },
      }).then(res => {
        console.log(res.data.username);
        this.found_user_name = res.data.username;
      });
    },
  },
  mounted() {
    let url = '';
    if (process.env.NODE_ENV === 'development') {
      url = 'http://127.0.0.1:5000/';
    } else {
      url = '/';
    }
    axios
      .get(url + 'content/discussion')
      .then(res => {
        this.total_discussions = res.data.discussion_size;
      })
      .catch(err => console.log('ERR ' + err));

    axios
      .get(url + 'auth/check')
      .then(res => {
        this.total_users = res.data.user_number;
      })
      .catch(err => console.log(err));

    axios.get(url + 'article/check').then(res => {
      this.total_artilces = res.data.article_number;
    });
  },
};
</script>

<style scoped>
.get-button {
  margin-top: 40px;
  background: #020080;
  color: white;
}
.search,
.ban {
  width: 200px;
}
</style>
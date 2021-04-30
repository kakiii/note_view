<template>
  <div>
    <h1>MANAGEMENT</h1>
    <p>Discussions: {{ total_discussions }}</p>
    <p>Articles: {{ total_artilces }}</p>
    <p>Users: {{ total_users }}</p>
    <el-button
        icon="el-icon-search"
        class="get-button"
        type="button"
        @click="getAllUser"
        value="GET All USERS"
        block
    >Get All Users</el-button>
    <!-- <input type="button" @click="getAllUser" value="GET ALL USERS" /> -->
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
    };
  },
  methods: {
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
</style>
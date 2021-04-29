<template>
  <div>
    <h1>THIS IS ADMIN PAGE</h1>
    <p>Currently, there's {{ total_discussions }} discussions</p>
    <p>And there's {{ total_artilces }} articles made by {{ total_users }} users.</p>
    <br /><br /><br />
    <h4>For further infos about every user's usename, press the button below.</h4>
    <input type="button" @click="getAllUser" value="GET ALL USERS" />
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

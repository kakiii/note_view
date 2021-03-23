import axios from 'axios'

const api = axios.create({
    headers: {
        'Content-Type': 'application/json',
        'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
    }
})

export default{
    gets(){
        return api.get('/').then(response => response.data)
    },
    // login({username, password, remember}) {
    //     return api.post('/auth/login', {username, password, remember}).then(response => response.data)
    // },
    // register({username, password}) {
    //     return api.post('/auth/register', {username, password}).then(response => response.data)
    // },
    // getSession() {
    //     return api.get('/auth/session').then(response => response.data)
    // }
}
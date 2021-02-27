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
    }
}
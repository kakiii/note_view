<template>
    <div>
        <h1>THIS IS ADMIN PAGE</h1>
        <p>Currently, there's {{total_artilces}} discussions</p>
    </div>
</template>

<script>
import axios from 'axios'
export default{
    name:"management",
    data(){
        return{
total_artilces:null,
        }
        
    },
    mounted(){
        let url = "";
        if(process.env.NODE_ENV === "development"){
            url = "http://127.0.0.1:5000/";
        }else{
            url = "/";
        }
        axios.get(url + "content/discussion").then((res) => {
            console.log(res.data.discussion_size);
            this.total_artilces = res.data.discussion_size;
        }).catch((err) => console.log("ERR " + err));
    }
}
</script>

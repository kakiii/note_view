export default function validateUsername(str){
    if(str.length >= 5){
        return true;
    }else{
        return false;
    }
}
<template>
  <div>
    <p>This is Search Page.</p>
  </div>
</template>

<script>
window.onload = function () {
  function $id(id) {
    return document.getElementById(id);
  } //avoid continuing writing to get
  $id("txt").onfocus = function () {
    if (this.value == "please input...") {
      this.value = ""; //set the value
      this.style.color = "#333"; //black
    }
  }; //the origibal characters disappear
  $id("txt").onblur = function () {
    if (this.value == "") {
      this.value = "please input...";
      this.style.color = "#ccc"; //grey
    }
  }; //the original state
  $id("btn").onclick = function () {
    alert("I can click on it");
  }; //test
};
</script>

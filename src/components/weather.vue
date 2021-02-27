<template>
  <div>
    <h1>My Weather App</h1>
    <button v-on:click="getWeatherData">Get Weather Data</button>
    <div>{{ weatherDataList }}</div>
  </div>
</template>

<script>
export default {
  name: "Weather",
  data() {
    return {
      weatherDataList: [],
    };
  },
  methods: {
    getWeatherData() {
      fetch("/weather")
        .then((response) => response.json())
        .then((data) => (this.weatherDataList = data));
    },
  },
};
</script>

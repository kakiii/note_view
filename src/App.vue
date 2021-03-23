<template>
  <v-app>

    <v-main>
      <TheHeader v-if="$route.name !== `login`"/>
      <router-view></router-view>
      <TheFooter/>
    </v-main>
  </v-app>
</template>

<script>
import TheFooter from "@/components/TheFooter";
import TheHeader from "@/components/TheHeader";

export default {
  name: 'App',

  components: {
    TheFooter,TheHeader
  },

  data: () => ({
    //
  }),
};
</script>

<template>
  <div class="q-pa-md">
    <q-layout
      view="lHh lpr lFf"
      container
      style="height: 33px"
      class="shadow-2 rounded-borders"
    >
      <q-header elevated>
        <q-bar>
          <div>Menu</div>
          <q-space/>
          <q-btn color="white" text-color="black" label="HOME" to="/" />
          <q-btn color="secondary" label="NEW ARTICLE" to="/editor" />
          <q-btn color="amber" glossy label="DISCUSSION BOARD" to="/discussion" />
          <q-btn color="deep-orange" glossy label="404" to="/404" />
        </q-bar>
      </q-header>
    </q-layout>
  </div>
</template>

<script>
export default {
    name:"Header"
};
</script>
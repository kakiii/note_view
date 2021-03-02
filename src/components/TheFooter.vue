<template>
  <q-layout>
    <q-footer reveal elevated>
      <q-bar>
        <div>NOTE VIEW</div>
        <q-space/>
        <div class="cursor-pointer non-selectable">
            More...
            <q-menu>
                <q-list dense style="min-width : 50px">
                    <q-item clickable v-close-popup to="/about">
                        <q-item-section>
                            ABOUT
                        </q-item-section>
                    </q-item>

                </q-list>
            </q-menu>
        </div>
      </q-bar>
    </q-footer>
  </q-layout>
</template>
<script>
export default {
  name: "footer",
};
</script>
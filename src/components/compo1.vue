<template>
  <div>
    <h1>HI, I'm a Component</h1>
    <input type="radio" id="one" value="One" v-model="picked" />
    <label for="one">One</label>
    <input type="radio" id="two" value="Two" v-model="picked" />
    <label for="two">Two</label>
    <br /><br />
    <span>What you just Picked is {{ picked }}</span>
    <br /><br />
    <ol>
      <li v-for="list in lists" :key="list.mes">
        {{ list.mes }} is the new locals
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: "compo1",
  data() {
    return {
      picked: "'默认选项'",
      lists: [
        {
          mes: 1,
        },
        {
          mes: 2,
        },
        {
          mes: 3,
        },
        {
          mes: 4,
        },
        {
          mes: 5,
        },
      ],
    };
  },
};
</script>

<template>
  <nav>
    <RouterLink :to="{name: 'home'}">Home</RouterLink>
    <RouterLink :to="{name: 'cart'}">Cart</RouterLink>
  </nav>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
a::before {
  content: "|";
  margin: 0 5px;
}
a:first-of-type::before {
  content: "";
}
a:visited {
  color: black;
}
</style>

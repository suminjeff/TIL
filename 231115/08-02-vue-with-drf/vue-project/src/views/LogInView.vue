<template>
  <div>
    <h1>Log In Page</h1>
    <form>
      <input type="text" v-model.trim="username">
      <input type="password" v-model.trim="password">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '../stores/counter';

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const login = function() {
  const payLoad = {
    username: username.value,
    password: password.value,
  }
  store.login(payLoad)
}
</script>

<style>

</style>

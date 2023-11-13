<template>
  <div>
    <form @submit.prevent="createTodo()">
      <input type="text" v-model="todoText">
      <button>제출</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const todoText = ref('')
const createTodo = function() {
  if (todoText.value.length > 0) {
    store.addTodo(todoText.value)
    todoText.value = ''
  }
}
</script>

<style scoped>

</style>
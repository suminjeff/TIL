<template>
  <div>
    <ParentChild
    my-msg="message"
    :dynamic-props="name"
    @some-event="someCallback"
    @emit-args="getNumbers"
    @update-name="updateName"
    />
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue';
import { ref } from 'vue'

const name = ref('Alice')
const someCallback = function() {
  name.value += 'a'
}
const getNumbers = function(...args) {
  console.log(args)
}
const updateName = function() {
  if (name.value === 'Alice') {
    name.value = 'Bella'
  } else {
    name.value = 'Alice'
  }
}
</script>

<style scoped>

</style>
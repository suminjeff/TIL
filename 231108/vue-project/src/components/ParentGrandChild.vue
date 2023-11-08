<template>
  <div>
    {{ myMsg }}
    <button @click="updateName">이름을 바꿀래</button>
  </div>
</template>

<script setup>
defineProps({
  myMsg: {
    type: String,
    required: true,
  },
})
const emit = defineEmits(['updateName'])
const updateName = function () {
  emit('updateName')
}
</script>

<style scoped>

</style>

<template>
  <div>
    <!-- {{ myMsg }} -->
    <ParentGrandChild
    :my-msg="myMsg"
    @update-name="updateName"
    />
    <p>{{ dynamicProps }}</p>
    <button @click="$emit('someEvent')">개추</button>
    <button @click="buttonClick">개추2</button>
    <button @click="emitArgs">개추3</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue';
// defineProps(['myMsg'])
const props = defineProps({
                myMsg: {
                  type: String,
                  required: true,
                  // validator(value) {
                  //   return ['success', 'warning', 'danger'].includes(value)
                  // }
                  validator(value) {
                    const validValues = ['success', 'warning', 'danger']
                    if (!validValues.includes(value)) {
                      console.error('비상')
                      return false
                    }
                    return true
                  }
                },
                dynamicProps: {
                  type: String,
                  required: true,
                }
              })

// defineProps({
//   myMsg: {
//     type: String,
//     required: true,
//   }
// })

const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])
const buttonClick = function() {
  emit('someEvent')
}
const emitArgs = function() {
  emit('emitArgs', 1, 2, 3)
}
const updateName = function() {
  emit('updateName')
}
</script>

<style scoped>

</style>
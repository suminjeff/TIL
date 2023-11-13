<template>
  <div>
    <h1>상품 페이지</h1>
    <div v-if="productIsEmpty">
      <strong>로딩중</strong>
    </div>
    <div v-else class="product-card">
      <img :src="product.image" alt="">
      <strong>{{ product.title }}</strong>
      <p>가격: ${{ product.price }}</p>
      <button @click="addToCart(product)">장바구니에 추가</button>
    </div>
  </div>
  
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const product = ref('')
const productId = route.params.productId

const storeUrl = `https://fakestoreapi.com/products/${productId}`


axios.get(storeUrl)
.then((response) => {
  // console.log(response.data)
  product.value = response.data
})
.catch((error) => {
  console.log(error)
})
const productIsEmpty = computed(() => {
  return product.value.length === 0 ? true: false
})
</script>

<style scoped>

</style>
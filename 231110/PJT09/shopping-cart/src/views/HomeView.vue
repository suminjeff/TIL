<template>
  <div>
    <h1>메인 페이지</h1>
    <div v-if="productIsEmpty">
      <strong>로딩중</strong>
    </div>
    <div v-else class="product-list">
      <div v-for="product in products" :key="product.id" class="product-card">
        <img :src="product.image" alt="">
        <strong>{{ product.title }}</strong>
        <p>가격: ${{ product.price }}</p>
        <button @click="goDetail(product)">상세 페이지로 이동</button>
        <button @click="addToCart(product)">장바구니에 추가</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios'

const products = ref([])
const router = useRouter()
const storeUrl = 'https://fakestoreapi.com/products'

axios.get(storeUrl)
  .then((response) => {
    // console.log(response.data)
    products.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })

const productIsEmpty = computed(() => {
  return products.value.length === 0 ? true: false
})

const goDetail = (product) => {
  console.log(product)
  router.push(`/${product.id}`)
}

</script>

<style scoped>
.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
</style>

<style>
.product-card {
  border: 1px solid black;
  width: 200px;
}
.product-card img {
  width: 200px;
  height: 200px;
  object-fit: fill;
}
</style>
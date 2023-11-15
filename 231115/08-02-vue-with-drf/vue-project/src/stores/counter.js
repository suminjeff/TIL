import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function(payLoad) {
    const { username, password1, password2 } = payLoad
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
      }
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function(payLoad) {
    const { username, password } = payLoad
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password,
      }
    })
      .then((res) => {
        console.log(res)
        token.value = res.data.key
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { articles, API_URL, getArticles, signUp, token }
}, { persist: true })

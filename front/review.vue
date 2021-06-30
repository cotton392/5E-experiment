<template>
  <div id="app">
        <h1>ここ弄って欲しい</h1>
        <input type="text" v-model="message">
        <div class="error" v-if="error.require">必須項目です。</div>
        <div class="error" v-if="error.tooLong">長すぎます。</div>
        <div class="error" v-if="error.tooShort">短すぎます。</div>
  </div>
</template>

<script>
module.exports = {
  data: function() {
    return {
      title: 'review.vue',
      message: 'Hello',
        
    }
  },
  methods: {
  },
  watch :{
    
  }
}
</script>

<style scoped>
#hoge.error {
        color: red;
}
</style>

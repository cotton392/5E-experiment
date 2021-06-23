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
        error: {
            require: false,
            tooLong: false,
            tooShort: false
        }
    }
  },
  methods: {
  },
  watch :{
    message: function(newVal, oldVal) {
        this.error.require = (newVal.length < 1) ? true : false;
        this.error.tooLong = (newVal.length > 255) ? true : false;
        this.error.tooShort = (newVal.length < 4) ? true : false;
    }
  }
}
</script>

<style scoped>
#hoge.error {
        color: red;
}
</style>

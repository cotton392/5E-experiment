<template>
  <div id="app">
        <h1>ここ弄って欲しい</h1>
        <input type="text" v-model="message">
        <div class="error" v-if="error.require">必須項目です。</div>
        <div class="error" v-if="error.tooLong">長すぎます。</div>
        <div class="error" v-if="error.tooShort">短すぎます。</div>
 <!--        
<select v-model="selectedMenues">
  <option disabled value="">メニュー一覧</option>
  <option v-for="menu in optionMenues" 
    v-bind:value="menu.name" 
    v-bind:key="menu.id">
  {{ Menu.name }}
  </option>
</select>
-->
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
      
/*      selectedMenues: '',
      optionMenues: [
        {id: 1, name: 'Aセット'},
        {id: 2, name: 'Bセット'},
        {id: 3, name: 'その他これ増やす'}
      ],*/
    }
  },
  methods: {
  },
  watch :{
    
  }
}
</script>

<style scoped>
#app.error {
        color: red;
}
</style>

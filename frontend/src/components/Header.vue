<template>
  <div>
    <h1 class="text-center">딜딜딜</h1>
    <v-toolbar class="search-center" flat>
      <v-text-field v-model="inputText" hide-details append-icon="mdi-magnify"></v-text-field>
    </v-toolbar>
  </div>
</template>

<script>
import Vue from 'vue'

export let EventBus = new Vue();

export default {
  data: () => ({
    inputText:""
  }),
  watch:{
    inputText: function(newVal) {
      EventBus.$emit('searchKeyword', newVal)
    }
  }
};
</script>

<style scoped>
.text-center {
  text-align: center;
}
.search-center {
  width: 45%;
  margin-left: auto;
  margin-right: auto;
}
</style>
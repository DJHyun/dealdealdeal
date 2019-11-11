<template>
  <div class="list-center mt-3">
    <v-list v-for="(item, index) in itemsSliced" :key="index" class="py-0">
      <Card :title="item.title" :link="item.link" :time="item.time" />
    </v-list>
    <div class="text-center mt-3">
      <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" :total-visible="totalVisible" :color="color"/>
    </div>
  </div>
</template>

<script>
import Card from "@/components/dealList/Card";
import axios from 'axios';
import {EventBus} from "@/components/Header";

export default {
  components: {
    Card
  },
  data: () => ({
    items: [],
    cardsPerPage: 9,
    page: 1,
    totalVisible:8,
    color: '#2196f3',
    keyword:""
  }),
  computed: {
    searched: function() {
      return this.items.filter(x=>x.title.toLowerCase().includes(this.keyword.toLowerCase())).sort((x,y)=>{
      if (x.time<=y.time){
        return -1
      } else return 1
    })
    },
    itemsSliced: function() {
      let result = this.searched
      let length = result.length
      let start = length - this.cardsPerPage *this.page
      start = start < 0 ? 0 : start
      let last = length - this.cardsPerPage * (this.page-1)
      return result.slice(start, last).sort((x,y)=>{
      if (x.time>=y.time){
        return -1
      } else return 1
    })
    },
    maxPages: function() {
      return Math.ceil(this.searched.length/this.cardsPerPage)
    }
  },
  watch:{
    keyword: function(){
      this.page = 1
    }
  },
  async mounted(){
    const {data} = await axios.get('/api/hotdeal');
    this.items = data
  },
  methods:{
    onReceive(text) {
      this.keyword = text;
    }
  },
  created(){
    EventBus.$on('searchKeyword',this.onReceive)
  },
};
</script>

<style scoped>
.list-center {
  display: flex;
  flex-direction: column;
  justify-items: center;
}
</style>
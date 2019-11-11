<template>
  <v-container class="space">
      <Header/>
      <List />
  </v-container>
</template>

<script>
import Header from '@/components/Header';
import List from '@/components/dealList/List';

export default {
  name: 'App',
  components: {
    Header,
    List
  },
  data: () => ({

  }),
};
</script>

<style>
.space{
  justify-content: center;
  margin-top:2rem;
  margin-bottom: 2rem;
}
.mx-auto{
  margin-left: auto;
  margin-right: auto;
}
.text-center{
  text-align: center;
}
</style>
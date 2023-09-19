<script setup>
  import { reactive } from 'vue';
  import Interval from '@/components/Interval.vue'
  import Chart from '@/components/Chart.vue'
  

  const chartData = reactive({})
  const interval = reactive({
    startDate: '',
    endDate: ''
  })

</script>

<template>
  
  <div class="container">
    <header>
      <h1>Dashboard</h1>
      <Interval :startDate="interval.startDate" :endDate="interval.endDate"/>
    </header>
    <main>
      <Chart :startDate="interval.startDate" :endDate="interval.endDate"/>
    </main>
  </div>

</template>

<style scoped>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  width: calc(100% - 4rem);
  height: calc(100% - 4rem);
  background-color: #f5f5f5;
}

h1 {
  margin-bottom: 4rem;
  font-size: 2rem;
  font-weight: 700;
  color: #363636;
  text-align: center;
}

header {
  margin-bottom: 3rem;
}


</style>


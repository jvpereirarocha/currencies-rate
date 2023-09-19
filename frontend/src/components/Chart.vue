<script setup>
import { reactive, onMounted } from 'vue'
import { Chart as ChartJS, registerables } from 'chart.js'
import { LineChart } from 'vue-chart-3'
import Interval from './Interval.vue'

ChartJS.register(...registerables)

const props = defineProps({
    startDate: {
        type: String,
        required: true
    },
    endDate: {
        type: String,
        required: true
    }
})

const labels = []
const data = {
    labels: labels,
    datasets: [{
        label: 'My First Dataset',
        data: [65, 59, 80, 81, 56, 55, 40],
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ]
    }]
}

</script>

<template>

    <div class="chart-container">
        <LineChart :chartData="data"/>
    </div>

</template>

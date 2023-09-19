<script setup>
import { reactive, watchEffect, watch, ref } from 'vue'
import Date from './Date.vue'
import ChartComponent from './Chart.vue'

const props = defineProps({
    startDate: {
        type: String,
        required: false
    },
    endDate: {
        type: String,
        required: false
    }
})

const startDate = ref(props.startDate)
const endDate = ref(props.endDate)

watch(startDate, (newValue, oldValue) => {
    console.log(newValue, oldValue)
})

const formatOfDate = '##/##/####'

defineEmits(['update:startDate', 'update:endDate', 'change'])

</script>

<template>
    <div class="interval-area">
        <div class="date-container">
            <Date
                :name="'Data inicial'"
                :date="startDate"
                :formatOfDate="formatOfDate"
                @input="startDate = $event.target.value"
                @change="$emit('update:startDate', startDate)"
            />
        </div>
        <div class="date-container">
            <Date
                :name="'Data final'"
                :date="endDate"
                :formatOfDate="formatOfDate"
                @input="endDate = $event.target.value"
                @change="$emit('update:endDate', endDate)"/>
        </div>
        <button @click="validarIntervalo($event)" type="button">Filtrar</button>
    </div>
</template>

<style scoped>

.interval-area {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 3rem;
}

.content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 3rem;
}

</style>
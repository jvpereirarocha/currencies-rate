<script setup>
import { reactive, watchEffect, watch, ref } from 'vue'
import Date from '@/components/Date.vue'
import ChartComponent from '@/components/Chart.vue'
import Alert from '@/components/Alert.vue'

import validateInterval from '@/domain/interval';
import clearAlertAfterSpecifiedTime from '@/domain/alert.js';
import { useAlertStore } from '../stores/alert';

const alertStore = useAlertStore()

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

const validarIntervalo = () => {
    try {
        validateInterval(startDate.value, endDate.value)
        alertStore.success('Intervalo válido')
        clearAlertAfterSpecifiedTime(alertStore, 5);
    }
    catch (error) {
        alertStore.error(error.message)
        clearAlertAfterSpecifiedTime(alertStore, 5);
    }
}

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
        <button @click="validarIntervalo()" type="button">Filtrar</button>
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
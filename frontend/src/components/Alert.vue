<script setup>
import { storeToRefs } from 'pinia'

import { useAlertStore } from '@/stores/alert.js'

const alertStore = useAlertStore()
const { alert } = storeToRefs(alertStore)

</script>


<template>
    <div v-if="alert" class="container">
        <div class="alert" :class="alert.type">
            {{ alert.message }}
        </div>
    </div>
</template>

<style scoped>

.alert {
    padding: 20px;
    color: white;
    margin-bottom: 15px;
}

.success {
    background-color: #4CAF50;
}

.info {
    background-color: #2196F3;
}

.warning {
    background-color: #ff9800;
}

.danger {
    background-color: #f44336;
}

/* The close button */
.closebtn {
    margin-left: 15px;
    color: white;
    font-weight: bold;
    float: right;
    font-size: 22px;
    line-height: 20px;
    cursor: pointer;
    transition: 0.3s;
}

/* When moving the mouse over the close button */
.closebtn:hover {
    color: black;
}

</style>
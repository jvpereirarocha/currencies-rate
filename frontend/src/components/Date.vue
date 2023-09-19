<script setup>
import { ref, onMounted, onUpdated } from 'vue'
import { vMaska } from 'maska'

const props = defineProps({
    name: {
        type: String,
        required: true
    },
    date: {
        type: String,
        required: true
    },
    formatOfDate: {
        type: String,
        required: true
    }
})

defineEmits(['change'])

const dateValue = ref(props.date)

</script>

<template>
    <div class="control">
        <input
            class="input"
            :placeholder="name"
            name="date"
            v-maska
            :value="dateValue"
            :data-maska="formatOfDate"
            type="text"
            @input="dateValue = $event.target.value"
            @change="$emit('change', dateValue)"
            />
    </div>
</template>

<style scoped>

input {
    width: 100%;
    height: 1rem;
    padding: 0.5rem;
    border: none;
    border-radius: 0.25rem;
    outline: none;
}

</style>
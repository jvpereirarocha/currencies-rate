import { defineStore } from 'pinia'


export const useAlertStore = defineStore({
    id: 'alert',
    state: () => ({
        alert: null
    }),
    actions: {
        success(message) {
            this.alert = {
                type: 'success',
                message
            }
        },
        error(message) {
            this.alert = {
                type: 'danger',
                message
            }
        },
        warning(message) {
            this.alert = {
                type: 'warning',
                message
            }
        },
        info(message) {
            this.alert = {
                type: 'info',
                message
            }
        },
        clear() {
            this.alert = null
        }
    }
})
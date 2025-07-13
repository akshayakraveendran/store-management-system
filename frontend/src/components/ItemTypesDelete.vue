<template>
  <DeleteConfirm
    v-if="isVisible"
    @confirm="handleConfirm"
    @close="handleClose"
  />
</template>

<script setup>
import DeleteConfirm from './DeleteConfirm.vue'

const props = defineProps({
  isVisible: Boolean
})

const emit = defineEmits(['confirm', 'close'])

const handleConfirm = () => {
  emit('confirm')
}

const handleClose = () => {
  emit('close')
}
</script>
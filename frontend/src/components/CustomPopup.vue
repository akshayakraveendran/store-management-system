<template>
  <div
    :id="modalId"
    :class="[
      'fixed inset-0 z-50 flex items-center justify-center overflow-y-auto overflow-x-hidden',
      isOpen ? 'block' : 'hidden'
    ]"
    tabindex="-1"
    aria-hidden="true"
  >
    <div 
      class="fixed inset-0  bg-opacity-50" 
      @click="closeModal"
    ></div>
    
    <div class=" relative w-full max-w-2xl max-h-full p-4">
      <div class="border border-gray-400 relative bg-white rounded-lg shadow dark:bg-gray-700">
        <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            {{ title }}
          </h3>
          <button
            type="button"
            class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
            @click="closeModal"
          >
            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
        </div>
        
        <div class="p-4 md:p-5 space-y-4">
          <slot name="body">
            <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              Default modal content
            </p>
          </slot>
        </div>
    
      </div>
    </div>
  </div>
</template>

<script setup>
import { watch, onMounted, onUnmounted, computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: 'Modal Title'
  },
  modalId: {
    type: String,
    default: 'default-modal'
  },
  closeOnBackdrop: {
    type: Boolean,
    default: true
  },
  closeOnEscape: {
    type: Boolean,
    default: true
  },
  size: {
    type: String,
    default: 'max-w-2xl',
    validator: (value) => ['max-w-sm', 'max-w-md', 'max-w-lg', 'max-w-xl', 'max-w-2xl', 'max-w-3xl', 'max-w-4xl', 'max-w-5xl', 'max-w-6xl', 'max-w-7xl'].includes(value)
  }
})

const emit = defineEmits(['update:modelValue', 'close', 'confirm'])

const isOpen = computed(() => props.modelValue)

const closeModal = () => {
  if (props.closeOnBackdrop) {
    emit('update:modelValue', false)
    emit('close')
  }
}

const handleConfirm = () => {
  emit('confirm')
}

const handleEscape = (event) => {
  if (event.key === 'Escape' && props.closeOnEscape && isOpen.value) {
    closeModal()
  }
}

watch(isOpen, (newValue) => {
  if (newValue) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = 'unset'
  }
})

onMounted(() => {
  if (props.closeOnEscape) {
    document.addEventListener('keydown', handleEscape)
  }
})

onUnmounted(() => {
  if (props.closeOnEscape) {
    document.removeEventListener('keydown', handleEscape)
  }
  // Reset body overflow when component is destroyed
  document.body.style.overflow = 'unset'
})
</script>
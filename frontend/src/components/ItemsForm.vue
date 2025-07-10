<template>
    <CustomPopup
      v-model="showModal" 
      :title="title"
      :modal-id="modalId"
      :close-on-backdrop="true"
      :close-on-escape="true"
      @close="handleModalClose"
      @confirm="handleModalConfirm"
    >
        <template #body>
            <div class="p-4" v-if="errors && errors.length">
                <div v-for="(error, property) in errors" :key="property"
                class="flex items-center p-2 mb-2 text-xs text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400" role="alert">
                    <svg class="shrink-0 inline w-4 h-4 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
                    </svg>
                    <div>
                        <span class="font-medium">{{ error }} </span>
                    </div>
                </div>
            </div>

            <form class="p-4 md:p-5" @submit.prevent="handleSubmit" v-if="modelValue">
                <div class="grid gap-4 mb-4 grid-cols-2">
                    <div class="col-span-2">
                        <label for="name"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
                        <input :value="modelValue.name" @input="updateField('name', $event.target.value)"
                            type="text" name="name" id="name"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Type product name" required="">
                    </div>
                    <div class="col-span-2 sm:col-span-1">
                        <label for="price"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Price</label>
                        <input :value="modelValue.price" @input="updateField('price', $event.target.value)"
                            type="number" name="price" id="price" step="0.01"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="$2999" required="">
                    </div>
                    <div class="col-span-2 sm:col-span-1">
                        <label for="category"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Item
                            Type</label>
                        <select :value="modelValue.item_type"
                            @change="updateField('item_type', parseInt($event.target.value))" id="category"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option value="">Select Item Type</option>
                            <option value="1">Clothing</option>
                            <option value="2">Groceries</option>
                            <option value="3">Electrical</option>
                        </select>
                    </div>
                    <div class="col-span-2">
                        <label for="description"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label>
                        <textarea :value="modelValue.description"
                            @input="updateField('description', $event.target.value)" id="description" rows="4"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="Write product description here"></textarea>
                    </div>
                </div>
                <button type="submit"
        a            class="text-white inline-flex items-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    <svg class="me-1 -ms-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
                            clip-rule="evenodd"></path>
                    </svg>
                    {{ modelValue.id ? 'Update Item' : 'Add Item' }}
                </button>
            </form>
        </template>
    </CustomPopup>
</template>

<script setup>
import { watch, ref, computed } from 'vue';
import CustomPopup from './CustomPopup.vue'

const props = defineProps({
    modelValue: {
        type: Object,
        required: true,
    },
    isVisible: {
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
    errors: {
        type: Array
    }
})

const emit = defineEmits(['update:modelValue', 'close', 'submit'])

const showModal = ref(props.isVisible);

const updateField = (field, value) => {
    const updatedItem = { ...props.modelValue }
    updatedItem[field] = value
    emit('update:modelValue', updatedItem)
}

const handleSubmit = () => {
    emit('submit', props.modelValue)
}

const handleModalClose = () => {
    showModal.value = false
    emit('close')
}

const handleModalConfirm = () => {
    showModal.value = false
    emit('close')
}

watch(() => props.isVisible, (newVal) => {
    showModal.value = newVal;
})

watch(showModal, (newVal) => {
    if (!newVal) {
        emit('close')
    }
})
</script>
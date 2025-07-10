<template>
    <CustomPopup v-model="showModal" :title="title" :modal-id="modalId" :close-on-backdrop="true"
        :close-on-escape="true" @close="handleModalClose" @confirm="handleModalConfirm">
        <template #body>
            <div class="p-4" v-if="errors && errors.length">
                <div v-for="(error, property) in errors" :key="property"
                    class="flex items-center p-2 mb-2 text-xs text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400"
                    role="alert">
                    <svg class="shrink-0 inline w-4 h-4 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor" viewBox="0 0 20 20">
                        <path
                            d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
                    </svg>
                    <div><span class="font-medium">{{ error }}</span></div>
                </div>
            </div>

            <form class="p-4 md:p-5" @submit.prevent="handleSubmit" v-if="modelValue">
                <div class="grid gap-4 mb-4 grid-cols-2">
                    <div class="col-span-2">
                        <label for="description"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label>
                        <textarea :value="modelValue.description"
                            @input="updateField('description', $event.target.value)" id="description" rows="4"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="Write description here"></textarea>
                    </div>

                    <div class="col-span-2 sm:col-span-1">
                        <label for="quantity"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Quantity</label>
                        <input :value="modelValue.quantity" @input="updateField('quantity', $event.target.value)"
                            type="number" name="quantity" id="quantity" step="0.01"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Enter quantity" required>
                    </div>

                    <div class="col-span-2 sm:col-span-1">
                        <label for="item"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Item</label>
                        <select v-model="modelValue.item" 
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option value="">Select an item</option>
                            <template v-for="item in items" :key="item.id">
                                <option :value="item.id">{{ item.name }}</option>
                            </template>
                        </select>
                    </div>
                </div>

                <button type="submit"
                    class="text-white inline-flex items-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    <svg class="me-1 -ms-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
                            clip-rule="evenodd"></path>
                    </svg>
                    {{ modelValue.id ? 'Update Inventory' : 'Add Inventory' }}
                </button>
            </form>
        </template>
        >
    </CustomPopup>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import CustomPopup from './CustomPopup.vue'
import { useApi } from '@/composables/useApi';

const { get } = useApi();
const items = ref();

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
    },
    items: {
        type: Array,
        default: () => []
    }
})

const emit = defineEmits(['update:modelValue', 'close', 'submit'])

const showModal = ref(props.isVisible)

const updateField = (field, value) => {
    const updated = { ...props.modelValue }
    updated[field] = value
    emit('update:modelValue', updated)
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

watch(() => props.isVisible, (val) => {
    showModal.value = val
})

watch(showModal, (val) => {
    if (!val) {
        emit('close')
    }
})

const getItems = async () => {
    const response = await get('/items');
    if (response.status === 200) {
        items.value = response.data;
    }
}

onMounted(async () => {
    await getItems()
});
</script>

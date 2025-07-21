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
      <!-- Display validation and stock errors -->
      <div class="p-4" v-if="errors && errors.length">
        <div
          v-for="(error, property) in errors"
          :key="property"
          class="flex items-center p-2 mb-2 text-xs text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400"
          role="alert"
        >
          <svg class="shrink-0 inline w-4 h-4 me-3" fill="currentColor" viewBox="0 0 20 20">
            <path
              d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"
            />
          </svg>
          <div><span class="font-medium">{{ error }}</span></div>
        </div>
      </div>

      <form class="p-4 md:p-5 max-h-[300px] overflow-y-auto" @submit.prevent="handleSubmit">
        <div v-for="(entry, index) in formItems" :key="index" class="grid gap-4 mb-4 grid-cols-2">
          <div>
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Item</label>
            <select
              v-model="entry.item"
              @change="() => onItemChange(entry)"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:text-white"
            >
              <option value="">Select an item</option>
              <option v-for="inv in invItems" :key="inv.item" :value="inv.item">
                {{ items.find(i => i.id === inv.item)?.name || 'Unknown' }}
              </option>
            </select>
          </div>

          <div>
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Price</label>
            <input
              type="number"
              :value="entry.price"
              readonly
              class="bg-gray-200 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 dark:bg-gray-700 dark:text-white"
            />
          </div>

          <div>
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Quantity</label>
            <input
              type="number"
              v-model="entry.quantity"
              min="1"
              @change="() => getstocks(entry)"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:text-white"
            />
          </div>
        </div>

        <div class="mb-4">
          <button type="button" @click="addItem" class="text-sm text-blue-600">+ Add Another Item</button>
        </div>
        <div class="col-span-2">
                        <label for="description"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Shipping Addess</label>
                        <textarea :value="modelValue.description"
                            @input="updateField('description', $event.target.value)" id="description" rows="4"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="Write description here"></textarea>
                    </div>
        <div v-if="stockError" class="text-red-600 text-sm mb-4">{{ stockError }}</div>

        <button
          type="submit"
          class="text-white inline-flex items-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
        >
          <svg class="me-1 -ms-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path
              fill-rule="evenodd"
              d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
              clip-rule="evenodd"
            ></path>
          </svg>
          Submit Purchase
        </button>
      </form>
    </template>
  </CustomPopup>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import CustomPopup from './CustomPopup.vue'
import { useApi } from '@/composables/useApi'

const { get } = useApi()

const items = ref([])
const invItems = ref([])
const stockError = ref(null)
const formItems = ref([{ item: null, price: 0, quantity: 1 }])

const props = defineProps({
  isVisible: Boolean,
  title: String,
  modalId: String,
  errors: Array,
  items: Array
})

const emit = defineEmits(['close', 'submit'])
const showModal = ref(props.isVisible)

const handleSubmit = () => {
  emit('submit', formItems.value)
  emit('close')
}

const handleModalClose = () => emit('close')
const handleModalConfirm = () => emit('close')

const addItem = () => {
  formItems.value.push({ item: null, price: 0, quantity: 1 })
}

const onItemChange = (entry) => {
  const itemDetail = items.value.find(i => i.id === entry.item)
  entry.price = itemDetail ? itemDetail.price : 0
  getstocks(entry)
}

const getstocks = (entry) => {
  const selected = invItems.value.find(t => t.item === entry.item)
  if (selected && entry.quantity > selected.stock) {
    stockError.value = 'Out of stock'
  } else {
    stockError.value = null
  }
}

const getItemsInventory = async () => {
  const response = await get('/inventory')
  if (response.status === 200) invItems.value = response.data
}

const getItems = async () => {
  const response = await get('/items')
  if (response.status === 200) items.value = response.data
}

onMounted(async () => {
  await getItemsInventory()
  await getItems()
})

watch(() => props.isVisible, (val) => showModal.value = val)
</script>
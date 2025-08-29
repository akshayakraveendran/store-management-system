<template>
  <CustomPopup
    v-model="visible"
    :title="title"
    :modal-id="modalId"
    :close-on-backdrop="true"
    :close-on-escape="true"
    @close="handleClose"
    @confirm="handleSubmit"
  >
    <template #body>
      <form @submit.prevent="handleSubmit" class="space-y-4">
       <div>
          <label class="block text-sm font-medium text-gray-700">Customer</label>
          <select
            v-model="localModel.customer"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          >
            <option value="" disabled>Select Purchases</option>
            <option
              v-for="type in customers"
              :key="type.id"
              :value="type.id"
            >
              {{ type.name }}
            </option>
          </select>
          <p v-if="errors?.purchase" class="text-sm text-red-600">{{ errors.purchase[0] }}</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Item</label>
          <select
            v-model="localModel.item"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          >
            <option value="" disabled>Select Items</option>
            <option
              v-for="type in customers"
              :key="type.id"
              :value="type.id"
            >
              {{ type.name }}
            </option>
          </select>
          <p v-if="errors?.customer" class="text-sm text-red-600">{{ errors.customer[0] }}</p>
        </div>
      <div class="flex space-x-4">
        <div class="w-1/2">
          <label class="block text-sm font-medium text-gray-700">Quantity</label>
          <input
            type="number"
            v-model="localModel.quantity"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.quantity" class="text-sm text-red-600">{{ errors.quantity[0] }}</p>
        </div>

        <div class="w-1/2">
          <label class="block text-sm font-medium text-gray-700">Price</label>
          <input
            type="number"
            v-model="localModel.price"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.price" class="text-sm text-red-600">{{ errors.price[0] }}</p>
        </div>
      </div>

      <div class="flex space-x-4">
        <div class="w-1/2">
          <label class="block text-sm font-medium text-gray-700">Total Price</label>
          <input
            type="number"
            v-model="localModel.total_price"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.total_price" class="text-sm text-red-600">{{ errors.total_price[0] }}</p>
        </div>

        <div class="w-1/2">
          <label class="block text-sm font-medium text-gray-700">Discount Amount</label>
          <input
            type="number"
            v-model="localModel.discount_amount"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.discount_amount" class="text-sm text-red-600">{{ errors.discount_amount[0] }}</p>
        </div>
      </div>  
      <div class="flex space-x-4">
        <div class="w-1/2">
          <label class="block text-sm font-medium text-gray-700">Tax Amount</label>
          <input
            type="number"
            v-model="localModel.tax_amount"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.tax_amount" class="text-sm text-red-600">{{ errors.tax_amount[0] }}</p>
        </div>

        <div class="w-1/2">
          <label class="block text-sm font-medium text-gray-700">Shipping Address</label>
          <input
            type="number"
            v-model="localModel.shipping_address"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.shipping_address" class="text-sm text-red-600">{{ errors.shipping_address[0] }}</p>
        </div>
      </div>
        <div>
          <label class="block text-sm font-medium text-gray-700">Sub Total</label>
          <input
            type="number"
            v-model="localModel.sub_total"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.sub_total" class="text-sm text-red-600">{{ errors.sub_total[0] }}</p>
        </div>

        <div class="pt-4 flex justify-end">
        <button
            type="button"
            @click="handleSubmit"
            class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition relative right-120"
        >
            Add Item
        </button>
       </div>
      </form>
    </template>
  </CustomPopup>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import CustomPopup from '@/components/CustomPopup.vue'
import { useApi } from '@/composables/useApi'

const props = defineProps({
  modelValue: {
    type: Object,
    default: () => ({})
  },
  errors: {
    type: Object,
    default: null
  },
  title: {
    type: String,
    default: 'Form Title'
  },
  modalId: {
    type: String,
    default: 'item-modal'
  },
  isVisible: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue', 'submit', 'close'])

const { get } = useApi()

const visible = ref(props.isVisible)
const localModel = ref({ ...props.modelValue })
const customers = ref([]) 
const items = ref([]) 


onMounted(async () => {
  const response = await get('/customers')
  if (response.status === 200) {
    customers.value = response.data
  }
})
onMounted(async () => {
  const response = await get('/items')
  if (response.status === 200) {
    items.value = response.data
  }
})

// Keep localModel in sync
watch(
  () => props.modelValue,
  (newValue) => {
    localModel.value = { ...newValue }
  },
  { deep: true, immediate: true }
)

// Sync visibility
watch(
  () => props.isVisible,
  (val) => {
    visible.value = val
  }
)

watch(visible, (val) => {
  emit('update:isVisible', val)
})

const handleSubmit = () => {
  emit('update:modelValue', localModel.value)
  emit('submit')
}

const handleClose = () => {
  emit('close')
}
</script>
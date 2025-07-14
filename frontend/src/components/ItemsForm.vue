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
          <label class="block text-sm font-medium text-gray-700">Name</label>
          <input
            type="text"
            v-model="localModel.name"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.name" class="text-sm text-red-600">{{ errors.name[0] }}</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Description</label>
          <textarea
            v-model="localModel.description"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          ></textarea>
          <p v-if="errors?.description" class="text-sm text-red-600">{{ errors.description[0] }}</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Price</label>
          <input
            type="number"
            v-model="localModel.price"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.price" class="text-sm text-red-600">{{ errors.price[0] }}</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Item Type</label>
          <select
            v-model="localModel.item_type"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          >
            <option value="" disabled>Select Item Type</option>
            <option
              v-for="type in itemTypes"
              :key="type.id"
              :value="type.id"
            >
              {{ type.name }}
            </option>
          </select>
          <p v-if="errors?.item_type" class="text-sm text-red-600">{{ errors.item_type[0] }}</p>
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
const itemTypes = ref([]) // For dropdown options

// Load item types on mount
onMounted(async () => {
  const response = await get('/item-types')
  if (response.status === 200) {
    itemTypes.value = response.data
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
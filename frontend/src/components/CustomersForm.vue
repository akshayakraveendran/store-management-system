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
            <label class="block text-sm font-medium text-gray-700">Email</label>
            <input
              type="email"
              v-model="localModel.email"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
            />
            <p v-if="errors?.email" class="text-sm text-red-600">{{ errors.email[0] }}</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Phone</label>
          <input
            type="text"
            v-model="localModel.phone"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.phone" class="text-sm text-red-600">{{ errors.phone[0] }}</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Address</label>
          <textarea
            v-model="localModel.address"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          ></textarea>
          <p v-if="errors?.address" class="text-sm text-red-600">{{ errors.address[0] }}</p>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">City</label>
          <input
            type="text"
            v-model="localModel.city"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
          />
          <p v-if="errors?.city" class="text-sm text-red-600">{{ errors.city[0] }}</p>
        </div>

        <div>
            <label class="block text-sm font-medium text-gray-700">pin Code</label>
            <input
              type="text"
              v-model="localModel.pincode"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring focus:ring-blue-200"
            />
            <p v-if="errors?.pincode" class="text-sm text-red-600">{{ errors.pincode[0] }}</p>
        </div>

        <div class="pt-4 flex justify-end">
        <button type="submit"
                    class="text-white inline-flex items-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    <svg class="me-1 -ms-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
                            clip-rule="evenodd"></path>
                    </svg>
                    {{ modelValue.id ? 'Update Customer' : 'Add Customer' }}
                </button>
       </div>
      </form>
    </template>
  </CustomPopup>
</template>

<script setup>
import { ref, watch} from 'vue'
import CustomPopup from '@/components/CustomPopup.vue'

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

const visible = ref(props.isVisible)
const localModel = ref({ ...props.modelValue })

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
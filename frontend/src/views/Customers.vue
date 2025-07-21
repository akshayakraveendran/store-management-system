<template>
  <div class="flex flex-wrap gap-8" v-if="items">
    <div class="flex flex-wrap gap-4 w-full justify-between">
      <h1 class="font-bold text-2xl">Customers</h1>
      <button
        class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        type="button"
        @click="openModal()"
      >
        Add
      </button>
    </div>

    <List
      :headers="headers"
      :items="items"
      @edit="editItemClicked"
      @delete="deleteItemClicked"
    />

    <!-- Item Form Modal -->
    <CustomersForm
      v-if="showModal"
      v-model="formCustomer"
      :is-visible="showModal"
      :errors="formError"
      :title="formCustomer?.id ? 'Edit Customer' : 'Add New Customer'"
      modal-id="item-modal"
      @close="showModal = false"
      @submit="saveItem"
    />

    <!-- Delete Confirmation Modal -->
    <ItemTypesDelete
      :is-visible="showDeleteModal"
      @close="showDeleteModal = false"
      @confirm="confirmDelete"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import List from '@/components/List.vue'
import ItemTypesDelete from '@/components/ItemTypesDelete.vue'
import { useApi } from '@/composables/useApi'
import { computed } from 'vue'
import CustomersForm from '@/components/CustomersForm.vue'

const itemTypes = ref([])
const { get, post, put, delete: del } = useApi()

// State references
const showModal = ref(false)
const showDeleteModal = ref(false)
const items = ref([])
const formCustomer = ref(null)
const formError = ref(null)

const formCustomerTemplate = {
  id: null,
  name: '',
  email: '',
  phone: '',
  address: '',
  city: '',
  pincode: '',
  created_at: '',
  updated_at: '',
}

// Table headers
const headers = ref([
  { label: 'Name', property: 'name' },
  { label: 'Email', property: 'email' },
  { label: 'Phone', property: 'phone' },
  { label: 'Address', property: 'address' },
  { label: 'City', property: 'city' },
  { label: 'Pin Code', property: 'pincode' },
  { label: 'Created At', property: 'created_at' },
  { label: 'Updated At', property: 'updated_at' }
])


const openModal = () => {
  formCustomer.value = { ...formCustomerTemplate }
  formError.value = null
  showModal.value = true
}


const editItemClicked = (item) => {
  formCustomer.value = { ...item }
  formError.value = null
  showModal.value = true
}


const deleteItemClicked = (item) => {
  formCustomer.value = item
  showDeleteModal.value = true
}


const confirmDelete = async () => {
  await deleteItem(formCustomer.value.id)
  await getList()
  showDeleteModal.value = false
}


const getList = async () => {
  const response = await get('/customers')
  if (response.status === 200) {
    items.value = response.data
  }
}


const createItem = async () => {
  const response = await post('/customers/', formCustomer.value)
  if (response.errors) {
    formError.value = response.errors
    return
  }
  await getList()
  showModal.value = false
}

// Update existing item
const updateItem = async () => {
  const response = await put(`/customers/${formCustomer.value.id}/`, formCustomer.value)
  if (response.data) {
    await getList()
    showModal.value = false
  }
}

// Save item handler (create or update)
const saveItem = async () => {
  if (!formCustomer.value) return

  if (!formCustomer.value.id) {
    await createItem()
  } else {
    await updateItem()
  }
}

// Delete item
const deleteItem = async (id) => {
  await del(`/customers/${id}/`)
}

onMounted(async () => {
  await getList()
})
</script>
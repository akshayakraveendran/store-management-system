<template>
  <div class="flex flex-wrap gap-8" v-if="items">
    <div class="flex flex-wrap gap-4 w-full justify-between">
      <h1 class="font-bold text-2xl">Purchases</h1>
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
      :items="itemTypeName"
      @edit="editItemClicked"
      @delete="deleteItemClicked"
    />

   
    <PurchaseForm
      v-if="showModal"
      v-model="formItem"
      :is-visible="showModal"
      :errors="formError"
      :title="formItem?.id ? 'Edit Purchase' : 'Add New Purchase'"
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
import ItemsForm from '@/components/ItemsForm.vue'
import ItemTypesDelete from '@/components/ItemTypesDelete.vue'
import { useApi } from '@/composables/useApi'
import { computed } from 'vue'
import PurchaseForm from '@/components/PurchaseForm.vue'

const itemTypes = ref([])
const { get, post, put, delete: del } = useApi()

// State references
const showModal = ref(false)
const showDeleteModal = ref(false)
const items = ref([])
const formItem = ref(null)
const formError = ref(null)

const formItemTemplate = {
  id: null,
  customer: '',
  item: '',
  quantity: '',
  price: '',
  total_price: '',
  discount_amount: '',
  tax_amount: '',
  shipping_address: '',
  sub_total: '',
  created_at: '',
  updated_at: '',
}

// Table headers
const headers = ref([
  { label: 'Customer', property: 'customer' },
  { label: 'Item', property: 'item' },
  { label: 'Quantity', property: 'quantity' },
  { label: 'Price', property: 'price' },
  { label: 'Total Price', property: 'total_price' },
  { label: 'Discount Amount', property: 'discount_amount' },
  { label: 'Tax Amount', property: 'tax_amount' },
  { label: 'Shipping Address', property: 'shipping_address' },
  { label: 'Sub Total', property: 'sub_total' },
  { label: 'Created At', property: 'created_at' },
  { label: 'Updated At', property: 'updated_at' }
])

// Open modal for new item
const openModal = () => {
  formItem.value = { ...formItemTemplate }
  formError.value = null
  showModal.value = true
}

// Edit existing item
const editItemClicked = (item) => {
  formItem.value = { ...item }
  formError.value = null
  showModal.value = true
}

// Delete confirmation
const deleteItemClicked = (item) => {
  formItem.value = item
  showDeleteModal.value = true
}

// Confirm delete
const confirmDelete = async () => {
  await deleteItem(formItem.value.id)
  await getList()
  showDeleteModal.value = false
}

// Fetch all items
const getList = async () => {
  const response = await get('/items')
  if (response.status === 200) {
    items.value = response.data
  }
}

const getItemTypes = async () => {
  const response = await get('/item-types');
  if (response.status === 200) {
    itemTypes.value = response.data;
  }
}

const itemTypeName = computed(() => {
  if (!items.value || !itemTypes.value) return []

  return items.value.map(item => {
    const type = itemTypes.value.find(t => t.id === item.item_type)
    return {
      ...item,
      itemType: type ? type.name : 'Unknown'
    }
  })
})
// Create new item
const createItem = async () => {
  const response = await post('/purchases/', formItem.value)
  if (response.errors) {
    formError.value = response.errors
    return
  }
  const purchaseResponse = await post('/purchased-items/', {
    item_id: response.id, 
    quantity: formItem.value.quantity,
    price: formItem.value.price
  })

  if (purchaseResponse.errors) {
    formError.value = purchaseResponse.errors
    return
  }
  await getList()
  showModal.value = false
}

// Update existing item
const updateItem = async () => {
  const response = await put(`/items/${formItem.value.id}/`, formItem.value)
  if (response.data) {
    await getList()
    showModal.value = false
  }
}

// Save item handler (create or update)
const saveItem = async () => {
  if (!formItem.value) return

  if (!formItem.value.id) {
    await createItem()
  } else {
    await updateItem()
  }
}

// Delete item
const deleteItem = async (id) => {
  await del(`/items/${id}/`)
}

onMounted(async () => {
  await getList()
  await getItemTypes();
})
</script>
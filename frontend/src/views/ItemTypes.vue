<template>
  <div class="flex flex-wrap gap-8" v-if="items">
    <div class="flex flex-wrap gap-4 w-full justify-between">
      <h1 class="font-bold text-2xl">Item Types</h1>
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

    <ItemTypesForm 
      v-model="formItem"
      :is-visible="showModal"
      :errors="formError"
      :title="formItem?.id ? 'Edit Item' : 'Add New Item type'"
      modal-id="item-modal"
      @close="showModal = false"
      @submit="saveItem"
    />

    <ItemTypesDelete 
      :is-visible="showDeleteModal"
      @close="showDeleteModal = false"
      @confirm="confirmDelete"
    />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import List from '@/components/List.vue'
import { useApi } from '@/composables/useApi'
import ItemTypesForm from '@/components/ItemTypesForm.vue'
import ItemTypesDelete from '@/components/ItemTypesDelete.vue'

const { get, post, put, delete: del } = useApi()

const showModal = ref(false)
const showDeleteModal = ref(false)

const headers = ref([
  { label: 'Name', property: 'name' },
  { label: 'Created At', property: 'created_at' },
  { label: 'Updated At', property: 'updated_at' }
])

const items = ref()
const formItem = ref(null)
const formItemTemplate = ref({
  id: null,
  name: null,
  created_at: null,
  updated_at: null
})
const formError = ref(null)

const openModal = () => {
  formItem.value = { ...formItemTemplate.value }
  formError.value = null
  showModal.value = true
}

const editItemClicked = (item) => {
  formItem.value = { ...item }
  formError.value = null
  showModal.value = true
}

const deleteItemClicked = (item) => {
  formItem.value = item
  showDeleteModal.value = true
}

const confirmDelete = async () => {
  await deleteItem(formItem.value.id)
  await getList()
  showDeleteModal.value = false
}

const getList = async () => {
  const response = await get('/item-types')
  if (response.status === 200) {
    items.value = response.data
  }
}

const createItem = async () => {
  const response = await post('/item-types/', formItem.value)
  if (response.errors) {
    formError.value = response.errors
    return
  }
  await getList()
  showModal.value = false
  formError.value = null
}

const updateItem = async () => {
  const response = await put(`/item-types/${formItem.value.id}/`, formItem.value)
  if (response.data) {
    await getList()
    showModal.value = false
  }
}

const saveItem = async () => {
  if (!formItem.value) return
  if (!formItem.value.id) {
    await createItem()
    return
  }
  await updateItem()
}

const deleteItem = async (id) => {
  await del(`/item-types/${id}/`)
}

onMounted(async () => {
  await getList()
})
</script>
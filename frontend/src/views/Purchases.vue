<template>
    <div class="flex flex-wrap gap-8" v-if="items">
        <div class="flex flex-wrap gap-4 w-full justify-between">
            <h1 class="font-bold text-2xl">Purchases</h1>
            <button data-modal-target="crud-modal" data-modal-toggle="crud-modal"
                class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                type="button" @click="openModal()"
                >
                Add
            </button>
        </div>

        <List 
            :headers="headers" 
            :items="inventoryList"
            @edit="e=>editItemClicked(e)"
            @delete="e=>deleteItemClicked(e)"
        />

        <PurchaseForm 
             v-model="formItem"
            :is-visible="showModal"
            :errors="formError"
            :title="formItem?.id ? 'Edit Purchase' : 'Add New Purchase'"
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
import InventoryForm from '@/components/InventoryForm.vue'
import ItemTypesDelete from '@/components/ItemTypesDelete.vue'
import {useApi} from '@/composables/useApi';
import { computed } from 'vue'
import PurchaseForm from '@/components/PurchaseForm.vue';

const {get, post, put, delete: del  } = useApi();

const showModal = ref(false);
const showDeleteModal = ref(false)
const items = ref([])

const headers = ref([
    
    {
        label: 'Description',
        property: 'description'
    },
    {
        label: 'Quantity',
        property: 'quantity'
    },
    {
        label: 'Item',
        property: 'itemVal'
    },
    {
        label: 'Created At',
        property: 'created_at'
    },
    {
        label: 'Updated At',
        property: 'updated_at'
    }
]);

const inventory = ref();
const formItem = ref(null);
const formItemTemplate=ref({
    "id": null,
    "description": null,
    "quantity": null,
    "created_at": null,
    "updated_at": null,
    "item_val": null
});
const formError =  ref(null);

const openModal=()=>{
    formItem.value=formItemTemplate.value;
    formError.value = null;
    showModal.value = true;
}

const editItemClicked=(item)=>{
    formItem.value = item;
        formError.value = null;
        showModal.value = true;
}
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

const getList = async () => {
    const response = await get('/purchases');
    if(response.status === 200){
        inventory.value = response.data;
    }
}
const getItems = async () => {
  const response = await get('/items');
  if (response.status === 200) {
    items.value = response.data;
    console.log(items.value);
  }
}

const inventoryList = computed(() => {
  if (!inventory.value || !items.value) return []

  return inventory.value.map(inv => {
    const type = items.value.find(t => t.id === inv.item)
    return {
      ...inv,
      itemVal: type ? type.name : 'Unknown'
    }
  })
})

const createItem = async () =>{
    const response = await post('/purchases/', formItem.value);
    if(response.errors){
        console.log(response);
        formError.value = response.errors;
        return;
    }

    await getList();

}

const updateItem = async () =>{
    const response = await put(`/purchases/${formItem.value.id}/`, formItem.value);
    if(response.data){
        getList();
    }
}

const saveItem = async () => {
    if(!formItem.value) return;

    if(!formItem.value.id) {
        await createItem();
        return;
    }

    updateItem();
}

const deleteItem = async (id) => {
  await del(`/purchases/${id}/`)
}

onMounted(async ()=>{
    await getList();
    await getItems();
});

</script>


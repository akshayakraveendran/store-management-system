<template>
    <div class="flex flex-wrap gap-8" v-if="items">
        <div class="flex flex-wrap gap-4 w-full justify-between">
            <h1 class="font-bold text-2xl">Inventory</h1>
            <button data-modal-target="crud-modal" data-modal-toggle="crud-modal"
                class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                type="button" @click="openModal()"
                >
                Add
            </button>
        </div>

        <List 
            :headers="headers" 
            :items="items"
            @edit="e=>editItemClicked(e)"
            @delete="e=>deleteItemClicked(e)"
        />

        <InventoryForm 
            v-model="formItem" 
            @submit="saveItem"
            :errors="formError"
        />
        <DeleteConfirm  @delete="deleteItem()"/>
    </div>
</template>

<script setup>
import { onMounted, ref, registerRuntimeCompiler } from 'vue'
import List from '@/components/List.vue'
import ItemsForm from '@/components/ItemsForm.vue'
import InventoryForm from '@/components/InventoryForm.vue'
import DeleteConfirm from '@/components/DeleteConfirm.vue'
import {useApi} from '@/composables/useApi';

const {get, post, put, delete: del  } = useApi();

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
        property: 'item'
    },
    {
        label: 'Created At',
        property: 'createdAt'
    },
    {
        label: 'Updated At',
        property: 'updatedAt'
    }
]);

const items = ref();
const formItem = ref(null);
const formItemTemplate=ref({
    "id": null,
    "description": null,
    "quantity": null,
    "created_at": null,
    "updated_at": null,
    "item": null
});
const formError =  ref(null);

const openModal=()=>{
    formItem.value=formItemTemplate.value;
}

const editItemClicked=(item)=>{
    formItem.value = item;
}

const deleteItemClicked=(item)=>{
    formItem.value = item;
}

const getList = async () => {
    const response = await get('/inventory');
    if(response.status === 200){
        items.value = response.data;
    }
}

const createItem = async () =>{
    const response = await post('/inventory/', formItem.value);
    if(response.errors){
        console.log(response);
        formError.value = response.errors;
        return;
    }

    await getList();

}

const updateItem = async () =>{
    const response = await put(`/inventory/${formItem.value.id}/`, formItem.value);
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

const deleteItem = async () => {
    if(!formItem.value) return;

    const response = await del(`/inventory/${formItem.value.id}/`);
    getList();
}


onMounted(async ()=>{
    await getList();
});

</script>


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
            :items="items"
            @edit="e=>editItemClicked(e)"
            @delete="e=>deleteItemClicked(e)"
        />

        <PurchaseForm 
            v-model="formItem" 
            @submit="saveItem"
            :errors="formError"
        />
        <DeleteConfirm  @delete="deleteItem()"/>s        
    </div>
</template>

<script setup>
import { onMounted, ref, registerRuntimeCompiler } from 'vue'
import List from '@/components/List.vue'
import PurchaseForm from '@/components/PurchaseForm.vue'
import DeleteConfirm from '@/components/DeleteConfirm.vue'
import {useApi} from '@/composables/useApi';

const {get, post, put, delete: del  } = useApi();

const headers = ref([
    {
        label: 'Date',
        property: 'created_at'
    },
    {
        label: 'Total Price',
        property: 'total_price'
    },
    {
        label: 'Tax Amount',
        property: 'tax_amount'
    },
    {
        label: 'Discount',
        property: 'discount_amount'
    },
    {
        label: 'Sub Total',
        property: 'sub_total'
    },
    {
        label: 'Updated At',
        property: 'updated_at'
    }
]);

const items = ref();
const formItem = ref(null);
const formItemTemplate=ref({
        "id": null,
        "total_price": null,
        "discount_amount": null,
        "tax_amount": null,
        "sub_total": null,
        "created_at": null,
        "updated_at": null,
        "shipping": null
    },);
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
    const response = await get('/purchases');
    if(response.status === 200){
        items.value = response.data;
    }
}

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

const deleteItem = async () => {
    if(!formItem.value) return;

    const response = await del(`/purchases/${formItem.value.id}/`);
    getList();
}


onMounted(async ()=>{
    await getList();
});

</script>


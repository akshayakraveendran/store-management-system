<script setup>
import { onMounted, ref } from 'vue'
import List from '@/components/List.vue'
import CrudModal from '@/components/CrudModal.vue'
import DeleteConfirm from '@/components/DeleteConfirm.vue'
import {useApi} from '@/composables/useApi';

const {get} = useApi();

const headers = ref([
    {
        label: 'Name',
        property: 'name'
    },
    {
        label: 'Description',
        property: 'description'
    },
    {
        label: 'Price',
        property: 'price'
    },
    {
        label: 'Item Type',
        property: 'itemType'
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

onMounted(async ()=>{
   items.value = await get('/items');
});

</script>

<template>
    <div class="flex flex-wrap gap-8">
        <div class="flex flex-wrap gap-4 w-full justify-between">
            <h1 class="font-bold text-2xl">Items</h1>
            <button data-modal-target="crud-modal" data-modal-toggle="crud-modal"
                class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                type="button">
                Add
            </button>
        </div>

        <List v-if="items" :headers="headers" :items="items"/>

        <CrudModal/>
        <DeleteConfirm/>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import List from '@/components/List.vue'
import CrudModal from '@/components/CrudModal.vue'
import DeleteConfirm from '@/components/DeleteConfirm.vue'
import {useApi} from '@/composables/useApi';

const {get} = useApi();

const headers = [
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
];

const items = [
    {
        name: 'Lenovo ThinkPad X1',
        description: 'Carbon Fiber',
        itemType: 'Laptop',
        price: '$1450',
        createdAt: '05-01-2024',
        updatedAt: '10-03-2024'
    },
    {
        name: 'Dell UltraSharp Monitor',
        description: '27 inch 4K',
        itemType: 'Monitor',
        price: '$599',
        createdAt: '15-02-2024',
        updatedAt: '18-03-2024'
    },
    {
        name: 'Logitech MX Master 3S',
        description: 'Wireless Mouse',
        itemType: 'Accessories',
        price: '$99',
        createdAt: '01-01-2024',
        updatedAt: '05-01-2024'
    },
    {
        name: 'HP LaserJet Pro',
        description: 'Mono Printer',
        itemType: 'Printer',
        price: '$250',
        createdAt: '22-11-2023',
        updatedAt: '02-12-2023'
    },
    {
        name: 'Apple iPad Air',
        description: '10.9 inch Blue',
        itemType: 'Tablet',
        price: '$699',
        createdAt: '07-06-2024',
        updatedAt: '07-06-2024'
    }
];

onMounted(()=>{
   const i = get('/items/');
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

        <List :headers="headers" :items="items"/>

        <CrudModal/>
        <DeleteConfirm/>
    </div>
</template>

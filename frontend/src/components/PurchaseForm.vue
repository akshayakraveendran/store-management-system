<template>
    <div id="crud-modal" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-md max-h-full">
            <div class="border relative bg-white rounded-lg shadow-sm dark:bg-gray-700" v-if="modelValue">
                <div class="p-4" v-if="errors && errors.length">
                    <div v-for="(error, property) in errors"
                        class="flex items-center p-2 mb-2 text-xs text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400"
                        role="alert">
                        <svg class="shrink-0 inline w-4 h-4 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                            fill="currentColor" viewBox="0 0 20 20">
                            <path
                                d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
                        </svg>
                        <div>
                            <span class="font-medium">{{ error }} </span>
                        </div>
                    </div>
                </div>
                <div
                    class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200">
                    <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                        <span v-if="modelValue.id">Edit Purchase</span>
                        <span v-else>Add New Purchase</span>
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-toggle="crud-modal" @click="$emit('close')">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <form class="p-4 md:p-5" @submit.prevent="handleSubmit">
                    <div class="grid gap-4 mb-4 grid-cols-2">

                        <div class="col-span-2">
                            <label for="total_price"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Total Price</label>
                            <input :value="modelValue.total_price" @input="updateField('name', $event.target.value)"
                                type="number" name="total_price" id="total_price"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Total Price" required="">
                        </div>
                        <div class="col-span-2">
                            <label for="tax_amount"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Tax Amount</label>
                            <input :value="modelValue.tax_amount" @input="updateField('name', $event.target.value)"
                                type="number" name="tax_amount" id="tax_amount"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Tax Amount" required="">
                        </div>
                        <div class="col-span-2">
                            <label for="discount_amount"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Discount
                                Amount</label>
                            <input :value="modelValue.discount_amount" @input="updateField('name', $event.target.value)"
                                type="number" name="discount_amount" id="discount_amount"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Discount Amount" required="">
                        </div>
                    </div>
                    <button
                        class="text-white inline-flex items-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                        @click="addPurchasedItem()">
                        <svg class="me-1 -ms-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
                                clip-rule="evenodd"></path>
                        </svg>
                        Add Item
                    </button>

                    <form class="m-4 p-4 border rounded"  v-for="purchasedItem in purchasedItems">
                        <div class="grid gap-4 mb-4 grid-cols-2">
                            <div class="col-span-2">
                                <label for="item"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Item</label>
                                <select :value="purchasedItem?.id || purchasedItem.item"
                                    @change="handleItemChange($event)" id="item"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    required>
                                    <option value="">Select an item</option>
                                    <template v-for="item in items" :key="item.id">
                                        <option :value="item.id">{{ item.name }}</option>
                                    </template>
                                </select>
                            </div>

                            <div class="col-span-1">
                                <label for="price"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Price</label>
                                <input :value="purchasedItem.price"
                                    @input="updateField('price', parseFloat($event.target.value))" type="number"
                                    name="price" id="price" step="0.01" min="0"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    placeholder="0.00" required>
                            </div>

                            <div class="col-span-1">
                                <label for="quantity"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Quantity</label>
                                <input :value="modelValue.quantity"
                                    @input="updateField('quantity', parseInt($event.target.value))" type="number"
                                    name="quantity" id="quantity" min="1"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                    placeholder="1" required>
                            </div>
                        </div>
                    </form>

                    
                     <button type="submit"
                        class="m-4 text-white inline-flex items-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                        <svg class="me-1 -ms-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
                                clip-rule="evenodd"></path>
                        </svg>
                        Save
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>
<script setup>
import {onMounted, ref, watch} from 'vue';
import {useApi} from '@/composables/useApi';

const emit = defineEmits(['update:modelValue', 'close', 'submit'])

const {get} = useApi();

// Define props for v-model
const props = defineProps({
    modelValue: {
        type: Object,
        required: true,
    },
    errors: {
        type: Array
    }
})

const purchasedItemTemplate = ref({
    item: null,
    price: null,
    quantity: null
});
const purchasedItems = ref([]);
const totalPrice = ref(0);
const items = ref([]);


const updateField = (field, value) => {
    const updatedItem = { ...props.modelValue }
    updatedItem[field] = value
    emit('update:modelValue', updatedItem)
}


const handleSubmit = () => {
    emit('submit', props.modelValue)
}

const addPurchasedItem = () => {
    purchasedItems.value.push(JSON.parse(JSON.stringify(purchasedItemTemplate.value)))
}


const handleItemChange = (event) => {
    const selectedId = parseInt(event.target.value);
    if (selectedId) {
        const selectedItem = items.value.find(item => item.id === selectedId);
        if (selectedItem) {
            updateField('item', selectedItem);
        }
    } else {
        updateField('item', null);
    }
}

const getItems = async () => {
    const response = await get('/items');
    if(response.status === 200){
        items.value = response.data;
    }
}

const getPurchasedItems = async (item) => {
    const response = await get(`/purchased-items/${item.id}`);
    if(response.status === 200){
        purchasedItems.value = response.data;
    }
}


watch(purchasedItems, (newItems) => {
    totalPrice.value = newItems.reduce((total, item) => {
        const price = parseFloat(item.price) || 0;
        const quantity = parseInt(item.quantity) || 0;
        return total + (price * quantity);
    }, 0);
}, { deep: true });

onMounted( async ()=>{

    await getItems();
        modelValue.id ? await getPurchasedItems(modelValue) : addPurchasedItem();

});

</script>
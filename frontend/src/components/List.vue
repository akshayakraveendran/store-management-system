<template>
  <table
            class="border rounded border-gray-500 w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th v-for="(header, key) in headers" :key="key" class="px-6 py-3">
                        {{ header.label }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, key) in items" :key="key"
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200">

                    <td v-for="(header, headerKey) in headers" :key="headerKey" class="px-6 py-4">
                        <span class="text-gray-700 whitespace-nowrap dark:text-white">
                            {{ item[header.property] }}
                        </span>
                    </td>

                    <td>
                        <button type="button" data-modal-target="crud-modal" data-modal-toggle="crud-modal"
                            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-xs px-5 py-2 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
                            Edit
                        </button>
                    </td>
                    <td>
                        <button type="button" data-modal-target="popup-modal" data-modal-toggle="popup-modal"
                            class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-xs px-5 py-2 me-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900">
                            Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
</template>

<script setup>
defineProps({
    headers: {
        type: Array,
        required: true
    },
    items: {
        type: Array,
        required: true
    }
})
</script>
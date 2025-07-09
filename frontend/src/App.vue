<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>

  <div class="grid grid-cols-6 h-full">
    <div class="col-span-1 border p-4">
      <ul
        class="w-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white">
        <li class="w-full px-4 py-2 border-b border-gray-200 rounded-t-lg dark:border-gray-600">
          <RouterLink to="/items">Items</RouterLink>
        </li>
        <li class="w-full px-4 py-2 border-b border-gray-200 dark:border-gray-600">
          <RouterLink to="/itemTypes">Item Types</RouterLink>
        </li>
        <li class="w-full px-4 py-2 border-b border-gray-200 dark:border-gray-600">
          <RouterLink to="/inventory">Inventory</RouterLink>
        </li>
        <li class="w-full px-4 py-2 rounded-b-lg">
          <RouterLink to="/purchases">Purchases</RouterLink>
        </li>
        <li class="w-full px-4 py-2 rounded-b-lg">
          <RouterLink to="/purchasedItems">Purchased Items</RouterLink>
        </li>
        
      </ul>
    </div>
    <div class="col-span-5">
      <div class="p-4 border-b"></div>
      <div class="p-4 h-full">
        <RouterView />
      </div>
    </div>
  </div>

</template>

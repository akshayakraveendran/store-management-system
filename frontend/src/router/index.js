import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Items from '@/views/Items.vue'
import ItemTypes from '@/views/ItemTypes.vue'
import Inventory from '@/views/Inventory.vue'
import Shipping from '@/views/Shipping.vue'
import Purchases from '@/views/Purchases.vue'
import PurchasedItems from '@/views/PurchasedItems.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/items', 
      name: 'items',
      component: Items,

    },
    {
      path: '/itemTypes', 
      name: 'itemTypes',
      component: ItemTypes,

    },
    {
      path: '/inventory', 
      name: 'inventory',
      component: Inventory,

    },
    {
      path: '/shipping', 
      name: 'shipping',
      component: Shipping,

    },
    {
      path: '/purchases', 
      name: 'purchases',
      component: Purchases,

    },
    {
      path: '/purchasedItems', 
      name: 'purchasedItems',
      component: PurchasedItems,

    },
  ],
})

export default router

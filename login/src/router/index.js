import { createRouter, createWebHashHistory } from 'vue-router'
const routes = [
  {
    path: '/',
    name: 'Table',
    component: function () {
          return import(/* webpackChunkName: "Table" */  '../views/Table.vue')
        }
  },
  {
    path: '/Ping',
    name: 'Ping',
    component: function () {
          return import(/* webpackChunkName: "Ping" */  '../views/Ping.vue')
        }
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

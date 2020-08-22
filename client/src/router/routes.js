import MapPage from 'pages/Map.vue';
import FoodMenu from 'components/FoodMenu.vue';

const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'food',
        components: {
          default: MapPage,
          inspector: FoodMenu,
        }
      }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes

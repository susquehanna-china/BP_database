import { createRouter, createWebHistory } from 'vue-router'
import Index from '../views/Index'
import Login from '../views/Login'
import Create from '../views/Create'
import Edit from '../views/Edit'
import Search from "../views/Search"
import Account from '../views/Account'

const routes = [
  {
    path: '/',
    name: '',
    redirect: '/login',
  },
  {
    path: '/index',
    name: 'index',
    component: Index,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/create',
    name: 'create',
    component: Create,
  },
  {
    path: '/edit',
    name: 'edit',
    component: Edit,
  },
  {
    path: '/search',
    name: 'search',
    component: Search,
  },
  {
    path: '/account',
    name: 'account',
    component: Account,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) =>{

  let flag = sessionStorage.getItem("user")
  if (to.name === 'login' && !flag){next()}
  else{
  if (!flag){
    next('/login')
  }
  else {
  next()}}
})

export default router

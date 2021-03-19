import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin: false,
    user: '',
  },
  mutations: {
    login(state, user){
      state.isLogin = true;
      state.user = user;
    }
  },
  actions: {
  },
  modules: {
  }
})

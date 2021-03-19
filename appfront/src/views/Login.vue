<template>
  <a-form
      layout="inline"
      :model="data"
      @finish="handleFinish"
      @finishFailed="handleFinishFailed"
  >
    <a-form-item>
      <a-input v-model:value="data.user" placeholder="Username">
        <template #prefix>
        </template>
      </a-input>
    </a-form-item>
    <br>
    <br>
    <a-form-item>
      <a-input v-model:value="data.password" type="password" placeholder="Password">
        <template #prefix>
        </template>
      </a-input>
    </a-form-item>
    <br>
    <br>
    <a-form-item>
      <a-button
          type="primary"
          html-type="submit"
          :disabled="data.user === '' || data.password === ''"
      >
        Log in
      </a-button>
    </a-form-item>
  </a-form>
  <a-modal v-model:visible="modal.visible" :footer="null">
    <h1>用户名或密码错误！</h1>
  </a-modal>
</template>
<script>

import {reactive} from 'vue';
import router from "@/router";
import axios from 'axios';

export default {
  name: 'Login',
  setup() {
    const data = reactive({
      user: '',
      password: '',
    });
    const modal = reactive({
      visible: false,
    })

    const handleFinish = () => {

      let send_data = {
        'user': data.user,
        'passwd': data.password
      }
      let pass = 0
      axios.post("http://127.0.0.1:8000/project/login_api/", send_data).then((res) => {
        pass = res.data
        if (pass === 1||pass === 2) {
          sessionStorage.setItem("user", data.user)
          //store.commit('login', data.user)
          sessionStorage.setItem('authority', pass)
          router.push('/index')
        } else {
          data.user=''
          data.password=''
          modal.visible=true
          router.push('/')
        }
      })

    };

    const handleFinishFailed = errors => {
      console.log(errors);
    };

    return {
      data,
      modal,
      handleFinish,
      handleFinishFailed,
    };
  },

};
</script>
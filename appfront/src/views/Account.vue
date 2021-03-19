<template>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4"><h3>UserName</h3></a-col>
    <a-col :span="4"><h3>{{account.user}}</h3></a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4"><h3>Old Password</h3></a-col>
    <a-col :span="4"><a-input v-model:value='account.old_password'/></a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4"><h3>New Password</h3></a-col>
    <a-col :span="4"><a-input v-model:value='account.new_password'/></a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <a-row style="padding-top: 1vh">
    <a-col :span="10"></a-col>
    <a-col :span="2">
      <a-button @click="change_confirm">Change</a-button>
    </a-col>
    <a-col :span="2">
      <a-button @click="home">
        Cancel
      </a-button>
    </a-col>
    <a-col :span="10"></a-col>
  </a-row>
  <a-modal v-model:visible="visible.change" :centered="true" @ok="change">
    是否确认修改密码？
  </a-modal>
  <a-modal v-model:visible="visible.cancel" :centered="true" @ok="home">
    是否返回首页？
  </a-modal>
  <a-modal v-model:visible="visible.success" :centered="true" @ok="home">
    密码修改成功！
  </a-modal>
  <a-modal v-model:visible="visible.fail" :centered="true" @ok="close">
    密码修改失败！
  </a-modal>
</template>

<script>
import {reactive} from 'vue'
import axios from "axios";
import router from "@/router";
export default {
  name: 'Account',
  setup() {
    let account = reactive({
      user: sessionStorage.getItem('user'),
      old_password: '',
      new_password: '',
    })
    let visible = reactive({
      change: false,
      cancel: false,
      success: false,
      fail: false,
    })
    const change_confirm = () => {
      visible.change = true
    }
    const change = () =>{
      let form_data = new FormData();
      form_data.append('user', account.user)
      form_data.append('old_password', account.old_password)
      form_data.append('new_password', account.new_password)
      axios({
        url: 'http://127.0.0.1:8000/project/changepasswd/',
        method: 'post',
        data: form_data,
        headers: {'Content-Type': 'multipart/form-data'},
      }).then((res)=>{
        visible.change = false
        if(res.data === 1){visible.success = true}
        else{visible.fail = true}
      })
    }
    const home = () => {
      router.push('/index')
    }
    const close = () => {
      visible.fail = false
    }
    return {account, visible, change, change_confirm, home, close}
  }
}

</script>
<style scoped>
h1{
  text-align: left;
}
</style>
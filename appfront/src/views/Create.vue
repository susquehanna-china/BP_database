<template>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4">
      <h2>Investment Manager</h2>
    </a-col>
    <a-col :span="4">
      <a-input v-model:value="project.submitter" :disabled=true style="width: 500px"/>
    </a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4">
      <h2>Company Name</h2>
    </a-col>
    <a-col :span="4">
      <a-input v-model:value="project.name" style="width: 500px"/>
    </a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4">
      <h2>FA</h2>
    </a-col>
    <a-col :span="4">
      <a-input v-model:value="project.FA" style="width: 500px"/>
    </a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4">
      <h2>Category</h2>
    </a-col>
    <a-col :span="4">
      <a-select v-model:value="project.category" style="width: 500px">
        <a-select-option value="Blockchain">Blockchain</a-select-option>
        <a-select-option value="Consumer_product&service">Consumer_product&service</a-select-option>
        <a-select-option value="Content">Content</a-select-option>
        <a-select-option value="BEnterprise_service">Enterprise_service</a-select-option>
        <a-select-option value="E_commerce">E_commerce</a-select-option>
        <a-select-option value="Industrial_internet">Industrial_internet</a-select-option>
        <a-select-option value="FinTech">FinTech</a-select-option>
        <a-select-option value="Core_tech">Core_tech</a-select-option>
        <a-select-option value="Social_media">Social_media</a-select-option>
        <a-select-option value="Education">Education</a-select-option>
        <a-select-option value="Travel_accommodation_tourism">Travel_accommodation_tourism</a-select-option>
        <a-select-option value="Healthcare">Healthcare</a-select-option>
        <a-select-option value="Unclassified">Unclassified</a-select-option>
      </a-select>
    </a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4">
      <h2>Summary</h2>
    </a-col>
    <a-col :span="4">
      <a-textarea v-model:value="project.summary" autoSize style="width: 500px"/>
    </a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4">
      <h2>BP</h2>
    </a-col>
    <a-col :span="4">
      <input type="file" id="BP">
    </a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <a-row>
    <a-col :span="8"></a-col>
    <a-col :span="4">
      <h2>Datapack</h2>
    </a-col>
    <a-col :span="4">
      <input type="file" id="datapack">
    </a-col>
    <a-col :span="8"></a-col>
  </a-row>
  <br>
  <br>
  <a-row>
    <a-col :span="10"></a-col>
    <a-col :span="2">
      <a-button type="primary" @click="confirm_modal">submit</a-button>
    </a-col>
    <a-col :span="2">
      <a-button type="primary" @click="leave">cancel</a-button>
    </a-col>
    <a-col :span="10"></a-col>

  </a-row>
  <a-modal v-model:visible="confirm.visible" @ok="commit" :centered="true">
    <h2>是否确认提交？</h2>
  </a-modal>
  <a-modal v-model:visible="exit.visible" @ok="home" :centered="true">
    <h2>是否离开当前页面？</h2>
  </a-modal>
</template>

<script>
import {reactive} from 'vue'
import axios from "axios";
import router from "@/router";

export default {
  name: 'Create',
  setup() {
    let project = reactive({
      submitter: sessionStorage.getItem('user'),
      name: '',
      FA: '',
      category: '',
      summary: '',
    })
    let confirm = reactive({
      visible: false,
    })
    let exit = reactive({
      visible: false,
    })
    const confirm_modal = () => {
      confirm.visible = true
    }
    const commit = () => {
      let form_data = new FormData();
      form_data.append('submitter', project.submitter)
      form_data.append('name', project.name)
      form_data.append('FA', project.FA)
      form_data.append('category', project.category)
      form_data.append('summary', project.summary)
      form_data.append('file_BP', document.getElementById('BP').files[0])
      form_data.append('file_datapack', document.getElementById('datapack').files[0])
      axios({
        url: 'http://127.0.0.1:8000/project/create/',
        method: 'post',
        data: form_data,
        headers: {'Content-Type': 'multipart/form-data'},
      }).then(router.push('/index'))
    }
    const home = () => {
      router.push('/index')
    }
    const leave = () => {
      exit.visible = true
    }

    return {project, commit, confirm, confirm_modal, home, exit, leave}
  }
}
</script>
<style scoped>
h2 {
  text-align: left;
}

</style>




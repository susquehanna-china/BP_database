<template>
  <a-input-search v-model:value="search.value" enter-button style=" width: 50vw" @search="onsearch"/>
  <a-button @click="clear_search">clear</a-button>
  <a-card style="width: 60vw; margin-left: 20vw;margin-top: 2vh; background: lightskyblue">
    <a-row>
      <a-col :span="6">Investment Manager</a-col>
      <a-col :span="6">Company Name</a-col>
      <a-col :span="6">FA</a-col>
      <a-col :span="6">Category</a-col>
    </a-row>
  </a-card>
  <div v-for="(item, index) in search.result" :key="index">
    <a-card :bordered=true :hoverable=true style="width: 60vw; margin-left: 20vw"
            @click="showmodal(item)">
      <a-row>
        <a-col :span="6">{{ item['submitter'] }}</a-col>
        <a-col :span="6">{{ item['name'] }}</a-col>
        <a-col :span="6">{{ item['FA'] }}</a-col>
        <a-col :span="6">{{ item['category'] }}</a-col>
      </a-row>
    </a-card>

  </div>
  <a-modal :visible="modal.visible_mine" @cancel="closemodal" @ok="save" width="80vw">
    <h1>Investment Manager</h1>
    <a-input v-model:value="project.submitter" :disabled=true style="width: 20vw"/>
    <h1>project name</h1>
    <a-input v-model:value="project.name" style="width: 40vw"/>
    <h1>FA</h1>
    <a-input v-model:value="project.FA" style="width: 40vw"/>
    <h1>category</h1>
    <a-select v-model:value="project.category" style="width: 500px">
      <a-select-option value="Blockchain">Blockchain</a-select-option>
      <a-select-option value="Consumer_product&service">Consumer_product&service</a-select-option>
      <a-select-option value="Content">Content</a-select-option>
      <a-select-option value="BEnterprise_service">Enterprise_service</a-select-option>
      <a-select-option value="E-commerce">E-commerce</a-select-option>
      <a-select-option value="Industrial_internet">Industrial_internet</a-select-option>
      <a-select-option value="FinTech">FinTech</a-select-option>
      <a-select-option value="Core_tech">Core_tech</a-select-option>
      <a-select-option value="Social_media">Social_media</a-select-option>
      <a-select-option value="Education">Education</a-select-option>
      <a-select-option value="Travel_accommodation_tourism">Travel_accommodation_tourism</a-select-option>
      <a-select-option value="Healthcare">Healthcare</a-select-option>
      <a-select-option value="Unclassified">Unclassified</a-select-option>
    </a-select>
    <h1>summary</h1>
    <a-textarea v-model:value="project.summary" autoSize style="width: 60vw"/>
    <h1>BP</h1>
    <h3>{{ project.file_BP }}</h3>
    <a-button type="primary" @click="download('BP', project.file_BP)">Download</a-button>
    <input type="file" id="BP">
    <h1>Datapack</h1>
    <h3>{{ project.file_datapack }}</h3>
    <a-button type="primary" @click="download('datapack', project.file_datapack)">Download</a-button>
    <input type="file" id="datapack">
  </a-modal>
  <a-modal :visible="modal.visible" @cancel="closemodal" @ok="closemodal" width="80vw">
    <h1>Investment Manager</h1>
    <a-input v-model:value="project.submitter" :disabled=true style="width: 20vw"/>
    <h1>project name</h1>
    <a-input v-model:value="project.name" :disabled=true style="width: 40vw"/>
    <h1>FA</h1>
    <a-input v-model:value="project.FA" :disabled=true style="width: 40vw"/>
    <h1>category</h1>
    <a-select v-model:value="project.category" :disabled=true style="width: 500px">
    </a-select>
    <h1>summary</h1>
    <a-textarea v-model:value="project.summary" :disabled=true autoSize style="width: 60vw"/>
    <h1>BP</h1>
    <h3>{{ project.file_BP }}</h3>
    <a-button type="primary" @click="download('BP', project.file_BP)">Download</a-button>
    <h1>Datapack</h1>
    <h3>{{ project.file_datapack }}</h3>
    <a-button type="primary" @click="download('datapack', project.file_datapack)">Download</a-button>
  </a-modal>
</template>

<script>
import {reactive, onMounted} from 'vue'
import axios from "axios";

export default {
  name: 'Search',
  setup() {
    let search = reactive({
      value: '',
      result: [],
    })
    let project = reactive({
      id: '',
      submitter: '',
      name: '',
      FA: '',
      category: '',
      summary: '',
      file_BP: '无',
      file_datapack: '无',
    })
    let modal = reactive({
      visible_mine: false,
      visible: false
    })
    const clear = () => {
      project.id = ''
      project.submitter = ''
      project.name = ''
      project.FA = ''
      project.category = ''
      project.summary = ''
      project.file_BP = '无'
      project.file_datapack = '无'
    }
    const clear_search = () => {
      search.value = ''
      onsearch()
    }
    const showmodal = (item) => {
      clear()
      project.id = item['id']
      project.name = item['name']
      project.category = item['category']
      project.submitter = item['submitter']
      project.FA = item['FA']
      project.summary = item['summary']
      if (item['file_BP'] !== null) {
        project.file_BP = item['file_BP'].substring(10)
      }

      if (item['file_datapack'] !== null) {
        project.file_datapack = item['file_datapack'].substring(16)
      }
      if (sessionStorage.getItem('user') === project.submitter) {
        modal.visible_mine = true
      } else {
        modal.visible = true
      }
    }
    const closemodal = () => {
      modal.visible_mine = false
      modal.visible = false
    }
    const save = () => {
      let form_data = new FormData();
      form_data.append('id', project.id)
      form_data.append('submitter', project.submitter)
      form_data.append('name', project.name)
      form_data.append('FA', project.FA)
      form_data.append('category', project.category)
      form_data.append('summary', project.summary)
      if (document.getElementById('BP').files.length > 0) {
        form_data.append('file_BP', document.getElementById('BP').files[0])
      }

      if (document.getElementById('datapack').files.length > 0) {
        form_data.append('file_datapack', document.getElementById('datapack').files[0])
      }
      axios({
        url: 'http://127.0.0.1:8000/project/edit/',
        method: 'post',
        data: form_data,
        headers: {'Content-Type': 'multipart/form-data'},
      })
      modal.visible_mine = false
      location.reload()
    }

    const download = (type, file) => {
      const path = 'http://127.0.0.1:8000/media/' + type + '/' + file
      window.open(path)
    }

    const onsearch = () => {
      axios.post('http://127.0.0.1:8000/project/search/', {'value': search.value})
          .then((res) => {
            search.result = []
            for (let i = 0; i < res.data.length; i++) {
              search.result.push(res.data[i])
            }
          })
    }

    onMounted(() => {
      axios.get('http://127.0.0.1:8000/project/default/')
          .then((res) => {
            search.result = []
            for (let i = 0; i < res.data.length; i++) {
              search.result.push(res.data[i])
            }
          })
    })


    return {search, onsearch, showmodal, download, closemodal, modal, project, save, clear_search}
  }
}

</script>
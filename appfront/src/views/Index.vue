<template>
  <h1> Hello {{ info.user }}</h1>
  <a-row style="margin-top: 5vh">
    <a-col :span="3"></a-col>

    <a-col :span="6">
      <router-link to="/create">
        <PlusCircleTwoTone :style="{fontSize: '6vh'}"/>
        <br>
        <h1>Create New Project</h1>
      </router-link>
    </a-col>

    <a-col :span="6">
      <router-link to="/edit">
        <EditTwoTone :style="{fontSize: '6vh'}"/>
        <br>
        <h1>Edit My Projects</h1>
      </router-link>
    </a-col>

    <a-col :span="6">
      <div @click.prevent="check">

          <SearchOutlined :style="{fontSize: '6vh', color: 'blue'}"/>
          <br>
          <h1>View All Projects</h1>

      </div>
    </a-col>
    <a-col :span="3"></a-col>
  </a-row>
  <a-modal v-model:visible="visible.warning" :centered=true @ok="close">
    无权限！
  </a-modal>

</template>

<script>
import {PlusCircleTwoTone, EditTwoTone, SearchOutlined} from '@ant-design/icons-vue'
import {reactive} from 'vue'
import router from "@/router";


export default {
  name: 'Index',
  components: {
    PlusCircleTwoTone,
    EditTwoTone,
    SearchOutlined,
  },
  setup() {
    const info = reactive({
      user: sessionStorage.getItem('user')
    })
    const visible = reactive({
      warning: false
    })
    const check = () => {
      if (sessionStorage.getItem("authority") === '1') {
        visible.warning = true
      } else {
        router.push('/search')
      }
    }
    const close = () => {
      visible.warning = false
    }

    return {info, check, close, visible}

  }
}
</script>

<style>

</style>
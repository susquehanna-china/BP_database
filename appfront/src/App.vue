<template>
  <a-row>
    <a-col :span="6">
    </a-col>
    <a-col :span="12">
      <router-link to="/index">
        <img src="./assets/logo.jpg" style="margin-top:6vh;margin-bottom: 12vh; width: 15vw">
      </router-link>
    </a-col>
    <a-col :span="2">
      <router-link to="/index">
        <home-two-tone style="font-size: 5vh;margin-top: 6vh"/>
        <h2>Home</h2>
      </router-link>
    </a-col>
    <a-col :span="4">
      <router-link to="/account">
        <profile-two-tone style="font-size: 5vh;margin-top: 6vh"/>
        <h2>My Account</h2>
      </router-link>
    </a-col>
  </a-row>
  <br>
  <router-view/>
</template>
<script>
import {HomeTwoTone, ProfileTwoTone} from '@ant-design/icons-vue'

export default {
  name: 'app',
  components: {
    HomeTwoTone,
    ProfileTwoTone,
  }
}
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


</style>

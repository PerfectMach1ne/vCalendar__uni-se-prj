<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<script>
export default {
  methods: {
    goToHome() {
      this.$router.push('/');
    }
  }
}
</script>

<template>
  <!-- 
    Keeping this for <img> with assets/ usage reference.
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
  -->
  <header>
    <img @click="goToHome" src="@/assets/logo.png" alt="vCalendar logo" class="logo" width="80" height="80"/>
    <nav> <!-- do NOT mistake this with "Navbar" as in component NavbarContainer and all related components -->
      <RouterLink to="/" class="router">Home</RouterLink>
      <RouterLink to="/tasks" class="router">Tasks</RouterLink>
      <RouterLink to="/about" class="router">About</RouterLink>
    </nav>
  </header>
  <div class="wrapper">
    <!-- <HelloWorld msg="You did it!" /> -->
    <RouterView />
  </div>
  <footer>
    <p>Helo this is the footer</p>
    <p>April 2023</p>
  </footer>
</template>

<style scoped>
header {
  display: inline-flex;
  justify-content: flex-start;
  align-items: center;
}

footer {
  display: inline-flex;
  justify-content: flex-start;
  align-items: center;
  height: 2vh;
  gap: 20px;
}

img:hover {
  cursor: pointer;
}

.router {
  margin: 5px;
  border: 1px solid gray;
  padding: 10px;
}
</style>

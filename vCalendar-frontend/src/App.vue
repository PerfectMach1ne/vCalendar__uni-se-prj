<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<script>
export default {
  methods: {
    goToHome() {
      this.$router.push('/');
    },
    goToTasks() {
      this.$router.push('/tasks');
    },
    goToAbout() {
      this.$router.push('/about');
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
      <button @click="goToHome" class="router">Home</button>
      <button @click="goToTasks" class="router">Tasks</button>
      <button @click="goToAbout" class="router">About</button>
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
  margin: 10px;
  border: 1px solid gray;
  padding: 10px 20px;
  border: none;
  border-radius: 12px;
  background-color: indianred;
  font-size: 1.2rem;
  color: #fff;
}

.router:hover {
  background-color: tomato;
  transition: all 0.3s ease;
}

.router:not(:hover) {
  transition: all 0.3s ease;
}
</style>

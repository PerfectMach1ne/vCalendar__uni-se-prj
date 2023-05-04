<script>
import NavbarContainer from '../components/containers/NavbarContainer.vue';
import ToolsContainer from '../components/containers/ToolsContainer.vue';
import CalendarContainer from '../components/containers/CalendarContainer.vue';

export default {
  components: {
    NavbarContainer,
    ToolsContainer,
    CalendarContainer
  }
}
</script>

<template>
  <main>
    <NavbarContainer class="nav__isolator"/>
    <div class="home">
      <ToolsContainer/>
      <CalendarContainer/>
    </div>
  </main>
</template>

<style scoped>
.home {
  display: flex;
}

.nav__isolator {
  display: flex;
  /* align-items: stretch; */
/* 
  .home {
    min-height: 75vh; /* 75% viewport height */ /*
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
  } */
}
</style>

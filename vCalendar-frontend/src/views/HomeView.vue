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
    <div class="home">
      <NavbarContainer/>
      <ToolsContainer/>
      <CalendarContainer/>
    </div>
  </main>
</template>

<style scoped>
@media (min-width: 1024px) {
  .home {
    min-height: 75vh; /* 75% viewport height */
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
  }
}
</style>

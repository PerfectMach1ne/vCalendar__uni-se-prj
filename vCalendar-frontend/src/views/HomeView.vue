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
    <NavbarContainer/>
    <ToolsContainer/>
    <CalendarContainer/>
    <p>a</p>
  </main>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

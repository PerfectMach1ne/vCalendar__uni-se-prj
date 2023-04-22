<script>
import NavbarContainer from '../components/containers/NavbarContainer.vue';
import ToolsContainer from '../components/containers/ToolsContainer.vue';
import AboutPage from '../components/AboutPage.vue';

export default {
  components: {
    NavbarContainer,
    ToolsContainer,
    AboutPage
  }
}
</script>

<template>
  <div class="about">
    <NavbarContainer/>
    <ToolsContainer/>
    <AboutPage/>
  </div>
  <p>AboutView</p>
</template>

<style scoped>
@media (min-width: 1024px) {
  .about {
    min-height: 75vh; /* 75% viewport height */
    display: flex;
    /* flex-direction: row; */
    align-items: center;
  }
}
</style>

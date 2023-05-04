<script>
import NavbarContainer from '../components/containers/NavbarContainer.vue';
import ToolsContainer from '../components/containers/ToolsContainer.vue';
import AboutPage from '../components/pages/AboutPage.vue';

export default {
  components: {
    NavbarContainer,
    ToolsContainer,
    AboutPage
  }
}
</script>

<template>
  <NavbarContainer class="nav__isolator"/>
  <div class="about">
    <ToolsContainer/>
    <AboutPage/>
  </div>
</template>

<style scoped>
.about {
  display: flex;
}

.nav__isolator {
  display: flex;
}
</style>

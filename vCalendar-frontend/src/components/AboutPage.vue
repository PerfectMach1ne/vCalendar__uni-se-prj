<script>
export default {

}
</script>

<template>
  <div class="about__page__container">
    <h1>
      Don't delete this just yet. Could be used for a nice little About page with
      a GitHub repo link and all the technologies listed nicely (just because it'd look cool).
    </h1>
    <p>AboutPage</p>
  </div>
</template>

<style scoped>
.about__page__container {
  margin: 5px;
  border: 1px solid gray;
  padding: 5px;
  width: calc(100vw - 238px - 70px); /* 238px = ToolsContainer width */
  /* 70px is the widest AboutPage can be without being "sent downstairs";
     it's aligned pixel-to-pixel with NavbarContainer */
}
</style>

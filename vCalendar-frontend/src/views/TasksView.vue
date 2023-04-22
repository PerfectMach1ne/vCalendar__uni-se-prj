<script>
import TaskPage from '../components/TaskPage.vue';

export default {
  components: {
    TaskPage
  }
}
</script>

<template>
  <div class="tasks">
    <TaskPage/>
  </div>
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

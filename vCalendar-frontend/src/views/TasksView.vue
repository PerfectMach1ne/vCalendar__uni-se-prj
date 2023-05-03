<script>
import TaskPage from '../components/pages/TaskPage.vue';

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
  .tasks {
    margin: 5px;
    border: 1px solid gray;
    padding: 5px;
    min-height: 79vh;
  }
}
</style>

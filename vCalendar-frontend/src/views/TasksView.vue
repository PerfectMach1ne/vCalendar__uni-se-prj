<script>
import TaskContainer from '../components/containers/TaskContainer.vue';

export default {
  components: {
    TaskContainer
  }
}
</script>

<template>
  <div class="tasks">
    <TaskContainer/>
  </div>
</template>

<style scoped>

.tasks {
  margin: 5px;
  border: 1px solid gray;
  padding: 5px;
  min-height: 79vh;
}

</style>

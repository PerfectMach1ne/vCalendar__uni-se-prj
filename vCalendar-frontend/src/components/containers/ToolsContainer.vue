<script>
export default {

}
</script>

<template>
  <div class="tools__container">
    <p>ToolsContainer</p>
  </div>
</template>

<style scoped>
.tools__container {
  margin: 5px;
  border: 1px solid gray;
  padding: 5px;
  width: 238px; /* any more and flexbox sends CalendarContainer downstairs */
  height: calc(57vh - 1vh); /* same as above */
}
</style>

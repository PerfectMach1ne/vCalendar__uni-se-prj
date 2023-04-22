<script>
import BigCalendar from '../BigCalendar.vue';

export default {
  components: {
    BigCalendar
  }
}
</script>

<template>
  <div class="calendar__container">
    <p>CalendarContainer</p>
    <BigCalendar/>
  </div>
</template>

<style scoped>
.calendar__container {
  margin: 5px;
  border: 1px solid gray;
  padding: 5px;
  width: 80vw;
}
</style>

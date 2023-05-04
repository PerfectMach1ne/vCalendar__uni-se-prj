<script>
import BigCalendar from '../BigCalendar.vue';

export default {
  components: {
    BigCalendar
  }
}
</script>

<template>
  <div class="calendar__container scrollbar-vertical">
    <BigCalendar/>
  </div>
</template>

<style scoped>
.calendar__container {
  margin: 5px;
  border: 1px solid gray;
  max-height: 56vh;
  width: 85%
}
/* .calendar__container {
  margin: 5px;
  border: 1px solid gray;
  width: 79.55vw;
  max-height: 57.5vh;
} */
</style>

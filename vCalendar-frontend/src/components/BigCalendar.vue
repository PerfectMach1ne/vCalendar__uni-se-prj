<script>
export default {
  data() {
    return { }
  },
  computed: {
    weekdayArray() {
      return ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
    }
  }
}
</script>

<template>
  <div class="wrapper__big__calendar">
    <ul class="weekday__box">
      <li class="filler__cell"></li>
      <li v-for="i in 7" class="weekday__label">
        <p>
          {{ weekdayArray[i - 1] }}
        </p>
      </li>
    </ul>
    <div class="calendar__with__hours">
      <div v-for="i in 24" v-bind:id="`${String(i - 1).padStart(2, '0') + ':00'}`" class="calendar__hour__row">
        <div class="hour__box">
          {{ String(i - 1).padStart(2, '0') + ':00' }}
        </div>
        <div v-for="j in 7" v-bind:id="`${weekdayArray[j - 1].substring(0,3)}${i - 1}`" class="hour__row__day">
          <!-- This is a hour grid box -->
        </div>
      </div>
    </div>
  </div>
</template>

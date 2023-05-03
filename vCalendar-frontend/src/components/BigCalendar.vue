<script>
export default {
  data() {
    return {

    }
  },
  computed: {
    weekdayArray() {
      return ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
    }
  }
}
</script>

<template>
  test
  <ul class="weekday__labels">
    <li v-for="i in 7" class="weekday__singular__label">
      {{ weekdayArray[i - 1] }}
    </li>
  </ul>
  <ul class="hours__labels">
    <li v-for="i in 24" class="hours__singular__label">
      {{ String(i).padStart(2, '0') + ':00' }}
    </li>
  </ul>
</template>

<style>
.hours__labels {
  list-style-type: none;
  padding: 0;
}

.hours__singular__label {
  border: 1px solid gray;
  width: fit-content;
  padding: 30px;
}

.weekday__labels {
  list-style-type: none;
  padding: 0;
}

.weekday__singular__label {
  border: 1px solid gray;
  width: fit-content;
  padding: 30px;
}
</style>

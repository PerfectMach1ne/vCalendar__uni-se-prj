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
  <ul class="weekday__labels">
    <li v-for="i in 7" class="weekday__singular__label">
      <p :style="{ 'z-index': 1 }">
        {{ weekdayArray[i - 1] }}
      </p>
    </li>
  </ul>
  <ul class="hours__labels">
    <li v-for="i in 23" class="hours__singular__label">
      <p :style="{ 'z-index': 1 }">
        {{ String(i - 1).padStart(2, '0') + ':00' }}
      </p>
    </li>
    <li :style="{ 
      border: '1px',
      'border-color': 'lightgray',
      'border-style': 'solid solid solid none',
      width: 'fit-content',
      'padding': '30px',
      'z-index': 0
     }">
      <p :style="{ 'z-index': 1 }">
        {{ String(23).padStart(2, '0') + ':00' }}
      </p>
    </li>
  </ul>
  <table id="7daycal">
    <tr v-for="i in 25" v-bind:id="`${i == 1 ? 'weekday-labels' : String(i - 2).padStart(2, '0') + ':00'}`">
      <div v-if="i - 1 == 0" class="table__day__labels">
        <th id="mon-label">mon</th>
        <th id="tue-label">tue</th>
        <th id="wed-label">wed</th>
        <th id="thu-label">thu</th>
        <th id="fri-label">fri</th>
        <th id="sat-label">sat</th>
        <th id="sun-label ">sun</th>
      </div>
      <div v-else>
        <th :id="`mon${i - 2}`">[]</th>
        <th :id="`tue${i - 2}`">[]</th>
        <th :id="`wed${i - 2}`">[]</th>
        <th :id="`thu${i - 2}`">[]</th>
        <th :id="`fri${i - 2}`">[]</th>
        <th :id="`sat${i - 2}`">[]</th>
        <th :id="`sun${i - 2}`">[]</th>
      </div>
    </tr>
  </table>
</template>

<style>
table, th {
  border: 1px solid lightgray;
  border-collapse: collapse;
  z-index: 0;
}

th {
  padding: 60px 50px;
}

.table__day__labels {
  /* font-family: 'Fira Sans', sans-serif; */
  font-variant-caps: small-caps;
}

.weekday__labels {
  list-style-type: none;
  padding: 0;
  z-index: 1;
}

.weekday__singular__label {
  border: 1px solid lightgray;
  width: fit-content;
  padding: 28px;
  z-index: 1;
  max-height: 90px;
  /* min-width: 75px; */
}

.hours__labels {
  list-style-type: none;
  padding: 0;
  z-index: 1;
}

.hours__singular__label {
  border: 1px;
  border-color: lightgray;
  border-style: solid solid none none;
  width: fit-content;
  padding: 30px;
  z-index: 1;
}
</style>

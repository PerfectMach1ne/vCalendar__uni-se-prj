<script>
import ChangeWeek from './buttons/ChangeWeek.vue'

export default {
  components: { ChangeWeek },
  data() {
    return {
      weekdayBoxWidth: '',
      currentDate: new Date(),
      currentWeek: 18, // throwaway default value
      currentMonths: 'Aug - Sep', // throwaway default value
      currentFirstWeekday: 0,
      currentLastWeekday: 0,
      currentYear: 2020, // throwaway default value
      left: "&#10094;",
      right: "&#10095;"
    }
  },
  computed: {
    weekdayArray() {
      return ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
    },
    monthNames() {
      return ["January", "February", "March", "April", "May", "June", "July", "August", "September",
       "October", "November", "December"];
    }
  },
  methods: {
    getTodaysWeek() {
      var currentDate = this.currentDate;
      
      var startYearDate = new Date(currentDate.getFullYear(), 0, 1); // get 1st January of today's year
      var daysInYear = Math.floor( (currentDate - startYearDate) / (24 * 60 * 60 * 1000) ); // count year days passed so far
      var weekNumeral = Math.round(daysInYear / 7) + 1; // evaluate the number of the week from all days in year

      return weekNumeral;
    },
    getTodaysMonths() {
      var currentDate = this.currentDate;

      // (current day) - (how many days of the week have already "taken place") + 1 correction day
      var firstWeekdayMonth = currentDate.getMonth(); // evaluate month at first day of the week
      // called "firstMonthDay" and not "firstWeekDay" because it's a day numeral in relation to the month;
      // probably done by me to avoid confusion with "weekdays" which should range from 1 to 7 
      var firstMonthDay = currentDate.getDate() - currentDate.getDay() + 1; // evaluate the first day of today's week
      var lastWeekdayMonth = new Date(currentDate.getFullYear(), currentDate.getMonth(), firstMonthDay + 6).getMonth(); // evaluate month at last day of the week

      if (firstWeekdayMonth == lastWeekdayMonth)
        return this.monthNames[firstWeekdayMonth];
      else
        return this.monthNames[firstWeekdayMonth] + ' - ' + this.monthNames[lastWeekdayMonth];
    },
    getFirstWeekday() {
      var currentDate = this.currentDate;
      var firstMonthDay = currentDate.getDate() - currentDate.getDay() + 1;
      
      // (current day) - (how many days of the week have already "taken place") + 1 correction day
      // var firstMonthDay = currentDate.getDate() - currentDate.getDay() + 1; // evaluate the first day of today's week
      
      return firstMonthDay;
    },
    getLastWeekday() {
      var currentDate = this.currentDate;
      var firstMonthDay = this.currentFirstWeekday;
      var lastMonthDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), firstMonthDay + 6).getDate(); // evaluate the last day of today's week

      return lastMonthDay;
    },
    getTodaysYear() {
      var currentDate = this.currentDate;

      return currentDate.getFullYear();
    },
    getWeekSpecificDateFoolproof(dayOffset) {
      var currentDate = this.currentDate; // get current date

      var firstMonthDay = currentDate.getDate() - currentDate.getDay() + 1; // evaluate the first day of today's week
      var returnDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), firstMonthDay + dayOffset).getDate();

      return returnDate;
    },
    // ChangeWeek.vue events
    goToPastWeek() {
      var currentDate = this.currentDate;
      var firstMonthDay = currentDate.getDate() - currentDate.getDay() + 1; // evaluate the first day of today's week
      currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), firstMonthDay - 7); // get destination date (1st day of past week)
      this.currentDate = currentDate;
      // var currentDate = new Date(); // get current date
      // var firstMonthDay = currentDate.getDate() - currentDate.getDay() + 1; // evaluate the first day of today's week
      // var gotoDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), firstMonthDay - 7); // get destination date (1st day of week)
      this.currentMonths = this.getTodaysMonths();
      this.currentFirstWeekday = this.getFirstWeekday();
      this.currentLastWeekday = this.getLastWeekday();
      this.currentYear = this.getTodaysYear();
      this.currentWeek = this.getTodaysWeek();

      // silly print testing
      console.log(this.currentWeek + ', ' + this.currentMonths + ', ' + this.currentFirstWeekday + ', ' + this.currentLastWeekday + ', ' + this.currentYear)
    },
    goToFutureWeek() {
      var currentDate = this.currentDate;
      var firstMonthDay = currentDate.getDate() - currentDate.getDay() + 1; // evaluate the first day of today's week
      currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), firstMonthDay + 7); // get destination date (1st day of future week)
      this.currentDate = currentDate;
      // var currentDate = new Date(); // get current date
      // var firstMonthDay = currentDate.getDate() - currentDate.getDay() + 1; // evaluate the first day of today's week
      // var gotoDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), firstMonthDay + 7); // get destination date (1st day of week)
      this.currentMonths = this.getTodaysMonths();
      this.currentFirstWeekday = this.getFirstWeekday();
      this.currentLastWeekday = this.getLastWeekday();
      this.currentYear = this.getTodaysYear();
      this.currentWeek = this.getTodaysWeek();

      // silly print testing
      console.log(this.currentWeek + ', ' + this.currentMonths + ', ' + this.currentFirstWeekday + ', ' + this.currentLastWeekday + ', ' + this.currentYear)
    }
  },
  mounted() {
    // Load the current data
    this.currentMonths = this.getTodaysMonths();
    this.currentFirstWeekday = this.getFirstWeekday();
    this.currentLastWeekday = this.getLastWeekday();
    this.currentYear = this.getTodaysYear();
    this.currentWeek = this.getTodaysWeek();

    // silly print testing
    console.log(this.currentWeek + ', ' + this.currentMonths + ', ' + this.currentFirstWeekday + ', ' + this.currentLastWeekday + ', ' + this.currentYear)
    
    // Easy fix for yearmonth__display class element being sized correctly - steal weekday__box's width after render. >:)
    this.weekdayBoxWidth = document.getElementById('weekdaybox-width-source').offsetWidth + 'px';
    // console.log(document.getElementById('weekdaybox-width-source').offsetWidth + 'px');
  }
}
</script>

<template>
  <div class="wrapper__big__calendar">
    <div class="yearmonth__display" :style="{ width: weekdayBoxWidth }">
      <div class="lazy__filler__box" :style="{
        width: '15px'
      }"></div>
      <ChangeWeek
        :character="left"
        @past-week="goToPastWeek()" />
      <!-- <span>&#10094;</span> move "left" button -->
      <ChangeWeek
        :character="right"
        @future-week="goToFutureWeek()" />
      <!-- <span>&#10095;</span> move "right" button -->
      <div class="lazy__filler__box" :style="{
        width: '7px'
      }"></div>
      <span id="year__label">{{ currentYear }}</span>
      <span>&bull;</span>
      <span id="month__label">{{ currentMonths }}</span>
      <span>&bull;</span>
      <span id="week__label">Week {{ currentWeek }}</span>
    </div>
    <div class="long__task__display">
      <!-- TODO for that specific feature later; NOTE: it is to only appear when relevant -->
    </div>
    <ul class="weekday__box" id="weekdaybox-width-source">
      <li class="filler__cell"></li>
      <li v-for="i in 7" class="weekday__label">
        <p>
          {{ getWeekSpecificDateFoolproof(i - 1) }}
        </p>
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

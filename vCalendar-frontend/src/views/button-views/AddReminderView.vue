<script>
export default {
  data() {
    return {

    }
  }
}
</script>

<template>
  <div class="event__page__container">
    <div class="event__page__box">
      <span>
        <label for="reminder-title-input">Title: </label>
        <input id="reminder-title-input" name="reminder-title-input">
      </span>
      <span>
        <label for="reminder-date-input">Date: </label>
        <input id="reminder-date-input" name="reminder-date-input">
      </span>
      <span>
        <label for="hours-choice">Hours: </label>
        <input list="hours-list" id="hours-choice" name="hours-choice">
        <datalist id="hours-list">
          <option value=""></option>
          <option v-for="i in 24" v-bind:value="`${String(i - 1).padStart(2, '0') + ':00'}`"></option>
        </datalist>
      </span>
      <button>Create</button>
    </div>
  </div>
</template>
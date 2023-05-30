<script>
export default {
  props: ['character'],
  emits: [],
  data() {
    return {
      displayChar: ""
    }
  },
  computed: {

  },
  methods: {
    
  },
  created() {
    this.displayChar = this.character;
  }
}
</script>

<template>
  <button class="change__week" v-html="this.displayChar">
  
  </button>
</template>
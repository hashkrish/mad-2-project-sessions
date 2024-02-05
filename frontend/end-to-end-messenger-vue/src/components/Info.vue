<script>
import { defineProps } from "vue";
import { useCounterStore } from "../stores/counter";

defineProps({
  msg: {
    type: String,
    required: true,
  },
});

export default {
  data() {
    return {
      msg: this.$props.msg,
      counter: useCounterStore(),
    };
  },
  methods: {
    handleClick() {
      this.counter.increment();
    },
  },
};
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      This is a simple
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a> application using
      <a href="https://flask.palletsprojects.com/en/2.3.x/">Flask</a> as the backend.
    </h3>
  </div>

  <div style="cursor: pointer" @click="handleClick">{{ counter.count }} clicks</div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>

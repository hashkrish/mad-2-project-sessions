import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import "./assets/main.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";

const pinia = createPinia();
const app = createApp(App);

app.use(router);
app.use(pinia);
app.mount("#app");

/*
// For Vue2
// https://pinia.vuejs.org/getting-started.html#Installation

import { createPinia, PiniaVuePlugin } from 'pinia'

Vue.use(PiniaVuePlugin)
const pinia = createPinia()

new Vue({
  el: '#app',
  // other options...
  // ...
  // note the same `pinia` instance can be used across multiple Vue apps on
  // the same page
  pinia,
})
*/

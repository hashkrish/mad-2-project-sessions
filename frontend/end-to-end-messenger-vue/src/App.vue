<script setup>
import { RouterLink, RouterView } from "vue-router";
import Info from "./components/Info.vue";
</script>

<template>
  <header>
    <div class="wrapper">
      <div class="row">
        <!-- <img
          alt="Flask logo"
          class="logo col"
          src="@/assets/flask_logo.png"
          width="198"
          height="135"
        /> -->
        <img alt="Vue logo" class="logo col" src="@/assets/logo.svg" width="125" height="125" />
      </div>

      <Info msg="End to End Messenger" />

      <div style="border: 1px solid black; margin: 10px">
        <audio controls>
          <source src="http://localhost:5000/music/1" type="audio/mpeg" />
          Your browser does not support the audio element.
        </audio>
      </div>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/conversation">Conversation</RouterLink>
        <RouterLink to="/logout">Logout</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 1.5rem;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>

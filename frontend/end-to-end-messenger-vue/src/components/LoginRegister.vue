<script>
import { useAuthStore } from "@/stores/local";

export default {
  data() {
    return {
      username: "krishnan", // TODO remove this
      email: "some@example.com", // TODO remove this
      password: "password", // TODO remove this
      confirm_password: "password", // TODO remove this
      login: true,
    };
  },
  computed: {
    isJWTExpired() {
      return Date.now() >= localStorage.getItem("exp");
    },
  },
  methods: {
    debounce(func, wait, immediate) {
      let timeout;
      return function () {
        const context = this,
          args = arguments;
        const later = function () {
          timeout = null;
          if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
      };
    },
    handleLoginRegister() {
      fetch(`http://localhost:5000/${this.login ? "login" : "api/v1/users"}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
          email: this.email,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          if (this.login) {
            localStorage.setItem("jwt", data.jwt);
            localStorage.setItem("user_id", data.user_id);
            localStorage.setItem("username", data.user_id);
            localStorage.setItem("exp", data.exp);
            this.$router.push("/conversation");
          } else {
            localStorage.setItem("user_id", data.id);
            this.login = true;
            this.username = data.username;
            this.password = "";
            this.$router.push("/");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<template>
  <form v-if="isJWTExpired" id="login" @submit.prevent="handleLoginRegister">
    <div class="row d-flex my-3">
      <div
        class="col text-center mx-1"
        style="
          cursor: pointer;
          user-select: none;
          border-color: var(--color-border);
          border-width: 1px;
          border-style: solid;
          padding: 5px;
          border-radius: 5px;
        "
        :style="login ? 'background-color: var(--color-border)' : ''"
        @click="login = true"
      >
        Login
      </div>
      <div
        class="col text-center mx-1"
        style="
          cursor: pointer;
          user-select: none;
          border-color: var(--color-border);
          border-width: 1px;
          border-style: solid;
          padding: 5px;
          border-radius: 5px;
        "
        :style="!login ? 'background-color: var(--color-border)' : ''"
        @click="login = false"
      >
        Register
      </div>
    </div>
    <div class="mb-3">
      <label for="username" class="form-label">Username</label>
      <input
        v-model="username"
        type="text"
        class="form-control"
        id="username"
        aria-describedby="usernameHelp"
      />
    </div>
    <div v-if="!login" class="mb-3">
      <label for="email" class="form-label">Username</label>
      <input
        v-model="email"
        type="text"
        class="form-control"
        id="email"
        aria-describedby="emailHelp"
      />
    </div>
    <div class="mb-3">
      <label for="password" class="form-label">Password</label>
      <input v-model="password" type="password" class="form-control" id="password" />
    </div>
    <div v-if="!login" class="mb-3">
      <label for="confirm-password" class="form-label">Confirm Password</label>
      <input
        v-model="confirm_password"
        type="password"
        class="form-control"
        id="confirm-password"
      />
    </div>
    <button type="submit" class="btn btn-primary">{{ login ? "Login" : "Register" }}</button>
  </form>
  <div v-else>
    <h1>You are logged in</h1>
    <!-- TODO add logout button -->
  </div>
</template>

<style scoped>
#login {
  width: 300px;
  margin: 0 auto;
}

form {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
</style>

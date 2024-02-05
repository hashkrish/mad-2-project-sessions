<script>
export default {
  data() {
    return {
      username: "krishnan",
      password: "password",
    };
  },
  methods: {
    handleLogin() {
      fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      })
        .then((res) => {
          if (res.ok) {
            this.$router.push("/conversation");
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
  <form id="login" @submit.prevent="handleLogin">
    <div class="mb-3">
      <label for="exampleInputEmail1" class="form-label">Username</label>
      <input
        :value="username"
        type="username"
        class="form-control"
        id="username"
        aria-describedby="usernameHelp"
      />
    </div>
    <!-- <div class="mb-3">
      <label for="exampleInputEmail1" class="form-label">Email address</label>
      <input
        :value="email"
        type="email"
        class="form-control"
        id="email"
        aria-describedby="emailHelp"
      />
    </div> -->
    <div class="mb-3">
      <label for="password" class="form-label">Password</label>
      <input :value="password" type="password" class="form-control" id="password" />
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
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

<script type="text/javascript">
export default {
  data() {
    return {
      message: "",
    };
  },
  mounted() {
    localStorage.removeItem("jwt");
    localStorage.removeItem("exp");
    localStorage.removeItem("user_id");
    localStorage.removeItem("username");
  },
};
</script>

<template>
  <h1>You have been logged out.</h1>
</template>

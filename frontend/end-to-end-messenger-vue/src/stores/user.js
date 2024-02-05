import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({}),
  actions: {
    getUser(user_id) {
      return this[user_id];
    },
  },
});

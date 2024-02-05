import { defineStore } from "pinia";

export const useMessageStore = defineStore("message", {
  state: () => ({
    messages: [],
  }),
  getters: {
    getMessages(state) {
      return state.messages;
    },
  },
});

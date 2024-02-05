<script type="text/javascript">
import { useRouter } from "vue-router";
import { useUserStore } from "../stores/user";
const router = useRouter();
export default {
  data() {
    return {
      conversation: [],
      userStore: useUserStore(),
      username: localStorage.getItem("username"),
      user_id: Number(localStorage.getItem("user_id")),
      current_opponent_id: null,
    };
  },
  computed: {
    getCurrentSender() {
      return Number(this.current_opponent_id);
    },
    getSenders() {
      let senders = [];
      for (let message of this.conversation) {
        if (this.username == this.userStore[message.sender_id]?.username) {
          continue;
        }
        if (!senders.includes(message.sender_id)) {
          senders.push(message.sender_id);
        }
      }
      return senders;
    },
    getConversation() {
      return this.conversation
        .filter(
          (message) =>
            (Number(message.sender_id) === this.current_opponent_id &&
              Number(message.receiver_id) === this.user_id) ||
            (Number(message.sender_id) === this.user_id &&
              Number(message.receiver_id) == this.current_opponent_id),
        )
        .sort((a, b) => a.timestamp - b.timestamp);
    },
  },
  mounted() {
    if (!localStorage.getItem("jwt")) {
      router.push("/");
    }
    fetch("http://localhost:5000/api/v1/messages", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("jwt")}`,
      },
    })
      .then((res) => res.json())
      .then(async (data) => {
        this.conversation = data;
        for (let message of data) {
          let user = await this.userStore[message.sender_id];
          if (!this.userStore[message.sender_id]) {
            fetch(`http://localhost:5000/api/v1/user/${message.sender_id}`, {
              method: "GET",
              headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${localStorage.getItem("jwt")}`,
              },
            })
              .then((res) => res.json())
              .then((data) => {
                this.userStore[message.sender_id] = data;
              });
          }
        }
      });
  },
  methods: {
    sendMessage(event) {
      console.log(
        `Sending message: "${event.target[0].value}" from ${this.username} to ${this.userStore[this.current_opponent_id]?.username}`,
      );
      let payload = {
        sender_id: this.user_id,
        receiver_id: this.current_opponent_id,
        text: event.target[0].value,
      };
      fetch("http://localhost:5000/api/v1/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("jwt")}`,
        },
        body: JSON.stringify(payload),
      })
        .then((res) => res.json())
        .then((data) => {
          this.conversation.push(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
      event.target[0].value = "";
    },
    getSenderName(sender_id) {
      return this.userStore[sender_id]?.username;
    },
  },
};
</script>
<template>
  <div class="coversation mt-4 mt-md-1">
    <div class="d-md-flex justify-content-center d-none" ><h1 class="my-4">Conversation</h1></div>
    <div class="row d-flex my-3">
      <div
        v-for="sender in getSenders"
        :key="sender"
        class="col text-center mx-1"
        style="
          cursor: pointer;
          border-color: var(--color-border);
          border-width: 1px;
          border-style: solid;
          padding: 5px;
          border-radius: 5px;
        "
        :style="{
          backgroundColor: sender == current_opponent_id ? 'var(--color-background-mute)' : '',
        }"
        @click="current_opponent_id = sender"
      >
        {{ getSenderName(sender) }}
      </div>
    </div>
    <hr />
    <div
      class="d-flex flex-column max-height-100"
      style="overflow-y: auto; max-height: 80vh; min-height: 60vh"
    >
      <p
        v-for="message in getConversation"
        :key="message.id"
        :class="{ 'text-end': userStore[message.sender_id]?.username == username }"
        :style="{
          'padding-right': '10px',
          'padding-left': '10px'
        }"
      >
        <b>
          {{
            userStore[message.sender_id]?.username == username
              ? "You"
              : userStore[message.sender_id]?.username
          }}
        </b>
        <br />
        {{ message?.text }}
      <hr />
      </p>
    </div>
    <div>
      <form @submit.prevent="sendMessage">
        <input type="text" class="form-control mb-2" />
      </form>
    </div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .conversation {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}

input {
  color: var(--color-text) !important;
  background-color: var(--color-background) !important;
  border-color: var(--color-border) !important;
}
</style>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");
let message = ref("");
let errors = ref([]);

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then(res => res.json())
    .then(data => {
      csrf_token.value = data.csrf_token;
    });
}

function saveMovie() {
  let form = document.getElementById("movieForm");
  let form_data = new FormData(form);

  form_data.append("csrf_token", csrf_token.value);

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrf_token.value
    }
  })
    .then(res => res.json())
    .then(data => {
      if (data.errors) {
        errors.value = data.errors;
        message.value = "";
      } else {
        message.value = data.message;
        errors.value = [];
        form.reset();
      }
    })
    .catch(err => console.log(err));
}

onMounted(() => {
  getCsrfToken();
});
</script>

<template>
  <div class="form-wrapper">

    <h2 class="form-title">Add New Movie</h2>

    <!-- SUCCESS -->
    <div v-if="message" class="alert success">
      {{ message }}
    </div>

    <!-- ERRORS -->
    <div v-if="errors.length" class="alert error">
      <ul>
        <li v-for="(error, index) in errors" :key="index">
          {{ error }}
        </li>
      </ul>
    </div>

    <form id="movieForm" @submit.prevent="saveMovie">

      <div class="form-group">
        <label>Title</label>
        <input type="text" name="title" />
      </div>

      <div class="form-group">
        <label>Description</label>
        <textarea name="description"></textarea>
      </div>

      <div class="form-group">
        <label>Poster</label>
        <input type="file" name="poster" />
      </div>

      <button type="submit" class="submit-btn">
        Add Movie 🎬
      </button>

    </form>

  </div>
</template>

<style scoped>

/* 💎 WRAPPER (MATCHES MOVIES PAGE) */
.form-wrapper {
  max-width: 600px;
  margin: 0 auto;

  padding: 35px;
  border-radius: 20px;

  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(20px);

  border: 1px solid rgba(255,255,255,0.08);

  box-shadow:
    0 25px 80px rgba(0,0,0,0.8),
    0 0 40px rgba(34,211,238,0.15);
}

/* 🎬 TITLE */
.form-title {
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 25px;

  background: linear-gradient(90deg, #22d3ee, #a855f7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* 🧾 FORM GROUP */
.form-group {
  margin-bottom: 18px;
}

.form-group label {
  display: block;
  margin-bottom: 6px;
  color: #94a3b8;
  font-size: 0.9rem;
}

/* ✨ INPUTS */
input, textarea {
  width: 100%;
  padding: 10px;

  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.08);
  color: white;

  border-radius: 10px;
}

/* FOCUS */
input:focus, textarea:focus {
  outline: none;
  border-color: #22d3ee;
  box-shadow: 0 0 0 2px rgba(34,211,238,0.3);
}

/* 🎯 BUTTON */
.submit-btn {
  width: 100%;
  padding: 12px;

  border: none;
  border-radius: 12px;

  background: linear-gradient(90deg, #22d3ee, #a855f7);
  color: white;

  font-weight: 600;
  cursor: pointer;

  transition: all 0.3s ease;
}

.submit-btn:hover {
  transform: scale(1.03);
  box-shadow: 0 10px 30px rgba(34,211,238,0.4);
}

/* 🚨 ALERTS */
.alert {
  padding: 12px;
  border-radius: 10px;
  margin-bottom: 15px;
}

.success {
  background: rgba(0,255,150,0.15);
  color: #00ff95;
}

.error {
  background: rgba(255,0,80,0.15);
  color: #ff4d6d;
}

.error ul {
  padding-left: 18px;
}

</style>
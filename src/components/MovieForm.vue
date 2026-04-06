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
  <div class="container mt-4">
    <h2>Add Movie</h2>

    <!-- Success Message -->
    <div v-if="message" class="alert alert-success">
      {{ message }}
    </div>

    <!-- Errors -->
    <div v-if="errors.length" class="alert alert-danger">
      <ul>
        <li v-for="(error, index) in errors" :key="index">
          {{ error }}
        </li>
      </ul>
    </div>

    <form id="movieForm" @submit.prevent="saveMovie">
      <div class="mb-3">
        <label>Title</label>
        <input type="text" name="title" class="form-control" />
      </div>

      <div class="mb-3">
        <label>Description</label>
        <textarea name="description" class="form-control"></textarea>
      </div>

      <div class="mb-3">
        <label>Poster</label>
        <input type="file" name="poster" class="form-control" />
      </div>

      <button type="submit" class="btn btn-primary">
        Submit
      </button>
    </form>
  </div>
</template>
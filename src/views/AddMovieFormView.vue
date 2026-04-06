<script setup>
import MovieForm from "../components/MovieForm.vue";
</script>

<template>
  <div class="app-page">

    <div class="form-container">

      <h2 class="page-title">Add New Movie</h2>

      <MovieForm />

    </div>

  </div>
</template>

<style scoped>

/* 💎 GLASS FORM WRAPPER */
.form-container {
  max-width: 600px;
  margin: 0 auto;

  padding: 30px;
  border-radius: 20px;

  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(20px);

  border: 1px solid rgba(255,255,255,0.08);

  box-shadow:
    0 25px 80px rgba(0,0,0,0.8),
    0 0 40px rgba(34,211,238,0.15);
}

/* 🎬 TITLE */
.page-title {
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 20px;

  background: linear-gradient(90deg, #22d3ee, #a855f7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

</style>
<script setup>
import { ref } from "vue";

let message = ref("Discover Movies. Experience Cinema.");
</script>

<template>
  <div class="home">

    <!-- 🌌 HERO -->
    <div class="hero">

      <div class="hero-content">
        <h1>{{ message }}</h1>

        <p>
          Explore trending movies, discover new releases, and enjoy a modern
          cinematic experience built with Vue & Flask.
        </p>

        <RouterLink to="/movies" class="cta-btn">
          Browse Movies 🎬
        </RouterLink>
      </div>

    </div>

  </div>
</template>

<style scoped>

/* 🌌 PAGE */
.home {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at top, #0f172a, #020617);
}

/* 🎬 HERO CONTAINER */
.hero {
  width: 100%;
  max-width: 900px;
  padding: 40px;
  border-radius: 20px;

  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(20px);

  border: 1px solid rgba(255,255,255,0.08);

  text-align: center;

  box-shadow:
    0 25px 80px rgba(0,0,0,0.8),
    0 0 60px rgba(34,211,238,0.15);
}

/* ✨ TITLE */
.hero h1 {
  font-size: 2.8rem;
  font-weight: 800;
  margin-bottom: 15px;

  background: linear-gradient(90deg, #22d3ee, #a855f7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* 📝 DESCRIPTION */
.hero p {
  font-size: 1.1rem;
  color: #94a3b8;
  margin-bottom: 30px;
  line-height: 1.6;
}

/* 🚀 BUTTON */
.cta-btn {
  display: inline-block;
  padding: 12px 24px;
  border-radius: 12px;

  background: linear-gradient(90deg, #22d3ee, #a855f7);
  color: white;
  font-weight: 600;
  text-decoration: none;

  transition: all 0.3s ease;
}

/* ✨ BUTTON HOVER */
.cta-btn:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 30px rgba(34,211,238,0.4);
}

</style>
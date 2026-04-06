<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);
let selectedMovie = ref(null);

function fetchMovies() {
  fetch("/api/v1/movies")
    .then(res => res.json())
    .then(data => {
      movies.value = data.movies;
    })
    .catch(err => console.log(err));
}

function selectMovie(movie) {
  selectedMovie.value = movie;
}

onMounted(() => {
  fetchMovies();
});
</script>

<template>
  <div class="app-page movies-page" :class="{ 'modal-open': selectedMovie }">
    <!-- 🎬 TITLE -->
    <h2 class="page-title">Trending Now</h2>

    <!-- 🎞️ MOVIE ROW -->
    <div class="scroll-row">
      <div 
        class="movie-card"
        v-for="movie in movies"
        :key="movie.id"
        @click="selectMovie(movie)"
      >
        <div 
          class="poster-wrapper"
          :style="{ '--bg-image': `url(http://127.0.0.1:5000${movie.poster})` }"
        >
          <img :src="'http://127.0.0.1:5000' + movie.poster" />

          <div class="overlay">
            <h3>{{ movie.title }}</h3>
          </div>
        </div>
      </div>
    </div>

    <!-- 🎥 MODAL -->
    <div 
      v-if="selectedMovie"
      class="movie-modal"
      @click.self="selectedMovie = null"
    >
      <div class="modal-content">

        <img :src="'http://127.0.0.1:5000' + selectedMovie.poster" />

        <div class="content">
          <h2>{{ selectedMovie.title }}</h2>
          <p>{{ selectedMovie.description }}</p>
        </div>

      </div>
    </div>

  </div>
</template>

<style scoped>

/* 🌌 PAGE */
.movies-page {
  padding: 80px 20px 20px;
}

/* 🎬 TITLE */
.page-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 20px;
  background: linear-gradient(90deg, #22d3ee, #a855f7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* 🎞️ ROW */
.scroll-row {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding-left: 10px;
}

.scroll-row::-webkit-scrollbar {
  display: none;
}

/* 🎬 CARD */
.movie-card {
  min-width: 260px;
  height: 160px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.movie-card:hover {
  transform: scale(1.12);
  z-index: 5;
  box-shadow:
    0 25px 80px rgba(34,211,238,0.4),
    0 0 40px rgba(168,85,247,0.3);
}

/* 🎥 WRAPPER */
.poster-wrapper {
  width: 100%;
  height: 100%;
  position: relative;
  border-radius: 14px;
  overflow: hidden;
  background: #000;
}

/* 🔥 BLURRED BACKGROUND */
.poster-wrapper::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: var(--bg-image);
  background-size: cover;
  background-position: center;
  filter: blur(20px) brightness(0.5);
  transform: scale(1.2);
}

/* 🎯 MAIN IMAGE (NO CROPPING) */
.poster-wrapper img {
  position: relative;
  z-index: 2;

  max-width: 100%;
  max-height: 100%;
  margin: auto;
  display: block;

  object-fit: contain;
}

/* 🎬 OVERLAY */
.overlay {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 12px;
  z-index: 3;

  background: linear-gradient(to top, rgba(0,0,0,0.95), transparent);
}

.overlay h3 {
  font-size: 1rem;
  font-weight: 600;
  color: white;
}

/* 🎥 MODAL */
.movie-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;

  background: rgba(2,6,23,0.9);
  backdrop-filter: blur(10px);

  display: flex;
  justify-content: center;
  align-items: center;

  z-index: 9999;
}

/* 💎 MODAL CARD */
.modal-content {
  position: relative;
  z-index: 10000;

  width: 600px;
  max-width: 90%;
  border-radius: 20px;
  overflow: hidden;

  background: rgba(15,23,42,0.95);
  border: 1px solid rgba(255,255,255,0.08);

  box-shadow: 0 25px 80px rgba(0,0,0,0.8);
}

/* IMAGE */
.modal-content img {
  width: 100%;
  height: auto;
  object-fit: contain;
}

/* CONTENT */
.modal-content .content {
  padding: 20px;
}

.modal-content h2 {
  margin-bottom: 10px;
}

.modal-content p {
  color: #94a3b8;
}

/* 🔥 DISABLE BACKGROUND WHEN MODAL OPEN */
.modal-open .scroll-row {
  filter: blur(6px);
  opacity: 0.3;
  pointer-events: none;
}

.modal-open .movie-card:hover {
  transform: none;
  box-shadow: none;
}

</style>
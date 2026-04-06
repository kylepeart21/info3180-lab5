<template>
  <header>
    <nav class="navbar navbar-expand-lg custom-nav">
      <div class="container-fluid">

        <a class="navbar-brand" href="/">VueJS with Flask</a>

        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">

            <li class="nav-item">
              <RouterLink to="/" class="nav-link">Home</RouterLink>
            </li>

            <li class="nav-item">
              <RouterLink to="/about" class="nav-link">About</RouterLink>
            </li>

            <li class="nav-item">
              <RouterLink to="/movies" class="nav-link" active-class="active-link">Movies
              </RouterLink>
            </li>

            <li class="nav-item">
            <RouterLink to="/movies/create" class="nav-link">
              + Add Movie
            </RouterLink>
          </li>
          </ul>
        </div>

      </div>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style scoped>
.custom-nav {
  background: rgba(10, 15, 25, 0.65);
  backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.navbar-brand {
  font-weight: 700;
  color: #00e5ff !important;
  letter-spacing: 1px;
}

.nav-link {
  color: #cbd5f5 !important;
}

.nav-link:hover {
  color: #00e5ff !important;
}

.custom-nav {
  height: 60px;
  display: flex;
  align-items: center;
}

.active-link {
  color: #00e5ff !important;
  border-bottom: 2px solid #00e5ff;
}

.nav-link:last-child {
  background: linear-gradient(90deg, #00e5ff, #8a2be2);
  border-radius: 8px;
  padding: 6px 12px;
  color: white !important;
  margin-left: 15px;
}

.nav-link:last-child:hover {
  transform: scale(1.05);
}

</style>
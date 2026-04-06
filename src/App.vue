<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <AppHeader />

  <main class="app-main">
    <RouterView />
  </main>

  <AppFooter />
</template>

<style>
/* 🌌 GLOBAL APP BACKGROUND */
html, body, #app {
  margin: 0;
  padding: 0;
  height: 100%;

  background: radial-gradient(circle at top, #0f172a, #020617) !important;
}

/* 🎯 MAIN CONTENT */
.app-main {
  min-height: 100vh;
  background: radial-gradient(circle at top, #0f172a, #020617);
}
</style>
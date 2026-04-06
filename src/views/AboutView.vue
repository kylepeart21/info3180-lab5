<template>
  <div class="about-page">

    <div class="about-card">

      <h2>About This App</h2>

      <p class="subtitle">
        A modern movie browsing experience built with Vue.js & Flask.
      </p>

      <div class="about-content">
        <p>
          This platform allows users to explore trending movies, upload new titles,
          and view detailed information in a clean and cinematic interface.
        </p>

        <p>
          Built with a full-stack architecture using Flask for the backend and Vue.js
          for the frontend, this application demonstrates modern UI design principles
          including glassmorphism, dynamic layouts, and responsive interaction.
        </p>
      </div>

      <div class="tech-stack">
        <span>Vue.js</span>
        <span>Flask</span>
        <span>REST API</span>
        <span>SQLite</span>
      </div>

    </div>

  </div>
</template>

<style scoped>

/* 🌌 PAGE */
.about-page {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;

  padding: 100px 20px 20px;

  background: radial-gradient(circle at top, #0f172a, #020617);
}

/* 💎 CARD */
.about-card {
  width: 100%;
  max-width: 700px;
  padding: 40px;
  border-radius: 20px;

  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(20px);

  border: 1px solid rgba(255,255,255,0.08);

  box-shadow:
    0 25px 80px rgba(0,0,0,0.8),
    0 0 60px rgba(34,211,238,0.15);
}

/* 🎬 TITLE */
.about-card h2 {
  font-size: 2rem;
  margin-bottom: 10px;

  background: linear-gradient(90deg, #22d3ee, #a855f7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* ✨ SUBTITLE */
.subtitle {
  color: #94a3b8;
  margin-bottom: 20px;
}

/* 📝 TEXT */
.about-content p {
  color: #cbd5f5;
  line-height: 1.6;
  margin-bottom: 15px;
}

/* 🚀 TECH TAGS */
.tech-stack {
  margin-top: 20px;
}

.tech-stack span {
  display: inline-block;
  margin: 5px;
  padding: 6px 12px;
  border-radius: 10px;

  background: linear-gradient(90deg, #22d3ee, #a855f7);
  color: white;
  font-size: 0.85rem;
}

/* 📱 MOBILE */
@media (max-width: 768px) {
  .about-card {
    padding: 25px;
  }

  .about-card h2 {
    font-size: 1.5rem;
  }
}

</style>
function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
    updateThemeText();
  }
  
  function updateThemeText() {
    const themeTextEl = document.getElementById('theme-text');
    if (themeTextEl) {
      themeTextEl.textContent = getThemeText();
    }
  
    const clock = document.getElementById('clock');
    if (clock) {
      const timePart = clock.textContent.split(' — ')[0] || '';
      clock.textContent = `${timePart} — ${getThemeText()}`;
    }
  }
  
  function getThemeText() {
    return document.body.classList.contains('dark-theme') ? 'День' : 'Ночь';
  }
  
  function updateClock() {
    const now = new Date();
    const options = { hour: '2-digit', minute: '2-digit', second: '2-digit' };
    const timeString = now.toLocaleTimeString('ru-RU', options);
    document.getElementById('clock').textContent = timeString;
  }
  
  setInterval(updateClock, 1000);
  
  window.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
      document.body.classList.add('dark-theme');
    }
  
    updateClock();
    updateThemeText();
  
    // Теперь, когда всё готово — показываем страницу
    document.body.style.visibility = 'visible';
  });
  function loadNewsDetail(newsId) {
    fetch(`/news/${newsId}/`)
      .then(res => res.text())
      .then(html => {
        document.querySelector('.news-container').innerHTML = html;
      });
  }
  function getTimeOfDay() {
    const hour = new Date().getHours();
    if (hour >= 5 && hour < 12) return 'Утро';
    if (hour >= 12 && hour < 17) return 'День';
    if (hour >= 17 && hour < 21) return 'Вечер';
    return 'Ночь';
  }

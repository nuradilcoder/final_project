
  function updateClock() {
    const now = new Date();
    const options = { hour: '2-digit', minute: '2-digit', second: '2-digit' };
    const timeString = now.toLocaleTimeString('ru-RU', options);
    document.getElementById('clock').textContent = timeString;
  }
  
  setInterval(updateClock, 10);
  
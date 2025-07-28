function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
}

window.onload = () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
};

function updateClock() {
    const now = new Date();
    const options = { 
        hour: '2-digit', 
        minute: '2-digit', 
        second: '2-digit' 
    };
    const timeString = now.toLocaleTimeString('ru-RU', options);
    document.getElementById('clock').textContent = 'Текущее время: ' + timeString;
}
setInterval(updateClock, 1000);
updateClock();  // для немедленного запуска

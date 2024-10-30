const chart = document.querySelector('#chart').getContext('2d');

// Create a new Chart instance
new Chart(chart, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [
            {
                label: 'GOLD',
                data: [1796, 1908, 1936, 1895, 1836, 1807, 1765, 1710, 1660, 1632, 1768, 1822],
                borderColor: 'green',
                borderWidth: 2
            },
            {
                label: 'ETH',
                data: [2688, 2922, 3282, 2728, 1940, 1071, 1679, 1554, 1328, 1572, 1294, 1194],
                borderColor: 'blue',
                borderWidth: 2
            }
        ]
    },
    options: {
        responsive: true
    }
});

// Sidebar show/hide
const menuBtn = document.querySelector('#menu-btn');
const closeBtn = document.querySelector('#close-btn');
const sidebar = document.querySelector('aside');

menuBtn.addEventListener('click', () => {
    sidebar.style.display = 'block';
});
closeBtn.addEventListener('click', () => {
    sidebar.style.display = 'none';
});

// Theme Toggle with Persistence
const themeBtn = document.querySelector('.theme-btn');
const darkTheme = () => document.body.classList.contains('dark-theme');

// Load saved theme from localStorage
if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-theme');
}

themeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');

    const isDark = darkTheme();
    localStorage.setItem('theme', isDark ? 'dark' : 'light');

    themeBtn.querySelector('span:first-child').classList.toggle('active');
    themeBtn.querySelector('span:last-child').classList.toggle('active');
});

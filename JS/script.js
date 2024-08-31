let score = 0;
const coin = document.getElementById('coin');
const scoreDisplay = document.getElementById('score');

function showPoints(points, x, y) {
    const pointsElement = document.createElement('div');
    pointsElement.className = 'points';
    pointsElement.textContent = `+${points}`;
    pointsElement.style.left = `${x}px`;
    pointsElement.style.top = `${y}px`;
    document.body.appendChild(pointsElement);

    setTimeout(() => {
        pointsElement.remove();
    }, 1000);
}

function handleCoinClick(event) {
    score++;
    scoreDisplay.textContent = score;
    const x = event.clientX || event.touches[0].clientX;
    const y = event.clientY || event.touches[0].clientY;
    showPoints(1, x, y); // Показываем число 1 при каждом клике
    coin.style.transform = 'scale(0.9)'; // Уменьшение изображения
    setTimeout(() => {
        coin.style.transform = 'scale(1)'; // Возвращение к исходному размеру
    }, 100);
}

coin.addEventListener('click', handleCoinClick);
coin.addEventListener('touchstart', (event) => {
    event.preventDefault(); // Предотвращение всплытия событий на мобильных устройствах
    handleCoinClick(event);
});

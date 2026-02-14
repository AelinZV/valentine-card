const cat = document.getElementById('cat');
const yesBtn = document.getElementById('yesBtn');
const noBtn = document.getElementById('noBtn');
const catContainer = document.querySelector('.cat-container');

// Пути к изображениям
const IMAGES = {
    neutral: 'neutral.jpg',
    happy: 'happy.jpg',
    sad: 'sad.jpg'
};

yesBtn.addEventListener('click', () => {

    cat.src = IMAGES.happy;
    

    cat.style.transform = 'translateY(-50px)';
    

    createHearts();
    

    disableButtons();
});

noBtn.addEventListener('click', () => {

    cat.src = IMAGES.sad;
    

    disableButtons();
});

function createHearts() {
    const colors = ['#ff1493', '#ff69b4', '#ffb6c1', '#ff00ff'];
    
    for (let i = 0; i < 15; i++) {
        setTimeout(() => {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.innerHTML = '❤️';
            heart.style.left = Math.random() * 100 + '%';
            heart.style.color = colors[Math.floor(Math.random() * colors.length)];
            catContainer.appendChild(heart);
            
            setTimeout(() => {
                heart.remove();
            }, 2000);
        }, i * 150);
    }
}

function disableButtons() {
    yesBtn.disabled = true;
    noBtn.disabled = true;
    yesBtn.style.opacity = '0.5';
    noBtn.style.opacity = '0.5';
    yesBtn.style.cursor = 'not-allowed';
    noBtn.style.cursor = 'not-allowed';
}
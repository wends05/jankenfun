const timer = document.getElementById('timer')
countdown = 3;

setInterval(() => {
    
    if (countdown >= 0) {
    timer.innerHTML = countdown;
    countdown --;
}
}, 1000);




var images = ["/menuFiles/timer3.png", "/menuFiles/timer2.png", "/menuFiles/timer1.png"];

index = 0;

timer = setInterval(() => {
    if (index < 3) {
    const timer = document.getElementById('timer');
    timer.src =images[index];
    index = index + 1;
    } else {
        console.log("hello");
        addBackButton();
        clearInterval(timer)
    }
}, 1000);

function addBackButton() {
    var cont = document.getElementById('containerr');
    
}







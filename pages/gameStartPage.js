
var images = ["/menuFiles/timer3.png", "/menuFiles/timer2.png", "/menuFiles/timer1.png"];

index = 0;

timer = setInterval(() => {
    if (index < 3) {
    const time = document.getElementById('timer');
    time.src =images[index];
    index = index + 1;
    } else {
        haha();
    }
}, 1000);

let back = document.getElementById("tae");

function haha() {
    console.log("hello");

    var container = document.getElementById('containerr');
    const back = document.createElement("button");

    back.classList.add("bg-[url('/menuFiles/bck.png')]", "h-40", "w-60", "bg-center", "bg-contain", "bg-no-repeat");
    back.id = "tae"
    clearInterval(timer);
    container.removeChild(document.getElementById('timer')); 
    container.appendChild(back)

    back.addEventListener("click" , function() {
        window.location = '../mainMenu.html'
    })
}

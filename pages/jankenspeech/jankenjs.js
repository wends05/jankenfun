var startButton = document.getElementById('startButton')
var isOnRound = false;

startButton.addEventListener("click", () => {
    startRound();
    isOnRound = true;
})
document.addEventListener("keydown", (event) => {
    if (event.key == "s" && isOnRound == false) {
    startRound();
    isOnRound =true;
    }
})

// game proper

// initialize voice recog from mozilla(?) and chrome
if ('webkitSpeechRecognition' in window) {
    listener = new webkitSpeechRecognition()
} else if ('SpeechRecognition' in window) {
    listener = new SpeechRecognition()
}

//recognize speech to sentence

let finalTranscript = "";

function startRound() {

    isOnRound = true;
    console.log('haha');

    time = setInterval(() => {
        listener.stop();
        startButton.style.display = "block";
        
        clearInterval(time);
        comparePicks();
        finalTranscript = "";
    }, 5000);

    //timer display

    timerDisplay

    startButton.style.display = "none";
    
    listener.start();

    listener.onresult = (event) => {
        for (let i = event.resultIndex; i < event.results.length; i++) {
            const transcript = event.results[i][0].transcript;
            finalTranscript += transcript
        console.log(transcript);
        
    }
}};

// get player input, sentence to latest word that matches
// rock paper scissors

var pick = ["rock", "paper", "scissors"]
var playerPick = "";
var compPick = "";

function checkUserInput() {
    var listWords = finalTranscript.split(' ');
    console.log(listWords)
    for (let i = listWords.length - 1; i >= 0; i--){
        var wordchecking = listWords[i];
        console.log(i);
        console.log(wordchecking)
        if (pick.includes(wordchecking)) {
            playerPick = wordchecking;
            break
        } else {
            playerPick = "none"
        }
    };
    console.log("Player: " + playerPick)
}

function computerInput() {
    compPick = pick[Math.floor(Math.random() * 3)]
}

//check + displays
function comparePicks() {
    checkUserInput()
    computerInput()

    console.log("Computer: " + compPick, "Player: " + playerPick)

    if (compPick == playerPick) {
        Tie();
    } else {
        const conditions = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        };
        if (conditions[playerPick] == compPick) {
            Win();
        } else {
            Lose()
        }
    }


}

var compHealth = 5;
var PlayerHealth = 5;

// health system
function Tie() {
    console.log("Tied")
}

function Win() {
    compHealth -= 1;
    console.log("Win")
}

function Lose() {
    PlayerHealth -= 1;
    console.log("Lose")
}
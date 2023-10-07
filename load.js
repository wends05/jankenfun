const button = document.querySelectorAll('button');



function loadingPageOpen() {
    console.log("hahahq")
    document.location = '/pages/gameStartPage.htm'
}  

function mazeCraze() {
    
    window.open('/pages/voice-controlled-maze/index.html', '_blank');
    // nick / patrick dri kamo butang sang code kay
    // connected n siya sa play button sa main menu    
    loadingPageOpen()
}


function jankenspeech() {
    
    window.open('/pages/jankenspeech/jankenspeech.html', '');
    loadingPageOpen()
}

function jankenpy() {

    loadingPageOpen();
}
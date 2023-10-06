const button = document.querySelectorAll('button');

function testings() {

    button.forEach(button => button.addEventListener('click', () => {
        console.log(button.textContent);
        document.location = '/pages/gameStartPage.maze.htm'
    }));    
    
}

function mazeCraze() {
    window.open('/pages/jankenspeech/butang di inyo na html file', '_blank');
    // nick / patrick dri kamo butang sang code kay
    // connected n siya sa play button sa main menu    
}


function jankenspeech() {
    window.open('/pages/jankenspeech/jankenspeech.html', '');

}

function jankenpy() {


}
const button = document.querySelectorAll('button');

function testings() {

    button.forEach(button => button.addEventListener('click', () => {
        console.log(button.textContent);
        document.location = '/pages/gameStartPage.maze.htm'
    }));    
    
}

function mazeCraze(params) {
    
}

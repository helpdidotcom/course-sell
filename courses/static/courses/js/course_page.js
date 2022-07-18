let player;
let videoList;


document.onreadystatechange = function () {
    if (document.readyState = 'interactive') {
        player = document.getElementById('player')
        videoList = document.getElementById('video-list')
        mentainRatio()
    }
}




function mentainRatio() {
    let width = player.clientWidth
    let height = (width * 9) / 16
    player.height = height
    videoList.style.maxHeight = height + 'px'
}

window.onresize = mentainRatio
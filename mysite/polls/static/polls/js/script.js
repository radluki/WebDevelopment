
function createChessBoard() {
    var board = document.createElement("div")
    for(let r=0; r<8; r++){
        var row = document.createElement("div")
        row.style.width = "400px"
        for(let c=0; c<8; c++){
            var field = document.createElement("div")
            field.style.background = (c + r)%2==0 ? "black" : "white"
            field.style.height = "50px"
            field.style.width = "50px"
            field.style.float = "left"
            field.onclick = function() {console.log(c,r)}
            row.appendChild(field)
        }
        board.appendChild(row)
    }
    document.body.appendChild(board)
}

window.load = initall;
var saveAnsButton;

function initall(){
    saveAnsButton = document.getElementById('save_ans');
    saveAnsButton.onclick = saveans
}

function saveans(){
    var ans = $("input:radio[name=name]:checked").val()
    alert("Pergunta respondida. Clique em próxima")

    var req = new XMLHttpRequest();
    var url = '/saveans?ans=' + ans

    req.open("GET", url, true)
    req.send()
}

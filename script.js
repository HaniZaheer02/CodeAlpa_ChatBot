function send() {
    var userText = document.getElementById("userInput").value;
    document.getElementById("userInput").value = "";
    var chatlog = document.getElementById("chatlog");
    chatlog.innerHTML += "<div>You: " + userText + "</div>";
    
    fetch("/get?msg=" + userText)
        .then(response => response.text())
        .then(data => {
            chatlog.innerHTML += "<div>Bot: " + data + "</div>";
            chatlog.scrollTop = chatlog.scrollHeight;
        });
}

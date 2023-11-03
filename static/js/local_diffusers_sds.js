res_width = 1024;
res_height = 1024;

function send() {
    model = loaded_model;
    value = document.getElementById("user_input").value;
    document.getElementById("conversation").innerHTML += "<div>User: " + value + "</div>";
    fetch("/diffusers/api_chat_request?model=" + model + "&value=" + value + "&width=" + res_width + "&height=" + res_height)
        .then(response => response.json())
        .then(data => {
            document.getElementById("conversation").lastElementChild.innerHTML += "<br/>";
            const imageElement = document.createElement("img");
            imageElement.style = "max-width: 90%;";
            imageElement.src = "data:image/jpeg;base64," + data.image;
            document.getElementById("conversation").lastElementChild.appendChild(imageElement);
        })
        .catch(error => {
            console.error(error);
        });
}

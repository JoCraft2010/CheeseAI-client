function send() {
    model = loaded_model;
    value = document.getElementById("user_input").value;
    document.getElementById("conversation").innerHTML += "<div>User: " + value + "</div>";
    fetch("/transformers/api_chat_request?model=" + model + "&value=" + value + "&length=" + document.getElementById("simple_chat_outLen").value)
        .then(response => response.json())
        .then(data => {
            document.getElementById("conversation").lastElementChild.innerHTML += "<br/>Bot: " + data["message"];
        })
        .catch(error => {
            console.error(error);
        });
}

function get_last_n_characters(string) {
    if (string.length <= document.getElementById("simple_chat_conLen").value) {
        return string;
    } else {
        return string.substring(string.length - document.getElementById("simple_chat_conLen").value);
    }
}

let conversation = "";
function asend(iteration) {
    if (iteration > document.getElementById("simple_chat_iter").value) {
        let c = document.getElementById("conversation").lastElementChild;
        c.innerHTML += "<button onclick='asend(-1)' class='mb'>More</button>";
        return;
    }
    model = loaded_model;
    if (iteration == 0) {
        conversation = document.getElementById("user_input").value;
        document.getElementById("conversation").innerHTML += "<div>User: " + conversation + "</div>";
        try{ document.getElementById("conversation").querySelectorAll("button")[0].remove(); } catch(error) {}
    }
    if (iteration == -1) {
        document.getElementById("conversation").querySelectorAll("button")[0].remove();
        conversation = get_last_n_characters(conversation);
        asend(1);
        return;
    }
    fetch("/transformers/api_chat_request_small?model=" + model + "&value=" + conversation)
        .then(response => response.json())
        .then(data => {
            let c = document.getElementById("conversation").lastElementChild;
            if (iteration == 0) {
                c.innerHTML += "<br/>Bot: ";
            }
            c.innerHTML += " " + data["message"];
            conversation += " " + data["message"];
            conversation = get_last_n_characters(conversation);
            asend(iteration + 1);
        })
        .catch(error => {
            console.error(error);
        });
}

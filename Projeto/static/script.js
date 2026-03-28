// Capturar cliques
document.addEventListener("click", function(e) {
    fetch("/coletar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            tipo: "click",
            elemento: e.target.tagName,
            texto: e.target.innerText,
            x: e.clientX,
            y: e.clientY
        })
    });
});

// Tempo de tarefa
let inicio = Date.now();

function tarefaConcluida() {
    let tempo = Date.now() - inicio;

    fetch("/coletar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            tipo: "tempo",
            tempo: tempo
        })
    });

    alert("Tempo registrado!");
}

// Esperar carregar a página
document.addEventListener("DOMContentLoaded", function() {

    let form = document.getElementById("feedbackForm");

    if (form) {
        form.addEventListener("submit", function(e) {
            e.preventDefault();

            let problema = e.target.problema.value;

            fetch("/coletar", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    tipo: "feedback",
                    mensagem: problema
                })
            });

            alert("Feedback enviado!");
        });
    }
});

// Perfil do usuário
document.addEventListener("DOMContentLoaded", function() {

    let perfil = document.getElementById("perfilForm");

    if (perfil) {
        perfil.addEventListener("submit", function(e) {
            e.preventDefault();

            fetch("/coletar", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    tipo: "perfil",
                    nome: e.target.nome.value,
                    idade: e.target.idade.value,
                    nivel: e.target.nivel.value
                })
            });

            alert("Perfil salvo!");
        });
    }
});
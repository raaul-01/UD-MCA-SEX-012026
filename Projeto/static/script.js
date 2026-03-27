// [MANTIDO] Capturar cliques
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

// [MANTIDO] Tempo de tarefa
let inicio = Date.now();
function tarefaConcluida() {
    let tempo = Date.now() - inicio;
    fetch("/coletar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ tipo: "tempo", tempo: tempo })
    });
    alert("Tempo registrado!");
}

// [MANTIDO] Feedback e [ATUALIZADO] Perfil
document.addEventListener("DOMContentLoaded", function() {
    let formFeedback = document.getElementById("feedbackForm");
    if (formFeedback) {
        formFeedback.addEventListener("submit", function(e) {
            e.preventDefault();
            fetch("/coletar", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({ tipo: "feedback", mensagem: e.target.problema.value })
            });
            alert("Feedback enviado!");
        });
    }

    let formPerfil = document.getElementById("perfilForm");
    if (formPerfil) {
        formPerfil.addEventListener("submit", function(e) {
            e.preventDefault();
            fetch("/coletar", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    tipo: "perfil",
                    nome: e.target.nome.value,
                    idade: e.target.idade.value,
                    universidade: e.target.universidade.value // Campo novo
                })
            }).then(() => {
                window.location.href = "/usuarios"; // Pula para a lista
            });
        });
    }
});
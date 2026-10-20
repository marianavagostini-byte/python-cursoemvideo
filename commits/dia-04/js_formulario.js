const formulario = document.querySelector("#formulario");
const mensagem = document.querySelector("#mensagem");

formulario.addEventListener("submit", function (evento) {
    evento.preventDefault();

    const nome = document.querySelector("#nome").value.trim();
    const email = document.querySelector("#email").value.trim();

    if (nome.length < 3 || !email.includes("@")) {
        mensagem.textContent = "Confira os dados preenchidos.";
        return;
    }

    mensagem.textContent = `Cadastro local validado para ${nome}.`;
    formulario.reset();
});

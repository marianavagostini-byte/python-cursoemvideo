const formulario = document.querySelector("#form-tarefa");
const entrada = document.querySelector("#nova-tarefa");
const lista = document.querySelector("#lista-tarefas");

formulario.addEventListener("submit", function (evento) {
    evento.preventDefault();

    const texto = entrada.value.trim();

    if (texto === "") {
        return;
    }

    const item = document.createElement("li");
    const descricao = document.createElement("span");
    const botao = document.createElement("button");

    descricao.textContent = texto;
    botao.textContent = "Remover";
    botao.type = "button";

    botao.addEventListener("click", function () {
        item.remove();
    });

    item.append(descricao, " ", botao);
    lista.appendChild(item);

    formulario.reset();
    entrada.focus();
});

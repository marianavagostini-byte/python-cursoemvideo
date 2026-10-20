function validarCadastro(usuario) {
    const erros = [];

    if (usuario.nome.trim().length < 3) {
        erros.push("O nome deve ter pelo menos 3 caracteres.");
    }

    if (!usuario.email.includes("@")) {
        erros.push("O e-mail precisa conter @.");
    }

    if (usuario.idade < 18 || usuario.idade > 120) {
        erros.push("A idade deve estar entre 18 e 120.");
    }

    if (usuario.senha.length < 8) {
        erros.push("A senha precisa ter pelo menos 8 caracteres.");
    }

    return {
        valido: erros.length === 0,
        erros: erros
    };
}

const usuario = {
    nome: "Ana",
    email: "anaexemplo.com",
    idade: 17,
    senha: "1234"
};

const resultado = validarCadastro(usuario);

if (resultado.valido) {
    console.log("Cadastro válido.");
} else {
    console.log("Cadastro inválido:");
    resultado.erros.forEach(erro => console.log("-", erro));
}

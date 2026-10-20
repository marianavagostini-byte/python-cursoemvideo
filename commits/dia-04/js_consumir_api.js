async function buscarUsuario(id) {
    try {
        const resposta = await fetch(
            `https://jsonplaceholder.typicode.com/users/${id}`
        );

        if (!resposta.ok) {
            throw new Error(`Erro HTTP: ${resposta.status}`);
        }

        const usuario = await resposta.json();

        console.log("Nome:", usuario.name);
        console.log("E-mail:", usuario.email);
        console.log("Cidade:", usuario.address.city);
    } catch (erro) {
        console.error("Não foi possível buscar o usuário:", erro.message);
    }
}

buscarUsuario(1);

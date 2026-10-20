const produtos = [
    { nome: "Teclado", categoria: "Perifericos", preco: 150 },
    { nome: "Mouse", categoria: "Perifericos", preco: 80 },
    { nome: "Monitor", categoria: "Video", preco: 900 },
    { nome: "Webcam", categoria: "Video", preco: 300 },
    { nome: "Headset", categoria: "Perifericos", preco: 250 }
];

const grupos = {};

for (const produto of produtos) {
    const categoria = produto.categoria;

    if (!grupos[categoria]) {
        grupos[categoria] = [];
    }

    grupos[categoria].push(produto);
}

for (const categoria in grupos) {
    const itens = grupos[categoria];

    const total = itens.reduce(
        (soma, produto) => soma + produto.preco,
        0
    );

    console.log(categoria);
    console.log("Quantidade:", itens.length);
    console.log("Valor total: R$", total);
}

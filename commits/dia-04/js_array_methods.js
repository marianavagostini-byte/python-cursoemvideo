const produtos = [
    { nome: "Teclado", preco: 150, estoque: 4 },
    { nome: "Mouse", preco: 80, estoque: 0 },
    { nome: "Monitor", preco: 900, estoque: 3 },
    { nome: "Headset", preco: 250, estoque: 2 }
];

const nomes = produtos.map(produto => produto.nome);

const disponiveis = produtos.filter(
    produto => produto.estoque > 0
);

const valorEstoque = produtos.reduce(
    (total, produto) => total + produto.preco * produto.estoque,
    0
);

console.log("Produtos:", nomes);
console.log("Disponíveis:", disponiveis);
console.log("Valor total do estoque: R$", valorEstoque);

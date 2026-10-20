class Produto {
    constructor(nome, preco) {
        this.nome = nome;
        this.preco = preco;
    }

    calcularPrecoFinal() {
        return this.preco;
    }
}

class ProdutoPromocional extends Produto {
    constructor(nome, preco, desconto) {
        super(nome, preco);
        this.desconto = desconto;
    }

    calcularPrecoFinal() {
        return this.preco * (1 - this.desconto / 100);
    }
}

const produtos = [
    new Produto("Monitor", 900),
    new ProdutoPromocional("Teclado", 200, 15),
    new ProdutoPromocional("Mouse", 100, 10)
];

for (const produto of produtos) {
    console.log(
        `${produto.nome}: R$ ${produto.calcularPrecoFinal().toFixed(2)}`
    );
}

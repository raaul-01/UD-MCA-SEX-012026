let produtos = [
  { nome: 'Lápis', preco: 3, estoque: 80 },
  { nome: 'Caderno', preco: 40, estoque: 120 },
  { nome: 'Borracha', preco: 7, estoque: 50 },
  { nome: 'Marca texto', preco: 3, estoque: 90 },
  { nome: 'Caneta', preco: 20, estoque: 55 },
  { nome: 'Mouse Pad', preco: 70, estoque: 86 },
  { nome: 'Tablet', preco: 2000, estoque: 38 },
  { nome: 'Fone', preco: 60, estoque: 91 },
  { nome: 'Celular', preco: 1800, estoque: 47 },
  { nome: 'Calculadora', preco: 20, estoque: 50 }
];
console.log(produtos);

console.log("A) Preço do segundo objeto:", produtos[1].preco);

console.log("B) Nome do terceiro objeto:", produtos[2].nome);

console.log("C) Total de itens:", produtos.length);

console.log("D) Lista de nomes:");
for (let i = 0; i < produtos.length; i++) {
  console.log(produtos[i].nome);
}

let totalEstoque = 0;

for (let i = 0; i < produtos.length; i++) {
  totalEstoque += produtos[i].estoque;
}

console.log("E) Total de estoque:", totalEstoque);

let maiorEstoque = produtos[0];

for (let i = 1; i < produtos.length; i++) {
  if (produtos[i].estoque > maiorEstoque.estoque) {
    maiorEstoque = produtos[i];
  }
}

console.log("F) Produto com maior estoque:", maiorEstoque);
let produto = {
  nome: 'Celular',
  cor: 'Branco',
  preco: 2700,
  estoque: 100
};
console.log(produto);

console.log("A) Nome:", produto.nome);

console.log("B) Preço:", produto['preco']);

produto.estoque = 67;
console.log("C) Estoque atualizado:", produto.estoque);

console.log("D) Todas as propriedades:");
for (let chave in produto) {
  console.log(chave + ":", produto[chave]);
}
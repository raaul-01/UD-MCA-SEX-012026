let jogos = [
  'Fifa',
  'EFootball',
  'NBA2K',
  'Crash',
  'Sonic',
  'Clash Royale',
  'Bomba Patch',
  'God of War',
  'God of War 2',
  'GTA San Andreas',
  'GTA V',
  'Call of Dutty',
  'Far Cry',
  'Assassins creed black flag',
  'Assassins creed rogue',
  'Minecraft',
  'Formula 1',
  'Detroit Become Human',
  'Hitman',
  'Need for Speed',
  'Fifa Street'
];
console.log(jogos);

console.log("Posição 0:", jogos[0]);
console.log("Posição 7:", jogos[7]);
console.log("Posição 11:", jogos[11]);
console.log("Posição 15:", jogos[15]);
console.log("Posição 18:", jogos[18]);
console.log("Posição 20:", jogos[20]);

console.log("Penúltimo:", jogos[jogos.length - 2]);
console.log("Último:", jogos[jogos.length - 1]);

console.log("Total de elementos:", jogos.length);

jogos.push("NovoJogo");
console.log("Novo total:", jogos.length);

for (let i = 0; i < jogos.length; i++) {
  console.log(jogos[i]);
}
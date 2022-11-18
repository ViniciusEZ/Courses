const name = 'Vinicius';
const lastName = 'Ezequiel';
const age = 45;
const weight = 90;
const height = 1.90;
let imc;
let birthdate;
const currentYear = new Date();

imc = weight / (height ** 2);
birthdate = currentYear.getFullYear() - age;

console.log(`${name} ${lastName} tem ${age} anos, pesa ${weight}kg
tem ${height} de altura e seu imc é de ${imc.toFixed(2)},
${name} ${lastName} nasceu em ${birthdate}`);
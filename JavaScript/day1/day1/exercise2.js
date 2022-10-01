let varA = 'A';// B
let varB = 'B';// C
let varC = 'C'; // A
/*
const auxA = varA;

varA = varB;
varB = varC;
varC = auxA
*/

[varA, varB, varC] = [varB, varC, varA]
console.log(varA, varB, varC)
const numero = Number(prompt('Digite um número: '));
const titleNumber = document.getElementById('title-number');
const texto = document.getElementById('text');

titleNumber.innerHTML = numero;
texto.innerHTML = `<p>A raiz quadrada seu número é: ${numero ** (1/2)}</p>`;
texto.innerHTML += `<p>${numero} é inteiro: ${Number.isInteger(numero)}</p>`;
texto.innerHTML += `<p>É NaN: ${Number.isNaN(numero)}</p>`
texto.innerHTML += `<p>Arredondando para baixo: ${Math.floor(numero)}</p>`
texto.innerHTML += `<p>Arredondando para cima: ${Math.ceil(numero)}</p>`
texto.innerHTML += `<p>Com duas casas decimais: ${numero.toFixed(2)}</p>`


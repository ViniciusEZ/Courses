const input_n = Number(prompt('Type a Number: '));
const numTitle = document.getElementById('numtitle');
const texto = document.getElementById('text');

numTitle.innerHTML = input_n;
texto.innerHTML = `<p>The square is: ${input_n ** (1/2)}</p>`;
texto.innerHTML += `<p>${input_n} is integer: ${Number.isInteger(input_n)}</p>`;
texto.innerHTML += `<p>Is NaN: ${Number.isNaN(input_n)}</p>`;
texto.innerHTML += `<p>Floor round: ${Math.floor(input_n)} </p>`;
texto.innerHTML += `<p>Ceil round: ${Math.ceil(input_n)}</p>`;
texto.innerHTML += `With two decimals: ${input_n.toFixed(2)}</p>`;


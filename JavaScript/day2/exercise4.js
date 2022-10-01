const input_n = Number(prompt('Type a Number: '))
document.body.innerHTML += `<h1>Your number is: ${input_n}</h1></br>`
document.body.innerHTML += `The square is: ${input_n ** (1/2)}</br>`
document.body.innerHTML += `${input_n} is integer: ${Number.isInteger(input_n)}</br>`
document.body.innerHTML += `Is NaN: ${Number.isNaN(input_n)} </br>`
document.body.innerHTML += `Floor round: ${Math.floor(input_n)} </br>`
document.body.innerHTML += `Ceil round: ${Math.ceil(input_n)} </br>`
document.body.innerHTML += `With two decimals: ${input_n.toFixed(2)} </br>`

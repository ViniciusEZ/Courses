const form = document.querySelector('#forms');

form.addEventListener('submit', function (e) {
    e.preventDefault();
    const input_weight = e.target.querySelector('#weight');
    const input_height = e.target.querySelector('#height');
    const weight = Number(input_weight.value);
    const height = Number(input_height.value);

    if (!weight) {
        setResp('Invalid weight!', false);
        return; 
    }
    if (!height) {
        setResp('Invalid height!', false);
        return; 
    }
    const imc = getImc(weight, height);
    const levelImc = getImcLevel(imc)
    const msg = `Your imc is ${imc} (${levelImc})`
    setResp(msg, true)
});


function getImcLevel (imc) {
    const level = ['Abaixo do peso', 'Peso normal',
    'Sobrepeso', 'Obesidade grau 1', 'Obesidade grau 2',
     'Obesidade grau 3'];

    if (imc < 18.5) return level[0];
    if (imc <= 24.9) return level[1];
    if (imc <= 29.9) return level[2]
    if (imc <= 34.9) return level[3]
    if (imc <= 39.9) return level[4]
    else return level[5]
};

function getImc(weight, height) {
    const IMC = weight / (height ** 2);
    return IMC.toFixed(2);
}

function createP () {
    const p = document.createElement('p');
    return p;
};

function setResp (msg, isValid) {
    const resposta = document.querySelector('#resp');
    resposta.innerHTML = '';
    const p = createP();
    if (isValid) {
        p.classList.add('p-resp')
    } else {
        p.classList.add('bad')
    }

    p.innerHTML = msg
    resposta.appendChild(p);

};
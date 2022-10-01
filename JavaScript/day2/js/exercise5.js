// IIFE
function myScop () {
    const formul = document.querySelector('.forms');
    const res = document.querySelector('.Res')
    const people = []

    function getElementforms (event) {
        event.preventDefault();
        const name = formul.querySelector('.name');
        const lastname = formul.querySelector('.lastname');
        const weight = formul.querySelector('.weight');
        const height = formul.querySelector('.height');

        const peoples = {
            name : name.value,
            lastname : lastname.value,
            weight: weight.value,
            height: height.value 
        };
        people.push(peoples);
        console.log(peoples);
        res.innerHTML += `<p>${name.value} ${lastname.value} ${weight.value} ${height.value}</p>`
    };

    formul.addEventListener('submit', getElementforms);
}

myScop();


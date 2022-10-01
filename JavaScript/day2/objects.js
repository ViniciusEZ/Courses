
const person1 = {
    name : 'Vinicius',
    lastname : 'Ezequiel',
    age : 19,

    speak () {
        console.log(`${this.name} ${this.lastname} is speaking hi! My age is ${this.age}`)
    },

    ageincrement () {
        return this.age++;
    }
};


person1.speak();
person1.ageincrement();
person1.speak();
person1.ageincrement();
person1.speak();

// function createPerson (name, lastname, age) {
//     return {name, lastname, age}
// };

// const people1 = createPerson('Vinicius', 'Ezequiel', 19);
// const people2 = createPerson('Dante', 'Formiga', 19);
// const people3 = createPerson('Mario', 'José', 19);
// const people4 = createPerson('Vinicius', 'Magalhães', 19);

// let lista = [people1, people2, people3, people4]
// console.log(lista)


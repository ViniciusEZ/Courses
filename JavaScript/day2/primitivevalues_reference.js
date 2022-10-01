/*Primitives (imutables)
bigint, symbol - Copied values
*/ 
/*Reference (Mutable) - Arrays, Objects, functions - for reference*/ 
const person = {
    name : 'Vinicius',
    lastname: 'Ezequiel'
};
const b = {...person};
person.name = 'Maria';
console.log(b);



// let a = [1,2,3,4];
// let b = a;
// let c = [...a];
// b.push(19)
// console.log(a,b, c)

// let a = 'A';
// let b = a;
// console.log(a,b);
// a = 'Random Stuff';
// console.log(a,b);
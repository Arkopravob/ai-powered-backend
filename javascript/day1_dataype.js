//variable  = data container
let a = 23;
let b = 43;
const pi = 3.15;
var n = 'arko';
console.log(a);
console.log(b);

//let and const has block scope and var use for global scope
// {
//     let bike1 = "ducati";
// }
// console.log(bike1);
{
    var bike2="yamaha";
}
console.log(bike2);
//let and const are not hoisted
//let and const must be declared before use

carName = 'bmw';
var carName;
console.log(carName);

//using let its now allowed
// car2 ="audi";
// let car2;
// console.log(car2);

//var allowed redeclaring but let and const not allowed
var n = "marcedese";
console.log(n);
// let x = 'i m a js developer';
// let x = 'i m new here';

//javascript has 8 data type
let foo = 56; // number
console.log(typeof(foo));

bar = true; // boolean
console.log(typeof(bar));

let t; // undefined
console.log(typeof(t));

let x = null;
console.log(typeof(null));
let name = 'arko';
console.log(name);
console.log(typeof(name));




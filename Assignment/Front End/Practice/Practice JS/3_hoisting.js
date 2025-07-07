// Example of hoisting in JavaScript:

// Hoisting JavaScript ka ek important concept hai jo variable declarations aur function declarations ko unke scope ke top par le aata hai, chahe unhe code ke niche declare kiya gaya ho.

// Matlab, JavaScript apne variables aur functions ko memory mein "hoist" (move) kar leta hai, jiska matlab hai ki unhe unke respective scope mein top pe treat kiya jaata hai, chahe aap unhe code ke neeche declare karte ho.

// 1. var hoisting: Variable is hoisted with undefined value
console.log(a); // undefined
var a = 10;
console.log(a); // 10

// 2. Function hoisting: Function declaration is fully hoisted
hello(); // "Hello, World!"
function hello() {
  console.log("Hello, World!");
}

// 3. let and const hoisting (with TDZ): They are hoisted but cannot be accessed before initialization
try {
  console.log(b); // ReferenceError: Cannot access 'b' before initialization
} catch (e) {
  console.log(e.message);
}
let b = 20;

// 4. Example of type coercion: String concatenation and number operation
let result = "5" + 2;
console.log(result); // "52" (String concatenation)

let result2 = "5" - 2;
console.log(result2); // 3 (Automatic type coercion to number)

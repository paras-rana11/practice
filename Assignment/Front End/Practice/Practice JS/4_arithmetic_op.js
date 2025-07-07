// JavaScript Arithmetic Operators:

// Operator	    Description
//  +	        Addition
//  -	        Subtraction
//  *	        Multiplication
//  **	        Exponentiation (ES2016)
//  /	        Division
//  %	        Modulus (Division Remainder)
//  ++	        Increment
//  --	        Decrement


// JavaScript Arithmetic Operators:

//  +  Addition
let a = 5, b = 3;
console.log("Addition: " + (a + b));  // 5 + 3 = 8

//  -  Subtraction
console.log("Subtraction: " + (a - b));  // 5 - 3 = 2

//  *  Multiplication
console.log("Multiplication: " + (a * b));  // 5 * 3 = 15

//  **  Exponentiation (ES2016)
console.log("Exponentiation: " + (a ** b));  // 5 ** 3 = 125

//  /  Division
console.log("Division: " + (a / b));  // 5 / 3 = 1.666...

//  %  Modulus (Division Remainder)
console.log("Modulus: " + (a % b));  // 5 % 3 = 2

//  ++  Increment

// Pre-increment: value is incremented first, then used
let c = 10;
console.log();
console.log("Normal c: " + (c));  
console.log("Pre-increment c: " + (++c));  // ++c = 11 (c becomes 11 before use)
console.log("After Pre-increment c: " + (c));  

// Post-increment: value is used first, then incremented
let d = 10;
console.log();
console.log("Normal d: " + (d));  
console.log("Post-increment d: " + (d++));  // d++ = 10 (d is 10 before use, then becomes 11)
console.log("After Post-increment d: " + (d));  

//  --  Decrement

// Pre-decrement: value is decremented first, then used
let e = 10;
console.log();
console.log("Normal e: " + (e));  
console.log("Pre-decrement: " + (--e));  // --e = 9 (e becomes 9 before use)
console.log("After Pre-decrement e: " + (e));  

// Post-decrement: value is used first, then decremented
let f = 10;
console.log();
console.log("Normal f: " + (f));  
console.log("Post-decrement: " + (f--));  // f-- = 10 (f is 10 before use, then becomes 9)
console.log("After Post-decrement f: " + (f));  
console.log();

// Combined Example
let x = (100 + 50) * a;
console.log("a: " + a + ", x: " + x);  // (100 + 50) * 5 = 750

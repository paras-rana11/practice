// JavaScript Type Operators
// Operator	        Description
// typeof	        Returns the type of a variable
// instanceof	    Returns true if an object is an instance of an object type


// JavaScript Type Operators

// typeof - Returns the type of a variable
let number = 10;
let name = "Alice";
let isActive = true;
let obj = { name: "Bob" };

console.log("typeof number:", typeof number); // Output: "number"
console.log("typeof name:", typeof name);     // Output: "string"
console.log("typeof isActive:", typeof isActive); // Output: "boolean"
console.log("typeof obj:", typeof obj);       // Output: "object"

// Note: `typeof null` returns "object" (a historical bug in JavaScript)
let nullValue = null;
console.log("typeof null:", typeof nullValue); // Output: "object"

// instanceof - Returns true if an object is an instance of an object type
let person = new Object();  // Creating a generic object
let date = new Date();      // Creating a Date object

console.log("person instanceof Object:", person instanceof Object); // Output: true
console.log("date instanceof Date:", date instanceof Date);         // Output: true
console.log("date instanceof Object:", date instanceof Object);     // Output: true

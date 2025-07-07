
// 1. Using `for...in` with an Array
// The for...in loop is designed to iterate over enumerable property names (keys) in an object. When used with arrays, it iterates over the indices (keys) of the array.
// It doesn’t directly access the values, but rather the indices (keys) of the array.
// It can be used to iterate over the properties of an object, as well as the indices of an array.
let cars = ['Toyota', 'Honda', 'Ford'];

console.log("Using for...in with an Array:");
for (let index in cars) {   // Iterates over the indices (keys) of the array
  console.log(index);        // Prints index: 0, 1, 2
  console.log(cars[index]);  // Accesses the value using index (prints 'Toyota', 'Honda', 'Ford')
}
// Output:
// 0
// Toyota
// 1
// Honda
// 2
// Ford

// 2. Using `for...of` with an Array
console.log("\nUsing for...of with an Array:");
for (let car of cars) {     // Iterates directly over the values of the array
  console.log(car);          // Prints value: 'Toyota', 'Honda', 'Ford'
}
// Output:
// Toyota
// Honda
// Ford

// 3. Using `forEach()` with an Array
// The forEach() method is a built-in array method that executes a provided function once for each element in the array. It operates directly on the values in the array and is generally easier to use when you need to perform operations on the array values.

console.log("\nUsing forEach() with an Array:");
cars.forEach(function(car, index) {  // Iterates over the values and provides the index as well
  console.log(index);                // Prints index: 0, 1, 2
  console.log(car);                  // Prints value: 'Toyota', 'Honda', 'Ford'
});
// Output:
// 0
// Toyota
// 1
// Honda
// 2
// Ford

// --- Key Differences ---
// `for...in` is used for iterating over **keys** of an object or indices of an array.
// `for...of` is used for iterating over the **values** of an iterable (like an array, string, Set, Map).
// `forEach()` is an array method that also iterates over the **values** and allows access to the index and array itself inside the callback.






// forEach() Method Parameters
// The forEach() method in JavaScript is specifically designed for arrays and executes a provided function once for each element in the array. It takes up to 3 parameters in the callback function:

// Syntax of forEach():
array.forEach(function(currentValue, index, array) {
  // Code to be executed for each element
});

// currentValue: This represents the value of the current element.
// index: This represents the index of the current element (its position in the array).
// array: This is the array itself, which is available inside the function (optional but provided).

// Code Example with All Three Parameters:
let cars1 = ['Toyota', 'Honda', 'Ford'];

console.log("Using forEach with 3 Parameters:");

cars.forEach(function(currentValue, index, array) {
  console.log("Index:", index);           // Prints the index of the current element (0, 1, 2)
  console.log("Current Value:", currentValue); // Prints the value of the current element ('Toyota', 'Honda', 'Ford')
  console.log("Entire Array:", array);    // Prints the whole array on each iteration
});
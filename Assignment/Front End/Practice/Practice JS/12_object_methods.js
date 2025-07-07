// | **Method**                | **Description**                                                                                       | **Example**                     |
// | ------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------- |
// | `Object.keys()`           | Returns an array of the object's own enumerable property names (keys).                                | `Object.keys(person)`           |
// | `Object.values()`         | Returns an array of the object's own enumerable property values.                                      | `Object.values(person)`         |
// | `Object.entries()`        | Returns an array of the object's own enumerable property `[key, value]` pairs.                        | `Object.entries(person)`        |
// | `Object.assign()`         | Copies properties from one or more source objects to a target object.                                 | `Object.assign({}, obj1, obj2)` |
// | `Object.freeze()`         | Freezes an object, making it immutable.                                                               | `Object.freeze(person)`         |
// | `Object.seal()`           | Seals an object, preventing property addition/removal but allows modification of existing properties. | `Object.seal(person)`           |
// | `Object.create()`         | Creates a new object with a specified prototype and properties.                                       | `Object.create(person)`         |
// | `Object.hasOwnProperty()` | Checks if an object has a specific property as its own (not inherited).                               | `person.hasOwnProperty('name')` |
// | `JSON.stringify()`        | Converts a JavaScript object to a JSON string.                                                        | `JSON.stringify(person)`        |
// | `JSON.parse()`            | Converts a JSON string into a JavaScript object.                                                      | `JSON.parse(jsonString)`        |

// Example 1: Object.keys() - Returns an array of the object's own enumerable property names (keys).
const person = { name: "John", age: 30, city: "New York" };
console.log(Object.keys(person)); // Outputs: ["name", "age", "city"]

// Example 2: Object.values() - Returns an array of the object's own enumerable property values.
console.log(Object.values(person)); // Outputs: ["John", 30, "New York"]

// Example 3: Object.entries() - Returns an array of the object's own enumerable property [key, value] pairs.
console.log(Object.entries(person)); // Outputs: [["name", "John"], ["age", 30], ["city", "New York"]]

// Example 4: Object.assign() - Copies properties from one or more source objects to a target object.
const personCopy = Object.assign({}, person);
console.log(personCopy); // Outputs: { name: "John", age: 30, city: "New York" }

// Example 5: Object.freeze() - Freezes an object, making it immutable (cannot change its properties).
Object.freeze(person);
person.name = "Mike"; // This won't change the object since it's frozen
console.log(person.name); // Outputs: "John" (because the object is frozen)

// Example 6: Object.seal() - Seals an object, preventing property addition/removal but allows modification of existing properties.
Object.seal(person);
person.name = "Mike"; // This will work because modification is allowed
person.country = "USA"; // This won't work because new properties can't be added
console.log(person); // Outputs: { name: "Mike", age: 30, city: "New York" }

// Example 7: Object.create() - Creates a new object with a specified prototype and properties.
const personPrototype = { greet: function() { console.log("Hello, " + this.name); }};
const newPerson = Object.create(personPrototype);
newPerson.name = "Alice";
newPerson.greet(); // Outputs: "Hello, Alice"

// WHAT IS PROTOTYPE:
// In JavaScript, prototypes are a fundamental part of how objects inherit properties and methods. Every JavaScript object has an internal property called [[Prototype]] (often accessed via __proto__), which links to another object. This object is called the prototype.

// The prototype chain allows an object to inherit properties and methods from another object. If an object does not have a property or method, JavaScript looks for that property in its prototype, and then in the prototype's prototype, continuing up the chain until it reaches null.

const parent = {
    greet: function() {
        console.log("Hello from parent!");
    },
    desc: "greeting peoples!"
};
  
const child = Object.create(parent); // child inherits from parent
child.name = "Alice";
  
console.log(child.name); // Outputs: Alice (child's own property)
child.greet(); // Outputs: Hello from parent! (inherited from parent)

// Accessing Prototypes: You can access an object's prototype via Object.getPrototypeOf() or the __proto__ property.
console.log("\n\nPrototypes: "); // Outputs the prototype of 'child' (which is 'parent')
console.log(child.__proto__); // Outputs the prototype of 'child' (which is 'parent')
console.log(child.__proto__.__proto__); // Outputs the prototype of 'parent', which is 'Object.prototype'
console.log(child.__proto__.__proto__.__proto__, "\n\n"); // Outputs null
console.log(parent.__proto__); 
// console.log(Object.getPrototypeOf(child));   // same as: console.log(child.__proto__);


// Example 8: Object.hasOwnProperty() - Checks if an object has a specific property as its own (not inherited).
console.log(person.hasOwnProperty('name')); // Outputs: true (because 'name' is a direct property of person)
console.log(person.hasOwnProperty('toString')); // Outputs: false (because 'toString' is inherited from Object.prototype)

// Example 9: JSON.stringify() - Converts a JavaScript object to a JSON string.
const jsonString = JSON.stringify(person);
console.log(jsonString); // Outputs: '{"name":"Mike","age":30,"city":"New York"}'

// Example 10: JSON.parse() - Converts a JSON string into a JavaScript object.
const parsedPerson = JSON.parse(jsonString);
console.log(parsedPerson); // Outputs: { name: "Mike", age: 30, city: "New York" }

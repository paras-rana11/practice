// Displaying the Object Properties by name
// Displaying the Object Properties in a Loop
// Displaying the Object using Object.values()
// Displaying the Object using JSON.stringify()

// Object for demonstration
const person = {
    name: "Alice",
    age: 25,
    occupation: "Engineer"
};
  
// 1. Displaying the Object Properties by name
console.log("Displaying properties by name:");
console.log("Name:", person.name);
console.log("Age:", person.age);
console.log("Occupation:", person.occupation);
  
// 2. Displaying the Object Properties in a Loop (for...in loop)
console.log("\nDisplaying properties in a loop:");
for (let key in person) {
    if (person.hasOwnProperty(key)) {
      console.log(`${key}: ${person[key]}`);
    }
}
  
// 3. Displaying the Object using Object.values()
console.log("\nDisplaying properties using Object.values():");
console.log(Object.values(person));
  
// 4. Displaying the Object using JSON.stringify()
console.log("\nDisplaying the Object using JSON.stringify():");
console.log(JSON.stringify(person, null, 2));  // The `null, 2` arguments are used to pretty-print the JSON
  
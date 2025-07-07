//  Convert the following JSON string into a JavaScript object and print the "name" property:


let jsonData = '{"name":"Alice", "age":25}';
console.log(typeof jsonData);


jsonObject = JSON.parse(jsonData)
console.log(jsonObject);


console.log("Name: ", jsonObject.name);


// Real Life Objects
// In real life, objects are things like: houses, cars, people, animals, or any other subjects.
// Here is a car object example:

// Object	        Properties	                    Methods

// Car              car.name = Fiat                 car.start()
//                  car.model = 500                 car.drive()
//                  car.weight = 850kg              car.brake()
//                  car.color = white	            car.stop()

// Object Properties
// A real life car has properties like weight and color:
// car.name = Fiat, car.model = 500, car.weight = 850kg, car.color = white.
// Car objects have the same properties, but the values differ from car to car.

// Object Methods
// A real life car has methods like start and stop:
// car.start(), car.drive(), car.brake(), car.stop().
// Car objects have the same methods, but the methods are performed at different times.

// JavaScript Objects
// Objects are variables too. But objects can contain many values.
// This code assigns many values (Fiat, 500, white) to an object named car:

// Example
const car = {type:"Fiat", model:"500", color:"white"};



// Creating a JavaScript Object
// These examples create a JavaScript object with 4 properties:

// Examples:  Create an Object
const person = {firstName:"Roshan", lastName:"Rana", age:25, eyeColor:"blue"};


// This example creates an empty JavaScript object, and then adds 4 properties:
const person1 = {};

person1.firstName = "Rivan";                    // Add Properties
person1.lastName = "Roy";
person1.age = 30;
person1.eyeColor = "brown";


// This example create a new JavaScript object using new Object(), and then adds 4 properties:
const person2 = new Object();

person2.firstName = "Rakesh";                    // Add Properties
person2.lastName = "Mehta";
person2.age = 27;
person2.eyeColor = "Orange";

// accessing properties:
console.log(person2.age);
console.log(person2["age"]);
let a = "age"
console.log(person2[a]);

// adding new properties:
person2["gender"] = "male"
console.log(person2);

person2.fullName = function () {
    return (this.firstName + " " + this.lastName).toUpperCase();
};
console.log(person2);

console.log("\nfull name: ", person2.fullName(), "\n");


// deleting properties:
// delete person2["age"];
delete person2.age;
console.log("after delete age: " , person2);


// Nested Objects":  Property values in an object can be other objects:
myObj = {
    name:"John",
    age:30,
    myCars: {
        car1:"Ford",
        car2:"BMW",
        car3:"Fiat",
        allCars: function(){
            return this.car1 + ", " + this.car2 + ", " + this.car3    
        }
    }
}
console.log(myObj);

// accessing nested properties:
console.log("car2: ", myObj.myCars.car2);
console.log("car2: ", myObj.myCars["car2"]);
console.log("car2: ", myObj["myCars"]["car2"]);
let p1 = "myCars";
let p2 = "car2";
console.log("car2: ", myObj[p1][p2]);

console.log("allCars: ", myObj.myCars.allCars());
console.log("allCars: ", myObj["myCars"]["allCars"]());
console.log("allCars: ", myObj[p1]["allCars"]());



// JavaScript Object Methods:
// Methods are actions that can be performed on objects.
// Methods are function definitions stored as property values.

const person4 = {
    firstName: "John",
    lastName : "Doe",
    id       : 5566,
    fullName : function() {
                    return this.firstName + " " + this.lastName;
                }
};

console.log(person4.fullName());
console.log(person4["fullName"]());


// JavaScript Objects are Mutable:
// Objects are mutable: They are addressed by reference, not by value.
// If person is an object, the following statement will not create a copy of person:

const x = person4;                // The object x is not a copy of person. The object x is person.

// The object x and the object person share the same memory address.
// Any changes to x will also change person:

// Example:
const person5 = {
  firstName:"Jessica",
  lastName:"Jones",
  age:24, eyeColor:"red"
}

// Try to create a copy
const x5 = person5;
console.log(x5)

// This will change age in person:
x5.age = 28;

console.log(person5)

console.log(person5.age)
console.log(x5.age)

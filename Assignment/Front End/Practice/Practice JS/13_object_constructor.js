// Object Constructor Functions
// Sometimes we need to create many objects of the same type.
// To create an object type we use an object constructor function.
// It is considered good practice to name constructor functions with an upper-case first letter.

// class Person {
//     constructor(first, last, age, eye) {
//         this.firstName = first;
//         this.lastName = last;
//         this.age = age;
//         this.eyeColor = eye;
//         this.nationality = "English";
//     }
// }

// SAME AS ↑ :

function Person(first, last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
    this.nationality = "Indian";       // Default Value
    this.fullName = function(){
                        return `${this.firstName} ${this.lastName}`
                    }
}

const myFather = new Person("Aldo", "Burrows", 50, "green");
const myMother = new Person("Christina", "Scofield", 48, "blue");
const myBrother = new Person("Lincoln", "Burrows", 18, "green");

const mySelf = new Person("Michael", "Scofield", 23, "brown")
const myFriend = new Person("Jhon", "Abruzzi", 22, "green");


// Adding/Changing a property to a created object is easy:
console.log(myFather.nationality)
myFather.nationality= "American"
console.log(myFather.nationality)

// Adding a Property to a Constructor:
// but You can NOT add a new property to an object constructor:

Person.gender = "NULL"     // this will added to constructor person as defualt value but not in its objects(father, mother, etc)

console.log(Person.gender);
console.log(myFather.gender);

// To add a new property, you must add it to the constructor function prototype:

Person.prototype.hairColor = "black";

console.log("myFather: ", myFather)     // Here, myFather is not assigned hairColor directly, so, we get myFather without hairColor
console.log("myFather: ", myFather.hairColor)  // But, we can acces it by calling manually
myFather.hairColor = "Golden"          // After, setting hairColor manually it will added to myFather
console.log("myFather: ", myFather)    // So here, we get myFather with hairColor
console.log("myFather: ", myFather.hairColor)


// Adding a Method to an Object:
console.log("myFather FUll Name: ", myFather.fullName());

Person.changeLastName = function(lname){
    this.lastName = lname
}
Person.changeLastName("Scofield")           // yaha, Person constructor hone ke sath-sath khud bhi ek object he to person ka lastname scofield higa baki kisika nahi
console.log("\n\nPerson: ", Person)


// is liye hume ye func sab object pe lagana ho to prototype ka use krna pdega:
Person.prototype.changeLastName = function(lname){
    this.lastName = lname
}
myFather.changeLastName("Scofield") 
console.log("\n\nmyFather: ", myFather)        // So here, we get myFather with changed lastName



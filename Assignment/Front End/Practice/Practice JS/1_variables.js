let x, y, z;    // Statement 1
x = 5;          // Statement 2
y = 6;          // Statement 3
z = x + y;  
console.log(z)

function demo1(){
    
    var x = 10                                      // first time declaring
    console.log(x)
    x = 30                                          // assigning after declaration (changing)
    console.log(x)
    var x = 10                                      // second time redeclaring
    console.log(x)
    
    let y = 40
    console.log(y)
    y = 50
    console.log(y)

    
    
    const z = 60
    console.log(z)
    
    // z = x + y                                       // ERROR
    // console.log(z)
}   

demo1()

// MTLB VAR KAHI PE BHI CHLEGA(global, local, var x = 10), KAHI PE BHI CHANGE HOGA(assigning '=',  x = 30) AND KABHI BHI REDECLARE HOGA(again var x = 30),  
// LET SCOPE ME HI CHLEGA(local, var y = 40) AUR CHANGE HOGA(assigning '=',  y = 50) PR REDECLARE NHI HOGA AUR,
// CONST SCOPE ME CHLEGA(local, var z = 60)  PAR NA CHANGE HOGA NA REDECLARE HOGA


const obj = { name: 'Alice' };
console.log(obj)

obj.name = 'Bob'; // This is valid
console.log(obj)

// obj = { name: 'Charlie' };                        // ERROR

// Jab aap const se kisi object ya array ko declare karte hain, toh aap object ke reference ko change nahi kar sakte. Matlab, aap const ke saath variable ko new reference (ya new object) assign nahi kar sakte.

// Lekin, object ke properties ko mutate karna (change karna) allowed hai, kyunki object ka reference constant hai, lekin uske andar jo data hai, wo change ho sakta hai.


// -======================================================================================- //
// -======================================================================================- //

var a = 0;
console.log("var a:", a);  // Output: var a: 0

var a = 1;  // Allowed (var can be redeclared in the same scope)
console.log("var a:", a);  // Output: var a: 1


var b = 3;  // Allowed (var can be redeclared in the same scope)
// let b = 4;   // Not allowed (SyntaxError: Identifier 'b' has already been declared)
console.log("var b:", b); 


let c = 5;  // Allowed (var can be redeclared in the same scope)
// var c = 6;   // Not allowed (SyntaxError: Identifier 'c' has already been declared)
console.log("var c:", c); 


let x3 = 7;    // Allowed
// let x3 = 8;   // Error: Cannot redeclare block-scoped variable 'x3'
console.log("let x3:", x3)


const y3 = 9;  // Allowed : Par Iske aage const na to change hoga ya na redeclare hoga..
console.log("const y3:", y3); 
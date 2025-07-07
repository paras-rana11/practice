
let a = "5" + 2 + 3;
console.log(a);  // Output: "523"

// Pehle "5" ek string hai aur 2 ek number. Jab string ko number ke saath add kiya jaata hai, toh JavaScript automatic type coercion karta hai aur number ko string mein convert karke dono ko concatenate karta hai. So, "5" + 2 becomes "52" (string "5" aur string "2" ka concatenation).

// Ab, "52" ek string hai aur 3 ek number. Phir se, number ko string mein convert karke dono ko concatenate kiya jaata hai. So, "52" + 3 becomes "523".

let b = 2 + 3 + "5";
console.log(b);  // Output: "55"

// First operation: 2 + 3 results in 5 (numeric addition). Second operation: 5 + "5" becomes "55" (string concatenation).


// ### Examples of Automatic Type Coercion:

// #### 1. String and Number (Using `+` Operator)
// Agar aap string aur number ko **concatenate** karte hain, toh **number** ko **string** mein convert kar diya jaata hai.
let c = "5" + 2;
console.log(c); // Output: "52"

// #### 2. Number and String (Using `-`, `*`, `/` Operators)
// Jab aap **string** aur **number** ko **mathematical operations** mein use karte hain, toh JavaScript **string** ko **number** mein convert karne ki koshish karta hai.
let result1 = "5" - 2;  // Output: 3
let result2 = "5" * 2;  // Output: 10
let result3 = "6" / 2;  // Output: 3
console.log(result1, result2, result3);

// #### 3. Boolean and Number/String (Using Logical Operators)
// JavaScript mein **boolean values** (`true`/`false`) ko **numbers** mein convert kiya jaata hai:
// * `true` becomes `1`
// * `false` becomes `0`
console.log(true + 1);   // Output: 2
console.log(false + 1);  // Output: 1
console.log(true + "5"); // Output: "15"
console.log(false + "5"); // Output: "05"

// #### 4. Equality Operators (== vs ===)
// **`==`** (loose equality) operator **automatic type coercion** karta hai. Jab aap **`==`** use karte hain, toh JavaScript **types ko convert** karta hai agar necessary ho.
console.log(5 == "5"); // Output: true
console.log(0 == false); // Output: true
console.log(null == undefined); // Output: true

// **`===`** (strict equality) operator mein **type coercion** nahi hota. Yeh **exact match** (type aur value dono) check karta hai.
console.log(5 === "5"); // Output: false
console.log(0 === false); // Output: false
// * **`5 === "5"`** ka result **`false`** hai, kyunki types alag hain (ek number aur ek string).


// ### Summary:
// * **Automatic type coercion** JavaScript mein hota hai jab different types ko ek saath use kiya jaata hai.
// * **String + number** case mein JavaScript **number ko string** mein convert kar leta hai (concatenation).
// * **Mathematical operations** mein string ko **number** mein convert kiya jaata hai.
// * **Equality operators (`==`)** mein JavaScript values ko compare karte waqt **types ko convert** kar leta hai.

// **Good Practice:** JavaScript mein **`===` (strict equality)** ko use karna behtar hai, taaki aap **type coercion** se bach sakein aur errors na aaye.


// JavaScript Comparison Operators
// Operator	    Description
// ==	        equal to
// ===	        equal value and equal type
// !=	        not equal
// !==	        not equal value or not equal type
// >	        greater than
// <	        less than
// >=	        greater than or equal to
// <=	        less than or equal to
// ?	        ternary operator


// JavaScript Comparison Operators
// Operator         Description
// ==               equal to
// ===              equal value and equal type
// !=               not equal
// !==              not equal value or not equal type
// >                greater than
// <                less than
// >=               greater than or equal to
// <=               less than or equal to
// ?                ternary operator

// == (Equal to)
let a = 5;
let b = '5';
console.log("a == b: ", a == b);  // true, compares values, not types (string '5' == number 5)

// === (Equal value and equal type)
console.log("a === b: ", a === b);  // false, checks both value and type (number 5 !== string '5')

// != (Not equal)
let c = 10;
console.log("c != 5: ", c != 5);  // true, checks if values are not equal

// !== (Not equal value or not equal type)
let d = '10';
console.log("c !== d: ", c !== d);  // true, different value and type (number 10 !== string '10')

// > (Greater than)
let e = 15;
let f = 10;
console.log("e > f: ", e > f);  // true, checks if e is greater than f

// < (Less than)
console.log("e < f: ", e < f);  // false, checks if e is less than f

// >= (Greater than or equal to)
console.log("e >= f: ", e >= f);  // true, checks if e is greater than or equal to f

// <= (Less than or equal to)
console.log("e <= f: ", e <= f);  // false, checks if e is less than or equal to f

// Ternary operator (condition ? expr1 : expr2)
let age = 18;
let isAdult = (age >= 18) ? "Adult" : "Minor";
console.log("isAdult: ", isAdult);  // "Adult", checks if age is 18 or greater, assigns accordingly






console.log("A" < "B");
console.log("20" < "5");

// ✅ Exactly — JavaScript pehle character se hi comparison shuru karta hai, aur jahan pehle difference milta hai, wahi pe decision le leta hai.

// 🔁 Step-by-step JavaScript String Comparison:
console.log("Apple" < "Banana");    // 'A' vs 'B'
// 'A' (Unicode 65) < 'B' (Unicode 66) → ✅ true

// 👉 JavaScript ab aage ke letters nahi dekhega, kyunki pehla hi character se result mil gaya.

// ⚠️ Important:
// Agar first characters same hain, tabhi JavaScript next character ko check karega.

console.log("App" < "Apple");  // ✅ true    
// 'A' vs 'A' → same
// 'p' vs 'p' → same
// 'p' vs 'p' → same
// "App" ends, "Apple" has more letters → ✅ "App" < "Apple"


// 🧪 Example 1: "abc" < "abC"
console.log("abc" < "abC");  // ❌ false
// 'a' vs 'a' → same
// 'b' vs 'b' → same
// 'c' vs 'C' → Unicode of 'c' is 99, 'C' is 67
// ➡️ 'c' > 'C' → so "abc" < "abC" is false
// 🧠 Lowercase letters (a-z) have higher Unicode values than uppercase (A-Z)

// 🧪 Example 2: "Zebra" < "apple"
console.log("Zebra" < "apple");  // ✅ true  'Z' = 90, 'a' = 97, ➡️ 'Z' < 'a' → so "Zebra" < "apple" is true

// 🧪 Example 3: "cat" < "catalog"
console.log("cat" < "catalog");  // ✅ true

// Step-by-step:
// 'c' == 'c'
// 'a' == 'a'
// 't' == 't'
// Then: "cat" ends, but "catalog" has more characters → so "cat" < "catalog" true

// 🧪 Example 4: "catalog" < "cat"
console.log("catalog" < "cat");  // ❌ false

// 'c' == 'c'
// 'a' == 'a'
// 't' == 't'
// Now: "cat" ends → so it's considered less than "catalog"
// Therefore: "catalog" is NOT less than "cat"


// | **Type**      | **Description**                                        | **Example**                                 |
// | ------------- | ------------------------------------------------------ | ------------------------------------------- |
// | **String**    | Represents a sequence of characters.                   | `"Hello"`, `'World'`                        |
// | **Number**    | Represents numeric values.                             | `10`, `3.14`, `-100`                        |
// | **BigInt**    | Represents large integers beyond safe range.           | `1234567890123456789012345678901234567890n` |
// | **Boolean**   | Represents a logical value `true` or `false`.          | `true`, `false`                             |
// | **undefined** | Represents an uninitialized variable.                  | `let x;`                                    |
// | **null**      | Represents no value.                                   | `let x = null;`                             |
// | **Symbol**    | Represents unique and immutable identifiers.           | `let sym = Symbol("id");`                   |
// | **Object**    | A collection of key-value pairs.                       | `{ name: "Alice" }`                         |
// | **Array**     | An ordered collection of values.                       | `[1, 2, 3, 4]`                              |
// | **Function**  | A block of code that can be invoked.                   | `function greet() {}`                       |
// | **Date**      | A built-in object for working with dates.              | `let today = new Date();`                   |
// | **RegExp**    | A regular expression for pattern matching.             | `let regex = /abc/;`                        |
// | **Map**       | A collection of key-value pairs, keys can be any type. | `let map = new Map();`                      |
// | **Set**       | A collection of unique values.                         | `let set = new Set([1, 2, 3]);`             |
// | **WeakMap**   | A `Map` with weakly held keys (garbage collection).    | `let weakmap = new WeakMap();`              |
// | **WeakSet**   | A `Set` with weakly held values.                       | `let weakset = new WeakSet();`              |

// String: Represents a sequence of characters.
let str = "Hello"; // String example

// Number: Represents numeric values.
let num = 10; // Integer
let pi = 3.14; // Float

// BigInt: Represents large integers beyond the safe range.
let bigNum = 1234567890123456789012345678901234567890n; // BigInt example

// Boolean: Represents a logical value `true` or `false`.
let isTrue = true; // Boolean true
let isFalse = false; // Boolean false

// undefined: Represents an uninitialized variable.
let x; // Variable `x` is undefined

// null: Represents no value.
let emptyValue = null; // Null example

// Symbol: Represents unique and immutable identifiers.
let sym = Symbol("id"); // Symbol example

// Object: A collection of key-value pairs.
let obj = { name: "Alice", age: 25 }; // Object example

// Array: An ordered collection of values.
let arr = [1, 2, 3, 4]; // Array example

// Function: A block of code that can be invoked.
function greet() { // Function example
  console.log("Hello, World!");
}

// Date: A built-in object for working with dates.
let today = new Date(); // Current date and time

// RegExp: A regular expression for pattern matching.
let regex = /abc/; // Regular expression example

// Map: A collection of key-value pairs, keys can be any type.
let map = new Map();
map.set("name", "Alice"); // Map example

// Set: A collection of unique values.
let set = new Set([1, 2, 3]); // Set example

// WeakMap: A `Map` with weakly held keys (garbage collection).
let weakmap = new WeakMap();
let objKey = {};
weakmap.set(objKey, "value"); // WeakMap example

// WeakSet: A `Set` with weakly held values.
let weakset = new WeakSet();
weakset.add(objKey); // WeakSet example

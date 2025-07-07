// Array length - Returns the number of elements in the array.
console.log([1, 2, 3].length); // Output: 3

// Array toString() - Converts the array to a comma-separated string.
console.log([1, 2, 3].toString()); // Output: "1,2,3"

// Array at() - Returns the element at a specified index (supports negative indexing).
console.log([10, 20, 30].at(-1)); // Output: 30

// Array join() - Joins all elements into a string with a specified separator.
console.log(['a', 'b', 'c'].join('-')); // Output: "a-b-c"

// Array pop() - Removes and returns the last element of the array.
let arr1 = [1, 2, 3]; console.log(arr1.pop()); // Output: 3

// Array push() - Adds one or more elements to the end and returns new length.
let arr2 = [1, 2]; console.log(arr2.push(3)); // Output: 3

// Array shift() - Removes and returns the first element of the array.
let arr3 = [1, 2, 3]; console.log(arr3.shift()); // Output: 1

// Array unshift() - Adds elements to the beginning and returns the new length.
let arr4 = [2, 3]; console.log(arr4.unshift(1)); // Output: 3

// Array delete() - Removes the element at a given index (leaves undefined hole).
let arr5 = [1, 2, 3]; delete arr5[1]; console.log(arr5); // Output: [1, <1 empty item>, 3]

// Array concat() - Merges arrays and returns a new array.
let a = [1, 2], b = [3, 4]; console.log(a.concat(b)); // Output: [1, 2, 3, 4]

// Array copyWithin() - Copies part of the array within itself.
let arr6 = [1, 2, 3, 4]; console.log(arr6.copyWithin(1, 2)); // Output: [1, 3, 4, 4]

// Array flat() - Flattens nested arrays into a single-level array.
console.log([1, [2, [3]]].flat(2)); // Output: [1, 2, 3]

// Array splice() - Adds/removes elements at a specific index.
let arr7 = [1, 2, 3]; arr7.splice(1, 1, 'a'); console.log(arr7); // Output: [1, 'a', 3]

// Array toSpliced() - Returns a new array with elements added/removed (does not mutate original).
let arr8 = [1, 2, 3]; let result = arr8.toSpliced(1, 1, 'a'); console.log(result); // Output: [1, 'a', 3]

// Array slice() - Returns a shallow copy of a portion of the array.
let arr9 = [1, 2, 3]; console.log(arr9.slice(1, 3)); // Output: [2, 3]



// ======================================= ARRAY SEARCH ==================================================================================== //
// Array indexOf() - Returns the first index of a specified element, or -1 if not found.
console.log([1, 2, 3, 2].indexOf(2)); // Output: 1

// Array lastIndexOf() - Returns the last index of a specified element, or -1 if not found.
console.log([1, 2, 3, 2].lastIndexOf(2)); // Output: 3

// Array includes() - Checks if the array contains a specified element.
console.log([1, 2, 3].includes(2)); // Output: true

// Array find() - Returns the first element that satisfies the provided testing function.
console.log([1, 2, 3, 4].find(num => num > 2)); // Output: 3

// Array findIndex() - Returns the index of the first element that satisfies the provided testing function.
console.log([1, 2, 3, 4].findIndex(num => num > 2)); // Output: 2

// Array findLast() - Returns the last element that satisfies the provided testing function.
console.log([1, 2, 3, 4].findLast(num => num < 4)); // Output: 3

// Array findLastIndex() - Returns the index of the last element that satisfies the provided testing function.
console.log([1, 2, 3, 4].findLastIndex(num => num < 4)); // Output: 2



// ======================================= ARRAY SORTING ==================================================================================== //
// Array sort() - Sorts the elements of an array in place (default is lexicographically for strings).
console.log(['banana', 'apple', 'cherry'].sort()); // Output: ['apple', 'banana', 'cherry']

// Array reverse() - Reverses the elements of the array in place.
console.log([1, 2, 3].reverse()); // Output: [3, 2, 1]

// Array toSorted() - Returns a new array sorted (does not mutate the original array).
console.log([3, 1, 2].toSorted()); // Output: [1, 2, 3]

// Array toReversed() - Returns a new array with reversed elements (does not mutate the original array).
console.log([1, 2, 3].toReversed()); // Output: [3, 2, 1]

// Sorting Objects - Sorts an array of objects by a specific key.
const people = [{ name: 'John', age: 30 }, { name: 'Alice', age: 25 }, { name: 'Bob', age: 28 }];
console.log(people.sort((a, b) => a.age - b.age)); // Output: [{ name: 'Alice', age: 25 }, { name: 'Bob', age: 28 }, { name: 'John', age: 30 }]

// Numeric Sort - Sorts an array of numbers in ascending order.
console.log([3, 1, 2].sort((a, b) => a - b)); // Output: [1, 2, 3]

// Random Sort - Randomly sorts an array.
console.log([1, 2, 3, 4].sort(() => Math.random() - 0.5)); // Output: Random order

// Math.min() - Returns the smallest of the given numbers.
console.log(Math.min(1, 2, 3, 4)); // Output: 1

// Math.max() - Returns the largest of the given numbers.
console.log(Math.max(1, 2, 3, 4)); // Output: 4

// Home made Min() - Custom function to find the minimum number in an array.
function homeMadeMin(arr) {
  return arr.reduce((min, curr) => (curr < min ? curr : min), arr[0]);
}
console.log(homeMadeMin([3, 1, 4, 1, 5, 9])); // Output: 1

// Home made Max() - Custom function to find the maximum number in an array.
function homeMadeMax(arr) {
  return arr.reduce((max, curr) => (curr > max ? curr : max), arr[0]);
}
console.log(homeMadeMax([3, 1, 4, 1, 5, 9])); // Output: 9

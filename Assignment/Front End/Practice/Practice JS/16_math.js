// Math.abs() - Returns the absolute value of a number.
console.log(Math.abs(-5)); // Output: 5
console.log(Math.abs(3)); // Output: 3

// Math.ceil() - Rounds a number UP to the nearest integer.
console.log(Math.ceil(3.2)); // Output: 4
console.log(Math.ceil(-3.2)); // Output: -3

// Math.floor() - Rounds a number DOWN to the nearest integer.
console.log(Math.floor(3.7)); // Output: 3
console.log(Math.floor(-3.7)); // Output: -4

// Math.round() - Rounds a number to the nearest integer.
console.log(Math.round(3.5)); // Output: 4
console.log(Math.round(3.2)); // Output: 3

// Math.max() - Returns the largest of the given numbers.
console.log(Math.max(1, 2, 3, 4, 5)); // Output: 5

// Math.min() - Returns the smallest of the given numbers.
console.log(Math.min(1, 2, 3, 4, 5)); // Output: 1

// Math.pow() - Returns the base to the exponent power (base^exponent).
console.log(Math.pow(2, 3)); // Output: 8 (2^3)

// Math.sqrt() - Returns the square root of a number.
console.log(Math.sqrt(16)); // Output: 4
console.log(Math.sqrt(25)); // Output: 5

// Math.sin() - Returns the sine of a number (angle in radians).
console.log(Math.sin(Math.PI / 2)); // Output: 1 (sin(90°) = 1)

// Math.cos() - Returns the cosine of a number (angle in radians).
console.log(Math.cos(Math.PI)); // Output: -1 (cos(180°) = -1)

// Math.tan() - Returns the tangent of a number (angle in radians).
console.log(Math.tan(Math.PI / 4)); // Output: 1 (tan(45°) = 1)

// Math.log() - Returns the natural logarithm (base e) of a number.
console.log(Math.log(10)); // Output: 2.302585 (logarithm of 10)

// Math.exp() - Returns Euler's number raised to the power of a given number.
console.log(Math.exp(1)); // Output: 2.718281828459045 (e^1)

// Math.trunc() - Returns the integer part of a number (removes the decimal).
console.log(Math.trunc(3.7)); // Output: 3
console.log(Math.trunc(-3.7)); // Output: -3


// Math.random() - Returns a random floating-point number between 0 (inclusive) and 1 (exclusive).
console.log(Math.random()); // Output: Random number between 0 and 1

// Returns a random integer from 0 to 100: (+1 for include 100 in result)
console.log(Math.floor((Math.random() * 100) + 1))

// Returns a random integer from 0 to 9:
const randomFloat = Math.random() * 10
console.log(randomFloat)

const randomNumber = Math.floor((randomFloat))
console.log(randomNumber)

// Custom Random Function:
generateRandomNumber = (min, max) => {
    num = Math.floor((Math.random() * (max-min+1)) + min )
    return num
}

console.log(generateRandomNumber(20, 120));

console.log(undefined === false)
;
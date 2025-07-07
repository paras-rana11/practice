// Date getFullYear() - Returns the year (4 digits) of the specified date.
let date1 = new Date();
console.log(date1.getFullYear()); // Output: Current year (e.g., 2025)

// Date getMonth() - Returns the month (0-11) of the specified date (0 = January, 11 = December).
let date2 = new Date();
console.log(date2.getMonth()); // Output: Current month (e.g., 4 for May)

// Date getDate() - Returns the day of the month (1-31) for the specified date.
let date3 = new Date();
console.log(date3.getDate()); // Output: Current day of the month (e.g., 4)

// Date getDay() - Returns the day of the week (0-6) for the specified date (0 = Sunday, 6 = Saturday).
let date4 = new Date();
console.log(date4.getDay()); // Output: Current day of the week (e.g., 0 for Sunday)

// Date getHours() - Returns the hour (0-23) of the specified date.
let date5 = new Date();
console.log(date5.getHours()); // Output: Current hour (e.g., 10)

// Date getMinutes() - Returns the minutes (0-59) of the specified date.
let date6 = new Date();
console.log(date6.getMinutes()); // Output: Current minutes (e.g., 35)

// Date getSeconds() - Returns the seconds (0-59) of the specified date.
let date7 = new Date();
console.log(date7.getSeconds()); // Output: Current seconds (e.g., 42)

// Date getMilliseconds() - Returns the milliseconds (0-999) of the specified date.
let date8 = new Date();
console.log(date8.getMilliseconds()); // Output: Current milliseconds (e.g., 234)

// Date setFullYear() - Sets the year of the specified date (optionally, also the month and day).
let date9 = new Date();
date9.setFullYear(2020);
console.log(date9); // Output: Date with year set to 2020

// Date setMonth() - Sets the month of the specified date (0-11).
let date10 = new Date();
date10.setMonth(8); // Set to September (8 = September)
console.log(date10); // Output: Date with month set to September

// Date setDate() - Sets the day of the month (1-31) of the specified date.
let date11 = new Date();
date11.setDate(15); // Set to the 15th of the month
console.log(date11); // Output: Date with day set to 15

// Date setHours() - Sets the hour (0-23) of the specified date.
let date12 = new Date();
date12.setHours(14); // Set to 2 PM
console.log(date12); // Output: Date with hours set to 14 (2 PM)

// Date setMinutes() - Sets the minutes (0-59) of the specified date.
let date13 = new Date();
date13.setMinutes(45); // Set to 45 minutes past the hour
console.log(date13); // Output: Date with minutes set to 45

// Date setSeconds() - Sets the seconds (0-59) of the specified date.
let date14 = new Date();
date14.setSeconds(30); // Set to 30 seconds
console.log(date14); // Output: Date with seconds set to 30

// Date setMilliseconds() - Sets the milliseconds (0-999) of the specified date.
let date15 = new Date();
date15.setMilliseconds(500); // Set to 500 milliseconds
console.log(date15); // Output: Date with milliseconds set to 500

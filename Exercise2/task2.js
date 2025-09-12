/* Write a JavaScript program to find the largest of five numbers.
Display an alert box to show the result. */

let count = parseInt(prompt("How many numbers do you want to enter?"));

let numbers = [];
for (let i = 0; i < count; i++) {
    let value = parseFloat(prompt("Enter number " + (i + 1) + ":"));
    numbers.push(value);
}

let largest = Math.max(...numbers);
alert("The largest number is: " + largest);

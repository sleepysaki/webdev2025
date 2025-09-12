/* Write a JavaScript program to convert temperatures to and from
Celsius and Fahrenheit:
• Conversion Formula: c/5 = (f-32)/9 where c is temperature in Celsius and
f is temperature in Fahrenheit. */

// Function to convert Celsius to Fahrenheit
function celsiusToFahrenheit(celsius) {
    return (celsius * 9/5) + 32;
}

// Function to convert Fahrenheit to Celsius
function fahrenheitToCelsius(fahrenheit) {
    return (fahrenheit - 32) * 5/9;
}

// Usage
let celsiusTemp = 25;
let fahrenheitTemp = 77;
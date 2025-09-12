/* Write a JavaScript program that iterates from 1 to 15. For each
iteration, it will check if the current number is odd or even, and display a
message to the screen. The output should be: “1 is odd”, “2 is even”, ... */

for (let i = 1; i <= 15; i++) {
    if (i % 2 == 0) {
        console.log(i + " is even")
    } else {
        console.log(i + " is odd")
    }
}


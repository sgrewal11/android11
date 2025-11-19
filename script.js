// Create an array
let numbers = [1, 2, 3, 4, 5]; 

// Work with array properties and methods
let arrayLength = numbers.length; // Get the length of the array
let lastElement = numbers.pop(); // Remove the last element
numbers.push(6); // Add a new element to the end

// Create a program loop
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

// Work with the for loop
let sum = 0;
for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
}

// Write comparison and logical operators
let average = 2;
let isAverageGreaterThanThree = (average > 3) && (average < 6); // Comparison and logical operators

// Create a conditional statement
let outputMessage;
if (isAverageGreaterThanThree == true) {
    outputMessage = "The average is greater than three and less than six.";
} else {
    outputMessage = "The average is not in the range of three to six.";
}

// Use the if statement
if (outputMessage) {
    document.getElementById("output").innerText = outputMessage;
}

// Display results in the console
console.log("Array Length: " + arrayLength);
console.log("Last Element: " + lastElement);
console.log("Updated Array: " + numbers);
console.log("Sum: " + sum);
console.log("Average: " + average);
console.log("Output Message: " + outputMessage);



function calculateArea(length, width) {
    return length * width;
}

let x = 5;
let z = 10;
let area = calculateArea(x,z);
console.log("The area of the rectangle is: " + area);
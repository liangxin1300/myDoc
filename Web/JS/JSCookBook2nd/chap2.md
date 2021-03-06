## JavaScript Arrays
#### Searching Through an Array
```Javascript
var animals = new Array("dog", "cat", "seal", "elephant", "walrus", "lion", "cat");
console.log(animals.indexOf("elephant"));
console.log(animals.indexOf("cat"));
console.log(animals.lastIndexOf("cat"));

var nums = [2, 4, 19, 15, 183, 6, 7, 1, 1];

var over = nums.findIndex(function(element) {
  return (element >= 100);
});

console.log(nums[over]);
```
#### Flattening a Two-Dimensional Array with concat() and apply()
```JavaScript
var fruitarray = [];
fruitarray[0] = ['strawberry', 'orange'];
fruitarray[1] = ['lime', 'peach', 'banana'];
fruitarray[2] = ['tangerine', 'apricot'];
fruitarray[3] = ['raspberry', 'kiwi'];

var newArray = fruitarray.concat.apply([], fruitarray)
console.log(newArray[5]);
```
#### Removing or Replacing Array Elements
```JavaScript
var animals = new Array("dog", "cat", "seal", "walrus", "lion", "cat");
animals.splice(animals.indexOf("walrus"), 1);
console.log(animals.toString());
animals.splice(animals.lastIndexOf("cat"), 1, "monkey");
console.log(animals.toString());
```
```JavaScript
var animals = ["cat", "walrus", "lion", "cat"];
animals.splice(-1, 1, "monkey");
console.log(animals.toString()); // cat, walrus, lion, monkey

var animals = ["cat", "walrus", "lion", "cat"];
animals.splice(2);
console.log(animals.toString()); // cat, walrus

var animals = ["cat", "walrus", "lion", "cat"];
animals.splice(2, 1, "zebra", "elephant");
console.log(animals.toString()); // cat, walrus, zebra, elephant, cat
```
```JavaScript
var charSets = ["ab", "bb", "cd", "ab", "cc", "ab", "dd", "ab"];

while (charSets.indexOf("ab") != -1) {
    charSets.splice(charSets.indexOf("ab"), 1, "**");
}
console.log(charSets.toString());

while(charSets.indexOf("**") != -1) {
    charSets.splice(charSets.indexOf("**"), 1);
}
console.log(charSets.toString());
```
#### Extracting a Portion of an Array
```JavaScript
var animals = ['elephant', 'tiger', 'lion', 'zebra', 'cat', 'dog', 'rabbit', 'goose'];
var domestic = animals.slice(4, 7);
console.log(domestic);//['cat', 'dog', 'rabbit']
```
```JavaScript
var mArray = [];
mArray[0] = ['apple', 'pear'];
mArray[1] = ['strawberry', 'lemon'];
mArray[2] = ['lime', 'peach', 'berry'];

var nArray = mArray.slice(1, 2);
console.log(mArray[1]); //['strawberry', 'lemon']
nArray[0][0] = 'raspberry';
console.log(nArray[0]); //['raspberry', 'lemon']
console.log(mArray[1]); //['raspberry', 'lemon']
```
#### Applying a Function Against Each Array Element
```JavaScript
var charSets = ["ab", "bb", "cd", "ab", "cc", "ab", "dd", "ab"];

function replaceElement(element, index, array) {
    if (element == "ab") array[index] = "**";
}

charSets.forEach(replaceElement);
console.log(charSets);
```
#### Applying a Function to Every Element in an Array and Returning a New Array
```JavaScript
var decArray = [23, 255, 122, 5, 16, 99];
var hexArray = decArray.map(function(element){
    return element.toString(16);
});

console.log(hexArray);
```
Unlike forEach(), the map() method results in a new array rather than modifying the original array
#### Creating a Filtered Array
```JavaScript
// You want to filter element values in an array and assign
// the results to a new array
var charSet = ["**", "bb", "cd", "**", "cc", "**", "dd", "**"];
var newArray = charSet.filter(function(element) {
    return (element !== "**");
});

console.log(newArray);//["bb", "cd", "cc", "dd"]
```
#### Validating Array Contents
```JavaScript
// testing function
function testValue(element, index, array) {
  var textExp = /^[a-zA-Z]+$/;
  return textExp.test(element);
}

var elemSet = ["**", 123, "aaa", "abc", "-", 46, "AAA"];

// run test
var result = elemSet.every(testValue);
console.log(result);// false

var elemSet2 = ["elephant", "lion", "cat", "dog"];
result = elemSet2.every(testValue);
console.log(result);// true

result = elemSet.some(testValue);
console.log(result);// true
``` 
#### Using an Associative Array to Store Form Element Names and Values

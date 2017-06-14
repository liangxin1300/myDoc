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

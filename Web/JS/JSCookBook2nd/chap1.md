#### Extracting a List from a String
```JavaScript
var sentence = 'This is one sentence. This is a sentence with a list of items:' +
'cherries, oranges, apples, bananas. That was the list of items.';
var start = sentence.indexOf(':');
var end = sentence.indexOf('.', start+1);

var listStr = sentence.substring(start+1, end);
//var listStr = sentence.substr(start+1, end-start);

var fruits = listStr.split(',');
console.log(fruits); // ['cherries', ' oranges', ' apples', ' bananas']

fruits.forEach(function(elmnt, indx, arry) {
    arry[indx] = elmnt.trim();
});

//fruits = listStr.split(/\s*,\s*/);
console.log(fruits);
```
```JavaScript
//Using Chaining
var sentece = 'This is one sentece. This is a sentece with a list of items:' +
'cherries, oranges, apples, bananas. That was the list of items.'
var start = sentece.indexOf(':');
var end = sentece.indexOf('.', start+1);

var fruits = sentece.substring(start+1, end).split(/\s*,\s*/);
console.log(fruits);
```

#### Checking for an Existing, Noempty String
```JavaScript
var unknownVariable = "test";
if (typeof unknownVariable === 'string' && unknownVariable.length > 0) {
  console.log("is string");
} else {
  console.log("not a string");
}

var unknownVariable = new String("test");
if (typeof unknownVariable === 'string' && unknownVariable.length() > 0) {
  console.log("is string");
} else {
  console.log("not a string");
  console.log(typeof unknownVariable);
  console.log(typeof unknownVariable.valueOf());
}

var unknownVariable = new String("test");
if (((typeof unknownVariable != 'undefined' && unknownVariable) &&
      unknownVariable.length > 0) &&
      typeof unknownVariable.valueOf() == 'string') {
  console.log("is string");
} else {
  console.log("not a string");
}
```

#### Replacing Patterns with New Strings
```JavaScript
```

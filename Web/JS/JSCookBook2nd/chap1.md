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
var searchString = "Now is the time, this is the tame";
var re = /t\w{2}e/g;
var replacement = searchString.replace(re, "place");
console.log(replacement); // Now is the place, this is the place

var re = new RegExp('t\\w{2}e', "g");
var replacement = searchString.replace(re, "place");
console.log(replacement);
```

#### Finding and Highlighting All Instances of a Pattern
```JavaScript
var searchString = "Now is the time and this is the time and that is the time";
var pattern = /t\w*e/g;
var matchArray;

var str = "";
//matchArray = pattern.exec(searchString);
//console.log(matchArray)
while((matchArray = pattern.exec(searchString)) != null) {
  str += "at " + matchArray.index + " we found " + matchArray[0] + "\n";
}
console.log(str)

var re = /a(p+).*(pie)/ig;
var result = re.exec("The apples in the apple pie are tart");
console.log(result);
console.log(result.index);
console.log(result.input);
```

```JavaScript
<!DOCTYPE html>
<html>
<head>
<title>Searching for strings</title>
<style>
.found
{
  background-color: #ff0;
}
</style>

</head>
<body>
  <form id="textsearch">
    <textarea id="incoming" cols="150" rows="10">
    </textarea>
   <p>
     Search pattern: <input id="pattern" type="text" />
   </p>
  </form>
  <button id="searchSubmit">Search for pattern</button>
  <div id="searchResult"></div>

<script>

  document.getElementById("searchSubmit").onclick=function() {

    // get pattern
    var pattern = document.getElementById("pattern").value;
    var re = new RegExp(pattern,"g");

    // get string
    var searchString = document.getElementById("incoming").value;

    var matchArray;
    var resultString = "<pre>";
    var first=0; 
    var last=0;

    // find each match
    while((matchArray = re.exec(searchString)) != null) {
      last = matchArray.index;
      
      // get all of string up to match, concatenate
      resultString += searchString.substring(first, last);

      // add matched, with class
      resultString += "<span class='found'>" + matchArray[0] + "</span>";
      first = re.lastIndex;
    }

    // finish off string
    resultString += searchString.substring(first,searchString.length);
    resultString += "</pre>";

    // insert into page
    document.getElementById("searchResult").innerHTML = resultString;
 }

</script>
</body>
</html>
```

#### Swapping Words in a String Using Capturing Parentheses
```JavaScript
<!DOCTYPE html>
<html>
<head>
<title>Searching for strings</title>
<style>
.found
{
  background-color: #ff0;
}
</style>
</head>
<body>
  <form id="textsearch">
    <textarea id="incoming" cols="100" rows="10">
    </textarea>
    <p>
      Search pattern: <input id="pattern" type="text" />
    </p>
  </form>
  <button id="searchSubmit">Search for pattern</button>
  <div id="searchResult"></div>

<script>

  document.getElementById("searchSubmit").onclick=function() {

    // get pattern
    var pattern = document.getElementById("pattern").value;
    var re = new RegExp(pattern,"g");

    // get string
    var searchString = document.getElementById("incoming").value;

    // replace
    var resultString = searchString.replace(re,"<span class='found'>$&</span>");
    // using $& instead of using loop

    // insert into page
    document.getElementById("searchResult").innerHTML = resultString;
 }

</script>
</body>
</html>
```

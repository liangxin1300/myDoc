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
#### Replacing HTML Tags with Named Entities
#### Using Function Closures with Timers
```JavaScript
<!DOCTYPE html>
<html>
<head>
<title>interval and anonymous function</title>
<style>
#redbox
{
  position: absolute;
  left: 100px;
  top: 100px;
  width: 200px; height: 200px;
  background-color: red;
}
</style>
</head>
<body>
<div id="redbox"></div>
<script>
  var intervalId = null;

  document.getElementById('redbox').addEventListener('click', startBox, false);

  function startBox() {
    if (intervalId == null) {
      console.log("start");
      var x = 100;
      intervalId = setInterval(
          function() {
            x += 5;
            var left = x + "px";
            document.getElementById("redbox").style.left = left;
          }, 100);
    } else {
      console.log("stop");
      clearInterval(intervalId);
      intervalId = null;
    }
  }

</script>
</body>
</html>
```
#### Summing All Numbers in a Table Column
```JavaScript
<!DOCTYPE html>
<html>
<head>
<title>Accessing numbers in table</title>
</head>
<body>
<table id="table1">
  <tr>
    <td>Washington</td><td>145</td>
  </tr>
  <tr>
    <td>Oregon</td><td>233</td>
  </tr>
  <tr>
    <td>Missouri</td><td>833</td>
  </tr>
</table>
<script type="text/javascript">
  var sum = 0;
  var cells = document.querySelectorAll("td + td");
  
  for (var i = 0; i < cells.length; i++) {
    sum+=parseFloat(cells[i].firstChild.data);
    console.log(cells[i])
    console.log(sum);
  }

  var newRow = document.createElement("tr");
  
  var firstCell = document.createElement("td");
  var firstCellText = document.createTextNode("Sum:");
  firstCell.appendChild(firstCellText);
  newRow.appendChild(firstCell);

  var secondCell = document.createElement("td");
  var secondCellText = document.createTextNode(sum);
  secondCell.appendChild(secondCellText);
  newRow.appendChild(secondCell);

  document.getElementById("table1").appendChild(newRow);

</script>
</body>
</html>
```
#### Find the Radius and Center of a Circle to Fit Within a Page Element
```JavaScript
<!DOCTYPE html>
<html>
<head>
<title>Using Math method to fit a circle</title>
<style type="text/css">
#elem
{
  width: 600px;
  height: 400px;
  border: 1px solid black;
}
</style>
<script type="text/javascript">

window.onload = window.onresize = function() {
  var box = document.getElementById("elem");
  var style = window.getComputedStyle(box, null);

  var height = parseInt(style.getPropertyValue("height"));
  var width = parseInt(style.getPropertyValue("width"));

  var x = width / 2;
  var y = height / 2;

  var circleRadius = Math.min(width, height) / 2;

  var circ = document.getElementById("circ");
  circ.setAttribute("r", circleRadius);
  circ.setAttribute("cx", x);
  circ.setAttribute("cy", y);
}
</script>
</head>
<body>
<div id="elem">
  <svg width="100%" height="100%">
    <circle id="circ" width="10"  height="10"  r="10" fill="red"/>
  </svg>
</div>
</body>
</html>
```
####

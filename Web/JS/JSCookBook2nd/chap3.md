## Functions:The JavaScript Building Blocks
#### Passing a Function As an Argument to Another Function
```JavaScript
function otherFunction(x, y, z) {
    x(y, z)
}

var param = function(arg1, arg2) {
    alert(arg1 + " " + arg2);
};

otherFunction(param, "Hello", "World");
otherFunction(function(arg1, arg2) {
alert(arg1 + " " + arg2);}, "Hello", "World");
```
```JavaScript
var nums = [1, 45, 2, 16, 9, 12];
var sum = 0;
for (var i=0; i < nums.length; i++) {
    sum += nums[i];
}

console.log(sum)

var sum = nums.reduce(function(n1, n2){return n1+n2;});//functional programming
console.log(sum)
```
#### Implementing a Recursive Algorithm
```JavaScript
var reverseArray = function(x, indx, str) {
    return indx == 0 ? str :
        reverseArray(x, --indx, (str += " "+ x[indx]));
}

var arr = ['apple', 'orange', 'peach', 'lime'];
var str = reverseArray(arr, arr.length, "");
console.log(str)
```
#### Preventing Code Blocking with a Timer and a Callback
```JavaScript
function factorial(n) {
    console.log(n);
    return n == 1 ? 1 : n * factorial(n-1);
}

function noBlock(n, callback) {
    setTimeout(function() {
        var val = factorial(n);
        if (callback && typeof callback == 'function') {
            callback(val);
        }
    }, 0);
}

console.log("Top of the morning to you");

noBlock(3, function(n) {
    console.log('first call ends with ' + n);
    noBlock(n, function(m) {
        console.log("final result is " + m);
    });
});

var tst = 0;
for (i = 0; i < 10; i++) {
    tst += i;
}

console.log("value of tst is " + tst);

noBlock(4, function(n) {
    console.log("end result if " + n);
});

console.log("not doing too much");
/*
Top of the morning to you
value of tst is 45
not doing too much
3
2
1
first all ends with 6
4
3
2
1
end result is 24
6
5
4
3
2
1
final result is 720
*/

/*By setting the setTimeout() timer to zero, all we've done
  in the solution is to create an event that's pushed to the
  end of the execution queue
*/
```
#### Creating a Function That Remember Its State
```JavaScript
function greetingMaker(greeting) {
    function addName(name) {
        return greeting + " " + name;
    }
    return addName;
}

var daytimeGreeting = greetingMaker("Good Day to you");
var nightGreeting = greetingMaker("Good Evening");

var name = 'Reader';

console.log(daytimeGreeting(name));
console.log(nightGreeting(name));
```
#### Converting Function Arguments into an Array
```JavaScript
function sumRounds() {
    var args = [].slice.call(arguments);

    return args.reduce(function(val1, val2) {
        return parseInt(val1, 10) + parseInt(val2, 10);
    });
}

var sum = sumRounds("2.3", 4, 5, "16", 18.1);
console.log(sum);
```
```JavaScript
<!DOCTYPE html>
<html>
<body>
  <div>test</div>
  <div>test2</div>
  <div>test3</div>
  <script>
      var nlElems = document.querySelectorAll('div');
      var aElems = [].slice.call(nlElems);
  
      aElems.forEach(function(elem) {
          console.log(elem.textContent);
      });
  </script>
</body>
</html>
```
#### Reducing Redundancy by Using a Partial Application
```JavaScript
function makeString(ldelim, str, rdelim) {
    return ldelim + str + rdelim
}

function quoteString(str) {
    return makeString("'", str, "'")
}

function barString(str) {
    return makeString("-", str, "-")
}

function nameEntity(str) {
    return makeString("&#", str, ";")
}

console.log(quoteString("apple"));
console.log(barString("apple"));
console.log(nameEntity(169));
```
```JavaScript
function partial(fn) {
    var args = [].slice.call(arguments, 1);

    return function() {
        return fn.apply(this, args.concat([].slice.call(arguments)));
    };
}

function add(a, b) {
    return a + b;
}

var add100 = partial(add, 100);
console.log(add100(14)); //114

function makeString(ldelim, rdelim, str) {
    return ldelim + str + rdelim;
}

var nameEntity = partial(makeString, "&#", ";");

console.log(nameEntity(169));
```
```JavaScript
function makeString(ldelim, rdelim, str) {
  return ldelim + str + rdelim;
}

var named = makeString.bind(undefined, "&#", ";");

console.log(named(269));
```
#### Improving Application Performance with Memoization(Caching Calculations)
```JavaScript
//Momoized Function
var fibonacci = function() {
  var memo = [0,1];

  var fib = function(n) {
    var result = memo[n];
    if (typeof result != "number") {
      result = fib(n-1) + fib(n-2);
      memo[n] = result;
    }
    return result;
  };

  return fib;
}();

//nomemoized function
var fib = function(n) {
  return n < 2 ? n :  fib(n-1) + fib(n-2);
};

//run nonmemo function, with timer
console.time("non-memo");
for (var i = 0; i <= 10; i++) {
  console.log(i + " " + fib(i));
}
console.timeEnd("non-memo");

//now, memo function with timer
console.time("memo");
for (var i = 0; i <= 10; i++) {
  console.log(i + " " + fibonacci(i));
}
console.timeEnd("memo");
```
#### Using an Anonymous Function to Wrap Global Variables

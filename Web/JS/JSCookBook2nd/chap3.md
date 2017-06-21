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

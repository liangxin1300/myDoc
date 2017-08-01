## The Malleable JavaScript Object
#### Keeping Object Members Private
```JavaScript
function Tune(song,artist) {
  var title = song;
  this.concat = function() {
    return title + " " + artist;
  }
}

var happySongs = [];
happySongs[0] = new Tune("Putting on the Ritz", "Ella Fitzgerald");

console.log(happySongs[0].title); // undefined

// prints out correct title and artist
console.log(happySongs[0].concat());
```
#### Using Prototype to Create Objects
```JavaScript
var str = 'one';

String.prototype.exclaim = function() {
  if (this.length == 0) {
    return this;
  }
  return this + '!';
}

var str2 = 'two';

console.log(str.exclaim()); // one!
console.log(str2.exclaim()); // two!
```
```JavaScript
function Tune(title, artist) {
  this.concatTitleArtist = function() {
    return title + " " + artist;
  }
}

var happySong = new Tune("Putting on the Ritz", "Ella Fitzgerald");

console.log(happySong); // Tune {concatTitleArtist: function}
console.log(happySong.concatTitleArtist()); // Putting on the Ritz Ella Fitzgerald

Tune.prototype.addCategory = function(categoryName) {
  this.category = categoryName;
}

happySong.addCategory("Swing");

var song = "Title and artist: " + happySong.concatTitleArtist() + 
           "Category: " + happySong.category;

console.log(song);
// Title and artist: Putting on the Ritz Ella FitzgeraldCategory: Swing
```
#### Inheriting an Object's Functionality
```JavaScript
function origObject() {
  this.val1 = 'a';
  this.val2 = 'b';
}

origObject.prototype.returnVal1 = function() {
  return this.val1;
};

origObject.prototype.returnVal2 = function() {
  return this.val2;
};

function newObject() {
  this.val3 = 'c';
  origObject.call(this);
}

newObject.prototype = Object.create(origObject.prototype);
newObject.prototype.constructor = newObject;

newObject.prototype.getValues = function() {
  return this.val1 + " " + this.val2 + " " + this.val3;
};

var obj = new newObject();

console.log(obj instanceof newObject); // true
console.log(obj instanceof origObject); // true

console.log(obj.getValues()); // "a b c"
```
```JavaScript
function Book (title, author) {
   this.getTitle=function() {
      return "Title: " + title;
   };
   this.getAuthor=function() {
      return "Author: " + author;
   };
}

function TechBook (title, author, category) {

   this.getCategory = function() {
      return "Technical Category: " + category;
   };

   this.getBook=function() {
      return this.getTitle() + " " + author + " " + this.getCategory();
   };

  Book.apply(this, arguments);
}


TechBook.prototype = Object.create(Book.prototype);
TechBook.prototype.constructor = TechBook;

// get all values
var newBook = new TechBook("The JavaScript Cookbook",
  "Shelley Powers", "Programming");

console.log(newBook.getBook());

// now, individually
console.log(newBook.getTitle());
console.log(newBook.getAuthor());
console.log(newBook.getCategory());
```
#### Extending an Object by Defining a New Property
```JavaScript
```

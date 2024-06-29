# PHP

### [ web lang server] ⇒ so , it’s not work in web browser

[ Browser ] → Http Request → [ Web Server ] → SQL Query → [ Database ]

[ Browser ] ← Http Request ← [ Web Server ] ← SQL Query ← [ Database ]

WHAT WE NEED ?

1- XAMPP Server  [ Apache http server , MariaDB , PHP ]

2- VS CODE ⇒ EXT [ PHP intelephense , Live Server , PHP Server , Perl ]

access [localhost/](http://localhost/)  as a default URL

————————————————————————————————————————————

```php
<!DOCTYPE html>
	<html lang="en">
<head
	    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
// we write all php code here
/*
 php code can write in html code
*/
?>
</body>
</html>
```

### variable in PHP as same as all programing lang

```php
var_dump($variable_name);
//get data type of variable
```

**PHP Variables Scope :**

PHP has three different variable scopes:

- local
- global
- static

→ A variable declared **outside** a function has a GLOBAL SCOPE and can only 
be accessed outside a function .

→ A variable declared **within** a function has a LOCAL SCOPE and can only 
be accessed within that function .

---

The `global` keyword is used to access a global variable from within a function.

To do this, use the `global` keyword before the variables (inside the 
function):

```php
$x = 5;
$y = 10;
function myTest() {
  global $x, $y;
  $y = $x + $y;
}
myTest();
echo $y; // outputs 15
```

PHP also stores all global variables in an array called 
`$GLOBALS[*index*]`. 
The `*index*` holds the name of the variable. This array is also accessible from 
within functions and can be used to update global variables directly.

The example above can be rewritten like this:

```php
$x = 5;
$y = 10;

function myTest() {
  $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['y'];
}

myTest();
echo $y; // outputs 15
```

**PHP Constants variable :**

```php
const MYCAR = "Volvo";
echo MYCAR;
```

Declare variable ⇒  

```php
<?php
$name = "mersa_v6";
$age = 20;   
$_COOKIE = "87124hu12v9487-23LJHalhuDas_1ou1kbasd";
$_email = "alaamersa@gmail.com";
echo "hello <h3> {$name} </h3> , your age is {$age} and cookie is {$_cookie} <br>";
// we don't must declare data type of variable like cpp .
?>
```

## PHP Data Types

- String
- Integer
- Float (floating point numbers - also called double)
- Boolean
- **Array**

```php
$cars = array("Volvo","BMW","Toyota");
var_dump($cars);
```

- **Object  ⇒  OOP CONCEPTS**

```php
 class Car {
  public $color;
  public $model;
  public function __construct($color, $model) {
    $this->color = $color;
    $this->model = $model;
  }
  public function message() {
    return "My car is a " . $this->color . " " . $this->model . "!";
  }
}

$myCar = new Car("red", "Volvo");
var_dump($myCar);

```

- NULL
- Resource

**Change Data Type:**

```php
$x = 5;
var_dump($x);

$x = "Hello";
var_dump($x);
//دا التغير 
```

**PHP Casting :**

بتتكتب قبل الحاجه الي عايز اغيرها 

```php
$d = true;    // Boolean
$c = (string) $c; //casting to string
```

- `(string)` - Converts to data type String
- `(int)` - Converts to data type Integer
- `(float)` - Converts to data type Float
- `(bool)` - Converts to data type Boolean
- `(array)` - Converts to data type Array
- `(object)` - Converts to data type Object
- `(unset)` - Converts to data type NULL

```php
$x = 5;
$x = (string) $x;
var_dump($x);
//CASTING
```

- **string built-in function**
    
    `strlen("mersa_v6")` ⇒ Return the length of the string "mersa_v6":  //8
    
    `str_word_count("alaa mersa_v6")` ⇒ Return counts the number of words in a string. //3
    
    `strpos("mersa is here bro","here")` ⇒ searches for a specific text within a string.  //9 
    
    **Modify Strings :**
    `echo strtoupper("mersa_v6");` ⇒ function returns the string in upper case: //MERSA_V6
    
    `strtolower("mersa_v6")`  ⇒ function returns the string in lower case: //mersa_v6
    
    `strrev(&password)` ⇒ function reverses a string.
    
    `str_replace("mr","Mersa_v6",$the_hello)`:
    
    ```php
    $x = "Hello World!";
    echo str_replace("World", "Dolly", $x);
    //الكلمه الي موجوده اصلا وعايز اغيره
    // + الكلمه الجديده الي هحطها مكانها
    // + المتغير من نوع سترينج الي هعمل عليه العمليه 
    ```
    
- **String Concatenation**
    
    ```php
    //اول طريقه
    $x = "Hello";
    $y = "World";
    $z = $x . $y;
    ```
    
    ```php
    //ثاني طريقه
    $x = "Hello";
    $y = "World";
    $z = "$x $y";
    echo $z;
    
    ```
    

**Escape Character**

we use `\` :

ex:   echo \”mersa_v6”\  ⇒ “mersa_v6”

| Code | Result |
| --- | --- |
| \' | Single Quote |

| \" | Double Quote |
| --- | --- |
| \$ | PHP variables |
| \n | New Line |
| \r | Carriage Return |
| \t | Tab |

---

---

## **PHP Numbers :**

There are three main numeric types in PHP:

- `Integer`
- `Float`
- `Number Strings`

In addition, PHP has two more data types used for numbers:

- `Infinity`
- `NaN`

```php
<?php
$a = 5;
$b = 5.34;
$c = "25";

var_dump($a);  // int(5)
var_dump($b);  // float(5.34)
var_dump($c);  // string(2) "25"
?> 
```

we have `is_int()` ,`is_float()` function:

ex:

```php
$x = 5985;
var_dump(is_int($x)); // bool(true) 
$x = 59.85;
var_dump(is_int($x)); // bool(false) 
```

- **MATH Functions**
    
    `pi()`
    `min(0, 150, 30, 20, -8, -200)`
    `max(0, 150, 30, 20, -8, -200)`
    `abs(-6.7)`
    `sqrt(64)`
    `round(0.49)` //بترجع اقرب رقم صحيح من الرقم الي مدهولو ⇒  0
    
    `rand()`  //2314133
    `rand(10, 100)` //97
    

# **Operators :**

- Arithmetic operators ⇒ + , -  , *  ,  /  , %  , @ , **
- Assignment operators ⇒  x = y  ,  x += y   ,  x /= y ,   x *= y  ,  x -= y
- Comparison operators ⇒ == ( نفس القيمه )  ,  === ( نفس القيمه والداتا تيب )  , !=  , <> ( not eqal also)  , !==   ( ليست نفس القيمه ولا الداتا تيب ليس)  ,  >  ,  <  ,  >=  ,  <=
- Increment/Decrement operators ⇒ ++$x   ,   $x++ ,  --$x  ,   $x--
- Logical operators ⇒ and ,  or ,  xor ( True if either $x or $y is true, but not both ) , &&  ,  ||  , !
- String operators ⇒  . ( $txt1 . $txt2; ) Concatenation

    

## IF  ,   SWITCH   , LOOP  ,  FUNCTIONS

                                 [ ALL SAME CPP AND JS ]

examples:

```php
if ($t < "20") 
{
  echo "Have a good day!";
}
 else 
 {
  echo "Have a good night!";
 }
?>
```

```php
switch (expression) {
  case label1:
    //code block
    break;
  case label2:
    //code block;
    break;
  case label3:
    //code block
    break;
  default:
    //code block
}
```

```php
$i = 1;
while ($i < 6) {
  echo $i;
  $i++;
}
```

```php
$i = 1;
while ($i < 6):
  echo $i;
  $i++;
endwhile;
```

```php
$i = 0;
while ($i < 6) {
  $i++;
  if ($i == 3) continue;
  echo $i;
}
```

```php
$i = 8;
do {
  echo $i;
  $i++;
} while ($i < 6);
```

```php
for (expression1,expression2,expression3) {
  //code block}
```

**foreach**
The `foreach` loop - Loops 
through a block of code for each element in an array or each property in an object.

```php
<?php
$colors = array("red", "green", "blue", "yellow");
foreach ($colors as $x) {
echo "$x <br>";
}
?>
//result
red
green
blue
yellow 
```

---

```php
function familyName($fname) {
  echo "$fname Refsnes.<br>";
}
```

## Arrays

```php
$cars = array("Volvo", "BMW", "Toyota");
equal
$cars = ["Volvo", "BMW", "Toyota"];
//multiple array
$cars = array (
  array("Volvo",22,18),
  array("BMW",15,13),
  array("Saab",5,2),
  array("Land Rover",17,15)
);

$myArr = array("Volvo", 15, ["apples", "bananas"], myFunction);

echo count($cars); //3
var_dump($cars); 
/* array(3) {
  [0]=>
  string(5) "Volvo"
  [1]=>
  string(3) "BMW"
  [2]=>
  string(6) "Toyota"
  */
  
  array_push($cars, "Ford"); //ford index 4
}
```

### **Array Keys:**

associative array ⇒ an array mode of key ⇒ value pairs 

```php
$cars = [
  0 => "Volvo",
  1 => "BMW",
  2 =>"Toyota"
];

$myCar = [
  "brand" => "Ford",
  "model" => "Mustang",
  "year" => 1964
];

$cars = [];
$cars[0] = "Volvo";
$cars[1] = "BMW";
$cars[2] = "Toyota";

$myCar = [];
$myCar["brand"] = "Ford";
$myCar["model"] = "Mustang";
$myCar["year"] = 1964;

echo $cars["year"];
echo $cars[2];
```

**Delete Array Items:**

`array_splice()` ⇒ بتاخد 3 قيم الاولي اسم الاراي والثانيه بدايه الانديكس الي هبدا الحذف منه الثالثه الي هينتهس عندها الحذف 

```php
$cars = array("Volvo", "BMW", "Toyota");
array_splice($cars, 1, 2);
//هتحذف كلو ماعدا volvo
```

`unset()` ⇒ بتحذف انديكس معين 

```php
$cars = array("Volvo", "BMW", "Toyota");
unset($cars[1]);
//array => ("volovo" , "Toyota" )
// for more than one =>  unset($cars[0], $cars[1]);
```

`array_pop($cars);` ⇒ **Remove the Last Item .**
`array_shift($cars);` ⇒ **Remove the First Item .**

`array_push($cars,"toyota","marcides")` ⇒ add a new index

**Sort Functions For Arrays:**

- `sort()` - sort arrays in ascending order ترتيب تصاعدي
- `rsort()` - sort arrays in descending order ترتيب تنازلي

Important functions 

isset( ) = returns true if a variabls is declared and not null 

empty( ) = returns true if a variabls is not declared , false , null , ” ”

تستخدم مع ال checkbox

```php
<php
$username = "mersa_v6";
echo isset($username);         //1
echo empty($username)          //0

$username = "";
echo isset($username);         //0
echo empty($username)          //1
?>
```

# **PHP Global Variables - Superglobals**

Some predefined variables in PHP are "superglobals", which means that they are always accessible, regardless of scope - and you can access them from any function, class or file without having to do anything special.

The PHP superglobal variables are:

- `$GLOBALS` is an array that contains all global variables.

```php
$x = 75;

function myfunction() {
  echo $GLOBALS['x'];
}

myfunction()

```

- [`$_SERVER`](https://www.w3schools.com/php/php_superglobals_server.asp) is a PHP super global variable which holds information about headers, paths, and script locations.

| Element/Code | Description | output |
| --- | --- | --- |
| $_SERVER['PHP_SELF'] | Returns the filename of the currently executing script |  /index.php  |
| $_SERVER['GATEWAY_INTERFACE'] | Returns the version of the Common Gateway Interface (CGI) the server is using | CGI/1.1  |
| $_SERVER['SERVER_ADDR'] | Returns the IP address of the host server |  127.0.0.1  |
| $_SERVER['SERVER_NAME'] | Returns the name of the host server (such as www.w3schools.com) |  http://localhost  |
| $_SERVER['SERVER_SOFTWARE'] | Returns the server identification string (such as Apache/2.2.24) |  Apache/2.4.58 (Win64) OpenSSL/3.1.3 PHP/8.2.12  |
| $_SERVER['SERVER_PROTOCOL'] | Returns the name and revision of the information protocol (such as HTTP/1.1) |  HTTP/1.1  |
| $_SERVER['REQUEST_METHOD'] | Returns the request method used to access the page (such as POST) |  POST  |
| $_SERVER['REQUEST_TIME'] | Returns the timestamp of the start of the request (such as 1377687496) |  1715869042  |
| $_SERVER['QUERY_STRING'] | Returns the query string if the page is accessed via a query string |  |
| $_SERVER['HTTP_ACCEPT'] | Returns the Accept header from the current request | text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8  |
| $_SERVER['HTTP_ACCEPT_CHARSET'] | Returns the Accept_Charset header from the current request (such as 
utf-8,ISO-8859-1) |  |
| $_SERVER['HTTP_HOST'] | Returns the Host header from the current request | localhost |
| $_SERVER['HTTP_REFERER'] | Returns the complete URL of the current page (not reliable because not all 
user-agents support it) |  http://localhost/index.php  |
| $_SERVER['HTTPS'] | Is the script queried through a secure HTTP protocol |  |
| $_SERVER['REMOTE_ADDR'] | Returns the IP address from where the user is viewing the current page |  127.0.0.1  |
| $_SERVER['REMOTE_HOST'] | Returns the Host name from where the user is viewing the current page |  |
| $_SERVER['REMOTE_PORT'] | Returns the port being used on the user's machine to communicate with the 
web server |  61988  |
| $_SERVER['SCRIPT_FILENAME'] | Returns the absolute pathname of the currently executing script |  D:/xampp/htdocs/index.php  |
| $_SERVER['SERVER_ADMIN'] | Returns the value given to the SERVER_ADMIN directive in the web server 
configuration file (if your script runs on a virtual host, it will be the value 
defined for that virtual host) (such as someone@w3schools.com) |  mailto:postmaster@localhost  |
| $_SERVER['SERVER_PORT'] | Returns the port on the server machine being used by the web server for 
communication (such as 80) |  80  |
| $_SERVER['SERVER_SIGNATURE'] | Returns the server version and virtual host name which are added to 
server-generated pages | Apache/2.4.58 (Win64) OpenSSL/3.1.3 PHP/8.2.12 Server at localhost Port 80 |
| $_SERVER['PATH_TRANSLATED'] | Returns the file system based path to the current script |  |
| $_SERVER['SCRIPT_NAME'] | Returns the path of the current script |  /index.php  |
| $_SERVER['SCRIPT_URI'] | Returns the URI of the current page |  |

```php
echo $_SERVER['PHP_SELF'];
echo $_SERVER['SERVER_NAME'];
echo $_SERVER['HTTP_HOST'];
echo $_SERVER['HTTP_REFERER'];
echo $_SERVER['HTTP_USER_AGENT'];
echo $_SERVER['SCRIPT_NAME'];
```

- [`$_REQUEST`](https://www.w3schools.com/php/php_superglobals_request.asp)

```php
<html><body><form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Name: <input type="text" name="fname"><input type="submit"></form><?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = htmlspecialchars($_REQUEST['fname']);
  if (empty($name)) {
    echo "Name is empty";
  } else {
    echo $name;
  }
}
?></body></html>
```

- [`$_POST`](https://www.w3schools.com/php/php_superglobals_post.asp)
- [`$_GET`](https://www.w3schools.com/php/php_superglobals_get.asp)
- `$_FILES`
- `$_ENV`
- [`$_COOKIE`](https://www.w3schools.com/php/php_cookies.asp)
- [`$_SESSION`](https://www.w3schools.com/php/php_sessions.asp)

## _GET  ,  $_POST

Special Variables used to collect data from an html form data is sent to the file in the action attribute of <form> .

```php
<formm action="index.php" method="post">
    <lable>username :</lable><br>
    <input type="test" name="username">
    <lable>password :</lable><br>
    <input type="password" name="password">
    <input type="submit" value="Log In">
</form>
<?PHP
echo "{$_POST["username"]}<br>" ;
echo "{$_POST["password"]}<br>";
?>
```

$_GET   

1-  Data is appended to the URL  “ [localhost/index.php?username=alaa&password=1337](http://localhost/index.php?username=alaa&password=1337) ”

2-  Not Secure  , Char Limit

3-  Better for search page

$_POST  

There are two main ways to send variables via the HTTP Post method:

- HTML forms
- JavaScript HTTP requests

JavaScript function

```jsx
function myfunction() {
  const xhttp = new XMLHttpRequest();
  xhttp.open("POST", "demo_phpfile.php");
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.onload = function() {
    document.getElementById("demo").innerHTML = this.responseText;
  }
  xhttp.send("fname=Mary");
  }
}

```

The code above will:

1. Intiate a HTTP request
2. Set the HTTP method to POST
3. Set a valid request header
4. Create a function to execute when the request is done
5. Send the HTTP request with a variable `fname` set to `Mary`

---

**PHP Form Validation** 

| Field | Validation Rules |
| --- | --- |
| Name | Required. + Must only contain letters and whitespace |
| E-mail | Required. + Must contain a valid email address (with @ and .) |
| Website | Optional. If present, it must contain a valid URL |
| Comment | Optional. Multi-line input field (textarea) |
| Gender | Required. Must select one |

**What is the `htmlspecialchars()` function?**

The

```
htmlspecialchars()
```

function converts special characters into HTML entities. 
This means that it will replace HTML characters like

```
<
```

and

```
>
```

with

```
&lt;
```

and

```
&gt;
```

. 
This prevents attackers from exploiting the code by injecting HTML or Javascript code
(Cross-site Scripting attacks) in forms.

wrong
`<form method="post" action="test_form.php">`

`<form method="post" action="test_form.php/"><script>alert('hacked')</script>`

secure
`<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">`

`<form method="post" action="test_form.php/&quot;&gt;&lt;script&gt;alert('hacked')&lt;/script&gt;">`

```php

<!DOCTYPE HTML>  
<html>
<head>
</head>
<body>  

<?php
// define variables and set to empty values
$name = $email = $gender = $comment = $website = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = test_input($_POST["name"]);
  $email = test_input($_POST["email"]);
  $website = test_input($_POST["website"]);
  $comment = test_input($_POST["comment"]);
  $gender = test_input($_POST["gender"]);
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<h2>PHP Form Validation Example</h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  Name: <input type="text" name="name">
  <br><br>
  E-mail: <input type="text" name="email">
  <br><br>
  Website: <input type="text" name="website">
  <br><br>
  Comment: <textarea name="comment" rows="5" cols="40"></textarea>
  <br><br>
  Gender:
  <input type="radio" name="gender" value="female">Female
  <input type="radio" name="gender" value="male">Male
  <input type="radio" name="gender" value="other">Other
  <br><br>
  <input type="submit" name="submit" value="Submit">  
</form>

<?php
echo "<h2>Your Input:</h2>";
echo $name;
echo "<br>";
echo $email;
echo "<br>";
echo $website;
echo "<br>";
echo $comment;
echo "<br>";
echo $gender;
?>

</body>
</html>
```

output

![Untitled](PHP%20af17e23dbfee43af822a7e0a3315ca0e/Untitled.png)

![Untitled](PHP%20af17e23dbfee43af822a7e0a3315ca0e/Untitled%201.png)

```php
**PHP - Required Fields**

<!DOCTYPE HTML>  
<html>
<head>
<style>
.error {color: #FF0000;}
</style>
</head>
<body>  

<?php
// define variables and set to empty values
$nameErr = $emailErr = $genderErr = $websiteErr = "";
$name = $email = $gender = $comment = $website = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $name = test_input($_POST["name"]);
  }
  
  if (empty($_POST["email"])) {
    $emailErr = "Email is required";
  } else {
    $email = test_input($_POST["email"]);
  }
    
  if (empty($_POST["website"])) {
    $website = "";
  } else {
    $website = test_input($_POST["website"]);
  }

  if (empty($_POST["comment"])) {
    $comment = "";
  } else {
    $comment = test_input($_POST["comment"]);
  }

  if (empty($_POST["gender"])) {
    $genderErr = "Gender is required";
  } else {
    $gender = test_input($_POST["gender"]);
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<h2>PHP Form Validation Example</h2>
<p><span class="error">* required field</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  Name: <input type="text" name="name">
  <span class="error">* <?php echo $nameErr;?></span>
  <br><br>
  E-mail: <input type="text" name="email">
  <span class="error">* <?php echo $emailErr;?></span>
  <br><br>
  Website: <input type="text" name="website">
  <span class="error"><?php echo $websiteErr;?></span>
  <br><br>
  Comment: <textarea name="comment" rows="5" cols="40"></textarea>
  <br><br>
  Gender:
  <input type="radio" name="gender" value="female">Female
  <input type="radio" name="gender" value="male">Male
  <input type="radio" name="gender" value="other">Other
  <span class="error">* <?php echo $genderErr;?></span>
  <br><br>
  <input type="submit" name="submit" value="Submit">  
</form>

<?php
echo "<h2>Your Input:</h2>";
echo $name;
echo "<br>";
echo $email;
echo "<br>";
echo $website;
echo "<br>";
echo $comment;
echo "<br>";
echo $gender;
?>

</body>
</html>

```

![Untitled](PHP%20af17e23dbfee43af822a7e0a3315ca0e/Untitled%202.png)

in the following code we have added some new variables: `$nameErr`, `$emailErr`, 
`$genderErr`, and `$websiteErr`. These error variables will hold error messages for the 
required fields. We have also added an `if else` statement for each `$_POST` variable. This 
checks if the `$_POST` variable is empty (with the PHP `empty()` 
function). If it is empty, an error message is stored in the different error variables, 
and if it is not empty, it sends the user input data through the `test_input()` 
function.

---

## **PHP Date and Time**

date( )

```php
echo date("Y")      //2024
echo "Today is " . date("Y/m/d") . "<br>";       //Today is 2024/05/16
echo "Today is " . date("Y.m.d") . "<br>";       //Today is 2024.05.16
echo "Today is " . date("Y-m-d") . "<br>";       //Today is 2024-05-16
echo "Today is " . date("Y-M");                  //Today is 2024-May
echo "Today is " . date("d");                    //Today is 16
```

**Get Your Time Zone:**

```php
date_default_timezone_set("America/New_York");
echo "The time is " . date("h:i:sa"); //10:51:37
date_default_timezone_set("Egypt");
echo "The time is " . date("h:i:sa");//05:51:37
```

## Create a Date With mktime()

The optional *timestamp* parameter in the date() function specifies a timestamp. If 
omitted, the current date and time will be used (as in the 
examples above).

The PHP `mktime()` function returns the Unix timestamp for a date. The Unix timestamp contains the number of seconds between the Unix Epoch 
(January 1 1970 00:00:00 GMT) and the time specified.

### Syntax

```php
mktime(*hour, minute, second, month, day, year*)
```

The example below creates a date and time with the 
`date()` function from a number of parameters in the 
`mktime()` function:

```php
 <?php
$d=mktime(11, 14, 54, 8, 12, 2014);
echo "Created date is " . date("Y-m-d h:i:sa", $d);
?> 
```

**String Length ⇒**`echo strlen("Hello world!");`

**Word Count ⇒**`echo str_word_count("Hello world!");` 

data type of variable **⇒**

```php
var_dump($variable_name);
```

## If statement and for loop and switch statement

> ***all same as cpp .***
> 

---

## Filter Function

filter_list ( )  ⇒ returns a list of all supported filters

filter_id ( )    ⇒ get a id of filter by filter name

filter_var ( )   ⇒ take value or variable i would to chick it and take filter_name or filter_id

```php
<?php
print_r(filter_list());  //print supported filters as array of filters 
echo filter_id("boolean"); //print a id of boolean filter
-------------------------------------------------------------------
$var = true;
//if(filter_var($var,258)) //with id
if(filter_var($var,FILTER_VALIDATE_BOOL))   //with name
{
echo "true"
} else {
echo"false"
}
?>
```

- **Filters Type**
    - **FILTER_VALIDATE ( للتحقق من الشيئ موجود بالوضع الصيحيح ولا لا )**
        
        FILTER_VALIDATE_BOOL
        
        FILTER_VALIDATE_URL
        
        FILTER_VALIDATE_IP
        
        FILTER_VALIDATE_MAC
        
        FILTER_VALIDATE_EMAIL
        
        FILTER_VALIDATE_FLOAT
        
        FILTER_VALIDATE_INT
        
    - **SANITIZE FILTER ( للتحقق من صحه الحروف والارقام داخل الشئ بعد التاكد من وضعه الصحيح )**
        
        FILTER_SANITIZE_EMAIL (remove all but letters + digits + ! @ ~ %  $ # ^ _ ` + _ = ’ ? { } | . [  ] )
        
        FILTER_SANITIZE_NUMBER_INT (remove all but  digits , + , -  )
        
        FILTER_SANITIZE_NUMBER_FLOAT (remove all but  digits , + , -  and [ . , eE] )
        
        FILTER_SANITIZE_EMAIL (remove all but letters + digits + ! @ ~ %  $ # ^ _ ` + _ = ’ ? { } | . [  ]  , ( )  \\ < > “ ; / : )
        
    - **FILTER_INPUT  ( TYPE [required] , VALUE [ required ] , FILTER [ optional ] , OPTIONS [ optional ]  )**
        
        INPUT_GET
        
        INPUT_POST 
        
        INPUT_COOKIE
        
        INPUT_SERVER
        
        INPUT_ENV
        
    
    ```php
     <?php
    $ip = "127.0.0.1";
    
    if (!filter_var($ip, FILTER_VALIDATE_IP) === false) {
      echo("$ip is a valid IP address");
    } else {
      echo("$ip is not a valid IP address");
    }
    ?> 
    ```
    

```php
<?php
$int = 100;

if (!filter_var($int, FILTER_VALIDATE_INT) === false) {
  echo("Integer is valid");
} else {
  echo("Integer is not valid");
}
?> 
```

```php
<!DOCTYPE html>
<html>
<body>

<form method="get" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>"> 
E-mail: <input type="text" name="email">
<input type="submit" name="submit" value="Submit"> 
</form>

<?php
if (isset($_GET["email"])) {
    if (!filter_input(INPUT_GET, "email", FILTER_VALIDATE_EMAIL , FILTER_SANITIZE_EMAIL) === false) {
        echo("Email is valid");
    } else {
        echo("Email is not valid");
    }
}
?>

</body>
</html>
```

## Include Function

```php
<php
include("header.html")
include("index.html")
include("footer.html")
?>
```

or

```php
<html>
<body>

<div class="menu">
<?php include 'menu.php';?>
</div>
```

# **PHP Cookies**

A cookie is often used to identify a user. A cookie is a small file that the server embeds on the user's computer. Each time the same computer requests a page with a browser, it will send the cookie too. With PHP, you can both create and retrieve cookie values.

## Create Cookies With PHP

A cookie is created with the `setcookie()` function.

### Syntax

```php
<php
setcookie()
setcookie(*name[required], value, expire, path, domain, secure, httponly*);
?>
```

name  =  cookie named 

value  = name of value

*expire = time() + (86400 * 30)      //86400   =  1 day*

*path*

*domain*

*secure*

*httponly*

```php
 <?php
$cookie_name = "user";
$cookie_value = "John Doe";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
?>
<html>
<body>

<?php
if(!isset($_COOKIE[$cookie_name])) {
  echo "Cookie named '" . $cookie_name . "' is not set!";
} else {
  echo "Cookie '" . $cookie_name . "' is set!<br>";
  echo "Value is: " . $_COOKIE[$cookie_name];
}
?>

</body>
</html> 
```

# **PHP Sessions**

A session is a way to store information (in variables) to be used across multiple pages.

Unlike a cookie, the information is not stored on the users computer.

الفرق بين السيشن والكوكيز 

الكوكيز ⇒  بتتخزن في الاستوريدج بتاعت الالبراوزر

السيشن ⇒  بتتخزن في متغير عشوائي في الاستوريدج بتاعت السيرفر 

السيرفر بيتعرف ع المستخدم عن طريق يوزر كي اللغه بتنشئه ليك وبتخزنه او بتضيفه في الكوكيز 

we use session_start( ) function to access the soper global var $_SESSION

بنستخدم السيشن عشان بنحتاج الاسم و الارقم السمتخدم مثلا او اعدادات المستخدم عاملها في كل السبدومينز عشان المستخدم مش هيسجل في كل سبدومين لوحده 

```php
<?php
// Start the session
session_start();
// Set session variables
$_SESSION["name"] = "mersa";
$_SESSION["id"] = 1541;
echo "Session variables are set.";
?>
```

session_id( )   ⇒ return the id of session

الايدي دا عباره عن اسم ملف موجود في ال تيمب ف ملفات الاجزامب وداخل الملف موجود محتويات السيشن  

 **remove all session variables**

session_unset();

destroy the session 

session_destroy();

---

# File System Function

disk_total_space( “ ” ) ⇒

بترجع المساحه بالبايت 

 kilo byte     [KB]= 1024 byte 

miga  byte  [MB]= 1024 kilo byte = 1024 * 1024 byte 

giga byte     [GB]= 1024  miga  byte =1024 * 1024 kilo byte = 1024 * 1024 * 1024 byte 

The fun return bytes so if i need GB:

```php
disk_total_space("C:")  / 1024 / 1024             //98.12312 GB
echo round(disk_total_space("C:")  / 1024 / 1024 )  //98 GB
```

disk_free_space( “ ” )  ⇒

return the free space of director .

file_exists( “ index.html ” )  ⇒

return true if the file index is exist in director and false if not exist .

---

> *note* : ctrl + shift + n ⇒ create new director
> 

---

is_dir( “name”) ⇒

return true if the name  is director  and false if not a dir.

mkdir( “path_naem”) ⇒

create a new director 

```php
mkdir( path[require] , mode[optional] = 0777 , recursive [optional] ,context [optional])
```

*note  :* permissions is ignored on windows 

0777

permissions  is octal number start with 0

second num [ 7 ] ⇒  owner permission 

third num [ 7 ] ⇒  user group permission 

second num [ 7 ] ⇒  for others permission 

| Symbolic notation | Numeric notation | English |
| --- | --- | --- |
| ---------- | 0000 | no permissions |
| -rwx------ | 0700 | read, write, & execute only for owner |
| -rwxrwx--- | 0770 | read, write, & execute for owner and group |
| -rwxrwxrwx | 0777 | read, write, & execute for owner, group and others |
| ---x--x--x | 0111 | execute |
| --w--w--w- | 0222 | write |
| --wx-wx-wx | 0333 | write & execute |
| -r--r--r-- | 0444 | read |
| -r-xr-xr-x | 0555 | read & execute |
| -rw-rw-rw- | 0666 | read & write |
| -rwxr----- | 0740 | owner can read, write, & execute; group can only read; others have no permissions |

recursive :

في حاله اني خليته يعمل دايريكتور جوا دايريكتور هيديني ايررو لان الديفولت بتاعها فولس

```php
mkdir("admin/dir/temp" , 0700)        //error
mkdir("admin/dir/temp" , 0700 , true)        //done 
```

rmdir( “test ”) ⇒  

if test is empty the mrdir will delete it but if not empty , it return error

pathinfo( )

```php
echo "<pre>";
print_r(pathinfo(__FILE__))       //__FILE__  = mean the file i exist naw
echo "<pre>";
```

outpot

```
Array
(
    [dirname] => D:\xampp\htdocs
    [basename] => index.php
    [extension] => php
    [filename] => index
)
اقدر اكسس اي واحده عن طريق الانديكس
```

---

The `readfile()` function reads a file and writes it to the output buffer.

```php
 <?php
echo readfile("webdictionary.txt");
?> 
JUST DISPLAY THE CONTENT OF THE FILE
```

A better method to open files is with the `fopen()` function. This function gives you more 
options than the `readfile()` function.

> fopen ( filename [require]  ,  mode [require] , includepath [optional ]  , context [optional ] )
> 

MODEs

[ r ]        →   for read , pointer at the beginning

[ r+ ]      →  for read & write , pointer at the beginning

[ w ]       →  for  write , pointer at the beginning + truncate to 0 length , create if not exist 

[ w + ]   →  for read & write , pointer at the beginning + truncate to 0 length , create if not exist 

alaa.txt contain 

alaa

hassan

mohamed

```php
$handle = fopen(" alaa.txt " )
```

fgets ( file_name , length )            & fread ( file_name , length [ requires] )

```php
echo fgets($handele) 
fclose($handele)            //لازم لما نخلص نقفل 
```

```php
 <?php
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = "John Doe\n";
fwrite($myfile, $txt);
$txt = "Jane Doe\n";
fwrite($myfile, $txt);
fclose($myfile);
?> 
```

The `fwrite()` function is used to write to a file.

The first parameter of `fwrite()` contains the name of the file to write to and 
the second parameter is the string to be written.

---

**copy() Function:**

Copy "source.txt" to "target.txt":

```php
 <?php
echo copy("source.txt","target.txt");
?> 
```

**unlink() Function:**

```php
 <?php
$file = fopen("test.txt","w");
echo fwrite($file,"Hello World. Testing!");
fclose($file);

unlink("test.txt");             //equal delete
?> 
```

---

**glob() Function :**

Return an array of filenames or directories that matches the specified pattern:

```php
 <?php
print_r(glob("*.txt"));
?> 

result:

Array (
  [0] => target.txt
  [1] => source.txt
  [2] => test.txt
  [3] => test2.txt
)
```

**rename() Function:**

Rename a directory + a file: in same place or another place .

rename(old , new);              //equl move or cut

```php
 <?php
rename("images","pictures");
rename("/test/file1.txt","/home/docs/my_file.txt");
?> 
```

### **file()        vs     file_get_contents()**

**file()    =** Read a file into an array:

```php
 <?php
print_r(file("test.txt"));
?> 

result

 Array 
 (
   [0] => Hello, this is a test file.
   [1] => There are three lines here. 
   [2] => This is the last line. 
 ) 
```

**file_get_contents() = Read a file into a string:**

```php
 <?php
echo file_get_contents("test.txt");
?> 

result

 Hello, this is a test file. There are three lines here. This is the last line. 
```

---

---
# Python Assignments

# Ex. 1 Random number
Create a program that creates a list of 10 random numbers and sums all the numbers.  The result is printed to the console.  The numbers in the list range from 0 - 100.  The program must use an f-string to display the output.

Example list: `[1, 34, 2, 33, 45, 67, 24, 87, 32, 38]`

Example Output:
```
The sum is: 363
```

# Ex. 2 Python in a Box
Create a program that uses the `input()` function to obtain the width, height and length of a box.  The program computes the volume of the box (width * height * length) and writes it to the console:

Example input:
```
Enter width: 1.1 
Enter height: 1.2
Enter length: 1.3
```

Example output:
```
Volume is: 1.72.
```

# Ex. 3 First and Last
Create a program that accepts a list of numbers using the `input()` function and writes `True` if the first and last numbers are the same, otherwise write `False` to the console.

Example input:
```
Enter list of numbers: 1,2,3
```

Example output:
```
False
```
# Ex. 4 Word Count
Create a program that counts the number of times the word `Python` appears in the text below and writes the result to the console. Do not use the `string.count()` method.

```
"Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
```
 Example output:
```
3
```

# Ex. 5 Bigger Set
Create a program that adds the following List of numbers to the Set and writes the final Set to the console:
```
myList = [1,2,3]
mySet = {3,4,5}
```
Example output:
```
{1,2,3,4,5}
```
# Ex. 6 Reverse Me
Create a program that writes the following list of numbers in reverse order to the console:
```
[11, 100, 101, 999, 1001]
```
Example output:
```
[1001, 999, 101, 100, 11]
```

# Ex. 7 Winner Winner
Create a program that generates a randon number between 1 and 100.  If the number is less than 10 the program prints the value of the number and `You lose.` on the console.  If the number is greater than 10 and less than 50 the program prints the value of the number and `Try again.` on the console.  If the number is greater than 50 the program prints the value of the number and `You win!` on the console.

Example output:
```
9: You lose.
17: Try again.
86: You win!
```

# Ex. 8 Shortest Straw
Create a program that finds the smallest number in this list and writes the result to the console.  Do not use the `min()` or `sort()` functions.
```
myList = [6,2,7,3,77,7,1]
```
Example output:
```
1
```

# Ex. 9 Uppers or Lowers
Create a program that writes `True` to the console if a string is upper case, `False` if a string is not.

Example input:
```
Enter string: "HELLO"
```

Example output:
```
True
```

# Ex. 10 Vs and Cs
Create a program that counts all the vowels and consonants in a word and writes the count to the console:

Example input:
```
Enter string: Apple
```

Example output:
```
Vowels: 2
Consonants: 3
```

# Ex. 11 Write Today's Date
Create a program that writes the current date to a file named: `output.txt`.  The program must use an f-string when writing to a file.

File Contents:
```
Today's date is: 08/17/2021.
```

# Ex. 12 Negative to Positive / Positive to Negative
Create a program that prompts the user to enter an integer value.  The program converts a positive integer to a negative integer, and converts a negative integer to a positive integer.  The result is written to the console. The program returns an error if the user enters a float value.  Do not use the `abs()` function.

Examples:
```
Enter integer: 12
-12
```

```
Enter integer: -133
133
```

```
Enter integer: 123232.1
ERROR: 123232.1 is not an integer.
```

# Ex. 13 Add Only Calculator
Create a program that prompts the user for two integers and adds them.  The program runs indefinitely until `exit` is typed.

Example:
```
Enter first integer: 1
Enter second integer: 3
Answer: 4.
Enter first integer: 5
Enter second integer: 5
Answer: 10.
Enter first integer: exit
```

# Ex. 14 Forever Calculator
Extend Exercise 13 and create a program that prompts the user for two integers.  The program also asks the user for a mathmetical operation (add, subtract, multiply, divide).  The program runs indefinitely until `exit` is typed.  Ensure the program does not crash when dividing by zero.

Example usage:
```
Enter first integer: 3
Enter second integer: 1
Enter operation (add, sub, mul, div): sub
Answer: 2.0
Enter first integer: 3
Enter second integer: 4
Enter operation (add, sub, mul, div): mul
Answer: 12.0
Enter first integer: exit
```

# Ex. 15 Forever Calculator Logger
Extend Exercise 14 and log every calculation to a file named `output.txt`.

Example log file:
```
08/17/2021 07:59:36 PM: 1.0 add 2.0 = 3.0
08/17/2021 07:59:40 PM: 4.0 sub 5.0 = -1.0
08/17/2021 07:59:44 PM: 2.0 mul 6.0 = 12.0
08/17/2021 07:59:51 PM: 1.0 div 2.0 = 0.5
```

# Ex. 16 Hash It, Print It
Hashing is often applied to passwords.  Instead of storing raw passwords in backend systems, passwords are hashed (optionally with a salt value) and the hash value is stored.

Create a program that prompts the user to enter a username and password.  The program hashes the password
using the `sha256()` algorithm and stores it in a dictionary.  The key for the dictionary is the user name.  The program loops forever unti `exit` is entered.  When `exit` is entered the program prints the key/value pairs from the dictionary to the console.

Example Usage:
```
Enter username: mburolla
Enter password: test
Enter username: joe
Enter password: test2
Enter username: exit
mburolla : 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
joe : 60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752
```

# Ex. 17 Simple Authentication, No Authorization
#### Background
Authentication is the process in which a set of credentials is validated.  Authorization is what the user is allowed to do once they have been Authenticated. To summarize, Authentication is proving who you are and Authorization is what you are allowed to do.

Extend the program created in Exercise 16 and prompt the user to select one of two modes: 
#### Add User 
"Add user mode" adds users to the dictionary (essentially Exercise 16).
#### Login 
"Login mode" provides a user to login with their username and password.  The program prints `Password is correct.` when the user has entered the correct password, and prints `Incorrect password.` when the password is incorrect.  If the user does not exist in the dictionary, print `User does not exist.`.

Example Usage:

```
Type exit at anytime to end program...
Enter mode (add|login): add
Enter username: mburolla
Enter password: test
Enter mode (add|login): login
Enter username: mburolla
Enter password: test
Password is correct.
Enter mode (add|login): login
Enter username: mburolla
Enter password: wrongpassword
Incorrect password.
Enter mode (add|login): exit
mburolla : 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
```

#### Pseudocode
```
main: 
  
  dictionary = {}

  loop:
    mode = input(enter mode)

    if mode is add:
      ex 16 stuff here...

    if mode is login:
      New stuff here...
      username = input(username)
      password = input(password)

      hashpassword = hash(password)
      lookup hashpassword for this user in dictionary
      compare hashes, print results
```

# Ex. 18 Random Number Game
Create a program generates a random number 1-10 inclusive.  The program prompts the user to enter a number between 1-10.  If the user number is too low the program prints `Too low`.  If the user number is too high, the program prints `Too high`.  If the user number is equal to the number the program generated print `You guessed it!!!` and the program terminates.

Example Usage:
```
Enter a number between 1-10: 5
Too high
Enter a number between 1-10: 1
Too low
Enter a number between 1-10: 4
Too high
Enter a number between 1-10: 3
Too high
Enter a number between 1-10: 2
You guessed it!!!!
```

# Ex. 19 Frame It
Create a program that contains a list of strings and prints them in a frame on the console:

```
wordlist = ["Hello", "World", "in", "a", "frame"]
```
```
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
```

# Ex. 20 Super Simple File Indexer
Create a program that reads the words from the following file: [input-file-1.txt](http://www.google.com).  The program contains a dictionary that keeps track of the word count and prints the results to the console.

Example output:
```
This:4
is:4
a:1
test:1
to:1
see:1
how:1
.
. 
.
```

# Ex. 21 Blast Off!!!
Create a program that asks the user for a countdown value in seconds, and then starts printing the countdown. When the countdown ends the program displays `Blast off!!!` on the console.  If the user enters a negative value, the programs terminates with an error message. 

Example output:
```
Enter countdown (sec): 5
5
4
3
2
1
Blast off!!
```

# Ex. 22 Morse Codify It
Create a program that converts text to morse code.  The program loops indefinitely until `control+c`is entered by the user.  The program will contain a function called `convertTextToMorseCode(inputString)`.  This function contains a parameter called `inputString` and will contain the following dictionary:

```
textToMorseDict = {
  'a' : '*-',
  'b' : '-***',
  'c' : '-*-*',
  'd' : '-**',
  'e' : '*',
  'f' : '**-*',
  'g' : '--*',
  'h' : '****',
  'i' : '**',
  'j' : '*---',
  'k' : '-*-',
  'l' : '*-**',
  'm' : '--',
  'n' : '-*',
  'o' : '---',
  'p' : '*--*',
  'q' : '--*-',
  'r' : '*-*',
  's' : '***',
  't' : '-',
  'u' : '**-',
  'v' : '***-',
  'w' : '*--',
  'x' : '-**-',
  'y' : '-*--',
  'z' : '--**'
}
```

This function will also contain the necessary business logic to convert English text to morse code.  Place a space between each Morse code and two spaces between each word.

Example Usage
```
Enter text: python rocks
Morse Code: *--* -*-- - **** --- -*  *-* --- -*-* -*- *** 
Enter text: marty was here
Morse Code: -- *- *-* - -*--  *-- *- ***  **** * *-* * 
```

 # Ex. 23 Morse to Text, Text to Morse
 Extend exercise 22 to convert Morse Code to text.  The program will contain a function called: `convertMorseCodeToText(morseCode)`.  This function contains a parameter called `morseCode` and will contain the following dictionary:

 ```
   morseToTextDict = {
    '*-'   : 'a', 
    '-***' : 'b',
    '-*-*' : 'c',
    '-**'  : 'd',
    '*'    : 'e',
    '**-*' : 'f',
    '--*'  : 'g',
    '****' : 'h',
    '**'   : 'i',
    '*---' : 'j',
    '-*-'  : 'k',
    '*-**' : 'l',
    '--'   : 'm',
    '-*'   : 'n',
    '---'  : 'o',
    '*--*' : 'p',
    '--*-' : 'q',
    '*-*'  : 'r',
    '***'  : 's',
    '-'    : 't',
    '**-'  : 'u',
    '***-' : 'v',
    '*--'  : 'w',
    '-**-' : 'x',
    '-*--' : 'y',
    '--**' : 'z'
  }
```

This function will also contain the necessary business logic to convert more code to English.

Example output:
```
Enter text or morse code: python rocks
Morse Code: *--* -*-- - **** --- -*  *-* --- -*-* -*- *** 
Enter text or morse code: *--* -*-- - **** --- -*  *-* --- -*-* -*- *** 
Text: python rocks 
```

# Ex. 24 Diagon Alley
Create a program that contains a function called `printDiagonally(word)`.  This function has a parameter called `word` and prints the word diagonally to the console.  The program prompts the user to enter a sentence.

Example Ouput:
```
Enter text: this is a test
t
 h
  i
   s
i
 s
a
t
 e
  s
   t
```
# Ex. 25 Count Case
Create a program that accepts a sentence and calculates the number of upper case letters and lower case letters.

Example output:
```
Enter text: This is a Test.
Upper case: 2
Lower case: 9
```

# Ex. 26 Print Dictionary
Create a program that contains a function called `printDictionary(dictionary)`.  This function contains a parameter called dictionary.  The function uses an f-string and prints the following dictionary to the screen in ascending order:
```
personDictionary = {
   '222-22-2222' : 'joe',
   '333-33-3333' : 'fred',
   '555-55-5555' : 'mary',
   '444-44-4444' : 'fred',
   '111-11-1111' : 'jane'
}
```
Example output:
``` 
111-11-1111 : jane
222-22-2222 : joe
333-33-3333 : fred
444-44-4444 : fred
555-55-5555 : mary
```
# Ex. 27 Lambda Sort & Print
Create a program that contains a function called `printPersonList(peopleList)`.  This function takes a parameter called `peopleList`.  `PeopleList` is defined below:

```
  peopleList = [
    { 
      'name' : 'joe', 
      'age' : 20 
    },
    { 
      'name' : 'fred', 
      'age' : 10 
    },
    { 
      'name' : 'sally', 
      'age' : 30 
    },
    { 
      'name' : 'sue', 
      'age' : 15 
    }
  ]
```

The function sorts `peopleList` by age (asc) and prints it to the console.

Example output:
```
fred : 10
sue : 15
joe : 20
sally : 30
```
 # Ex. 28 Split & Print
Given the following list:
 
`numList = [1,2,3,4,5,6,7,9,10,11]`

Create a function called `splitAndPrint(numList)` that takes a parameter named numList.  The function prints the fist half and the second half of the list on the console.  Make sure the function can accept list of various lengths.

Example ouput:

```
First half: [1, 2, 3, 4, 5]
Second half: [6, 7, 9, 10, 11]
```

 # Ex. 29 Floor It
 Implement the function stub in your student directory called `my_floor()`.  The `my_floor()` function will operate like the Python `floor()` function.  Do not use the `floor()` function in your floor function.  Make sure you switch to the `dev` branch before you pull the latest changed from the remote repo (`git pull origin dev`)

Desired output:
```
2 2
2 2
-3 -3
-4 -4
```
# Ex. 30 Filter
Given the following list:

```
  carList = [
    { 
      'make': 'ford' , 
      'engine' : { 'size' : 3.0, 'type': 'V6' } 
    },
    { 
      'make': 'chevy', 
      'engine' : { 'size' : 5.0, 'type': 'V8' }
    },
    { 
      'make': 'toyota',
      'engine' : { 'size' : 2.0, 'type': 'Flat 4' } 
    },
    { 
      'make': 'honda',
      'engine' : { 'size' : 5.2, 'type': 'Straight 6' },
    }
  ]
```

Use the `filter()` function to create a list that contains engines greater than 4.0 liters (size).  Print the list to the console.

Ouput:
```
chevy : 5.0
honda : 5.2
```

# Ex. 31 Map
Given the following list:

```
  carList = [
    { 
      'make': 'ford' , 
      'engine' : { 'size' : 3.0, 'type': 'V6' },
      'cost' : 20000 
    },
    { 
      'make': 'chevy', 
      'engine' : { 'size' : 5.0, 'type': 'V8' },
      'cost' : 23000 
    },
    { 
      'make': 'toyota',
      'engine' : { 'size' : 2.0, 'type': 'Flat 4' },
      'cost' : 24000 
    },
    { 
      'make': 'honda',
      'engine' : { 'size' : 5.2, 'type': 'Straight 6' },
      'cost' : 24000 
    }
  ]
```

Use the `map()` function to produce a new list:

Output:

```
[{'ford': 'V6'}, {'chevy': 'V8'}, {'toyota': 'Flat 4'}, {'honda': 'Straight 6'}]
```

The solution to this is one line of code.

# Ex. 32 Filter People
Create a program that contains two functions.  These functions are called by the `main()` function:

- `createPeopleList()`
- `filterPeopleList(peopleList)`

The `createPeopleList()` creates a list with the following people objects:
- 'name': 'joe',  'sex': 'male'
- 'name': 'fred', 'sex': 'male' 
- 'name': 'sue',  'sex': 'female' 
     
The `filterPeopleList(peopleList)` function accepts the peopleList and returns only the males.

The `main()` function uses an f-string and prints the names of all the males to the console:

Output
```
joe
fred
```

# Ex. 33 Exceptions
 Modify `ex-33.py` in your student directory to catch all the errors thrown by the program (`try/except`) so that the program fails gracefully with an error message to the console.

Example:
```
File not found
```

# Ex. 34 Create, Sort, Filter, Print
Create a program that has the following architecture:

```
def main():
  list = createList()
  sorted = sortList(list)
  filtered = filterList(sorted)
  printList(filtered)
```

The `createList()` function returns the following dataset:
```
  personList = [
    { 'ssn': '222-22-2222' , 'name' : 'charlie', 'weight' : 150 },
    { 'ssn': '333-33-3333' , 'name' : 'bob', 'weight' : 150 },
    { 'ssn': '555-55-5555' , 'name' : 'mary', 'weight' : 140 },
    { 'ssn': '444-44-4444' , 'name' : 'fred', 'weight' : 130 },
    { 'ssn': '111-11-1111' , 'name' : 'alex', 'weight' : 150 }
  ]
```

The `sortList()` function sorts the list by name (asc), The `filterList()` function filters the sorted list for people that weight 150 pounds.  The `printList()` function prints the list to the console:

```
alex : 150 
bob : 150 
charlie : 150 
```

# Ex. 35 Map Weight Loss
Given the following dictionary:

```
  personList = [
    { 'ssn': '222-22-2222' , 'name' : 'charlie', 'weight' : 150 },
    { 'ssn': '333-33-3333' , 'name' : 'bob', 'weight' : 150 },
    { 'ssn': '555-55-5555' , 'name' : 'mary', 'weight' : 140 },
    { 'ssn': '444-44-4444' , 'name' : 'fred', 'weight' : 130 },
    { 'ssn': '111-11-1111' , 'name' : 'alex', 'weight' : 150 }
  ]
```

Use the `map()` function to subtract 10 pounds from the weight for each person and print the following results to the console:

```
[{'charlie': 140}, {'bob': 140}, {'mary': 130}, {'fred': 120}, {'alex': 140}]
```
# Ex. 36 Map Number Lookup

Given the following:

```
  numDict = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four'
  }
  numList = [1,2,3,4]
```

Use the `map()` function to iterate over `numList`.  Each iteration will lookup the textual representation for the current number using the `numDict`.  Display the list in descending order.

Output:
```
['Four', 'Three', 'Two', 'One']
```

# Ex. 37 Tuple to Set Conversion
Given the following tuples:

```
tuples = [(1,'red'), (2, 'blue'), (3, 'green'), (4, 'green'), (5, 'red')]
```

Convert `tuples` to a set using the `map()` function.

Output:
```
{'blue', 'red', 'green'}
```

# Ex. 38 Carpets
You are a developer that works at a company called Our Carpets Really Are Pricey (OCRAP) Inc. The price to install carpet is $7.89 per square foot.  You have to calculate the price for a customer given the following data:
```
  roomsList = [
    { 
      'room' : 
      { 
        'name' : 'kitchen',
        'color' : 'blue',
        'dimensions' : 
        { 
          'width' : 10, 'length' : 10, 'height' : 8 
        }
      }
    },
    { 
      'room' : 
      { 
        'name' : 'living room',
        'color' : 'blue',
        'dimensions' : 
        { 
          'width' : 10, 'length' : 20, 'height' : 10 
        }
      }
    },
    { 
      'room' : 
      { 
        'name' : 'family room',
        'color' : 'tan',
        'dimensions' : 
        { 
          'width' : 10, 'length' : 20, 'height' : 8 
        }
      }
    },
    { 
      'room' : 
      { 
        'name' : 'bathroom',
        'color' : 'blue',
        'dimensions' : 
        { 
          'width' : 5, 'length' : 8, 'height' : 10 
        }
      }
    }
  ]
```

How much will it cost to install carpet for only the blue rooms?


# Ex. 39 Comprehending List Comprehensions
Given the following list:

```
numList = [1,2,3,4,5,6,7,8,9,10]
```

Create a list comprehension that that filters the list for all the even numbers and doubles each number and prints the results to the console.

Output
```
[4, 8, 12, 16, 20]
``` 

# Ex. 40 Tiny Movie Theater
### Part A.
Create a program that displays and keeps track of occupied seats for a tiny movie theater.  The theater has 3 rows with 10 seats in each row.  The program displays empty seats with a '0' and occupied seats with 'X'.  Row 1 is upper top left, Seat 10 is far right.

The program loops forever until `control+c` is entered by the user.

The program prompts the user to enter the row number and seat number.  Once the row number and seat number have been entered, the program displays all the seats.  The program displays the appropriate error message if the row number and seat number not valid.

Example usage:
```
0000000000
0000000000
0000000000
Enter row number: 1
Enter seat number: 1
X000000000
0000000000
0000000000
Enter row number: 2
Enter seat number: 5
X000000000
0000X00000
0000000000
Enter row number: 3
Enter seat number: 10
X000000000
0000X00000
000000000X
Enter row number: 4 
Enter seat number: 11
ERROR: Not enough rows and seats
X000000000
0000X00000
000000000X
Enter row number: 1   
Enter seat number: 11
ERROR: Not enough seats
X000000000
0000X00000
000000000X
```

HINT: Try to implement the solution from start to finish only using 1 row with 10 seats (optionally commit and push your branch), then modify your solution to support 3 rows with 10 seats.

HINT: My architecture:
```
def printSeats(movieSeats, numRows, numSeats):
  ...

def validateInput(row, seat, numRows, numSeats):
  raise Exception if not valid

def main():
  numRows = NUM_ROWS
  numSeats = NUM_SEATS
  movieSeats = ['0' for _ in range(numRows * numSeats)]
 
  while True:
    # print the seats
    # get row & seat number from user
    # validate user input
    # catch Exception, print error message
    # calculate seat index
    # add 'X' to list at seat index position
```


### Part B.
Prompt the user to enter the size of the movie theater only once when the program first runs.  You can assume the user input will be valid numbers (no reason to validate this input).

Example:
```
Enter number of rows: 2
Enter number of seats: 5
00000
00000
Enter row number: 1
Enter seat number: 1
X0000
00000
Enter row number: 3
Enter seat number: 1
ERROR: Not enough rows
X0000
00000
```
### Part C.
Print the total cost of ticket sales after a valid row and seat number have been added.  The cost of a movie ticket is linearly proporational to the row number.  In other words, tickets for row 1 cost $1.00, tickets for row 2 cost $2.00, tickets for row 3 cost $3.00, etc.  Be sure only to increment the ticket sales if a seat has not been sold.

Example 1:
```
Enter number of rows: 2
Enter number of seats: 10
0000000000
0000000000
$0.00
Enter row number: 1
Enter seat number: 5
0000X00000
0000000000
$1.00
Enter row number: 2
Enter seat number: 1
0000X00000
X000000000
$3.00
```

Example 2:
```
Enter number of rows: 1
Enter number of seats: 1
0
$0.00
Enter row number: 1
Enter seat number: 1
X
$1.00
Enter row number: 1
Enter seat number: 1
X
$1.00
```

### Part D.
Provide the user a way to exit the program (type exit).  When the user has exited the program, create a text file that represents the final state of the movie theater.  Store the file in S3 using the file keypath schema: `{your name}/movie/output.txt`

Example file contents:
```
0000X00000
X000000000
$3.00
```

# Ex. 41 Mask SSN
Given the knowledge obtained about short-circuiting, and given the following list:
```
  peopleList = [
    { 'ssn' : '222-22-2222' , 'name' : 'charlie' },
    { 'ssn' : '333-33-3333' , 'name' : 'bob' },
    { 'ssn' : '555-55-5555' , 'name' : 'mary' },
    { 'ssn' : '444-44-4444' , 'name' : 'fred' },
    { 'ssn' : '111-11-1111' , 'name' : 'alex' }
  ]
```
Create a Python program that uses the `map()` function and replaces all the social security numbers with `xxx-xx-xxxx`.

- Hint #1: A dictionary has an `update()` method that you might find useful.
- Hint #2: The `update()` method is an in-place method and does not return anything.

Output
```
[{'ssn': 'xxx-xx-xxxx', 'name': 'charlie'}, {'ssn': 'xxx-xx-xxxx', 'name': 'bob'}, {'ssn': 'xxx-xx-xxxx', 'name': 'mary'}, {'ssn': 'xxx-xx-xxxx', 'name': 'fred'}, {'ssn': 'xxx-xx-xxxx', 'name': 'alex'}]
```
# Ex. 42 Access Denied
Given the following data:
```
  peopleList = [
    { 'ssn' : '222-22-2222' , 'name' : 'joe' },
    { 'ssn' : '333-33-3333' , 'name' : 'bob' },
    { 'ssn' : '555-55-5555' , 'name' : 'tim' },
  ]
  accessDict = {
    '222-22-2222' : True,
    '333-33-3333' : False,
    '555-55-5555' : False,
  }
```
Create a promgram that checks to see if people have access to your server.  The program prompts the user for a username and runs until `control+c` is entered.  The program must handle users that do not exist.

Example:
```
Enter Username: Tim
Access denied.
Enter Username: Joe
Access granted.
Enter Username: Bob
Access denied.
Enter Username: Fred
Username does not exist.
```

# Ex. 43 Moving Company
You are a developer for a moving company call Move It Or Lose It (MIOLI) Inc.  You charge customers based on the size of the moving box.  Given the following data, how much will it cost to move this customer?

```
 costPerBoxDict = {
    'small' : 5.00,
    'medium' : 10.00,
    'large' : 15.00
  }

  customerDict = {
    'living room' : 
      { 
        'small' : 5, 
        'large' : 4
      },
    'bedroom' : 
      { 
        'small' : 1, 
        'medium' : 4,
        'large' : 5
      },
    'bathroom' : 
      { 
        'small' : 2, 
        'large' : 1
      }
  }
```
# Ex. 44 HL7 Old School

### Part A.

[HL7](https://www.hl7.org/) stands for Health Level Seven.  The seven refers to the 7th layer of the [OSI model](https://en.wikipedia.org/wiki/OSI_model).  HL7 is a standard for communicating hospital related data at the application layer, the 7th layer in the OSI model.  There are two versions of the standard, HL7 2.0 and HL7 3.0.  HL7 3.0 is XML based, and HL7 2.0 is not.  HL7 has many different types of messages, [here](https://www.interfaceware.com/hl7-message-types?utm_medium=ppc&utm_campaign=21Q3_Awareness+(HL7+Information)&utm_term=hl7%20obx&utm_source=adwords&hsa_acc=5413177600&hsa_net=adwords&hsa_kw=hl7%20obx&hsa_ver=3&hsa_mt=b&hsa_cam=14213006772&hsa_grp=125700790517&hsa_ad=538222308215&hsa_tgt=kwd-348003101271&hsa_src=g&gclid=CjwKCAjwj8eJBhA5EiwAg3z0m3odv6GRyXBhlMvaB65JuUnhgZLL_LXx7giEoPjMAklWbmA3DYCmUhoCeeAQAvD_BwE) are the most common ones. 

An HL7 2.0 message contains segments. The segment we are interested in is the [PID Segment](https://hl7-definition.caristix.com/v2/HL7v2.4/Segments/PID).

Patient identification is a problem in the health industry. You are a developer that has to parse HL7 2.0 messages from a file named [oru-r01.hl7](https://gitlab.com/mburolla/sia/-/blob/dev/oru-r01.hl7).  Write a program that checks if the patient SSN and name in the HL7 messages stored in the file match that in the following dictionary:

```
patientDict = {
  '111-11-1111' : 'John Smith', 
  '222-22-2222' : 'Sue Anderson',
  '333-33-3333' : 'Tim McCoy'
}
```

The program writes the patient match status to the console:
```
111-11-1111 JOHN SMITH: OK
222-22-2222 SUE ANDERSON: OK
333-33-3333 TIM MCOY: No Match!!!
```

### Part B.
Provide the user with the option of downloading the HL7 text file from S3 (//siua-bucket/hl7/oru-r01.hl7) or to use the file stored locally on the filesystem.

Example:
```
Use S3? Yes
Downloading from S3...
Downloaded file from S3
111-11-1111 JOHN SMITH: OK
222-22-2222 SUE ANDERSON: OK
333-33-3333 TIM MCOY: No Match!!!
```

```
Use S3? No
111-11-1111 JOHN SMITH: OK
222-22-2222 SUE ANDERSON: OK
333-33-3333 TIM MCOY: No Match!!!
```


# Ex. 45 PyCopy
Create a python program that works like robocopy.  Robocopy only copies files that have been updated, in other words the source and destination files are different.  PyCopy will essentially sync the source and destination directories not touching files that are the same.  If a file exists in the destination directory, but does not exist in the source, the file is deleted in the destination directory.  

Example:
```
pycopy.py c:\source c:\destination
```

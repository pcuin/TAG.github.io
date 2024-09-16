---
title: 'Step 2 - Intro to Menu.py'
nav_order: 2
---

# Table of Contents
1. [Core structure](#core)
1. [Menu Template](#template)
2. [Code Comment Convention](#convention)
1. [Implementing option Q](#optQ)
1. [Implementing option ?](#opt?)
1. [Implementing option A](#optA)
1. [Implementing option W](#optW)
1. [Implementing option P](#optP)
1. [Implementing option V](#optV)
1. [Implementing option D](#optD)
1. [Implementing option G](#optG)
1. [Implementing option O](#optO)

# Code Comment Convention  <a name="convention"></a>
Code must read in context, as you read along, any coding conventions present in the code chunk MUST BE REWRITTEN. \
\
The positioning and format of each convention is intentional, which gives clues to what must be re-written. 
Comments that don't follow convention, _are conceptual comments_, which will rely on you to fill in a key data strucutre or logical step that is expected at this point in CS8. \
\
**Do not use foreign coding techniques. Ensure `elif` matches the indent level with the previous logic statements above.**

| Code structure| Notation Verbatim   | Interpretation|
|:--------------|:------------------|:------|
| Function (user)| f(x), f(x,y), f(...)| Functions that use `def` keyword <br> Ex: f(x) is the abstract hint for `print_menu(menu)`  | 
| Variable |          ...   | Any assignment operation `var = ...` <br> Ex: cat = ... is the abstract hint for `cat = 'cat'`  |
| Feature (built-in)| <p‎⁤y>   | **All** operations for this lab can be referenced [here](#cheat) <br> Ex: `str(x)` turns **x** into a **string**| 
| Container | [],{},() | yumm  |
> `Container` can be populated with familar objects, here are some:
* \[factor\]
* {stats}
* {dicto}  

**This notation will be referenced when describing several object values, like a `return` value.**
> `Variable` is usually a *return* value or *updated* value that was initialized at the start of `Menu.py`.

## Core structure <a name="core"></a>

The basis of this entire menu system consistently calls upon these core variables, which requiere consistent updating and manipulation with the prpoer functions. \
Functions aside, the menu relies on the parameters:
### Interpretting the core parameters
In scope of the program, the purposes of these variables serve as the framework to the simulation and its real-world meaning
* `factors`
> string type, the input received, allows data to be queried in the developing database
* `stats`
> dict type, stores useful analytics, allocates important numbers or measures to communicate to functions
* `lanes`
> int type, stores an independent variable, shaping the results of simulation in the long run
* `menu`
> a local dictionary, to be used to produce a visual user display that anyone can read and execute commands from
* `print_menu()`
> function, mechanism that powers the user display and formats useful dictionaries _(no nested dict allowed)_ 
* `dicto`
> dict type, mainly used to read user input data, formats user-given data {option: input} (to be discussed later)

## Menu Template  <a name="template"></a>

```py
from TrafficQueue import *

factors = []# needed for data production, also called fields or keys
dicto = {}  # needed for viewing numbers
stats = {}  # needed for viewing qualities
lanes = 0   # needed as a fixed constant
menu = {"?" : "About this program",

        "A" : "Add factors/variables",
        
        "P" : "Probabilities (means) for fields",

        "W" : "Weight scalars (relative risk) for fields",

        "V" : "View current factors",
        
        "D" : "Data summary ",

        "G" : "Generate distribution traffic flow (WIP)",

        "Q" : "Quit this program",

        "0" : "Reinitialize this program"

        }

def print_menu(menu):

    """

    Given a dictionary with the menu,

    prints the keys and values as the

    formatted options.

    Adds additional prints for decoration

    and outputs a question

    "What would you like to do?"

    """

    print("%" * 26)
    print("Query began.")

    for entry in menu:
        print(f"{entry} - {menu[entry]}")

    print("%" *26)
    print("Query finished.")

```

This is the barebone code skeleton to be expanded upon. Next, we'll give the file its display feature.

## Implementing option Q  <a name="optQ"></a>
Thanks to while loops, we can implement user display. We can use the previous code to print a bunch of guiding information.
\
A while loop has a condition to fulfill until that condition is set to False. Essentially, the options nested within a loop indicate whether or not the loop should break.
> Options will vary in its functionality, but keep in mind that `option` refers to the code signature `key`, which is a sort of wild card *input*.
>
> `key` is input to ensure the while loop moves and updates necessary condtions, like the state of the loop, among other things!

Since all data is lost once the loop breaks, we want this program to run indefnitiely, unless the simulation malfunctions or is told to do so. Hence, we will cosntruct `option Q`.

```py
while True:
    print_menu(menu)
    key = input("+ Enter an option here + ")
    key = key.upper()
    if key == "Q":

        print("Program has been stopped!\n")

        ... # how would i break a while loop on command?
```
Once we give input (Q) to our file, the loop forcible ends. Hence, this option exits the loop. 

## Implementing option ?  <a name="opt?"></a>
Let's leave some directions for users. We'll use some print statements to practice and set the example for upcoming options. 
```py
elif key == '?':
        print("Welcome user, this menu requires a code execution, in listed order below, to ensure functionality is not compromised.\n")
        print(f"This program utilizes random sample data for fields created with cmd (A).\n")
        print(f"Next, having made 2 factors, the sample needs weights/probs with cmd (W/P).\n")
        print(f"If factors need editing, cmd (P/W) will overwrite random data.\n")
        print(f"Your input data is visible, use cmd (V) to view stored info & dictionaries.\n")
        print(f"Using cmd (D), stats are analyzed and ready for the traffic model.\n")
        print(f"Observed data is manipulated using cmd (G) for stats.\n")

        
        print(f"Data optimization, via cmd (O), can be run right after cmd (A). Optimization:")
        print("iterates over a range of incremental lane amounts")
        print("with fixed inputs given, to then return the best type of highway to implement")
```
* code can be hard to read sometimes, try to use print() for any return values, or any value you don't seem to be able to identify
* print() can be used during loops to investigate what happens inside "pandora's box" of python processes 

Now, we can give input (?) to see some logic flow of the program. This explain the programs psuedocode and lets you know where the Menu picks up from.

## Implementing option A  <a name="optA"></a>
Now, let's initialize our system. We can add factors as explained in the previous chapter. We build the `[factors]` container with looping inputs. 
```py
elif key == 'A':

        print("What would you like to add?")

        how_many = 2 

        i = ... # how do you initalize a while loop?
        while i in range(int(how_many)):
            fact = input("> Enter one factor here: ")
            
            if fact.<py>() is False: # make sure the input IS ALPHAbetical only
                print("No numbers nor symbols are allowed in making factors. Try again...")
                continue
            elif fact.lower() in factors:
                print(f"{fact} is already an existing factor.")
                continue
            
            factors.<py>(fact.lower()) # how do you add an element to a list
            i = ... # how do you continue the while loop?
```

## Implementing option W  <a name="optW"></a>

## Implementing option P  <a name="optP"></a>

## Implementing option V  <a name="optV"></a>

## Implementing option D  <a name="optD"></a>

## Implementing option G  <a name="optG"></a>

## Implementing option O  <a name="optO"></a>

## Cheat sheet for various python operations <a name="cheat"></a>

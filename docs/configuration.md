---
title: 'Step 2 - Intro to Menu.py'
nav_order: 2
---

{:toc}

## Core structure

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

## Menu Template

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

## Implementing option Q
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
Once we give input (Q) to our file, the loop forcible ends. Now, this option carries out its goal. Let's adapt something more interactive.

##  

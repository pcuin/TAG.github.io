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
|:--------------|:---------------------|:-----------------------------------------------------------------------------------------------|
| Function (user)| f(x), f(x,y), f(...)| Functions that use `def` keyword <br> Ex: f(x) is the abstract hint for `print_menu(menu)`     | 
| Variable       |          ...        | Any assignment operation `var = ...` <br> Ex: cat = ... is the abstract hint for `cat = 'cat'` |
| Feature (built-in)| <p‎⁤y>             | **All** operations for this lab can be referenced [here](#cheat) <br> Ex: `str(x)` turns **x** into a **string**| 
| Data Structure         | [?],{?},(?)         | Various datatypes enter these collections. <br> `Empty` lists are denoted as `[]`.|
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
Let's create a weight option within our system. This allows probabaitlies to have relative maginitude to each other. Essentially, traffic will be sorted through a paramters set by user input. /
**Definitions:**
* lanes – counts the number of lanes to be used for simulation
* priority percent (capacity rate) - the percent of population reserved for effective drivers, *effectiveness will be defined in option P*
* rmdr - the complement prob of priority percent, where risky drivers share the other lanes

The while loop enters option W, proceeds to print some info and collect `lane_weight`, a user input *stored as a float*. Then, weight variables are stored in `{stats}` & `{dicto}` is updated accordingly.
```py
elif key == 'W': 
        lanes = int(input("Enter how many lanes (max 10): "))
        print("For each factor, pick a range capacity to designate to the fastest lane.")
        print("Ex: .15 - only the top 15% of entire sample enter the fast lane.")
        print(f"With {lanes} lanes, the rmdr, {1-.15}%, share the other {lanes-1} lanes equally.") 
        print(f"Thus, approx. {round(.85/(lanes-1), 2)}% of all drivers, fit into remaining lanes, regardless of behaivor or frequency.")
        
        print()
        # lane weight needs to take input from the user, as a float
        lane_weight = ...
        stats['Priority Percent'] = lane_weight
        stats['Lanes'] = lanes
        print('Resultant lane priority: ', lane_weight)
        print()
        # rmdr needs to be the complement probabilty of lane weight,
        # use round(...,2) on rmdr to display percent approximation
        # multiply by 100x to display percent correctly
        rmdr = round((1-lane_weight), 2)
        rmdr *= 100
        print(f"{lane_weight} - only the top {lane_weight*100}% of entire sample enter the fast lane.")
        print(f"With {lanes} lanes, the rmdr, {rmdr}%, share the other {lanes-1} lanes equally.") 
        print(f"Thus, approx. {rmdr/(lanes-1)}% of all drivers, fit into remaining lanes, regardless of behaivor or frequency.")

        dicto[?] = ... # assign option as key, to the value <lane_weight>
```
## Implementing option P  <a name="optP"></a>
Let's create a probability option within our system. We have thus far made capacity guidelines (option W) and factor creation (option A). We should now assign **target values** (probs) to define a sample's rentention rates. \
> Rentention refers to whether or not the average driver can fall around this created target rate. It's used later for important functions.

Let's differentiate rentention based on factors. `dict_helper` provides easy assignment of inputs to return a **{dict}**. Using `for` loop, based on a given factor, `{stats}` is updated accordingly. `{dicto}` is updated too.
```py
elif key == 'P': 

        print("For each factor, pick a projected percent that will give x drivers a lane advantage.")
        print("Ex: (.90) - if factor observed at level at or near .90, fast lane privelege is awarded.")
        dicto_prob = dict_helper(factors)
        for elem in [?]: # how can i fetch all factors from list?
            prob_proj = dicto_prob.get(elem)
            stats[factor + '.probs' + '.projection'] = prob_proj
        print('Resultant fields and associated percent projections')
        print()
        print_menu(dicto_prob)
        print()
        # make a nested dict with the option selected as key, <dicto_prob> as value 
        dicto[?] = {?}
```

## Implementing option V  <a name="optV"></a>
This option is for convenience. Let's check our current input points and access our local data found within our system. The while loop cannot terminate, so instead of returning such values, we had to store and print instead. Below, two dictionaries that appear over and over throughout this program are printed below. 
```py
elif key == 'V':

        print(f"You are now viewing {len(factors)} factors within your factor list.")

        print(', '.join(factors))

        if input("Type + to see all fields' associated stats, otherwise any key to quit: ") == '+':
            print("<<< WEIGHTS & PRIORITY SCALARS >>>")
            print_menu({?}) # where are the probabilites and weights stored?
            print("<<< STATS >>>")
            print_menu({?}) # where are the statistics stored?
```
Inputting V, we see our work be built and automated with ease. Let's continue to interpreting our data.
# 🛑 Checkpoint - Redirecting...
Good job! We've ensured all the needed input capabilities for our program. Let's shift focus from the Menu.py file to the TrafficQueue.py file. Resume building the program on the other end *(TrafficQueue)* until redericted back here. 

# 🏁 Continue 
Once the code skeleton is complete, continue below and run the following option D. 
* Code will likely throw error codes, make use of print statements when debugging.
* Make sure fixing errors are isolated, fixing things step by step, isntead of rewritiing entire chunks.

## Implementing option D  <a name="optD"></a>
Option D uses a genereaged sample and stores the `return` value within `data`. 
* Return values are always the outcome results of functions
* Call the appropriate function from TrafficQueue

```py
elif key == 'D': 
        #size = lanes**3 + 15
        print(f"Calculating stats associated with a n={lanes**3 + 15} random sample.")

        data = f(x,y) # create data by using a sample function
        print()

        # BELOW: update <stats> with a return value (dictionary object)

        return_analysis = f(x) # what function will develop important figures in a container?
        
        {?}.<py>(return_analysis) # what function call cam 'add' dictionaries together?
        print_menu({?}) # print the updated dictionary
        f(x,y) # which function call updates stats and returns a distribution?
```
## Implementing option G  <a name="optG"></a>

```py
elif key == 'G':
        print(f"Generating reports for {lanes} lane")
        print("Do you want reports to be given on each iteration of simulation?")

        expand = input("Press <1> for reports, otherwise press any other key >>>")
        if expand == ...: # what input activates reports?
            f(x, y, int(expand))
        odds = f(x, y, int(expand))

        print(odds)
```

## Implementing option O  <a name="optO"></a>

```py
elif key == 'O':
        print('Optimizing freeway structure')
        print("Processing sub-menu, proceed to enter fields, using consistent parameters:")
        x = [?] # cmd (?) gives the requisite, otherwise refer to handout for help
        optimal = f(x) # which function returns the optimal lane amount
        print(optimal)
```

## Cheat sheet for various python operations <a name="cheat"></a>
| Code (commands to alter your existent variables)                      | Functionality (how it updates code)                                                                                                           | Usability (with other python features)                                                             |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| list.append(element) <br>*[].append(1)* `returns` [1]                             | Adds an element to tail end of a list <br> Updates list, returns `None`                                                                                 | Update a **list** within a *for loop*                                                                    |
| dict.get(key) <br> *{‘hello’:’world’}.get(‘hello’) >return ‘world’         | Reads a dictionary for any matching key, otherwise returns None>Returns value, updates nothing                                                | Find if a key exists within a for loop                                                             |
| dict[key]  = value>*dict = {key:value}*                               | Either creates or overwrites the followingkeyword:value pairing>Returns nothing, updates pair                                                 | Update or create a dictionary in a for loop                                                        |
| for idx in range(len(list)):>*range(0,n)>0, … , n– 1*                 | Instead of finding elements, idx keeps track of the position (starting from 0)>Begins for loop, only accesses data                            | Loops over integers, not elements belonging to list                                                |
| .keys()                                                               | Returns all dictionary keys>Returns half the dictionary item, NOT A LIST                                                                      | Limited usability by itself, gives only keys with no pairing values                                |
| .values()                                                             | Returns all dictionary values>Returns half the dictionary item, NOT A LIST                                                                    | Limited usability by itself, gives only values with no pairing keys                                |
| list(object)>*list(dict.values())*                                    | Returns object as a list if convertible>Allows .keys() or .values() to be ran with a for loop                                                 | Juggles distinct datatypes (words versus numbers) to access unique sections of the same dictionary |
| while idx in range(n):>*idx=0* has to be above loop to be initialized | Begins while loop that tracks index number idx>helpful for accessing slices of lists list[idx]                                                | In the presence of nested dictionaries, while loops can replace dense code (nested for loops)      |
| type(object)>1list1dict1int1float1str                                 | Given an object, The functions return a type of variable found in python>To self–check the data being passed along checking along the process | Useful for diagnosing error codes and visualizing code chunks                                      |
| Sum(object)                                                           | Given an object,The elements are added up and returns its sum>Helpful for calculating means if                                                | Useful for organized data that can be easily read                                                  |


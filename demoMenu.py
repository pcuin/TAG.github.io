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

while True:
    print_menu(menu)
    key = input("+ Enter an option here + ")
    key = key.upper()
    if key == "Q":

        print("Program has been stopped!\n")

        ... # how would i break a while loop on command?

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
            i = ? # how do you continue the while loop?
            
    elif key == 'V':

        print(f"You are now viewing {len(factors)} factors within your factor list.")

        print(', '.join(factors))

        if input("Type + to see all fields' associated stats, otherwise any key to quit: ") == '+':
            print("<<< WEIGHTS & PRIORITY SCALARS >>>")
            print_menu({?}) # where are the probabilites and weights stored?
            print("<<< STATS >>>")
            print_menu({?}) # where are the statistics stored?
    elif key == 'G':
        print(f"Generating reports for {lanes} lane")
        print("Do you want reports to be given on each iteration of simulation?")

        expand = input("Press <1> for reports, otherwise press any other key >>>")
        if expand == ...: # what input activates reports?
            f(x, y, int(expand))
        odds = f(x, y, int(expand))

        print(odds)

    elif key == 'O':
        print('Optimizing freeway structure')
        print("Processing sub-menu, proceed to enter fields, using consistent parameters:")
        x = [?] # cmd (?) gives the requisite, otherwise refer to handout for help
        optimal = f(x) # which function returns the optimal lane amount
        print(optimal)
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
    elif key == '0':
        print('All parameters are now reset.')
        factors = []
        dicto = {}
        stats = {}
        lanes = 0
    else:
        print(f"{key} is not a supported option, please select another.")

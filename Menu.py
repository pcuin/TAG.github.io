# RankSys

from TrafficQueue import *

factors = []
dicto = {}
stats = {}
lanes = 0

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

        break

    elif key == 'P': # what the user believes should take place in a closed model

        print("For each factor, pick a projected percent that will give x drivers a lane advantage.")
        print("Ex: (.90) - if factor observed at level at or near .90, fast lane privelege is awarded.")
        dicto_prob = dict_helper(factors)
        for factor in factors:
            prob_proj = dicto_prob.get(factor)
            print(prob_proj)
            stats[factor + '.probs' + '.projection'] = prob_proj
        print('Resultant fields and associated percent projections')
        print()
        print_menu(dicto_prob)
        print()
        dicto[key] = dicto_prob

    elif key == 'W': # what the user believes should take place in a closed model
        lanes = int(input("Enter how many lanes (max 10): "))
        print("For each factor, pick a range capacity to designate to the fastest lane.")
        print("Ex: .15 - only the top 15% of entire sample enter the fast lane.")
        print(f"With {lanes} lanes, the rmdr, {1-.15}%, share the other {lanes-1} lanes equally.") 
        print(f"Thus, approx. {round(.85/(lanes-1), 2)}% make up the density of each remaining lanes, regardless of behaivor or frequency.")
        
        print()
        lane_weight = float(input("Type value as a float (.xx) >>>"))
        stats['Capacity'] = lane_weight
        stats['Lanes'] = lanes
        print('Resultant lane priority: ', lane_weight)
        print()
        rmdr = round((1-lane_weight)*100, 2)
        print(f"{lane_weight} - only the top {lane_weight*100}% of entire sample enter the fast lane.")
        print(f"With {lanes} lanes, the rmdr, {rmdr}%, share the other {lanes-1} lanes equally.") 
        print(f"Thus, approx. {rmdr/(lanes-1)}% of all drivers, fit into remaining lanes, regardless of behaivor or frequency.")
        dicto[key] = (lane_weight)

    elif key == 'D': # what the user holds true as a combination of traits and behaviors
        #size = lanes**3 + 15
        print(f"Calculating stats associated with a n={lanes**3 + 15} random sample.")

        data = random_sample(factors, lanes)
        print()
        print_menu(data)
        stats.update(summary(data))
        print_menu(stats)
        sort_flow(stats, data) 

    elif key == 'A':

        print("What would you like to add?")

        how_many = 2

        i = 0
        while i in range(int(how_many)):
            fact = input("> Enter one factor here: ")
            if fact.isalpha() is False:
                print("No numbers nor symbols are allowed in making factors. Try again...")
                continue
            elif fact.lower() in factors:
                print(f"{fact} is already an existing factor.")
                continue
            factors.append(fact.lower())
            i += 1
            
    elif key == 'V':

        print(f"You are now viewing {len(factors)} factors within your factor list.")

        print(', '.join(factors))

        if input("Type + to see all fields' associated stats, otherwise any key to quit: ") == '+':
            print("<<< WEIGHTS & PRIORITY SCALARS >>>")
            print_menu(dicto)
            print("<<< STATS >>>")
            print_menu(stats)
    elif key == 'G':
        print(f"Generating reports for {lanes} lane")

        print("Do you want reports to be given on each iteration of simulation?")
        expand = input("Press <1> for reports, otherwise press any other key >>>")
        if expand == '1':
            reduction_odds(data, stats, int(expand))
        odds = reduction_odds(data, stats)

        print(odds)

    elif key == 'O':
        print('Optimizing freeway structure')
        print('Creating samples for variable lane amounts & sample distributions:')
        print("Processing sub-menu, proceed to enter fields, using consistent parameters:")
        
        #memory.append(factors)
        #memory.append(dicto)
        #memory.append(2) # mimimum lane amount

        print(infrastructure(factors, 2))
    elif key == '?':
        print("Welcome user, this menu requires a code execution, in listed order below, to ensure functionality is not compromised.\n")
        print(f"This program utilizes random sample data for fields created with cmd (A).\n")
        print(f"Next, having made 2 factors, the sample needs weights/probs with cmd (W/P).\n")
        print(f"If factors need editing, cmd (P/W) will overwrite random data.\n")
        print(f"Your input data is visible, use cmd (V) to view stored info & dictionaries.\n")
        print(f"Using cmd (D), stats are analyzed and ready for the traffic model.\n")
        print(f"Observed data is manipulated using cmd (G) for stats.\n")

        print(f"Data optimization, via cmd (O), can be run right after cmd (A). Optimization:")
        print("*\titerates over a range of incremental lane amounts")
        print("*\twith fixed inputs given, to then return the best type of highway to implement")
    elif key == '0':
        print('All parameters are now reset.')
        factors = []
        dicto = {}
        stats = {}
        lanes = 0
    else:
        print(f"{key} is not a supported option, please select another.")
   
#while memory != []:
##    stats = {} # creates allocation params
##
##    # TARGET RATE MANAGEMENT
##    print("For each factor, pick a projected percent that will give x drivers a lane advantage.")
##    print("Ex: (.90) - if factor observed at level at or near .90, fast lane privelege is awarded.")
##    dicto_prob = dict_helper(factors)
##    for factor in factors:
##        prob_proj = dicto_prob.get(factor)
##        print(prob_proj)
##        stats[factor + '.probs' + '.projection'] = prob_proj
##    print('Resultant fields and associated percent projections')
##    print()
##    print_menu(dicto_prob)
##    print()
##    dicto['P'] = dicto_prob
##
##    # LANE MANAGEMENT
##    print("For each factor, pick a range capacity to designate to the fastest lane.")
##    print("Ex: .15 - only the top 15% of entire sample enter the fast lane.")
##    lane_weight = float(input("Type value as a float (.xx) >>>"))
##    stats['Capacity'] = lane_weight
##    print('Resultant lane priority: ', lane_weight)
##    print()
##    rmdr = round((1-lane_weight)*100, 2)
##    print(f"{lane_weight} - only the top {lane_weight*100}% of entire sample enter the fast lane.")
##    dicto['W'] = (lane_weight)
##    
##    # CONSTANTS OVER RANGE OF LANES  
##    factors = memory[0]
##    #dicto = memory[1]
##    lanes = memory[-1]
##
##    print_menu(stats)
##    #print_menu(dicto)
##    print(factors)
##     
##    analysis = {}
##    for quantity in range(lanes, 11):
##        
##        lanes = quantity # tracks fixed variable
##        print(lanes)
##        print()
##        stats['Lanes'] = lanes
##        
##        print(f"With {lanes} lanes, the rmdr, {rmdr}%, share the other {lanes-1} lanes equally.") 
##        print(f"Thus, approx. {rmdr/(lanes-1)}% of all drivers, fit into remaining lanes, regardless of behaivor or frequency.")
##        
##        data = random_sample(factors, lanes) # produces probs for data manipulation
##        stats.update(summary(data)) # updates params
##        preformance = reduction_odds(data, stats) # calls sort_flow in background
##        # preformance = golden-ratio-approx, effectivity-rate <tuple>
##        analysis[lanes] = (preformance)
##        print(preformance)
##
##    thetas = list(analysis.values())
##    most_effective_rate = max(thetas)
##    quantity = list(analysis.keys())
##    
##    optimal_lane = quantity[thetas.index(most_effective_rate)]
##    print('The optimal lane quantity with new policy is >>>', optimal_lane)
##    #return optimal_lane




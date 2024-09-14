import random as r
import statistics as stat

def dict_helper(factors):
    """
    given factors, a list, will map such to values indicating its avg occurence.
    function will overwrite previous values, if any.
    """
    factor_dict = {}
    for elem in factors:
        factor_dict[elem] = round(float(input("Type value as a float (.xx) >>>")), 2)
    return factor_dict

def random_sample(factors, size):
    """
    factor_dict - {factor: prob} - uses factor as a key and its value-assigned probabilty
    given fields, a driver will produce a random prob respective to each field.
    given drivers, a nested dict is returned with fields dict as a key,
    and the randomized probabilites, fields, as a value.

    This functions will produce the data needed for distributions.
    """
    
    if type(factors) == list:
        drivers = {}
        for n in range(...): # which param counts # individuals?
            fields = {}
            for sample in factors: # 
                r.seed(r.randrange(n, size))
                fields[...] = round(r.random(), 2) # what variable should resemble a float (decimal)?
            drivers[n] = {?} # what stores factors? 
            
        return drivers

def find_categs(data):
    """
    helper function to manage the fields associated with sampling data.

    data - return value from random_sample(),
    this nested dict has to be combed through
    to collect random data as a population,
    rather than indiviudals with 2 attributes.

    returns <<categs>> that maps <<factor: [sample data]>>
    """
    size = 0
    sumn = 0
    categs = {}
    for driverID in data:
        for field in data[driverID]:
            probs = str(field) + '.probs'
            entry = data[driverID].get(field)

            if probs not in categs: # to make subfields, a new list needs to store probs
                categs[probs] = []
                categs.get(probs).append(entry)

            categs.get(probs).append(entry)                
            sumn += entry
            size += 1
    return categs

def summary(data):
    """
    data - a nested dict, return value acquired from random_sample()
    categs - returns <<categs>> that maps <<factor: [sample data]>>
    
    data values are extracted to collect 
    avg, median, and standard deviation, sample size values.
    """
    categs = f(x)
    stats = {} # stores details about factors
    
    for factor in categs: # factor can be used to access data
        
        sumnation = sum({?}.get(...)) # fetch all the sample data to sum up
        population = len({?}.get(...)) # fetch the amount of sample data points (same as above)
        mean = round(sumnation/population, 2)
        stats[str(factor) + str('.average')] = mean

        n = population - 1
        
        if type(n//2) == int:
            m = n//2 
            left = (m-1) # find the index exactly left to m
            right = (m+1) # find the index exactly right to m  
            a = categs.get(factor)[...] # find the factor exactly left to m
            b = categs.get(factor)[...] # find the factor exactly right to m
            median = round(..., 2) # find the midpt of a and b

        stats[str(factor) + str('.median')] = ... 


        diff = 0
        for percent in categs.get(factor):
            # diff must be updated with the difference between percent and mean
            # and then be squared, raised to the power of 2 (x^2)
            # before loop moves on
            diff = ...
            
        variance = (diff) / n # sampling formula
        
        stdv = round(...,2) #calculate the sqrt of variance
        stats[str(factor) + str('.StanDev')] = ...  # input the implied values 
        stats[str(factor) + str('.samplesize')] = ...

    return {?} # return the dict that describes your samples' factors

def sort_flow(stats, data):
    """
    stats =  number summary 
    
    Will the combined data be approx. normal or otherwise skewed? Check using this function.
    """
    normal = False # ratio check
    symmetric = False # skewness check
    categs = f(x) # which function needs to map data into readable factors? 
    distrib = []
    for i in range(len(categs.keys())):
        factor = list(categs.keys())[i]
        # find/access and assign variables to the following:
        # mean - measure of expected prob
        # median - measure of midpoint value (50% of all data falls under median)
        # standard deviation - measure of spread from mean
        # sample size - measure of size
    
        avg = ...
        stdv = ...
        n = ...
        med = ...
        # calculate bias: << 3 * (expected-midpoint)/(spread) >>
        skew = 0
        kurt = 0
        kurt_numer = 0
        kurt_denom = 0
        bias = 3 * (...-...) / (...)

        j = 0 
        sample = list(categs.get(factor))
        while j in range(n):
            # sample[j] is the prob contained for a given driver!
            distrib.append(sample[j]) # updates list to have driver probabilties regardless of factor

            skew += ((sample[j] - ...)/(...))**3 # take the dist from mean, divide by deviation
            kurt_numer += (sample[j] - avg)**4
            kurt_denom += (sample[j] - (avg)**2)**2

            if j == n-1:
                skew /= (n-1) 
                kurt = (.../...) # create kurt by calculating ratio from numerator & denomiantor
                kurt *= (n-1)
                kurt -= 6 
                kurt = round(kurt, 2)
                skew = round(skew, 2)
                bias = round(bias, 2)

                # update the fields!
                stats[str(factor) + '.Skew'] = ...
                stats[str(factor) + '.Bias'] = ...
                stats[str(factor) + '.Kurt'] = ...
                
                if -1 <= skew <= 1:
                    symmetric = True
                    
                if symmetric and (-1.50 <= bias <= 1.50):
                    normal = True
                    
                # update the fields!
                stats[str(factor) + str('.Normal')] = ...
                stats[str(factor) + str('.Symmetric')] = ...
                
                if 2.25 <= kurt <= 3.75:
                    
                    stats[str(factor) + str('.Stability')] = "Approx. Normal"
                elif kurt > 3.75:
                    stats[str(factor) + str('.Stability')] = "More than accounted for"
                elif kurt < 2.25:
                    stats[str(factor) + str('.Stability')] = "Less than accounted for"    

                i += 1
            j += 1

    return [?] # what list contains each probability obtained from each driver?

def reduction_odds(data, stats, diagnostics = False, recursive = False):
    """
    distrib are all sample points, regardless of factor.
    """
    
    distrib = f(x, y) # call the function that returns a list of all probabilties, regardless of factor 
    
    categs = f(x) # call the function that returns a dict, factor paired with its probabilities
    
    # use one factor to parametrize the distribution, acting as the main lurking factor

    #factor_residual = {} # store residuals
    for factor in categs:
        #print(factor)
        bias = stats.get(factor + '.Bias')
        lanes = stats.get('Lanes')
        avg = stats.get(factor + '.average')
        stdv = stats.get(factor + '.StanDev')
        n = stats.get(factor + '.samplesize')
        med = stats.get(factor + '.median')
        target_rate = stats.get(factor + '.projection')
        density_rate = (1-target_rate)/(lanes-1)

        # refer to 'rules of the simulation' to understand where each param stands in function
        
        capacity_rate = stats.get('Capacity') # area width of given sample
        capacity = round(capacity_rate*n)

        ## normality
        theta = stat.NormalDist(mu=avg, sigma=stdv).inv_cdf(capacity_rate) # yields an exact data cutoff point
        
        # phaseshift - ranging param to re-scale limiting value, to skewed distrib
        phaseshift = abs(round(bias*theta,4))
        target_hat = round(stat.NormalDist(mu=theta, sigma=phaseshift).inv_cdf(capacity_rate), 4)

        j = 0
        i = 0
        distrib.sort()
        priority = 0 # tracks any sample ratio value that falls below the cutoff limit (theta)
        freq = 0 # tracks occurences of theta-limiting values

        lane = [[],[]]
        parametrics = [[],[]]
        while j in range(len(distrib)) and i <= n:
            

            if len(lane[0]) <= capacity:

                # keep track of two means:
                    # priority mean: prob that falls under cutoff percentile
                if distrib[j] <= ...: #cutoff percentile
                    lane[0].append(distrib[j])
                    capacity -= 1
                    ... += distrib[j] # sum up successful percentiles with counter var
                    freq += 1 # counter variable for size

                r.shuffle(distrib) # ensures previous sort dogmatically picks the next best driver
                [???][i].append(distrib[j]) # add prob to the priority lane
                
            else:
                [???][i].append(distrib[j]) # add prob to the 'others' lane
                
            if i == n: # switches factor parametrization

                omega_mu = round(..., 4) # use stat.mean(seq) on entirety of priority lane
                theta_mu = round(..., 4) # use counter variables to manually calc avg success rate
                omicron_mu = round(..., 4) # use stat.mean(seq) on nonpriority lane
                
                omega_sigma = ... # use stat.stdev(seq) on entirety of priority lane
                omicron_sigma = ...# use stat.stdev(seq) on nonpriority lane


                # calc the a new limiting value, theta, with params of other distribs, to simulate change
                theta_hat = density_rate # to simulate a siphoning of a new traffic policy at its lowest maintenance

                # assuming the density rate provides a good fit for a normalizaed population percentile
                # assume normal population approaches the avg success rate collected above
                # use stat.NormalDist(mu, sigma).inv_cdf(area) to model two cases below
                
                omega_hat = round(..., 4) # assumes omega-case spread 
                omicron_hat = round(..., 4) # assumes omicron-case spread
                

                residual = ... # refer to handout 
                if residual < 1:
                    residual = 1/residual 
                
                if diagnostics:
                    print('target rate:', round(target_rate, 4)) 
                    print('\t* User input, % benchmark to limit traffic overall')
                    print('density rate:',round(density_rate, 4))
                    print('\t* Complementary derivation from <target_rate>, % benchmark to measure traffic flow overall')
                    print(f'In order to maximize priority lane quota: {capacity_rate}, given the {factor}-parametrized model...')
                    print(f'Predicted target rate ={target_hat}, given initial estimate ={target_rate}.')
                    print(f'3 main strata/distributions exist:')
                    print(f'Omega,{omega_mu} is avg occurence of mixed populations that enter the priority lane regardless of limit {round(theta, 2)}')
                    print(f'Theta,{theta_mu} is avg occurence of exclusive population whose rate <= {round(theta, 2)}')
                    print(f'Omicron,{omicron_mu} is avg occurence of discriminated population whose rate >= {round(theta, 2)}')
                    print(f'diff b/w omegas: {omega_mu-omega_hat}')
                    print(f'diff b/w omicrons: {omicron_mu-omicron_hat}') 
                    print(f'compare to golden ratio:', round(residual, 4))

                lane = [[],[]] # rebooting highway to ensure stratification
                parametrics[0].append(...)
                parametrics[-1].append(...)
                
            j+=1   
            i += 1

    #print(parametrics)
    theta_mu = max(parametrics[0])
    idx_golden_ratio = parametrics[0].index(theta_mu)
    # this idx denotes which factor serves the higher efficiency rate
    residual = round(parametrics[-1][idx_golden_ratio], 4)
        
    return theta_mu, residual

def infrastructure(factors, lanes = 2):
    stats = {} # creates allocation params
    dicto = {}
    # TARGET RATE MANAGEMENT
    print("For each factor, pick a projected percent that will give x drivers a lane advantage.")
    print("Ex: (.90) - if factor observed at level at or near .90, fast lane privelege is awarded.")
    dicto_prob = dict_helper(factors)
    for factor in factors:
        prob_proj = dicto_prob.get(factor)
        print(prob_proj)
        stats[factor + '.probs' + '.projection'] = prob_proj
    print('Resultant fields and associated percent projections')
    print()

    print()
    dicto['P'] = dicto_prob

    # LANE MANAGEMENT
    print("For each factor, pick a range capacity to designate to the fastest lane.")
    print("Ex: .15 - only the top 15% of entire sample enter the fast lane.")
    lane_weight = float(input("Type value as a float (.xx) >>>"))
    stats['Capacity'] = lane_weight
    print('Resultant lane priority: ', lane_weight)
    print()
    rmdr = round((1-lane_weight)*100, 2)
    print(f"{lane_weight} - only the top {lane_weight*100}% of entire sample enter the fast lane.")
    dicto['W'] = (lane_weight)
    
    #print(factors)

    #-----------------------------------EDIT----------------------------- 
    analysis = {}
    for quantity in range(lanes, 11):
        
        lanes = quantity # tracks fixed variable
        print(lanes)
        print()
        stats['Lanes'] = lanes
        
        print(f"With {lanes} lanes, the rmdr, {rmdr}%, share the other {lanes-1} lanes equally.") 
        print(f"Thus, approx. {rmdr/(lanes-1)}% of all drivers, fit into remaining lanes, regardless of behaivor or frequency.")
        
        data = f(x, y) # initializes raw data with integers as keys
        run_stats = f({x}) # returns {stats} in previous contexts
        {?}.update(run_stats) # updates built-in function dict
        preformance = f(x,y) # function call returns a tuple

        analysis[lanes] = ... # tuple object
        #print(preformance)

    thetas = list(analysis.values()) # use print statement above to view progress
    optimal_rate = ... # refer to handout
    quantity = list(analysis.keys())
    
    optimal_lane = quantity[[?].index(...)]
    print('The optimal lane quantity with new policy is >>>', optimal_lane)
    return optimal_lane



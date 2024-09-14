# who will be allowed on the road?
import random as r
import statistics as stat
def random_sample(factors, lanes):
    """
    factor_dict - {factor: prob} - uses factor as a key and its value-assigned probabilty
    given fields, a driver will produce a random prob respective to each field.
    given drivers, a nested dict is returned with fields dict as a key,
    and the randomized probabilites, fields, as a value.

    This functions will produce the data needed for distributions, GIVEN TO STUDENT.
    """
    size = lanes**3 + 15
    if type(factors) == list:
        drivers = {}
        for n in range(size): # counts how many individuals are to be iterated
            fields = {}
            for elem in (factors): # counts how many fields are to be assigned random prob
                r.seed(r.randrange(n, size))
                fields[elem] = round(r.random(), 2) # round to 2 digits
            drivers[n] = fields 
            
        print(drivers)
        return drivers
   
    
def dict_helper(factors):
    """
    given factors, a list, will map such to values indicating its avg occurence.
    function will overwrite previous values, if any.
    """
    factor_dict = {}
    for elem in factors:
        factor_dict[elem] = round(float(input("Type value as a float (.xx) >>>")), 2)
    return factor_dict

def find_categs(data):
    """
    helper function to manage the fields associated with sampling data.
    """
    size = 0
    sumn = 0
    categs = {}
    stats = {}
    for driverID in data:
        for field in data[driverID]:
            probs = str(field) + '.probs'
            entry = data[driverID].get(field)
            #print(data[driverID][field])
            if probs not in categs: # to make subfields, a new list needs to store probs
                categs[probs] = []
                categs.get(probs).append(entry)

            categs.get(probs).append(entry)                
            sumn += entry
            size += 1
    return categs
    
def summary(data):
    """
    passes data, a nested dict, return value acquired from random_sample func.
    data is extracted to isolate values from dict to
    find min, avg, max, variance, and standard deviation values.
    """
    categs = find_categs(data)
    stats = {}
    
    for factor in categs:
        mean = round(sum(categs.get(factor))/len(categs.get(factor)), 2)
        stats[str(factor) + str('.average')] = mean

        n = len(categs.get(factor)) - 1
        
        if type(n//2) == int:
            m = n//2
            left = (m-1)
            right = (m+1)
            a = categs.get(factor)[left]
            b = categs.get(factor)[right]
            median = round((a + b)/2, 2)

        stats[str(factor) + str('.median')] = median


        diff = 0
        for percent in categs.get(factor):
            diff += (percent - mean)**2
            
        variance = (diff) / n # sampling formula
        #print(variance)
        stdv = round(variance**(1/2), 2)
        stats[str(factor) + str('.StanDev')] = stdv   
        stats[str(factor) + str('.samplesize')] = n
        

        ######categs[str(factor) + str('_average')] = categs[factor]
        # deletion of old key is not necessary, as newkey name will
        ## overwrite the old key

    return stats

def sort_flow(stats, data):
    """
    stats =  number summary 
    lanes =  based on general data randomization

    Will the combined data be approx. normal or otherwise skewed? Check using this function.
    """
    normal = False # ratio check
    symmetric = False # skewness check
    categs = find_categs(data)
    distrib = []
    for i in range(len(categs.keys())):
        factor = list(categs.keys())[i]
        #print(factor)
        avg = stats.get(factor + '.average')
        stdv = stats.get(factor + '.StanDev')
        n = stats.get(factor + '.samplesize')
        med = stats.get(factor + '.median')
        skew = 0
        kurt = 0
        kurt_numer = 0
        kurt_denom = 0
        bias = 3*(avg - med)/(stdv)

        
        j = 0
        
        sample = list(categs.get(factor))
        while j in range(n):
            #print(i)
            distrib.append(sample[j])
            #print(j)
            skew += ((sample[j] - avg)/(stdv))**3
            kurt_numer += (sample[j] - avg)**4
            kurt_denom += (sample[j] - (avg)**2)**2

            #kurt /= ((sample[j] - avg)/(stdv))**4

            if j == n-1:
                skew /= (n-1)
                kurt = (kurt_numer/kurt_denom)
                kurt *= (n-1)
                kurt -= 6
                kurt = round(kurt, 2)
                skew = round(skew, 2)
                bias = round(bias, 2)
                print('SKEW', skew)
                stats[str(factor) + '.Skew'] = skew
                print('BIAS', bias)
                stats[str(factor) + '.Bias'] = bias
                print('KURT', kurt)
                stats[str(factor) + '.Kurt'] = kurt
                
                if -1 <= skew <= 1:
                    symmetric = True
                elif -2 <= skew <= 2:
                    symmetric = True
                if symmetric and (-1.50 <= bias <= 1.50):
                    normal = True
                    
                stats[str(factor) + str('.Normal')] = normal
                stats[str(factor) + str('.Symmetric')] = symmetric
                
                if 2.25 <= kurt <= 3.75:
                    
                    stats[str(factor) + str('.Stability')] = "Approx. Normal"
                elif kurt > 3.75:
                    stats[str(factor) + str('.Stability')] = "More than accounted for"
                elif kurt < 2.25:
                    stats[str(factor) + str('.Stability')] = "Less than accounted for"    

                i += 1
            j += 1
    #print(len(distrib))
    #print(n)
    return distrib

def reduction_odds(data, stats, diagnostics = False):
    """
    distrib are all sample points, regardless of factor.
    """
    
    distrib = sort_flow(stats, data)
    
    categs = find_categs(data)
    # use factor params to serve as main lurking factor

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
        
        
        capacity_rate = stats.get('Capacity') # area width of given sample
        capacity = round(capacity_rate*n)

        ## normality
        theta = stat.NormalDist(mu=avg, sigma=stdv).inv_cdf(capacity_rate) # yields an exact data cutoff point
        # theta describes the max proportion permitted to enter the priority lane
        # theta relies on using the present condtions as long term fixed oonstants
        if theta <0:
            print(f'theta: {theta} is neg')
        phaseshift = abs(round(bias*theta,4))
        # phaseshift - ranging param to re-scale limiting value, to skewed distrib
        
        target_hat = round(stat.NormalDist(mu=theta, sigma=phaseshift).inv_cdf(capacity_rate), 4)
        # how to achieve a dependnable quantity on numerous ocndtions like normality and bias,
        # with parameter adjustments, which will dictate the best-fit expectation
        j = 0
        i = 0
        distrib.sort()
        priority = 0 # tracks any sample ratio value that falls below the cutoff limit (theta)
        freq = 0 # tracks occurences of theta-limiting values

        lane = [[],[]]
        parametrics = [[],[]]
        while j in range(len(distrib)) and i <= n:
            
            #print('got in j range n loop')
            if len(lane[0]) <= capacity:
    
                if distrib[j] <= theta:
                    lane[0].append(distrib[j])
                    capacity -= 1
                    priority += distrib[j]
                    freq += 1

                r.shuffle(distrib) # ensures previous sort dogmatically picks the next best driver
                lane[0].append(distrib[j])
                
            else:
                lane[-1].append(distrib[j])
                
            if i == n:
                # note: omega & omicron are condtion-based stratum (groups),
                # omega - denote the primary (fast) lane exclusivity,
                # omicron - denote the restriction to the rest of the lanes (virtually identical)
                omega_mu = round(stat.mean(lane[0]), 4)
                theta_mu = round((priority/freq), 4)
                omicron_mu = round(stat.mean(lane[-1]), 4)
                
                omega_sigma = stat.stdev(lane[0])
                omicron_sigma = stat.stdev(lane[-1])

                # calc the a new limiting value, theta, with params of other distribs, to simulate change
                theta_hat = density_rate # to simulate a siphoning of a new traffic policy at its lowest maintenance
                omega_hat = round(stat.NormalDist(mu=theta_mu, sigma=omega_sigma).inv_cdf(theta_hat), 4)
                omicron_hat = round(stat.NormalDist(mu=theta_mu, sigma=omicron_sigma).inv_cdf(theta_hat), 4)

                # only one center of measure was used to paramtrize the normal distrib,
                    # omega_mu can be used in argument <<mu = >>
                    # omicron_mu can be used in argument <<mu = >>

                # assumes normality with adjusted parameters to forecast an ideal, but biased percentile,
                # to thus compare to other means from quasinormal distribs, using different criteria
                residual = (omega_mu-omega_hat) / (omicron_mu-omicron_hat)
                if residual < 1:
                    residual = 1/residual 

                
                if diagnostics:
                    print('target rate:', round(target_rate, 4)) # percentile limit that
                    print('\t* User input, % benchmark to limit traffic overall')
                    print('density rate:',round(density_rate, 4)) # percentile intervals that measure lane dist
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

                lane = [[],[]]
                parametrics[0].append(theta_mu)
                #print(theta_mu)
                parametrics[-1].append(residual)
                
            j+=1   
            i += 1


    print(parametrics)
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
    
    # CONSTANTS OVER RANGE OF LANES  
    #factors = memory[0]
    #dicto = memory[1]
    #lanes = memory[-1]


    print(factors)
     
    analysis = {}
    for quantity in range(lanes, 11):
        
        lanes = quantity # tracks fixed variable
        print(lanes)
        print()
        stats['Lanes'] = lanes
        
        print(f"With {lanes} lanes, the rmdr, {rmdr}%, share the other {lanes-1} lanes equally.") 
        print(f"Thus, approx. {rmdr/(lanes-1)}% of all drivers, fit into remaining lanes, regardless of behaivor or frequency.")
        
        data = random_sample(factors, lanes) # produces probs for data manipulation
        stats.update(summary(data)) # updates params
        preformance = reduction_odds(data, stats) # calls sort_flow in background
        # preformance = effectivity-rate, golden-ratio-approx  <tuple>
        analysis[lanes] = (preformance)
        print(preformance)

    thetas = list(analysis.values())
    optimal_rate = min(thetas)
    quantity = list(analysis.keys())
    
    optimal_lane = quantity[thetas.index(optimal_rate)]
    print('The optimal lane quantity with new policy is >>>', optimal_lane)
    return optimal_lane
    

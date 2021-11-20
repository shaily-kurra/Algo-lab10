import sys

def probs_from_weights(weights):
    total = sum(weights)
    probs = [x/total for x in weights]
    return probs

def best_response(probs):
    payoffs = [-0.5,0.5,-0.5,0.5]
    exp_utility = []
    for i,j in zip(payoffs,probs):
        exp_utility.append(i*j)
    
    max_util = max(exp_utility)
    return exp_utility.index(max_util)

def util_of_each_action(response):
    utility_matrix = [[0,-1,1,-0.5],[1,0,-1,0.5],[-1,1,0,-0.5],[0.5,-0.5,0.5,0]]
    utilities = [element*-1 for element in utility_matrix[response]]
    return utilities
    

def  convert_util_to_losses(utilities):
    losses = []
    for i in utilities:
        if i == 1:
            losses.append(0)
        if i == -1:
            losses.append(1)
        if i == 0.5:
            losses.append(0.5)
        else:
            losses.append(0.5)
    return losses
    
def update_weights(weights, losses, epsilon):
    for i in range(len((weights))):
        weights[i] = weights[i]*(1-epsilon*losses[i])
    return weights



T = int(sys.argv[1])
epsilon = float(sys.argv[2])
weights = [1,1,1,1]
list_of_probs = []
for i in range(T):
    probs = probs_from_weights(weights)
    list_of_probs.extend(probs)
    response = best_response(probs)
    utilities = util_of_each_action(response)
    losses = convert_util_to_losses(utilities)
    weights = update_weights(weights, losses, epsilon)

print( sum(list_of_probs)/len(list_of_probs))






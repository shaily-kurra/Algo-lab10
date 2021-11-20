import sys

def probs_from_weights(weights):
    total = sum(weights)
    probs = [x/total for x in weights]
    return probs

def best_response(probs):
    payoffs = [-0.5,0.5,-0.5,0.5]
    exp_utility = []
    exp_utility.append(payoffs*probs)
    max_util = max(exp_utility)
    return exp_utility.index(max_util)

def util_of_each_action(response):
    utility_matrix = [[0,-1,1,-0.5],[1,0,-1,0.5],[-1,1,0,-0.5],[0.5,-0.5,0.5,0]]
    return -1 * utility_matrix[response]

def  convert_util_to_losses(utilities):
    losses = []
    for i in utilities:
        if i == 1:
            losses.append(0)
        else if i == -1:
            losses.append(1)
        else if i == 0.5:
            losses.append(0.5)
        else:
            losses.append(0.5)
    return losses
    
def update_weights(weights, losses, epsilon):
    
    for i in range(len((weights))):
        weights[i] = weights[i]*(1-epsilon*losses[i])
    return weights



T = sys.srgv[1]
epsilon = sys.argv[2]
weights = [1,1,1,1]
list_of_probs = []
for in in range(T):
    probs = probs_from_weights(weights)
    list_of_probs.append(probs)
    response = best_response(probs)
    utilities = util_of_each_action(response)
    losses = convert_util_to_losses(utilities)
    weights = update_weights(weights, losses, epsilon)








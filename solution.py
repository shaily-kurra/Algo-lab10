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
    return utility_matrix[response]







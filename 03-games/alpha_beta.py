def is_game_over(node):
    winning_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for indexes in winning_indexes:
        hit_count = 0
        chosen_symbol = node[indexes[0]]

        for index in indexes:
            if node[index] is not None and node[index] == chosen_symbol:
                hit_count = hit_count + 1

        if hit_count == 3:
            return True, chosen_symbol

    if node.count(None) == 0:
        return True, None

    return False, None

def generate_children(node, chosen_symbol):
    result = []
    for i in range(9):
        if node[i] == None:
            node_aux = node.copy()
            node_aux[i] = chosen_symbol
            result.append(node_aux)                
    return result

def alternate_symbol(symbol):
    return 'o' if symbol == 'x' else 'x'

def mini_max_ab(node, is_maximizing_player_turn, chosen_symbol, alpha, beta): # TODO: Modify this minimax in order to turn it into an alpha-beta pruning version with depth cutting
    game_result = is_game_over(node)
    if game_result[0]:
        if game_result[1] is None:
            return 0, node
        return (-1, node) if is_maximizing_player_turn else (1, node)
    
    if is_maximizing_player_turn:
        maxEval = -1
        maxChild = None
        children = generate_children(node, chosen_symbol)
        for child in children:
            eval = mini_max_ab(child, False, 'o', alpha, beta)
            if eval[0] > maxEval:
                maxChild = child
                maxEval = eval[0]
            alpha = max(alpha, eval[0])
            if beta <= alpha:
                break
        return maxEval, maxChild
    else:
        minEval = 1
        minChild = []
        children = generate_children(node, chosen_symbol)
        for child in children:
            eval = mini_max_ab(child, True, 'x', alpha, beta)
            if eval[0] < minEval:
                minChild = child
                minEval = eval[0]
            beta = min(beta, eval[0])
            if beta <= alpha:
                break
        return minEval, minChild

def mini_max(node, is_maximizing_player_turn, chosen_symbol):
    # call the method that check if the game is over
    game_result = is_game_over(node)
    # check if the game is over
    if game_result[0]:
        # check if the game over in draw
        if game_result[1] is None:
            # return draw
            return 0, node
        # return the wining player (if the winner is the machine return -1, 
        # if the winner is the player return 1)
        return (-1, node) if is_maximizing_player_turn else (1, node)
    # generar childrens
    children = generate_children(node, chosen_symbol)
    # for each element of childrens apply mini_max changing the turn
    children_results = list(map(lambda child: 
        [mini_max(child, not is_maximizing_player_turn, alternate_symbol(chosen_symbol))[0], child], 
        children))
    # return the max score when is maximizing turn or min when is minimizing turn
    return max(children_results, key=str) if is_maximizing_player_turn else min(children_results, key=str)
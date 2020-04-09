def generate_children(node, chosen_symbol): # TODO: Create a function to generate the children states for minimax evaluation
    result = []
    for i in range(9):
        if node[i] == None:
            node_aux = node.copy()
            node_aux[i] = chosen_symbol
            result.append(node_aux)                
    return result

node = [None, None, None, None, 'o', None, None, None, None]

result = generate_children(node, 'x')
print(len(result))
print(result)
text = ["lorem ipsum dolor sit amet consectetur adipiscing elit something"]
MAX_CHARS = 11

def split_text(text, MAX_CHARS ):
    answer = []
    
    for words in text:
        word = ""
        count = 0
        
        for c in words:
            count += 1
            word += c
            
            if count == MAX_CHARS:
                answer.append(word)
                word = ""
                count = 0 
        if word != "": #ensures that a word that was shorter than the max gets added if its the last word.
            answer.append(word)
            
    return answer
    
class Node:
    def __init__(self, data = None, left = None, right = None, weight = 0):
        self.left = left
        self.right = right
        self.data = data
        self.weight = weight

    #prints the node data and weight
    def __repr__(self):
        return f"Node(data={self.data}, weight={self.weight})"
    
def create_leaf_nodes(answer):
    leaf_nodes = []
    
    for words in answer:
        node = Node(data = words, left = None, right = None, weight = len(words))
        leaf_nodes.append(node)
    
    return leaf_nodes
        
def build_rope_tree(leaf_nodes):    
    
    if len(leaf_nodes) == 1:
        return leaf_nodes[0]
    
    parents = []
    i = 0
    
    while i < len(leaf_nodes):
        left = leaf_nodes[i]
        
        if i + 1 < len(leaf_nodes):
            right = leaf_nodes[i + 1]
            left = leaf_nodes[i]
            weight = left.weight
            parent = Node(data = None, right = right, left = left, weight = weight)
            parents.append(parent)    
        
        else:
            parents.append(left)
        i += 2

    return build_rope_tree(parents)

def print_tree(node, level=0):
    if node:
        print("  " * level + f"Node(data={node.data}, weight={node.weight})")
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)    
     
chunks = split_text(text, MAX_CHARS)
leaf_nodes = create_leaf_nodes(chunks)
print_tree(build_rope_tree(leaf_nodes))
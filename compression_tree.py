class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Pre-order traversal with markers
def serialize_tree(node):
    if node is None:
        return "#"
    return f"{node.value} {serialize_tree(node.left)} {serialize_tree(node.right)}"

# Helper to serialize and compress tree
def compress_tree(root):
    serialized_tree = serialize_tree(root)
    
    # Split serialized tree into nodes and markers
    elements = serialized_tree.split()
    
    node_values = []
    structure = []
    
    # Build node values list and structure bit list
    for el in elements:
        if el == "#":
            structure.append(0)  # Null child
        else:
            node_values.append(el)
            structure.append(1)  # Real node
    
    # Compress node values using Huffman encoding (or another method)
    compressed_values = huffman_encode(node_values)
    
    # Compress structure using RLE or other techniques
    compressed_structure = rle_compress(structure)
    
    return compressed_values, compressed_structure

# Example Huffman encoding and RLE compression functions
def huffman_encode(values):
    # Placeholder: Implement Huffman coding
    pass

def rle_compress(structure):
    # Simple RLE compression: Count consecutive bits
    compressed = []
    count = 1
    for i in range(1, len(structure)):
        if structure[i] == structure[i - 1]:
            count += 1
        else:
            compressed.append((structure[i - 1], count))
            count = 1
    compressed.append((structure[-1], count))
    return compressed

# Example tree construction
root = Node("A", Node("B", Node("D"), Node("E")), Node("C"))

compressed_values, compressed_structure = compress_tree(root)
print("Compressed Node Values:", compressed_values)
print("Compressed Structure:", compressed_structure)

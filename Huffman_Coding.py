import heapq  # used for merging the min nodes of a nodes list
import sys  # sys function to get the size of en-/decoded data

# first create the Node class to enable huffman logic
class Node(object):

    def __init__(self, value=None, character=None):
        self.character = character
        self.value = value
        self.left = None
        self.right = None

    def setcharacter(self, character):
        self.character = character

    def setvalue(self, value):
        self.value = value

    def setleftchild(self, node):
        self.left = node

    def setrightchild(self, node):
        self.right = node

    def getvalue(self):
        return self.value

    def getcharacter(self):
        return self.character

    def getrightchild(self):
        return self.right

    def getleftchild(self):
        return self.left

    def hasleftchild(self):
        return self.left is not None

    def hasrightchild(self):
        return self.right is not None

    def __gt__(self, other):
        return self.value > other.value
    # this function makes nodes comparable!


# function for encoding a string
def huffman_encoding(data):

    # function to create a dict with the string
    # characters as keys and their frequency as values
    def count_letter(string):
        sum_letter = dict()
        for i in string:
            sum_letter[i] = sum_letter.get(i, 0) + 1
        sum_letter = dict(sorted(sum_letter.items(), key=lambda x: x[1]))
        return sum_letter

    # create Nodes from sorted frequency list
    # build a heap list to get min frequency of nodes
    def heap(sum_letter):
        heap = list()
        for key in sum_letter:
            node = Node(sum_letter[key], key)
            heapq.heappush(heap, node)
        heapq.heapify(heap)
        return heap

    # merge nodes according to huffman logic,
    # merge the two min frequency nodes from the heap
    def huff(heap):
        left_node = Node
        right_node = Node
        nodes = list()
        while len(heap) > 1:
            left_node = heapq.heappop(heap)
            right_node = heapq.heappop(heap)
            new_node = Node(
                left_node.getvalue() +
                right_node.getvalue(),
                left_node.getcharacter() +
                right_node.getcharacter())
            new_node.setleftchild(left_node)
            new_node.setrightchild(right_node)
            heapq.heappush(heap, new_node)
            nodes.append(new_node)
        return nodes
        # nodes[-1] is root of the tree!

    # recursive traversal through the tree
    # logic: visit first left node, then right node
    def traverse(root, code, char_freq, result):
        if root.hasleftchild() == False and root.hasrightchild() == False:
            char_freq[root.getcharacter()] = code
            # print(f'- {root.getcharacter()}: {code}')
            result[root.getcharacter()] = code
            return None
        else:
            # the code for the path from the root
            # to a leaf is stored in the code variable
            traverse(root.getleftchild(), code + '0', char_freq, result)
            traverse(root.getrightchild(), code + '1', char_freq, result)
        return result
        # the result is the code book (dictionary)

    # function to print the code for a given string in one line
    def encode(code_dict, string):
        encode = str()
        # print(f'\nThe code for the string "{string}" is:')
        for i in range(len(string)):
            encode += code_dict[string[i]]
        # print(f'{code_dict[string[i]]}', end='')
        # print('\n')
        return encode

    nodes = list()
    new_string = data
    code = str()
    result = dict()
    sum_letter = dict()
    sum_letter = count_letter(new_string)
    nodes = huff(heap(sum_letter))

    return encode(traverse(nodes[-1], code,
                           sum_letter, result), new_string), nodes[-1]
    # return the huffman encode and the tree for decoding


# function for decoding a string
def huffman_decoding(code, tree):

    def decoding(code, tree, decode):
        root = Node
        root = tree
        for i in range(len(code)):
            if code[i] == '0':
                tree = tree.getleftchild()
                if tree.hasleftchild() == False and tree.hasleftchild() == False:
                    decode += tree.getcharacter()
                    tree = root
            elif code[i] == '1':
                tree = tree.getrightchild()
                if tree.hasleftchild() == False and tree.hasleftchild() == False:
                    decode += tree.getcharacter()
                    tree = root
        return decode

    clear = decoding(code, tree, decode=str())
    return clear


# results print out for a string stored in variable a_great_sentence
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print(
        "The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

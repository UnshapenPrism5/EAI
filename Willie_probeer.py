#######################################################################################################################
#    Group Number:
#
#    Name:                         Student number:
#    Willie Broekman               21441562
#    David Nel                     21435058
#######################################################################################################################

################################### TASK 1 ###########################################################
class Nodes:
    """
    This is the main class of the tree
    This will be used to not only create a node, but also create its branches based on the depth
    """

    # Run on create
    # Three children for each element "R","P" or "S"
    # Parent element to determine the sequence followed, eg "RRR" or "PSR"
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.middle = None
        self.parent = None
        self.visited = False

    # Used to generate branches for a node
    # Setting depth equal to 1, will cause the program to generate only one row of elements
    # Setting depth more than 1 , will cause the program to generate an entire tree with the defined depth
    def generate_branch(self, depth=1):
        """Create branches for a node"""
        if depth != 0:
            # Create all children of the current node
            self.left = Nodes("R")
            self.left.parent = self
            self.middle = Nodes("P")
            self.middle.parent = self
            self.right = Nodes("S")
            self.right.parent = self

            # Recursively do the same for the entire level, if the depth is more than 1
            self.left.generate_branch(depth - 1)
            self.middle.generate_branch(depth - 1)
            self.right.generate_branch(depth - 1)
        return self


################################### TASK 2 ###########################################################
def depth_first_traversal(node):
    """Depth first search algorithm"""
    # check if valid node is inputted
    if (node == None):
        return []
    # Since this is a recursive function, the outputs will be returned and saved to an array
    arr = []
    if (node.name != "start"):
        arr.append(node)

    # Since this is a recursive function, the outputs will be returned and saved to an array
    new_arr = depth_first_traversal(node.left)
    for elements in new_arr:
        arr.append(elements)

    new_arr = depth_first_traversal(node.middle)
    for elements in new_arr:
        arr.append(elements)

    new_arr = depth_first_traversal(node.right)
    for elements in new_arr:
        arr.append(elements)

    return arr

def breadth_first_search(node):
    """ Breadth first search algorithm"""

    # Queues will be used to store each node from the leftmost child to the rightmost child
    queue = [node]
    arr = []

    while queue:
        # For each Node stored in the queue we will first remove it, then we will check if it has children and append
        # it to the queue if it has
        current_node = queue.pop(0)

        # The current node that is removed from the queue will be saved to the array
        if (current_node.name != "start"):
            arr.append(current_node)

        # Finally all children are checked and appended to the queue
        if (current_node.left != None):
            queue.append(current_node.left)
        if (current_node.middle != None):
            queue.append(current_node.middle)
        if (current_node.right != None):
            queue.append(current_node.right)
    return arr







################################### TASK 3 ###########################################################
""" GLOBAL VARIABLES """
bfs_dfs = 1
depth = 5
root = Nodes("start")
root.generate_branch()
beat_dict = {"R": "P", "P": "S", "S": "R"}
my_hist = ""
opp_hist = ""
length = 0
sequence = []
repeat_sequence = False


def print_name(node):
    name = ""
    if (node.parent != None):
        if (node.parent.name != "start"):
            name = print_name(node.parent)
    return name + node.name



if input == "":
    # here we will set/reset the original values
    root = Nodes("start")
    root.generate_branch()
    my_hist = ""
    opp_hist = ""
    length = 0
    sequence = []

    output = "R"
else:
    prev_opp = str(input)
    sequence_arr = []

    # check opponent history for repeat
    opp_hist = opp_hist + prev_opp
    if (opp_hist[-2] != input):
        repeat_sequence = False

    if (opp_hist[-2] == input and repeat_sequence != True):
        # go to a repeat state
        repeat_sequence = True
        # copy the length of the history out of personal history + value to beat the sequence
        sequence = my_hist[-length: len(my_hist) + 1] + beat_dict.get(prev_opp)
        sequence_arr = sequence.split()
        # repeat history

    # check if in repeat state
    if (repeat_sequence):
        # Pop each element out of array, plus move to beat sequence
        if (len(sequence_arr) > 1 ):
            output = sequence_arr.pop(0)
        else:
            output = sequence_arr[0]

    # else do search
    else:
        if bfs_dfs == 1:
            node = None
            root = depth_first_traversal(root)
            for elements in root:
                if elements.visited == False:
                    node = elements
                    break
            node.visited = True
            name = print_name(node)
            length = len(name)

            # after finding the node that is next, we first check if it has children, if not we generate some
            if node.left == None:
                node.generate_branch()

            # Now we have to set the output to the node's value and determine if we found the break sequence






























def printTree(arr):
    str1 = ""
    for elements in arr:
        str1 = str1 + " " + elements.name
    print(str1)


# def searchDFS():
#     """ This search will be used to traverse the tree and search for the break sequence"""
#
#     """
#                      start
#                    /   |   \
#                  R     P    S
#       On generate 1  : currently working on node start
#                      start
#                    /   |   \
#                  R     P    S
#               /  | \
#              R   P  S
#       On generate 2  : currently working on node R
#                      start
#                    /   |   \
#                  R     P    S
#               /  | \
#              R   P  S
#            / | \
#           R  P  S
#       On generate 3  : currently working on node RR
#
#     """
#
#     # Start with a node
#     root = [Nodes("start")]
#     printTree(root)
#
#     # Get the root node's children and save it to an array
#
#     # for the depth, we have to create nodes and their children, but we have already used 1 layer, so depth - 1
#     for i in range(depth - 1):
#         traverse_arr = arr;
#         arr = []
#         for element in traverse_arr:
#             element = depth_first_traversal(element)
#             arr.append(element.left)
#             arr.append(element.middle)
#             arr.append(element.right)
#         printTree(arr)



#
#
# def search(num, node):
#     if (num == 0):
#         breadth_first_search(node)
#     else:
#         depth_first_traversal(node)
#     return
#
#
# # my_node = Nodes("start")
# # my_node.generate_branch(5)\
# # #print(search(1, my_node))
#
#
# searchDFS()
#
# """
# def searchBFS():
#
#
#
# def task3():
#
#     if bfs_dfs == 0:
#         searchBFS()
#     else:
#         searchDFS()
# """

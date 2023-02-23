#######################################################################################################################
#    Group Number:
#
#    Name:                         Student number:
#    Willie Broekman               21441562
#    David Nel                     21435058
#######################################################################################################################


class Nodes:
    """
    This is the main class of the tree
    This will be used to not only create a node, but also create it's branches based on the depth
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


def array_append(arr, new_arr):
    """ Used to append one array to another"""
    for elements in new_arr:
        arr.append(elements)
    return arr


def DFS(node):
    """Depth first search algorithm"""
    # check if valid node is inputted
    if (node == None):
        return []

    # We want to save all sequences to an array, which will be used to determine the breaking sequence
    arr = []
    if (node.name != "start"):
        arr.append(print_name(node))

    # Since this is a recursive function, the outputs will be returned and saved to an array
    new_arr = DFS(node.left)
    arr = array_append(arr, new_arr)

    new_arr = DFS(node.middle)
    arr = array_append(arr, new_arr)

    new_arr = DFS(node.right)
    arr = array_append(arr, new_arr)

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
            arr.append(print_name(current_node))

        # Finally all children are checked and appended to the queue
        if (current_node.left != None):
            queue.append(current_node.left)
        if (current_node.middle != None):
            queue.append(current_node.middle)
        if (current_node.right != None):
            queue.append(current_node.right)
    return arr


def print_name(node):
    name = ""
    if (node.parent != None):
        if (node.parent.name != "start"):
            name = print_name(node.parent)
    return name + node.name


def search(num, node):
    if (num == 0):
        arr = breadth_first_search(node)
    else:
        arr = DFS(node)
    return arr


my_node = Nodes("start")
my_node.generate_branch(5)
print(search(0, my_node))

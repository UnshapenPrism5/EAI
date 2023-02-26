#######################################################################################################################
#    Group Number:
#
#    Name:                         Student number:
#    Willie Broekman               21441562
#    David Nel                     21435058
#######################################################################################################################
""" GLOBAL VARIABLES """
bfs_dfs = 0
depth = 5
moves = ["R", "P", "S"]
beat_dict = {
    "R": "P",
    "P": "S",
    "S": "R"
}


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
        self.depth = 0
        self.max_depth = depth

    # Used to generate branches for a node
    # Setting depth equal to 1, will cause the program to generate only one row of elements
    # Setting depth more than 1 , will cause the program to generate an entire tree with the defined depth
    def generate_branch(self, depth_to_traverse=1):
        """Create branches for a node"""
        if depth_to_traverse != 0 and self.depth < self.max_depth:
            # Create all children of the current node
            self.left = Nodes("R")
            self.left.depth = self.depth + 1
            self.left.parent = self
            self.middle = Nodes("P")
            self.middle.depth = self.depth + 1
            self.middle.parent = self
            self.right = Nodes("S")
            self.right.depth = self.depth + 1
            self.right.parent = self

            # Recursively do the same for the entire level, if the depth is more than 1
            self.left.generate_branch(depth_to_traverse - 1)
            self.middle.generate_branch(depth_to_traverse - 1)
            self.right.generate_branch(depth_to_traverse - 1)
        return self


################################### TASK 2 ###########################################################
def depth_first_traversal(node):
    """Depth first search algorithm"""
    # check if valid node is inputted
    if node == None:
        return []
    # Since this is a recursive function, the outputs will be returned and saved to an array
    arr = []
    if node.name != "start":
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


def get_next_move():
    tree = []
    global root
    if bfs_dfs == 0:
        tree = breadth_first_search(root)
    if bfs_dfs == 1:
        tree = depth_first_traversal(root)
    for elements in tree:
        if not elements.visited:
            elements.visited = True
            elements.generate_branch()
            return elements
    return None


def print_name(node):
    name = ""
    if (node.parent != None):
        if (node.parent.name != "start"):
            name = print_name(node.parent)
    return name + node.name


if input == "":
    # print("if")
    # global root
    root = Nodes("start")
    root.generate_branch()

    # The game state will be used to determine if we should repeat or find new break sequence or play the current
    # break sequence
    # 0 -> get_next_move
    # 1 -> play_break_sequence
    # 2 -> repeat winning move
    game_state = 0

    pos = 0
    opp_hist = ""
    my_hist = ""
    break_sequence = ""

    cur_node = get_next_move()
    break_sequence = print_name(cur_node)
    game_state = 1
    # print("RESET =================================")
    # print( break_sequence)
    # print("=================================")
    pos = pos + 1
    my_hist = my_hist + break_sequence[pos - 1]
    my_output = break_sequence[pos - 1]
else:
    save = input

    if len(opp_hist) > 5:
        opp_hist = opp_hist[1::]
    if len(my_hist) > 5:
        my_hist = my_hist[1::]

    opp_hist = opp_hist + save

    # print("Opp output " + save)
    # print("My output " + my_output)
    #
    # print("Opp hist " + opp_hist)
    # print("My hist " + my_hist)
    #
    #
    # print("")
    # print("ELse")

    if game_state == 0:
        # print("Else State 1")
        my_hist = ""
        opp_hist = ""
        cur_node = get_next_move()
        break_sequence = print_name(cur_node)
        game_state = 1
        # print(break_sequence)
        # print("=================================")
        # print(root)

    if game_state == 1:
        # print("Else State 2")
        if pos >= len(break_sequence) + 1:
            # print("Else State 2 If")
            if (opp_hist[-2] == opp_hist[-1]):
                game_state = 2
            else:
                my_hist = ""
                opp_hist = ""
                pos = 1
                cur_node = get_next_move()
                break_sequence = print_name(cur_node)

                my_output = break_sequence[pos - 1]
                my_hist = my_hist + my_output
                # print(break_sequence)
                # print("=================================")
                # arr = depth_first_traversal(root)
                # tree_str = ""
                # for element in arr:
                #     tree_str = tree_str + print_name(element) + " "
                # print(tree_str)


        elif (pos == len(break_sequence)):
            # print("Else State 2 Elif")
            pos = pos + 1
            my_output = beat_dict.get(opp_hist[-1])
            my_hist = my_hist + my_output
            # print(my_output)
        else:
            # print("Else State 2 Else")
            pos = pos + 1
            # print(break_sequence)
            my_hist = my_hist + break_sequence[pos - 1]
            my_output = break_sequence[pos - 1]
    if game_state == 2:
        if (opp_hist[-2] == opp_hist[-1]):
            my_output = beat_dict.get(opp_hist[-1])
        else:
            game_state = 1
            pos = 0
            my_output = break_sequence[pos]

output = my_output

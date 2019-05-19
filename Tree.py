# A recursive Python program to print REVERSE level order traversal

import random
# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, id, parent):
        self.id = id
        self.children = list()
        self.income = 0
        self.parent = parent

    def print(self, indent, last):
        print(indent, end="")
        if (last):
            print("\\-", end="")
            indent += "  "
        else:
            print("|-", end="")
            indent += "| "
        print(self.id)
        for i in range(0,len(self.children)):
            self.children[i].print(indent, i == len(self.children)-1)


# Function to print reverse level order traversal
def reverseLevelOrder(node):
    for child in node.children:
        reverseLevelOrder(child)
    print(node.data)
    # Print nodes at a given level


def makeChildren(node):
    for child in node.children:
        makeChildren(child)
    if (random.random() > 0.5):
        insertChildToNode(node)

# Function to get the count of leaf nodes in binary tree
def getLeafCount(node):
    if node is None:
        return 0
    if(len(node.children) == 0):
        return 1
    else:
        count = 1
        for child in node.children:
            count = count + getLeafCount(child)
        return count

def insertChildToNode(node):
    node.children.append(Node(getLeafCount(root) + 1, node))

def passStage(num):
    for x in range(0,num):
        makeChildren(root)

# Driver program to test above function
root = Node(1, None)
passStage(9)
root.print("", True)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
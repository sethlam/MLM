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

def findNodeByIdRecursive(id, node):
    if id == node.id:
        return node
    else:
        for child in node.children:
            result = findNodeByIdRecursive(id, child)
            if result != None:
                return result


def findNodeById(id):
    return findNodeByIdRecursive(id, root)

def createRoot():
    return Node(1, None)

def printFromRoot():
    root.print("", True)

# Driver program to test above function
root = createRoot()
insertChildToNode(root)
insertChildToNode(root)
insertChildToNode(root)
printFromRoot()
node3 = findNodeById(3)
print(node3.parent.id)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
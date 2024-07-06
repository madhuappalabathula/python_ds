"""
Populate Inorder Successor for all nodes

Given a Binary Tree, complete the function to populate the next pointer for all nodes. The next pointer for every node should point to the Inorder successor of the node.
You do not have to return or print anything. Just make changes in the root node given to you.

Note: The node having no in-order successor will be pointed to -1. You don't have to add -1 explicitly, the driver code will take care of this.

Examples :

Input:
       10
       /  \
      8   12
     /
    3
Output: 3->8 8->10 10->12 12->-1
Explanation: The inorder of the above tree is : 3 8 10 12. So the next pointer of node 3 is pointing to 8 , next pointer of 8 is pointing to 10 and so on.And next pointer of 12 is pointing to -1 as there is no inorder successor of 12.
Input:
       1
      /
     2
   /
 3
Output: 3->2 2->1 1->-1
Explanation: The inorder of the above tree is: 3 2 1. So the next pointer of node 3 is pointing to 2 , next pointer of 2 is pointing to 1. And next pointer of 1 is pointing to -1 as there is no inorder successor of 1.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1<= no. of nodes <=105
1<= data of the node <=105


"""


# User function Template for python3


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:
    def populateNext(self, root):
        def inorder(node):
            nonlocal prev
            if not node:
                return

            inorder(node.left)

            if prev is not None:
                prev.next = node

            prev = node

            inorder(node.right)

        prev = None

        inorder(root)


# {
# Driver Code Starts
# Initial Template for Python 3

from collections import defaultdict
from collections import deque
from sys import stdin, stdout


class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


def Inorder(root):
    if root.left == None:
        return root
    return Inorder(root.left)


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        root = buildTree(input())
        obj = Solution()
        obj.populateNext(root)
        ptr = Inorder(root)
        while ptr:
            print("{}->{}".format(ptr.data,
                                  (ptr.next.data if ptr.next else -1)),
                  end=" ")
            ptr = ptr.next
        print()

# } Driver Code Ends
"""
Construct Binary Tree from Parent Array

Given an array parent that is used to represent a tree. The array indices (0-based indexing) are the values of the tree nodes and parent[i] denotes the parent node of a particular node. The parent of the root node would always be -1, as there is no parent for the root. Construct the standard linked representation of Binary Tree from this array representation and return the root node of the constructed tree.

Note: If two elements have the same parent, the one that appears first in the array will be the left child and the other is the right child. You don't need to print anything, the driver code will print the level order traversal of the returned root node to verify the output.

Examples:

Input: parent[] = [-1, 0, 0, 1, 1, 3,5]
Output: 0 1 2 3 4 5 6
Explanation: the tree generated
will have a structure like
          0
        /   \
       1     2
      / \
     3   4
    /
   5
 /
6
Input: parent[] = [2, 0, -1]
Output: 2 0 1
Explanation: the tree generated will
have a sturcture like
             2
            /
           0
          /
         1
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ parent.size() ≤ 103


"""

# User function Template for python3


'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


class Solution:
    # Function to construct binary tree from parent array.
    def formTree(self, root, mpp):
        if not root:
            return None
        if root.key in mpp:
            if len(mpp[root.key]) > 0:
                root.left = mpp[root.key][0]
            if len(mpp[root.key]) > 1:
                root.right = mpp[root.key][1]
        if root.left:
            self.formTree(root.left, mpp)
        if root.right:
            self.formTree(root.right, mpp)
        return root

    def createTree(self, parent):
        node_list = [Node(i) for i in range(len(parent))]
        mpp = {}
        rootNode = None

        for i, ele in enumerate(parent):
            if ele == -1:
                rootNode = node_list[i]
            if ele in mpp:
                mpp[ele].append(node_list[i])
            else:
                mpp[ele] = [node_list[i]]

        return self.formTree(rootNode, mpp)


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict

# Contributed by : Nikhil Kumar Singh
'''
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
'''


# Python implementation to construct a Binary Tree from
# parent array


# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Function should print the level order of the tree in sorted format
def traverse_level_order(root):
    # Code here
    if root is None:
        return
    que = []
    que.append(root)
    while 1:
        n = len(que)
        if n == 0:
            break
        sorted_nodes = [node.key for node in que]
        sorted_nodes.sort()
        print(*sorted_nodes, end=" ")
        while (n > 0):
            node = que.pop(0)
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
            n -= 1


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(int,
                     input().strip().split()))  # parent child info in list
        ob = Solution()
        traverse_level_order(ob.createTree(a))
        print()

# } Driver Code Ends
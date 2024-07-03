"""
Duplicate Subtrees

Given a binary tree, your task is to find all duplicate subtrees from the given binary tree.

Note:  Return the root of each tree in the form of a list array & the driver code will print the tree in pre-order tree traversal in lexicographically increasing order.

Examples:

Input :

Output: 2 4
        4
Explanation: The above tree have two duplicate subtrees.i.e
  2
 /
4  and 4. Therefore, you need to return the above tree root in the form of a list.
Input:     5
          / \
         4   6
        / \
       3   4
          / \
         3   6
Output: 4 3
        6
Explanation: In the above tree, there are two duplicate subtrees.i.e
  4
 /
3   and 6. Therefore, you need to return the above subtrees root in the form of a list.
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:
1<= size of binary tree <=100
"""


class Solution:
    def printAllDups(self, root):
        # code here
        from collections import Counter
        counter = Counter()
        ans = []

        def walk(n):
            if not n:
                return None
            l = walk(n.left)
            r = walk(n.right)
            tree = (n.data, l, r)
            counter[tree] += 1
            if counter[tree] == 2:
                ans.append(n)
            return tree

        walk(root)
        return sorted(ans, key=lambda x: x.data)




from collections import deque
from collections import defaultdict


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


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


def preord(root):
    if not root:
        return
    print(root.data, end=' ')
    preord(root.left)
    preord(root.right)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = input()
        root = buildTree(s)
        ob = Solution()
        res = ob.printAllDups(root)
        for i in res:
            preord(i)
            print()

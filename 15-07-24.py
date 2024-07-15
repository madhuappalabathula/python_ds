"""
Smallest number

Given two integers s and d. The task is to find the smallest number such that the sum of its digits is s and the number of digits in the number are d. Return a string that is the smallest possible number. If it is not possible then return -1.

Examples:

Input: s = 9, d = 2
Output: 18
Explanation: 18 is the smallest number possible with the sum of digits = 9 and total digits = 2.
Input: s = 20, d = 3
Output: 299
Explanation: 299 is the smallest number possible with the sum of digits = 20 and total digits = 3.
Expected Time Complexity: O(d)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ s ≤ 100
1 ≤ d ≤ 6


"""


# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3
class Solution:
    def smallestNumber(self, s, d):
        # code here
        maxv = 9 * d
        if s > maxv: return -1
        ans = ""
        s -= 1
        for i in range(0, d - 1):
            if s >= 9:
                ans += str(9)
                s -= 9
            else:
                ans += str(s)
                s = 0
        ans += str(s + 1)
        ans = ans[::-1]
        return ans

# Driver Code Starts.


import sys
import math

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

#Driver Code Ends
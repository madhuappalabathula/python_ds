"""
Count Smaller elements
Difficulty: HardAccuracy: 38.16%Submissions: 72K+Points: 8
Given an array arr containing non-negative integers. Count and return an array ans where ans[i] denotes the number of smaller elements on right side of arr[i].

Examples:

Input: arr[] = [12, 1, 2, 3, 0, 11, 4]
Output: [6, 1, 1, 1, 0, 1, 0]
Explanation: There are 6 smaller elements right after 12. There is 1 smaller element right after 1. And so on.
Input: arr[] = [1, 2, 3, 4, 5]
Output: [0, 0, 0, 0, 0]
Explanation: There are 0 smaller elements right after 1. There are 0 smaller elements right after 2. And so on.
Expected Time Complexity: O(n*logn)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i]  ≤ 108
"""
import bisect
class Solution:
    def constructLowerArray(self,arr):
        ans=[0]
        right=[arr[-1]]
        for i in range(len(arr)-2,-1,-1):
            #count of element smaller than arr[i] in right
            count=bisect.bisect_left(right,arr[i])
            bisect.insort(right,arr[i])
            ans.append(count)
        return ans[::-1]



#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
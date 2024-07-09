"""
Closest Three Sum

Given an array, arr of integers, and another number target, find three integers in the array such that their sum is closest to the target. Return the sum of the three integers.

Note: If there are multiple solutions, return the maximum one.

Examples :

Input: arr[] = [-7, 9, 8, 3, 1, 1], target = 2
Output: 2
Explanation: There is only one triplet present in the array where elements are -7,8,1 whose sum is 2.
Input: arr[] = [5, 2, 7, 5], target = 13
Output: 14
Explanation: There is one triplet with sum 12 and other with sum 14 in the array. Triplet elements are 5, 2, 5 and 2, 7, 5 respectively. Since abs(13-12) ==abs(13-14) maximum triplet sum will be preferred i.e 14.
Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)

Constraints:
3 ≤ arr.size() ≤ 103
-105 ≤ arr[i] ≤ 105
1 ≤ target ≤ 105
"""


# User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest(self, arr, target):
        #
        arr.sort()
        n = len(arr)
        clsm = float('inf')
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                curr = arr[i] + arr[l] + arr[r]
                if curr == target:
                    return curr
                if abs(curr - target) < abs(clsm - target) or \
                        (abs(curr - target) == abs(clsm - target) and curr > clsm):
                    clsm = curr
                if curr < target:
                    l += 1
                else:
                    r -= 1
        return clsm


# Driver Code Starts

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.threeSumClosest(A, k))

# Driver Code Ends
"""
Maximum product subset of an array

Given an array arr. The task is to find and return the maximum product possible with the subset of elements present in the array.

Note:

The maximum product can be a single element also.
Since the product can be large, return it modulo 109 + 7.
Examples:

Input: arr[] = [-1, 0, -2, 4, 3]
Output: 24
Explanation: Maximum product will be ( -1 * -2 * 4 * 3 ) = 24
Input: arr[] = [-1, 0]
Output: 0
Explanation: Maximum product will be ( -1 * 0) = 0
Input: arr[] = [5]
Output: 5
Explanation: Maximum product will be 5.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 2 * 104
-10 <= arr[i] <= 10


"""


# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        n = len(arr)
        d = float("-inf")
        d = max(arr)
        ct = 0
        if n == 1:
            return arr[0]
        ans = 1
        res = float("-inf")
        mod = 10 ** 9 + 7
        for i in arr:
            if i == 0:
                ct += 1
            if i != 0:
                ans = ans * i
            if i < 0 and i > res:
                res = i
        if ans < 0:
            ans = ans // res
        if ct == n:
            return 0
        if d == 0 and ans == 1:
            return d
        return ans % mod


# {
# Driver Code Starts.
if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)

    for result in results:
        print(result)
# } Driver Code Ends
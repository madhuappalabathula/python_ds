"""Coverage of all Zeros in a Binary Matrix
Given a binary matrix contains 0s and 1s only, we need to find the sum of coverage of all zeros of the matrix where coverage for a particular 0 is defined as a total number of ones around a zero in left, right, up and bottom directions.

Examples:

Input:
matrix = [[0, 1, 0],
          [0, 1, 1],
          [0, 0, 0]]
Output: 6
Explanation: There are a total of 6 coverage are there

Input:
matrix = [[0, 1]]
Output: 1
Explanation: There are only 1 coverage.
Expected Time Complexity: O(n * m)
Expected Space Complexity: O(1)

Constraints:
1 <= matrix.size, matrix[0].size <= 100 """

#User function Template for python3

class Solution:
    def findCoverage(self, matrix):
        Sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i < len(matrix)-1 and matrix[i+1][j] == 1:
                        Sum += 1
                    if i > 0 and matrix[i-1][j] == 1:
                        Sum += 1
                    if j > 0 and matrix[i][j-1] == 1:
                        Sum += 1
                    if j < len(matrix[0])-1 and matrix[i][j+1] == 1:
                        Sum += 1
        return Sum


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = [[0,1,0],[0,1,1],[0,0,0]]
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)
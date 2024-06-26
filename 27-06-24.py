"""Toeplitz matrix
A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is constant, i.e., all elements in a diagonal are the same. Given a rectangular matrix mat, your task is to complete the function isToeplitz which returns true if the matrix is Toeplitz otherwise, it returns false.

Examples:

Input:
mat = [[6, 7, 8],
       [4, 6, 7],
       [1, 4, 6]]
Output: true
Explanation: The test case represents a 3x3 matrix
 6 7 8
 4 6 7
 1 4 6
Output:true, as values in all downward diagonals from left to right contain the same elements.

Input:
mat = [[1,2,3],
       [4,5,6]]
Output: false
Explanation: Matrix of order 2x3 will be 1 2 3 4 5 6 Output: false as values in all diagonals are not the same.

Constraints:
1<=mat.size,mat[0].size<=40
1<=mat[i][j]<=100

Expected time complexity: O(n*m)
Expected space complexity: O(1)"""



# You are required to complete this method
# Return True/False or 1/0
def isToepliz(mat):
    #code here
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if mat[i][j] != mat[i-1][j-1]:
                return False;
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k += 1
        b = isToepliz(matrix)

        if b == True:
            print("true")
        else:
            print("false")
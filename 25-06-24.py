"""You are given an integer k and matrix mat. Return a matrix where it is rotated Left k times.

Examples:

Input: k=1, mat=[[1,2,3],[4,5,6],[7,8,9]]
Output:
1 2 3
4 5 6
7 8 9
Explanation: Rotate the matrix by one
1 2 3       2 3 1
4 5 6  =>  5 6 4
7 8 9       8 9 7
Input: k=2, mat=[[1,2,3],[4,5,6],[7,8,9]]
Output:
3 1 2
6 4 5
9 7 8
Explanation: After rotating the matrix looks like
1 2 3       2 3 1       3 1 2
4 5 6  =>  5 6 4  =>   6 4 5
7 8 9       8 9 7       9 7 8
Expected Time Complexity: O(n*m)
Expected Auxillary Space: O(n*m)

Constraints:
1<= mat.size, mat[0].size, mat[i][j] <=1000
1<=k<=10000"""





class Solution:
    def rotateMatrix(self, k, mat,n):
        k = k%len(mat[0])
        for i in range(n):
            mat[i] = mat[i][k:]+mat[i][:k]
        return mat




import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = mat=[[1,2,3],[4,5,6],[7,8,9]]
        ob = Solution()
        ans = ob.rotateMatrix(k, mat,n)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()



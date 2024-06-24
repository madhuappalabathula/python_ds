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



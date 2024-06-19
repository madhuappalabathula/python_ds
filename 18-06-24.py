"""Number of Rectangles in a Circle
Given a circular sheet of radius, r. Find the total number of rectangles with integral length and width that can be cut from the sheet that can fit on the circle, one at a time.

Examples :

Input: r=1
Output: 1
Explanation: Only 1 rectangle of dimensions 1x1.
Input: r=2
Output: 8
Explanation: The 8 possible rectangles are
(1x1)(1x2)(1x3)(2x1)(2x2)(2x3)(3x1)(3x2).
Expected Time Complexity: O(r2)
Expected Auxillary Space: O(1)


Constraints:
1<=r<=1000 """


# User function template for Python

class Solution:
    def rectanglesInCircle(self, r):
        # code here
        count = 0
        R = 2 * r
        rs = r * r
        for l in range(1, R + 1):
            for w in range(1, R + 1):
                hl = l / 2
                hw = w / 2
                if (hl ** 2 + hw ** 2) <= rs:
                    count += 1
        return count


import math
if __name__=='__main__' :
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        ans=ob.rectanglesInCircle(N)
        print(ans)
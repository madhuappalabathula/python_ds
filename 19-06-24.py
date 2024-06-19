"""Find maximum volume of a cuboid
Difficulty: EasyAccuracy: 53.16%Submissions: 19K+Points: 2
You are given a perimeter & the area. Your task is to return the maximum volume that can be made in the form of a cuboid from the given perimeter and surface area.
Note: Round off to 2 decimal places and for the given parameters, it is guaranteed that an answer always exists.

Examples

Input: perimeter = 22, area = 15
Output: 3.02
Explanation: The maximum attainable volume of the cuboid is 3.02
Input: perimeter = 20, area = 5
Output: 0.33
Explanation: The maximum attainable volume of the cuboid is 0.33
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints :
1 ≤ perimeter ≤ 109
1 ≤ area ≤ 109  """



class Solution:
    def maxVolume(self, perimeter, area):
        d = perimeter*perimeter-24*area;
        l = (perimeter-math.sqrt(d))/12;
        h = (perimeter/4)-2*l;
        return l*l*h
import math
if __name__=='__main__' :
    t=int(input())
    for _ in range(t):
        perimeter ,area=[int(x) for x in input().split()]

        ob=Solution()
        print('%.2f' %ob.maxVolume(perimeter, area))
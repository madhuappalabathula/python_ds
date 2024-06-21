"""Extract the Number from the String
Given a sentence containing several words and numbers. Find the largest number among them which does not contain 9. If no such number exists, return -1.

Examples :

Input: sentence="This is alpha 5057 and 97"
Output: 5057
Explanation: 5057 is the only number that does
not have a 9.
Input: sentence="Another input 9007"
Output: -1
Explanation: Since there is no number that
does not contain a 9,output is -1.
Expected Time Complexity: O(n)
Expected Auxillary Space: O(n)

Constraints:
1<=n<=106
1<=answer<=1018

n is the length of a given sentence."""


class Solution:
    def ExtractNumber(self, sentence):
        # code here
        words = sentence.split(" ")
        large_number = -1

        for word in words:
            if word.isdigit() and '9' not in word:
                large_number = max(large_number, int(word))
        return large_number


t=int(input())
for _ in range(t):
    S=input()
    ob=Solution()
    ans=ob.ExtractNumber(S)
    print(ans)
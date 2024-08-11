# https://leetcode.com/problems/valid-anagram
s, t = "anagram", "nagaram"
def isAnagram(self, s, t) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

    # Time : O(N) as no sorting needed, manually counting
    # Memory : O(N)
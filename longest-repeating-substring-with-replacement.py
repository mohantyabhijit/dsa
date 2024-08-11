# https://leetcode.com/problems/longest-repeating-character-replacement/editorial/
class StringModifier:
    def characterReplacement(self, s: str, k: int) -> int:
        # Input: s = "AAABABB", k = 1
        # Output: 5

        # modified approach :
        # take a sliding window
        # for every window check the freq of characters, get most frequest character
        # keep maintaining the freq hashmap
        # increase for every time the right pointer is at a character
        # whenever the left pointer is moved, we shorten the sliding window and remove it from our frequency counter
        # we are only allowed max k swaps
        # whenever we increase k swaps we increment the left pointer and keep checking
        # r - l + 1 is the size of the sliding window
        freq = {}

        l = 0
        res = 0

        for r in range(l, len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while (r - l  + 1 ) - max(freq.values()) > k :
                freq[s[l]] -= 1
                l = l + 1

            res = max(res, r - l + 1)

        return res





if __name__ == '__main__':
    modifier = StringModifier()
    result = modifier.characterReplacement('AAABABB', 1)
    print("Output:", result)






# Brute Force approach : For all substrings, check frequency of each character
# Whichever character has most frequency, the other ones need to be swapped
# The number of swaps should be less than k
# find max substring
'''
        for start in range(len(s)):
            for end in range(start, len(s)):
                substring = s[start : end + 1]
                freq = {}

                for char in substring:
                    if char in freq :
                        freq[char] += 1
                    else :
                        freq[char] = 1

                max_recurring_character = max(freq.values(), default=0)
                number_of_swaps = len(substring) - max_recurring_character

                if number_of_swaps <= k :
                    max_length = max(max_length, len(substring))

        return max_length
'''
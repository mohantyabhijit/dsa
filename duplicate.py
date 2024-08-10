# https://leetcode.com/problems/contains-duplicate/description/
# insight : hashset of python only contains unique values

nums = [1,2,3,1]
def containsDuplicate(self, nums) -> bool:
    hashset = set()

    for n in nums :
        if n in hashset :
            return True
        hashset.add(n)

    return False

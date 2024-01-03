class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()

        left  , right = 0 , len(skill)-1
        myhash = {}

        myhash[skill[left] + skill[right]] = skill[left]*skill[right]
        Sum = 0
        while left < right:

            Sum += skill[left] * skill[right]
            if skill[left] + skill[right] not in myhash:
                return -1
            left += 1
            right-=1
        return Sum

# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []  
        idx = bisect_left(arr , x )
        if idx == 0:
            return arr[:k]
        N = len(arr)
        left , right = idx-1 , idx

        while k:
            if abs(arr[right%N] - x) < abs(arr[left] - x):
                ans.append(arr[right % N])
                right +=1
            elif abs(arr[right%N] - x) > abs(arr[left] - x):
                ans.append(arr[left])
                left -=1
            else:
                if arr[right%N] > arr[left]:
                    ans.append(arr[left])
                    left -=  1
                else:
                    ans.append(arr[right % N])
                    right +=1
            k-=1

        return sorted(ans)
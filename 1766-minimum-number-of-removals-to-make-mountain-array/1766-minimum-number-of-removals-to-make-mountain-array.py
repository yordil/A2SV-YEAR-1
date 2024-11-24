class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:


        lis = []
        front = [0] * len(nums)
        back = [0] * len(nums)


        for i in range(len(nums)):

            pos = bisect_left(lis , nums[i])

            if pos == len(lis):
                lis.append(nums[i])
            
            else:
                lis[pos] = nums[i]

            front[i] = pos+  1

     
        lis = []
        for i in range(len(nums)-1 , -1 ,-1):

            pos = bisect_left(lis , nums[i])

            if pos == len(lis):
                lis.append(nums[i])

            else:
                lis[pos] = nums[i]

            back[i] = pos + 1

        maxx = 0
   

        for i in range(len(back)):
            if back[i] > 1 and front[i] > 1:
                maxx = max(back[i] + front[i] - 1, maxx)

        return len(nums) - maxx

            

            
            



        
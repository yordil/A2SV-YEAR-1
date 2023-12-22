class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        myhash = defaultdict(list)
        ans = []
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                myhash[i+j].append(mat[i][j])
        
        for i in myhash:
            if i % 2 == 0:
                ans.extend(myhash[i][::-1])
            else:
                ans.extend((myhash[i]))
        return ans
                
            
            
        
        
        
        
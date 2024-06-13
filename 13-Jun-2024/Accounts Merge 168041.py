# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {i:i for i in range(len(accounts))}
        size = {i:0 for i in range(len(accounts))}

        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
            
            return x

        def union(x,y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if size[parentX] > size[parent[y]]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]
        
        visited = defaultdict(int)
        for index , value in enumerate(accounts):
            for email in value[1:]:
                if email in visited:
                    union(index , visited[email])

                visited[email] = index

        temp = defaultdict(set)
         
        for index , value in enumerate(accounts):
            idx = find(index)
            for email in value[1 : ]:
                temp[idx].add(email)

        ans = []

        for key, value in temp.items():
            name = accounts[key][0]
            val = sorted(list(value))
            added = [name] + val
            ans.append(added)

        return ans
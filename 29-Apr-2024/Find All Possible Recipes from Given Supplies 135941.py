# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipesset = set(recipes)
        foodhash = {recipes[i] : i for i in range(len(recipes))}
        indegree = [0] * len(recipes)
        supplies = set(supplies)
        graph = defaultdict(list)
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] in supplies:
                    continue
                elif ingredients[i][j] in recipesset:
                    graph[foodhash[ingredients[i][j]]].append(i)
                    indegree[i] +=1
        
        que= deque()
        answer = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                for ingri in ingredients[i]:
                    if ingri not in supplies:
                        break
                else:
                    que.append(i)
                    answer.append(recipes[i])
        
        while que:
            node = que.popleft()

            for nbr in graph[node]:
                indegree[nbr] -=1
                if indegree[nbr] == 0:
                    que.append(nbr)
                    answer.append(recipes[nbr])
                
        return answer
       
    






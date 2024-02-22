class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
       
        print(arr)
        for a in arr:
            if a == ".." and stack:
                stack.pop()
            elif a == "." or a == "":
                continue
            elif a != "..":
                stack.append(a)
        return  "/" + "/".join(stack) 
      

            

        


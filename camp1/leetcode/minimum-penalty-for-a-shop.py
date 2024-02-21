class Solution:
    def bestClosingTime(self, customers: str) -> int:
        suffixofy = customers.count("Y")
        prefixofn = 0
        answer = (suffixofy , 0)

        for i in range(len(customers)):
            if customers[i] == "Y":
                suffixofy -= 1
            else:
                prefixofn +=1
            
            penality = suffixofy + prefixofn

            answer = min(answer , (penality , i+1))
        
        return answer[1]

            
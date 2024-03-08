class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        prefix  = [0] *  len(s)
        candleprefix = [ 0] * len(s)
        for i in range(len(s)):
            if s[i] == "|":
                prefix[i] = 0
                candleprefix[i] = 1
             
            else:
                prefix[i] = 1
                candleprefix[i] = 0  
        candleprefix = list(accumulate(candleprefix))
        prefixsum = list(accumulate(prefix))
     
        print(prefixsum[queries[0][0]]  , prefixsum[queries[0][1]])
        i = 0
        for query in queries:
            start , end  = query

            if prefix[start] == 0 and prefix[end] == 0:
                 ans[i] = prefixsum[end] - prefixsum[start]
            else:
              
                if prefix[start] != 0:
                    val = candleprefix[start]
                    start = bisect_right(candleprefix , val)
                if prefix[end] != 0:
                    val2 = candleprefix[end]
                    end = bisect_left(candleprefix , val2 )
                # print(end , start)
                if start < end and start != len(s):
                    ans[i] = prefixsum[end] - prefixsum[start]       
                
                
            # print(start , end )
            i+=1
          

        return ans






                # if prefix[start] != 0:
                #    start +=1
                # if prefix[end] !=0:
                #     end -=1
                
                #     break  
            
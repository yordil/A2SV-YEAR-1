class Solution:
    def countGoodNumbers(self, n: int) -> int: 
        mod = 10**9 + 7
        even =  n // 2 if n % 2 == 0 else n // 2 + 1
        odd =  n // 2 
        print(even , odd)
        def power(x , n):
            if n == 0:
                return 1
            if n == 1:
                return x

            temp = power(x , n//2)
            return (temp * temp) % mod if n %2 == 0 else (x * temp * temp) % mod


        ans = power(5 , even)
        ans2 = power(4 , odd)

        return (ans * ans2) % mod


        # if n % 2 == 0:
        #     half = n // 2
        #     return ((5**half) % ((10**9) + 7) *  4** half % ((10**9) + 7)) % ((10**9) + 7)
        # else:
        #     half = n // 2
           
        #     # print(a , b , n//2)
        #     return  ((5 ** (half + 1)) % ((10**9) + 7) * (4**(half)  % ((10**9) + 7)))  % ((10**9) + 7)

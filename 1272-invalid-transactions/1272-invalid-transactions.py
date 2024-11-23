class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        myhash = defaultdict(list)

        
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            myhash[name].append([int(time), city])

        for name in myhash:
            myhash[name].sort()

        answer = []

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time, amount = int(time), int(amount)

            if amount > 1000:
                answer.append(transaction)
                continue

            
            all_transactions = myhash[name]

            print(all_transactions)
            for t, c  in all_transactions:
                if abs(t - time) <= 60 and c != city:
                    answer.append(transaction)
                    break
                

        return answer

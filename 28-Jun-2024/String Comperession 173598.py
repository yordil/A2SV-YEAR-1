# Problem: String Comperession - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:

        left = 0
        right = 0

        while right < len(chars):
            char = chars[right]
            count = 0

            while right < len(chars) and chars[right] == char:
                right += 1
                count += 1

            chars[left] = char
            left += 1

            if count > 1:
                for d in str(count):
                    chars[left] = d
                    left += 1

        return left

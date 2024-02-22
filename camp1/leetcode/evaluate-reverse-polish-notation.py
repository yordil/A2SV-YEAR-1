class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 + operand2
                stack.append(result)
            elif token == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = int(operand1 / operand2)
                stack.append(result)
            elif token == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 * operand2
                stack.append(result)
            elif token == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 - operand2
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[0]  # The final result should be at the top of the stack.


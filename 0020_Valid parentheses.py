class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

      

            if ch in "({[":
                stack.append(ch)

            else:
                if not stack:
                    return False

                top = stack.pop()

                if top != pairs[ch]:
                    return False

        0return len(stack) == 
        

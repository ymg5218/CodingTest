# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "{":
                stack.append("}")
            elif p == "(":
                stack.append(")")
            elif p == "[":
                stack.append("]")
            elif stack and stack[-1] == p:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))
# validParentheses: http://www.lintcode.com/en/problem/valid-parentheses/#

class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        if s is None or len(s) == 0:
            return True
        stack = []
        for item in s:
            if len(stack) == 0:
                stack.append(item)
            else:
                if stack[-1] == '(' and item == ')':
                    stack.pop()
                elif stack[-1] == '{' and item == '}':
                    stack.pop()
                elif stack[-1] == '[' and item == ']':
                    stack.pop()
                else:
                    stack.append(item)
        if len(stack) != 0:
            return False
        return True

s1 = "{}()[]"
s2 = "{[()]}"
s3 = "{[}()]"
s4 = "(])"
Sol = Solution()
print Sol.isValidParentheses(s1)
print Sol.isValidParentheses(s2)
print Sol.isValidParentheses(s3)
print Sol.isValidParentheses(s4)
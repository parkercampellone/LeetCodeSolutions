"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Ok so I need to use a stack here. when an open parentheses of any kind is added, the closing parentheses should be added to the stack.
if a closing parentheses is encountered, compare it to the top of the stack, and if it does not match, the string is invalid.

When parsing the string I need to be able to differentiate a closing parentheses from an opening. I could make a list for opening and closing, but then
the problem is iterating and also not knowing what the pair is.  I will create a pairs dict. The keys will be opening and the values will be closing. 

When parsing the string, if what we encounter is an opening, grab the value and add it to stack. 
If what we encounter is not an opening, compare the char to the char at top of stack. if they do not match the string is invalid.
"""

class Solution:

    pairs = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    def isValid(self, s: str) -> bool:

        close_stack = []
        
        for i in range(len(s)):
            char = s[i]

            if char in self.pairs:
                close_stack.append(self.pairs.get(char))

            else:
                if len(close_stack) < 1: return False
                top_of_stack = close_stack[-1]
                if top_of_stack == char:
                    close_stack.pop()
                    continue
                else:
                    return False

        if len(close_stack) > 0: return False                
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("}"))            
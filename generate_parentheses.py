"""
IF number is n, string must be n*2 long, if len(string) == n*2, append and return..

if open_count < target, recursive call, one adding ), and one adding (.
    only call the ")" so long as close count is less than open count.
if open_count == target, you must use ).

"""

class Solution:

    paran = "()"
    ans = []

    def get_combinations(self, open_count: int, close_count: int, target: int, curr_str: str):

        if len(curr_str) == target * 2:
            self.ans.append(curr_str)
            return

        else:
            if open_count < target:

                # run one with open parantheses
                self.get_combinations(open_count + 1, close_count, target, curr_str + "(")

                # run one with close parantheses if possible
                if close_count < open_count:
                    self.get_combinations(open_count, close_count + 1, target, curr_str + ")")

            elif open_count == target:
                self.get_combinations(open_count, close_count + 1, target, curr_str + ")")



            
                



    def generateParenthesis(self, n: int) -> List[str]:

        self.ans = []
        self.get_combinations(1, 0, n, "(")

        return self.ans

if __name__ == "__main__":

    sol = Solution()
    print(sol.generateParenthesis(3))
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

"""
So, it will be a recursive call. at every step, recursively call for every elemnt.
i.e. [1,2,3,4] and target = 4

will have to start a tree from each element.
.
├── 1/
│   ├── 1/
│   │   ├── 1
│   │   ├── 2
│   │   ├── 3
│   │   ├── 4
│   │   └── 5
│   ├── 2
│   ├── 3
│   ├── 4
│   └── 5
├── 2/
│   ├── 1
│   ├── 2
│   ├── 3
│   ├── 4
│   └── 5
├── 3/
│   ├── 1
│   ├── 2
│   ├── 3
│   ├── 4
│   └── 5
├── 4/
│   ├── 1
│   ├── 2
│   ├── 3
│   ├── 4
│   └── 5
└── 5/
    ├── 1
    ├── 2
    ├── 3
    ├── 4
    └── 5

I will go down every single tree until we reach the target.
Easy peasy. I did this one, just not on my laptop.s

"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


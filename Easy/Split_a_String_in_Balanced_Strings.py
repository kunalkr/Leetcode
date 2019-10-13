# Balanced strings are those who have equal quantity of 'L' and 'R' characters.

# Given a balanced string s split it in the maximum amount of balanced strings.

# Return the maximum amount of splitted balanced strings.

 

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:

# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".

 

# Constraints:

#     1 <= s.length <= 1000
#     s[i] = 'L' or 'R'


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) == 0:
            return 0

        p_count = 0
        count = 0
        
        for c in s:
            if not p_count:
                prev = c
                p_count = 1
                continue

            if c == prev:
                p_count += 1
            else:
                p_count -= 1

            if not p_count:
                count += 1
        return count

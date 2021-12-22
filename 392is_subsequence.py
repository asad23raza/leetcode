# Leetcode question 392: 
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by
#  deleting some (can be none) of the characters without disturbing the relative 
#  positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"
#   while "aec" is not).
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        if len(s) == 0:
            return True
        
        for x in range(len(t)):
            if t[x] == s[i]:
                i += 1
                if (i == len(s)):
                    return True
        return(i == len(s))
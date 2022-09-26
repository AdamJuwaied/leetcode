class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Creating the sentence into a list
        seperate = s.split()
        
        # Returning the last word in the list
        return len(seperate[-1])
# Longest Palindromic Substring
# Manacher's Algorithm

import operator

class Manacher(object):
    def longestPalindromeLen(self, str, index):
        """ Gives length of longest palindrome with center at index in str """
        length = 1
        while index + length < len(str) and index - length >= 0:
            if str[index + length] == str[index - length]:
                length += 1
            else:
                break
        return length - 1
    def longestPalindrome(self, str):
        """ Finds longest palindromic substring of str """
        # to speed things up, first check to see if the string consists of the same character repeated
        # this is a simplistic palindrome, but would take a long time to run without this case
        if str == len(str) * str[0]:
            return str
        center = 0 # index around which palindrome search is currently occurring
        right = 0 # the rightmost char reached by a palindrome
        str = "#" + "#".join(str) + "#" # turns "str" into "#s#t#r#"
        pLenArray = [0] * len(str) # array to keep track of palindrome lengths at each center
    
        for i in range(1, len(str)):
            mirrorPos = 2 * center - i # mirror position to i
            # two cases:
            # (1) i is not worth checking because...
            #       - the rightmost edge of any palindrome centered at i is within an existing palindrome
            #       - mirrorPos exceeds str's bounds
            if pLenArray[mirrorPos] + i <= right and mirrorPos >= len(str) - i:
                pLenArray[i] = pLenArray[mirrorPos] # i and its mirrorPos have the same palindrome length
            # (2) i is worth checking for palindromes in all other cases
            else:
                pLenCurr = self.longestPalindromeLen(str, i)
                pLenArray[i] = pLenCurr
                # if the palindrome length was greater than 1, need to update right bound for first cases
                if pLenCurr > 1:
                    center = i
                    right = center + pLenCurr/2 # could also be replaced by pLenCurr, but I halved it to improve accuracy
        
        print(pLenArray)           
        # get maximum element index and element
        maxi, maxv = max(enumerate(pLenArray), key=operator.itemgetter(1))
        
        # find palindrome, remove #s
        print(str)
        print(str[maxi-maxv:maxi])
        print(str[maxi:maxi+maxv])
        str = (str[maxi-maxv:maxi] + str[maxi:maxi+maxv]).replace("#", "")
        return str
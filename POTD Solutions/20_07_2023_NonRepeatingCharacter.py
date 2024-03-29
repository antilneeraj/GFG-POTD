class Solution:
    def nonrepeatingCharacter(self,s):
        mydict = dict()
        
        for letter in s:
            if(letter not in mydict): mydict[letter] = 0
            mydict[letter] += 1
        for letter in s:
            if(mydict[letter] == 1):
                return letter
        return '$'

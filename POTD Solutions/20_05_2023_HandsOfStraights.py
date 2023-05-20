from collections import Counter

class Solution:
    def isStraightHand(self, N, groupSize, hand):
        counter = Counter(hand)
        hand = sorted(hand)
        
        for item in hand:
            if counter[item] == 0:
                continue
            
            for i in range(groupSize):
                if counter[item + i] == 0:
                    return False
                
                counter[item + i] -= 1
        
        return True

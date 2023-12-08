import pytest
import heapq as hq
from enum import Enum
sample_input = "sample_input.txt"

card_values = {"T":10,"J":11,"Q":12,"K":13,"A":14}
class HAND(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

def getHand(hand):
        hand_dict = {}
        for c in hand:
            if c in hand_dict:
                hand_dict[c] += 1
            else:
                hand_dict[c] = 1
        sorted_card_frequency = [value for key, value in hand_dict.items()]
        sorted_card_frequency.sort(reverse=True)
        if len(hand_dict) == 1:
            # five of a kind
            return HAND.FIVE_OF_A_KIND
        elif len(hand_dict) == 5:
            # high card
            return HAND.HIGH_CARD
        elif len(hand_dict) == 2:
            # four of a kind
            if sorted_card_frequency[0] == 4:
                return HAND.FOUR_OF_A_KIND
            else:
                # full house
                return HAND.FULL_HOUSE
            pass
        elif len(hand_dict) == 3:
            # 3 of a kind
            if sorted_card_frequency[0] == 3:
                return HAND.THREE_OF_A_KIND
            else:
                # two pair
                return HAND.TWO_PAIR
        elif len(hand_dict) == 4:
            # one pair
            return HAND.ONE_PAIR

class Hand:
    def __init__(self, line):
        self.hand, self.val = line.split()
        self.val = int(self.val)
        self.type = getHand(self.hand)

    def __lt__(self, other):
        # overloaded comparison operator
        if self.type != other.type:
            return self.type.value < other.type.value
        else:
            for i in range(5):
                self_c = int(self.hand[i]) if (self.hand[i]).isdigit() else card_values[self.hand[i]]
                other_c = int(other.hand[i]) if (other.hand[i]).isdigit() else card_values[other.hand[i]]
                
                if self_c != other_c:
                    return self_c < other_c

        return 0 < 0
    
    def getWinning(self):
        return self.val

def solution(filename):
    f = open(filename) 
    lines = f.readlines()
    num_of_ranks = len(lines)
    hand_list = []
    rank = 1
    total_winnings = 0

    for line in lines:
        hand = Hand(line.strip())
        hand_list.append(hand)

    hand_list.sort()

    for hand in hand_list:
        total_winnings += hand.val * rank
        rank += 1

    print(total_winnings)
    return total_winnings  

def test_sample():
    assert(solution(sample_input) == 6440)

answer = solution('day_seven.txt')

#test_sample()
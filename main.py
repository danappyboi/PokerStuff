import random
from objs import Card, Suits, Ranks, HandRanks
from handrank_calc import hand_ranking
import copy
import itertools
 

def hand_to_str(hand):
    return hand.name

deck = set()
for rank in Ranks:
    for suit in Suits:
        deck.add(Card(rank, suit))


# hand = {Card(Ranks.ACE, Suits.SPADE), Card(Ranks.ACE, Suits.CLUB)}
# board = {Card(Ranks.ACE, Suits.DIAMOND), Card(Ranks.ACE, Suits.HEART), Card(Ranks.KING, Suits.HEART)}

# hand = {Card(Ranks.ACE, Suits.SPADE), Card(Ranks.TWO, Suits.CLUB)}
# board = {Card(Ranks.FOUR, Suits.DIAMOND), Card(Ranks.THREE, Suits.HEART), Card(Ranks.KING, Suits.HEART)}


# handrank, order = hand_ranking(hand, board)

# print(hand_to_str(handrank))

#TODO: if the input is shitty, you need errors to correct it
def str_to_card(input):
    input_rank, input_suit = input[0], input[1]
    card_rank = 0
    card_suit = 0

    if input_rank.isdigit():
        for rank in Ranks:
            if rank.value == int(input_rank):
                card_rank = rank
    else:
        if input_rank == "T":
            card_rank = Ranks.TEN
        elif input_rank == "J":
            card_rank = Ranks.JACK
        elif input_rank == "Q":
            card_rank = Ranks.QUEEN
        elif input_rank == "K":
            card_rank = Ranks.KING
        elif input_rank == "A":
            card_rank = Ranks.ACE

    if input_suit == "H":
        card_suit = Suits.HEART
    elif input_suit == "D":
        card_suit = Suits.DIAMOND
    elif input_suit == "C":
        card_suit = Suits.CLUB
    else: #not fw this else statement
        card_suit = Suits.SPADE

    return Card(card_rank, card_suit)
    
def list_to_cardset(input):
    result = set()
    for str in input:
        card = str_to_card(str)
        result.add(card)
    return result



def winning_hand(hand1, hand2, board):
    """Returns the winning hand, given a board. If the hands are equal, 
    it returns False."""
    handrank1, order1 = hand_ranking(hand1, board)
    handrank2, order2 = hand_ranking(hand2, board)

    if handrank1.value > handrank2.value:
        return hand1
    elif handrank1.value < handrank2.value:
        return hand2
    else:
        if len(order1) != len(order2):
            print(order1, order2)
        for i in range(len(order1)):
            if order1[i] > order2[i]:
                return hand1
            elif order1[i] < order2[i]:
                return hand2
            else:
                continue
        return False

def take_from_deck(num_of_cards, deck):
    result = set()
    for i in range(num_of_cards):
        card = random.choice(list(deck))
        deck.remove(card)
        result.add(card)
    return result


def percentage_calc(hand1, hand2, deck):
    """Calculates the percent chance one hand beats another for any given deck."""
    #TODO: should be able to do multiple hands, not just two
    all_combos = list(itertools.combinations(list(deck), 5))
    hand1_wins = 0
    hand2_wins = 0
    ties = 0
    for combo in all_combos:
        board = set(combo)
        winner = winning_hand(hand1, hand2, board)
        if winner == hand1:
            hand1_wins +=1
        elif winner == hand2:
            hand2_wins += 1
        else:
            ties += 1
    tot = hand1_wins+hand2_wins+ties
    print(tot)
    return (hand1_wins/tot, hand2_wins/tot, ties/tot)

hand1 = take_from_deck(2, deck)
hand2 = take_from_deck(2, deck)
 
# print(hand1)
# print(hand2)

# print(percentage_calc(hand1, hand2, deck))
# print()

# board = take_from_deck(5, deck)
# print(board)
# winner = winning_hand(hand1, hand2, board)
# print()

# hand1_hr, hand1_order = hand_ranking(hand1, board)
# print(f"Hand1: {hand1}\n{hand1_hr.name} - {hand1_order}")
# hand2_hr, hand2_order = hand_ranking(hand2, board)
# print(f"Hand2: {hand2}\n{hand2_hr.name} - {hand2_order}")


print(hand1)
print(hand2)
print(percentage_calc(hand1, hand2, deck))

# winner_hr, winner_order = hand_ranking(winner, board)
# print(f"The Winning Hand: {winner}\n{winner_hr.name} - {winner_order}")
# print()

# test_hand1 = list_to_cardset(["5C", "8C"])
# test_hand2 = list_to_cardset(["QH", "5H"])
# test_board = take_from_deck(5, deck-test_hand1-test_hand2)


# new_test_board = list_to_cardset(["6H", "6D", "9D", "7H", "2H"])
# print(new_test_board)
# print(test_hand1)
# print(test_hand2)
# test_hr1, test_order1 = hand_ranking(test_hand1, new_test_board)
# print(f"{test_hr1.name} - {test_order1}")
# test_hr2, test_order2 = hand_ranking(test_hand2, new_test_board)
# print(f"{test_hr2.name} - {test_order2}")


    
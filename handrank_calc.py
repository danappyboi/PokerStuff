import copy
from objs import HandRanks

def is_mult_hand(complete_hand):
    """Returns the rank of high card, pair, two pair, trips, 
    quads and full house as well as the order."""
    count_dict = {}
    fh, fh_high, fh_pair_high = False, -1, -1
    quads, quads_high = False, -1
    trips, trips_high = False, -1
    pair1, pair1_high = False, -1
    pair2, pair2_high = False, -1
    for card in complete_hand:
        if card not in count_dict:
            count_dict[card] = 1
        else:
            count_dict[card] += 1
    
    for rank in count_dict:
        #quad detection
        if count_dict[rank] == 4:
            quads = True
            quads_high = rank
        #full house and trip detection
        if count_dict[rank] == 3:
            one_counter = 0
            #to check for full house, make a new dict without the og trip
            #then figure out how many of the other ranks there are
            count_dict2 = count_dict.copy()
            count_dict2.pop(rank)
            for sub_rank in count_dict2:
                if count_dict2[sub_rank] == 3:
                    fh = True
                    fh_high = max(rank, sub_rank)
                    fh_pair_high = min(rank, sub_rank)
                    break
                elif count_dict2[sub_rank] == 2:
                    fh = True
                    fh_high = rank
                    if fh_pair_high < sub_rank:
                        fh_pair_high = sub_rank
                else:
                    one_counter += 1
                    if one_counter == 3:
                        trips = True
                        trips_high = rank
        #pair and two pair detection
        if count_dict[rank] == 2:
            #if you've already found a pair, check which is bigger
            #and set pair2 to True. Otherwise, just set pair1 to True
            #and set pair1_high accordingly
            if pair1 == True:
                if pair1_high < rank:
                    pair2 = True
                    pair2_high = pair1_high
                    pair1_high = rank
                else:
                    pair2 = True
                    pair2_high = rank
            else:
                pair1 = True
                pair1_high = rank
    
    #finding the order: usually by deleting the high, then 
    #finding the highest left for the full 5 and inserting
    #the high to the front
    ch_copy = copy.deepcopy(complete_hand)
    ch_copy = list(set(ch_copy))
    ch_copy.sort(reverse=True)
    if fh:
        ch_copy = [fh_high, fh_pair_high]
        return (HandRanks.FULL_HOUSE, ch_copy)
    if quads:
        ch_copy.remove(quads_high)
        while len(ch_copy) > 1:
            ch_copy.pop()
        ch_copy.insert(0, quads_high)
        return (HandRanks.QUADS, ch_copy)
    elif trips:
        ch_copy.remove(trips_high)
        while len(ch_copy) > 2:
            ch_copy.pop()
        ch_copy.insert(0, trips_high)
        return (HandRanks.TRIPS, ch_copy)
    elif pair2:
        ch_copy.remove(pair1_high)
        ch_copy.remove(pair2_high)
        while len(ch_copy) > 1:
            ch_copy.pop()
        ch_copy.insert(0, pair2_high)
        ch_copy.insert(0, pair1_high)
        return (HandRanks.TWO_PAIR, ch_copy)
    elif pair1:
        ch_copy.remove(pair1_high)
        while len(ch_copy) > 3:
            ch_copy.pop()
        ch_copy.insert(0, pair1_high)
        return (HandRanks.PAIR, ch_copy)
    else:
        while len(ch_copy) > 5:
            ch_copy.pop()
        return (HandRanks.HIGH_CARD, ch_copy)


def is_straight_func(complete_hand_ranks):
    """Returns whether or not the list of ranks given contains a straight
    and the highest number in the straight if so."""
    ch_list = copy.deepcopy(complete_hand_ranks)
    ch_list.sort(reverse=True)
    high = ch_list[0]
    counter = 0
    for i in range(len(ch_list)-1):
        if ch_list[i] - ch_list[i+1] == 1:
            counter += 1
            if counter == 4:
                return True, [high]
        else:
            counter = 0
            high = ch_list[i]
    return False, [high]

def is_flush_func(ch_ranks_suits):
    """Returns whether or not the list of ranks and suits contains
    a flush and the board following it."""
    count_dict = {}
    flush = False
    flush_suit = 0
    for (rank, suit) in ch_ranks_suits:
        if suit not in count_dict:
            count_dict[suit] = 1
        else: 
            count_dict[suit] += 1
            if count_dict[suit] == 5:
                flush = True
                flush_suit = suit
                break

    if flush:
        result_list = []
        for (rank, suit) in ch_ranks_suits:
            if suit == flush_suit:
                result_list.append(rank)
        result_list.sort(reverse=True)
        while len(result_list) > 5:
            result_list.pop()
        return True, result_list
    return False, [-1]


def hand_ranking(hand : set, board : set):
    """Returns a tuple of (hand rank, order) for any given hand and board."""
    complete_hand = hand | board
    #turn the cards into their respective enum values to be used in functions
    complete_hand_ranks = list(map(lambda card: (card.get_rank()), list(complete_hand)))
    ch_ranks_suits = list(map(lambda card: (card.get_rank(), card.get_suit()), list(complete_hand)))

    #For debugging:
    # print(complete_hand_ranks)
    # print(complete_hand_suits)

    hand_rank, order = is_mult_hand(complete_hand_ranks)
    is_straight, straight_order = is_straight_func(complete_hand_ranks)
    is_flush, flush_order = is_flush_func(ch_ranks_suits)

    if is_flush and is_straight:
        return (HandRanks.STRAIGHT_FLUSH, straight_order)
    elif hand_rank == HandRanks.QUADS:
        return (hand_rank, order)
    elif hand_rank == HandRanks.FULL_HOUSE:
        return (hand_rank, order)
    elif is_flush:
        return (HandRanks.FLUSH, flush_order)
    elif is_straight:
        return (HandRanks.STRAIGHT, straight_order)
    else:
        return (hand_rank, order)
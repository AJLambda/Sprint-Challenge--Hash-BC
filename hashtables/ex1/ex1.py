#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


# finds two items whose sum of weights equals the weight limit `limit`.
# Your function will return an instance of an `Answer` tuple that has the following form:
# (zero, one)
# where each element represents the item weights of the two packages
# If such a pair doesn’t exist for the given inputs, your function should return `None`.
# When calling `hash_table_retrieve` with a key that doesn't exist in the hash table,
# `hash_table_retrieve` will return `None`.


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    dict = {}

    for i in range(length):
        print("item", i)
        print("weights", weights[i])
        print("limit", limit)

        current = weights[i]
        difference = limit - current

        if difference in dict:
            return i, dict[difference]
        else:
            dict[current] = i
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

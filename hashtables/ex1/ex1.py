#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    if length <= 1:
        return None

    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)

    output = []
    for smaller_index, weight in enumerate(weights):
        higher_index = hash_table_retrieve(ht, limit - weight)
        if higher_index:
            output = [higher_index, smaller_index]
            break

    return output


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

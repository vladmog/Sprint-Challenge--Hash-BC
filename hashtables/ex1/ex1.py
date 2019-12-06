#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    print(f"WEIGGHHHTTTS: {weights}")
    print(f"LENGTHHH: {length}")
    print(f"LIMITTTTT: {limit}")

    # Get weights into the hashtable
    for weight in weights:
        ht.hash_table_insert(weight)

    # Check if weight's complement is present in ht
    for weight in weights:
        complement = limit - weight
        search_result = ht.hash_table_retrieve(complement)



    """
    YOUR CODE HERE
    """

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

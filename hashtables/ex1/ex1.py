#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)




    # Get weights into the hashtable
    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)

    # Check if weight's complement is present in ht
    for i, weight in enumerate(weights):

        complement = limit - weight
        search_result = hash_table_retrieve(ht, complement)
        if search_result:

            indexA = i
            indexB = search_result

            if indexA > indexB:
                return (indexA, indexB)
            else:
                return (indexB, indexA)





    """
    YOUR CODE HERE
    """

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

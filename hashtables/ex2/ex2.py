#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Add tickets to hashtable
    for ticket in tickets:
        # print(f"Source: {ticket.source},  Type: {type(ticket.source)}")
        if ticket.source == "NONE":
            ticket.source = None
        hash_table_insert(hashtable, key=ticket.source, value=ticket.destination)
    
    # Sort and record
    first_dest = hash_table_retrieve(hashtable, key=None)
    current = first_dest
    index = 0
    while current:
        route[index] = current
        index += 1
        current = hash_table_retrieve(hashtable, key=current)
    print(route)

    return route

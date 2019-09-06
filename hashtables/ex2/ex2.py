#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for x in range(length):
        hash_table_insert(hashtable, tickets[x].source, tickets[x].destination)

    source = "NONE"
    for y in range(length):
        destination = hash_table_retrieve(hashtable, source)
        route[y] = destination
        source = destination
    return route



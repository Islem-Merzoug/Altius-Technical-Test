from fastapi import FastAPI
from typing import List
import linked_list

app = FastAPI()


def convert_list_into_linked_list(list: List[int]):
    """ used to convert a python list into a linked list """
    ll = linked_list.LinkedList()
    for i in list:
        ll.add(i)
    ll.logout_linked_list()

    return ll


@app.post("/exercice-one/")
def exercice_one(inpt: List[int]):
    """ returns a list in witch we store the comparaisons results """

    # returned_list represents the results of the comparisons
    # if t = 2, first comparaison returns 1 and the second returns 0, than the returned_list = [1,0]
    returned_list = []

    print('all:', inpt)
    # define t from inpt and than delete it
    t = inpt[0]
    del inpt[0]

    for i in range(t):
        # define n from inpt and than delete it
        n = inpt[0]
        del inpt[0]

        #
        list1 = []
        for i in range(n):
            list1.append(inpt[i])

        # delete list1's elements from inpt
        for i in list1:
            del inpt[0]

        # define n from inpt and than delete it
        m = inpt[0]
        del inpt[0]

        list2 = []
        for i in range(m):
            list2.append(inpt[i])

        # delete list2's elements from inpt
        for i in list2:
            del inpt[0]

        llist1 = convert_list_into_linked_list(list1)
        llist2 = convert_list_into_linked_list(list2)

        returned_list.append(llist1.compare_lists(llist2))

    return returned_list


@app.post("/assignement-two/")
def minimum_distances(inpt: List[int]):

    # define a from inpt and than delete it
    a = inpt[0]
    del inpt[0]

    minimum_distance_list = []
    for i in range(a):
        for j in range(a):
            if inpt[i] == inpt[j] and i != j:
                minimum_distance_list.append(abs(i-j))

    if not(minimum_distance_list == []):
        return min(minimum_distance_list)

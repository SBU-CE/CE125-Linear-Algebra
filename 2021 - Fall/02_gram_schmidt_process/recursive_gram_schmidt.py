'''
    Author: Mohammad Mahdi Mazidabadi
'''

import math
import numpy as np


def normalizer(vector):
    # np.linalg.norm(vector) returns length(or norm) of vector
    return vector / np.linalg.norm(vector)


def proj(u, v):
    return (np.dot(u, v) / np.dot(v, v)) * v


# assigning a default value to new_base. new_base = None(something likes null)
def gram_schmidt(old_base: list, new_base=None):
    if new_base is None:
        # if the user does not assign any list to new_base, this code will assign an empty list.
        # this section is used at the beginning of function calling.
        new_base = []

    # this is condition of our recursive function.
    # if there is no item from the old_base, it returns the new_base.
    if not len(old_base):
        # returning the normalized new_base
        return list(map(normalizer, new_base))

        # you can use this return instead.
        # this returns new_base in shape of list.
        # return list(map(lambda item: list(map(lambda x: round(x, 4), normalizer(item).tolist())), new_base))

    # pop(index) --> remove from list and return the object.
    # from the beginning of list, we convert u to v : u in old base, v in new base
    v = old_base.pop(0)

    # converting all items of new_base to proj.
    proj_list = list(map(lambda item: proj(v, item), new_base))

    # subtracting proj_list items of from v
    for i in proj_list:
        v = np.subtract(v, i)

    # v is ready :)
    new_base.append(v)

    return gram_schmidt(old_base, new_base)


# example
base = [np.array([1, 1, 1]), np.array([1, 2, 2]), np.array([1, 1, 0])]
print(*gram_schmidt(base), sep='\n')

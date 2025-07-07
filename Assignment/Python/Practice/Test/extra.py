
from collections.abc import Iterable

l1 = [[2, 7, 9, 0], 1, [2, 3, 4], 5, 6, [
    7, 88, 9], 0, 33, 44, 55, [66, 777, 88]]
l2 = [1, 5, 8, 6, 3, 2, 5, (7, 88, 9)]
l3 = [2, 3, [1, 9, 0], 9, {6, 7, 4}, 4, 1, 8]

l4 = l1+l2+l3

l5 = [x
      for item in l4
      for x in (item if isinstance(item, (list, set, tuple)) else [item])]

# yaha pr item means:  for x in true: [2, 7, 9, 0] aka item, and then false: [1] aka [item]

print(l5)


l6 = [ele for li in l4 for ele in (li if isinstance(li, Iterable) else [li])]

print(l6)


l7 = [4, 5, 6, 58, 8, 5, 11, 5, 58, 6, 2, 1, 4]
l8 = ['f', 'g', 't', 'v', 'b', 'e', 'd', 'x', 'h']

d1 = {l7[i]: l8[i] for i in range(len(l7) if (len(l7) < len(l8)) else len(l8))}
print(d1)

d2 = {x: ord(x) for x in l8}
print(d2)


l9 = [4, 5, [6, 58, 8], 5, 11, 5, [58, 6, 2, 7], 1, 4]

l10 = [x
       for item in l9
       for x in (item if isinstance(item, list) else [item])]

print(l10)


def flatten(lst):
    return [x for sublist in lst for x in (flatten(sublist) if isinstance(sublist, list) else [sublist])]


l11 = [4, 5, [6, 58, 8], 5, 11, 5, [58, [6, 2], 7], 1, 4]
l12 = flatten(l11)

print(l12)


# Dynamic Approach
l1 = [[2, 7, 9, 0], 1, [2, 3, 4], 5, 6, [
    7, [2, 3, [6, 7, 8, 0], 7, 8, 7], 88, 9], 0, 33, 44, 55, [66, 777, [6, 0], 88]]
l2 = [1, 5, 8, 6, 3, 2, 5, (7, 88, 9)]
l3 = [2, 3, [1, 9, 0], 9, {6, 7, 4}, 4, 1, 8]

# Helper function to recursively flatten


def flatten(item):
    if isinstance(item, (list, tuple, set)):
        # Recursively flatten
        return [subitem for sublist in item for subitem in flatten(sublist)]
    return [item]  # Base case for non-iterable elements


# Merge and flatten using the helper function
merged_flat_list = [
    item
    for sublist in (l1 + l2 + l3)  # Merge the lists
    for item in flatten(sublist)  # Flatten the sublist
]

print(merged_flat_list)


l1 = [[2, 7, 9, 0], 1, [2, 3, 4], 5, 6, [4, [2, 3, [6, 7, 8, 0], 7, 8, 7], 88, 9], 0, 33, 2, 1, 0, 44, 1, 55, [66, 777, [6, 0], 88]]
l2 = [1, 5, 8, 6, 3, 2, 5, (7, 88, 9)]
l3 = [2, 3, [1, 9, 0], 9, {6, 7, 4}, 4, 1, 8]

l4 = l1+l2+l3

print(l1.count(1))


def flat_list(lst):
    result = []
    for ele in lst:
        if isinstance(ele, Iterable):
            result.extend(flat_list(ele))
        else:
            result.append(ele)
    return result 

flat_li = flat_list(l4)  

print("Flatten Result: ", flat_li)





car = {
  "brand": "Ford",
  "year": 1964,
  "model": "Mustang",
  "active": True
}

sortedcar = sorted(car.items(), key=(lambda x: str(x[1])))

print(car)
print()

print(sortedcar)
print()

print(dict(sortedcar))
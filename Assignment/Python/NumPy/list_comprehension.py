l1 = [ 1, [2, 5], [6, 7, 71, 22], 8, 9, [2, 3], 5, [6], [3, 56], 90]

l2 = [x 
      for sublist in l1
      for x in (sublist if isinstance(sublist, list) else [sublist])]

print(l2)



def flatten_list(lst):
    return [item 
            for element in lst
            for item in (flatten_list(element) if isinstance(element, list) else [element])]


l1 = [ 1, [2, [3, 4], 5], [6, 7,[78, 89, [45, 65, [7, 3], 23], 71, 22], 8], 9, [2, 3], 5, [6], [3, 56], 90]
print(flatten_list(l1))

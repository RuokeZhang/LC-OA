'''
https://www.fastprep.io/problems/amazon-get-final-locations
'''
locations = [1, 7, 6]
movedFrom = [1, 7, 2]
movedTo = [2, 9, 5,3]

locs = set(locations)
print(list(zip(movedFrom, movedTo)))
for a, b in zip(movedFrom, movedTo):
    locs.remove(a)
    locs.add(b)

print(list(locs))
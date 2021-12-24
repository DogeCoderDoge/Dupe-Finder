from collections import defaultdict

numbers = [7, 1, 5, 3, 9, 0, 2, 4, 6, 8, 9]
duplicates = defaultdict(list)

def findDupes():
    
    for i, pos in enumerate(numbers):
        duplicates[pos].append(i)

    result = {k:v for k,v in duplicates.items() if len(v) > 1}

    dupe = result.keys()
    position = result.values()

    print(*dupe, "is present at the following positions:", *position)

findDupes()

# Originally From:  https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBinarySearch.html

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

# badlist = [17, 13, 19, 8, 2, 1, 19, 32, 42,]
# print(binarySearch(badlist, 42))
# print(binarySearch(badlist, 13))

badlist = [ 42, 13, 17, 19, 1, 2, 8, 13, 32, ]
print(binarySearch(badlist, 42))
print(binarySearch(badlist, 13))

WIDTH = 2
def removeDuplicates(self, arr):
    i = 0
    for n in arr:
        if i < WIDTH or n > arr[i - WIDTH]:
            arr[i] = n
            i += 1
    return i

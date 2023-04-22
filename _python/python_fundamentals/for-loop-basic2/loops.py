# 1-Biggie-Size
def biggie_size(bigger):
    array = []
    for x in bigger:
        if x > 0:
            array.append("big")
        else:
            array.append(x)
    return array


print(biggie_size([-1, 3, 5, -5]))


# 1-Biggie-Size
def biggie_size(bigger):
    for x in range(0, len(bigger), 1):
        if bigger[x] > 0:
            bigger[x] = "big"
    return bigger


print(biggie_size([-1, 3, 5, -5]))


# 2-Count-Positives
def count_positives(box):
    count = 0
    for x in range(0, len(box), 1):
        if box[x] > 0:
            count += 1
    box[len(box)-1] = count
    return box


print(count_positives([1, 6, -4, -2, -7, -2]))
print(count_positives([-1, 1, 1, 1]))


# 3-Sum-Total
def sum_total(container):
    sum = 0
    for i in range(0, len(container), 1):
        sum += container[i]
    return sum


print(sum_total([1, 2, 3, 4]))


# 4-Average
def average(box):
    avg = 0
    sum = 0
    for i in range(0, len(box), 1):
        sum += box[i]
        avg = sum/len(box)
    return avg


print(average([1, 2, 3, 4]))


# 5-Length
def length(lst):
    return len(lst)


print(length([37, 2, 1, -9]))


# 6-Minimum
def minimum(lst):
    if not lst:
        return False
    mini = lst[0]
    for i in range(0, len(lst), 1):
        if lst[i] < mini:
            mini = lst[i]
    return mini


print(minimum([37, 2, 1, -9]))
print(minimum([]))


# 7-Maximum
def maximum(lst):
    if not lst:
        return False
    maxi = lst[0]
    for i in range(0, len(lst), 1):
        if lst[i] > maxi:
            maxi = lst[i]
    return maxi


print(maximum([37, 2, 1, -9]))


# 8-Ultimate-Analysis
def ultimate_analysis(lst):
    sum = 0
    avg = 0
    mini = 0
    maxi = 0
    length = 0
    for i in range(0, len(lst), 1):
        sum += lst[i]
        if lst[i] < mini:
            mini = lst[i]
        if lst[i] > maxi:
            maxi = lst[i]
    length = len(lst)
    avg = sum/length
    my_dict = {'sumTotal': sum, 'average': avg,
               'minimum': mini, 'maximum': maxi, 'length': length}
    return my_dict


print(ultimate_analysis([37, 2, 1, -9]))


# 9-Reverse-List
def reverse_list(lst):
    lst = lst[::-1]
    return lst


print(reverse_list([37, 2, 1, -9]))

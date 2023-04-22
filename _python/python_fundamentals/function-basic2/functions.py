#Countdown
def countdown(x):
    array= []
    for n in range (x, -1, -1):
        array.append(n)
    return array
array = countdown(10)
print(array)


#Print and Return
def print_and_return(x):
    print(x[0])
    return x[1]
print_and_return = [5,6]
print_and_return = [2,10]
print(print_and_return)


#First Plus Length
def sum(x=[]):
    return (len(x)+ x[0])
print(sum([1,2,3,4,5]))


#Values Greater than Second
def values_greater_than_second(x):
    newarray = []
    maximum= x[1]
    for i in range(0, len(x), 1):
        if x[i] > maximum:
            newarray.append(x[i])
    return newarray
print(values_greater_than_second([5,2,3,2,1,4]))


#This Length, That Value
def length_and_value(x,y):
    array=[]
    for x in range(0, x, 1):
        array.append(y)
    return array
print(length_and_value(3,7))

for x in range(151):
    print(x)


for x in range(0, 1001, 1):
    if (x%5 == 0):
        print(x)


for x in range (1, 101, 1):
    if ( x % 5 == 0):
        print('Coding')
    if ( x % 10 == 0):
        print('Coding Dojo')


sum=0
for x in range (0, 500001, 1):
    if (x % 2 == 1):
        sum += x
print(sum)


for x in range (2018, 0, -4):
    print(x)


lowNum=2
highNum=9
mult=3
for x in range (lowNum, highNum +1, 1):
    if(x % mult == 0):
        print(x)

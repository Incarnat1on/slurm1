value = int (input())
count = int (input())
i = 0
j = 0
for i in range(value):
    for j in range (i):
        print (count, end=" ")
        count-=1
    print()
# Problem 1
print("Problem 1 solution :")
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]

for i in list:
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in i:
        count[j] = count[j] + 1

    k = 0
    while(k < len(count)):
        if(count[k] > 1):
            print(f"{k} ' -> ' {count[k]}")
        k=k+1
print()
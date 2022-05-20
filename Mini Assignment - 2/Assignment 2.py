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

# Problem 2

print("Problem 2 solution : ")
list1 = ["hello", "take"]
list2 = ["Dear", "sir"]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i+j)

print(list3)
print()

# Problem 3
print("Problem 3 solution")

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)
print()

# Problem 4
print("Problem 4 Solution")

keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
dict = {}

for i in range(len(keys)):
    dict[keys[i]] = values[i]

print(dict)
print()
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

# Problem 5
print("Problem 5 Solution")

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)
print()

# Problem 6
print("Problem 6 solution")
sampleDict = {
 "name": "Kelly",
 "age":25,
 "salary": 8000,
 "city": "New york"
}

sampleDict["location"] = sampleDict["city"]
del sampleDict["city"]
print(sampleDict)
print()

# Problem 7
print("Problem 7 solution")

originalDict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print("The original dictionary is : " + str(originalDict))
res = []
for key, val in originalDict.items():
    res.append([key] + val)
print("The converted list is : " + str(res))
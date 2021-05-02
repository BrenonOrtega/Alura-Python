





""" def stockPairs(stocksProfit, target):
    # Write your code here
    distinct = list(set(stocksProfit))
    print(distinct)
    sum_list = [set(item,  item2)  for item in distinct if len(distinct) >2 for item2 in distinct if target == item+item2 ]
    print(sum_list)


    return target / ( len(sum_list) -1 )


a = [5,7,9,13,11,6,6,3,3]
b = 12

print(stockPairs(a, b)) """


""" 
a = [[5],[5],[1, 1, 1, 1, 1,], [2, 2, 2, 2, 2, ],[3, 3, 3, 3, 3], [4, 4, 4, 4, 4,],[5, 5, 5, 5, 5]]

print (len(a[0]))

for i in range(0, len(a)):
    for j in range (0, len(a[i])):
        print(i, j)
        p1 = []
        if (a[len(a[i])][len(a[j]) < a[range(a[i])][range(a[j])]]) :
            p1.append(j[i])
            print(j)
 """

def reverseArray(arr):
    # Write your code here
    new_list = []
    for i in range(0, len(a)):
        new_list.append(arr.pop(-1))
        print(new_list)
    return new_list

a = [1,2,3,4,5,6,7]
print(reverseArray(a))
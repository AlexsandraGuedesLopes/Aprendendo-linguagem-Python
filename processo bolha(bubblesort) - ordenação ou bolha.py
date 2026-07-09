num = [5,2,4,1,3]
for i in range(len(num)):
    for j in range(len(num)-1): 
        if num[j] > num[j+1]:
            num [j], num[j+1] = num[j+1], num[j]
    print(num)
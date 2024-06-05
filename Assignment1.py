### Q.1 Solution###
l1 = [1,-2,3,0,-4,5, 0]
d1 = {'a': 100, 'b': 200, 'c': 500, 'd':400}

# i. Inserting elements at the end of list
l1.append(6)

# ii. Sorting 
def sortingf(in_list):
    posil = []
    negil = []
    zerol = []
    for i in in_list:
        if i > 0:
            posil.append(i)
        elif i< 0:
            negil.append(i)
        else:
            zerol.append(i)
            
    print(f"Positive list: {posil}\nNegitive list: {negil}\nZeros list:{zerol}")
    
sortingf(l1)

# iii. Maximum
def maxf(in_dict):
    max_res = 0
    for key, value in in_dict.items():
        if value > max_res:
            max_res = value
            
    print(f"The max number is {max_res}\n")

maxf(d1)


###Q.2 Solution###

l2 = [100,200,400,500]
digi = []
for k in l2:
    count = 0
    m=k
    while m!=0:
        count+=1
        m =round(m/10)
    digi.append(count)
print(f"Number of digits in the number are: {digi}")

l2.insert(-1, -5)
print("Inserting at second last position:",l2)
sum1 = 0
for j in l2:
    sum1 += j
print(f"Sum: {sum1}")
def max_min_avg_mid(lis):
    max = 0
    min = 0 
    avg = 0
    for item in lis:
        avg += item
        if item>max:
            max = item
        if item < min:
            min = item
    avg /= len(lis)
    print(f"Max: {max}, Min: {min}, Avg: {avg}, Mid: {lis[round(len(lis)/2)]}")
max_min_avg_mid(l2)
l2.insert(2, 250)
print("Inserting at third position:", l2, end="\n\n")


###Q.3 Pattern printing###
def pattern():
    for i in range(5):
        for j in range(5-i):
            print(j+1, end="")
        print()
    print()
pattern()

###Q.4 Prime###
def prime(start,end):
    is_prime = True
    print("The Prime numbers are:", end=" ")
    for i in range(start, end + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")
                    
prime(5,19)

###Q.5 Neon Numbers###
def neon(end):
    print("The Neon Numbers are:",end=" ")
    for i in range(1, end+1):
        sum_list = []
        temp = i**2
        while temp != 0:
            last_digi = temp%10
            sum_list.append(last_digi)
            temp = int(temp/10)
        if sum(sum_list) == i:
            print(i, end=" ")
    print()
neon(50)


###Q.6 Frequency###
def frequency(st):
    freq_dic = dict()
    max = 0
    max_key = str()
    
    for i in range(len(st)):
        if st[i] in freq_dic:
            freq_dic[st[i]] += 1
        else:
            freq_dic[st[i]] = 1
            
    for key, value in freq_dic.items():
        if value > max:
            max_key = key
            max = value
    
    print("The most frequent character in the string is:", max_key)
frequency("Abhijeet Sapar")


###Q.7 Merge Dictornary###
d2 = {1: 'One', 2: 'Two', 3: 'Three'}
d3 = {'a': 100, 'b': 200, 'c': 500, 'd':400}

def merge_dict(d1,d2):
    for key, value in d2.items():
        d1[key] = value
    print(d1)
    
merge_dict(d2,d3)


###Q.8 Min number using lamda###
l3 = [4,7,3,4,5,6,6]
def min_lambda():
    return lambda x: min(x)

ans = min_lambda()
print("Minimum number is:",int(ans(l3)))
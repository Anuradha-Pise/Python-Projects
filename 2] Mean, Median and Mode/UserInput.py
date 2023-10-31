list1 = []
# Taking elements as input from user
number = int(input('Enter the number of elements :'))
for num in range(number):
    element = float(input(f'Enter the {num+1} element :'))
    list1.append(element)

# Mean
mean = sum(list1)/len(list1)
print(f'The mean is {mean}')

# Median
list1.sort()
if len(list1)%2 == 0:  # For even number
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1+m2)/2
else:   # For odd number
    median = list1[len(list1)//2]
print(f'The median is {median}')

# Mode
frequency = {}
for i in list1:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

max_freq = 0
mode = None

# Finding mode by iterating through the dictionary
for k,v in frequency.items():
    if v > max_freq:
        max_freq = v
        mode = k

print(f'The mode is {mode}')

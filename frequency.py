#Initiliaise dictionary
test_dict={'Codingal': 2, 'is' : 5, 'best': 0, 'for': 2, 'Coding': 1}

print("The original dictionary: " + str(test_dict))

#Initialise value
K=2

res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1

#printing result
print("Frequency of K is : " + str(res))
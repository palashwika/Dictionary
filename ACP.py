td={'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

freq=int(input("Enter the value to check frequency in " )) #convert to int since key values are integers

ctr=0
for i in td:
    if td[i]==freq: #compares the values in dictionary
        ctr=ctr+1

print("The frequency for", freq, "is", ctr) 
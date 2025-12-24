dic={'AP. Chem':3, 'AP CALC':2, 'AP LANG': 1}

print(dic.values()) #returns 3,2,1
print(dic.copy())


for i in dic:
    print(dic[i]) #only prints key values

#dict[key] = strict lookup (crashes if missing)
#dict.get(key) = safe lookup (returns None or default)
#dict.get(key[, d])  # invalid Python
#print(dic.get[3])


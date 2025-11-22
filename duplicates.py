student_date= {'idl':{'name':['Sara'], 'class': ['V'], 'subject_integration':['english, math, science']},
'id2': {'name': ['Damon'], 'class': ['V'], 'subject_integration': ['english, math, science']},
'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']},
}

result={}
for key, value in student_date.items():
    if value not in result.values():
        result[key]=value

print(result)
    





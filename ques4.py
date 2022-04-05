keys=['ten','twenty']
values=[10,20]

res={}
for key in keys:
    for value in values:
        res[key]= value
        values.remove(value)
        break
print("resultant dictionary is: "+str(res))
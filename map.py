lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
lst2 = list(map(lambda x: x.lower().count("a"), lst1))
print(lst2)
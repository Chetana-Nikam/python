# Dictionary - it doesnt allow duplicate values - denoted in {} - we can chamge and add, remove data
d={
    # key:value
    "name":"chetana",
    "age":21,
    "surname":"nikam",
    "name":"Manisha"
}
print(d)
print(len(d))
print(type(d))
print(d["name"])
print(d["age"])
print(d.get("age"))
print(d.keys())   #it will rpint all keys of dictionary
print(d.values()) #it will print all the values of dictionary 
print(d.items())  #it will print all keys and values
d["age"]=22       #  change the value of key
print(d)
d.update({"age":30})
print(d)
d["fathername"]="prakash"
print(d)
del d["name"]
print(d)
d.pop("age")
print(d)
d.popitem()       # it will delete last key
print(d)


# nested dictionary - means dictionary inside dictionary

a1={
    "n1":"Chetana",
    "s1":21
}
a2={
    "n2":"siddhesh",
    "s2":"18"
    
}
a3={
    "n3":"manisha",
    "s3":"46"
}
finaldict={
    "dict1":a1,
    "dict2":a2,
    "dict3":a3
}
print(finaldict)






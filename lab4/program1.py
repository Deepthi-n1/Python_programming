BCA={"1":"Ram",
     "2":"Ravi",
     "3":"Poorvi"}

#calling key values
print("here are the keys" )
for key in BCA:
    print(key)

print("Here are  the values")
for key in BCA:
    print(BCA[key])
    
#addind new element 
BCA["4"]="RVU"

print("updated dict")
print(BCA)    

for values in BCA.values():
    print(BCA[key])
    print(values)
    
print(BCA.values())    
print(BCA.keys())
print(BCA.items())

if "4" in BCA:
    print("I am here")
else:
    print("no")

        
    

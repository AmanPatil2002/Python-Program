
# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")                             # To add
#utensils.remove("fork")                            # To remove
#utensils.clear()                                   # To clear
#dishes.update(utensils)                            # To update
#dinner_table = utensils.union(dishes)              # To unite(union)

#print(utensils.difference(dishes))                 # To differenciate
print(utensils.intersection(dishes))               # To intersect

#for x in dinner_table:
    #print(x)
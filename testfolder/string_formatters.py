string1 = "Emeka has {} more oranges {} {}"
print(string1.format("32","than","apples"))


"""{0:.2f} are used to convert to float and decide on decimal place. they can be converted to d(decimal), s(string)"""
"""{0:44} numbers can be used for padding. adding either <^> will indicate left right or center padding. * when used will replace white space"""

print("emeka has {0:.2f} more oranges {1} {2:>44}".format(33, "than", "apples")) 

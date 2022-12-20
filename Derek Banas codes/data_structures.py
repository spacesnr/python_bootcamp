
#Lessions on data structures (lists, tuples, sets and dictionaries)
###LISTS

a_list = [1,2,3,4,5,6]
b_list =[2,30,11,66,0,6,8,10]
c_list = [0,2,4,5,8]

a_list.append(7) #this adds 7 to the end of the list 
a_list[len(a_list):] = [7] #produces same result as a_list.append(7)
print(a_list)

a_list.extend("45") #Used with quotes, this can add multiple numbers unlike append() 
print(a_list)

a_list.insert(1,2.0)
print(a_list) #inserts a number(2.0) at an index(1)

a_list.remove(4) #removes the first instance of the number 4
print(a_list)

a_list.pop(6) #removes the number at index 6. when used without an argument, it removes the last character on the list
print(a_list)

b_list.clear() #removes all items in the list

a_list.index(1) #returns the index of 1

a_list.count(4) #returns the number of times 4 appears

c_list.sort() #sorts the list in the right order

a_list.reverse() #displays in reverse of original order

a_list.copy() #returns a shallow copy of the list. Equivalent to a_list[:]


#list comprehension
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

#to this
a_squares = [(x**2) for x in range(10)]
print(a_squares)


###TUPLES: makes use of () and are immutable.



###SETS: are unordered collection with no duplicate elements. basic uses are membership testing and eliminating duplicates.
#sets cannot be indexed or sliced because its unordered

a_set ={"apples", "oranges", "banana", "apples", "pear", "banana"}
print(a_set) #the result here will show you that duplicates were eliminated

"apples" in a_set #fast membership testing. This returns true in interactive python

#SETS can also be written with the set() function. set() is used also to create empty sets. Using just {} doesnt create an empty set but creates an empty dictionary

a = set("abracadara")
b = set("alacazam")

print(a) #prints individual characters as unique
print(b) #prints individual characters as unique

a-b #letters in a but not in b
a|b #letters in a or b or both
a&b #letters in a and b
a^b #letters in a or b but not in both

#set comprehension
c = {x for x in "abracadabra" if x not in "abc"}
print(c)


###DICTIONARIES: Known as “associative memories” or “associative arrays” on other languages. They are indexed by a key which is imutable
tel = {"jack":102, "max":450, "jane":303, "bond":155}
tel["ada"]=419 #this adds ada to the dictionary
print(tel)

tel["max"] #works in interactive python to index tel using "max" as key
del tel["bond"] #deletes bond from the dictionary
print(tel)

list(tel) #works in interactive python, used to list the keys in tel dict.
sorted(tel) #works in interactine python, used to sort and display the keys accordingly

"max" in tel #works in interactive python, used to know if max is a key in tel
"ada" not in tel #works in interactive python, used to know if ada is not a key in tel

#dict() constructor builds dictionaries directly from sequences of key-value pairs:
n = dict([("jack",102),("max",450),("jane",303), ("bond",155)])
print(n)

m = dict(jack=102, max=450, jane=303, bond=155) #works same as the previous
print(m)

#dict comprehension
w = {x:x**2 for x in (2,3,4)}
print(w)

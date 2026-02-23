from tupple import lunch_menu

sample_tupple = ("a", "b", "c")
sample_tupple1= ("d")
print(sample_tupple1)
#length of tupple
print("the length of tupple : " , len(sample_tupple))

print("the index of number in tupple :" , sample_tupple[2])

print("Concatenating tuples:")
#Concatenating two tuples
sample_tupple = sample_tupple + tuple(sample_tupple1)
print(sample_tupple)

#adding elements
sample_tupple = sample_tupple + tuple("e")
print(sample_tupple)
#multiple elemenets
sample_tupple = sample_tupple +("E","F")
print(sample_tupple)
#iterating tuple using range function
lunch_menu = ("rice","dal" ,"vegetable" ,"curry" ,"dairy")
for index in range(0,len(lunch_menu)):
    print(lunch_menu[index])

#using in keyword
print("using in keyword")
for foodType in lunch_menu:
    print(foodType)
#searching element in tupple
for desert in lunch_menu:
    if desert == "sweet":
        print("desert is yes")
        break
    else:
       print("desert is not present")
       break



#slicing in tuple
print(lunch_menu[1:3])
print(lunch_menu[-5:2])


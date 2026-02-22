squares = [1,34,56,20,2,4]
print(squares)

#length
print(len(squares))

#store all pasengers ticket num
ticket_no_1 = 78808
ticket_no_2 = 26302
ticket_no_n = 48310
ticket_no = [78808 , 26306, 48310]
print(ticket_no)
sample_list = []
sample_list1 = ["mark", 9 , "jhon" , "max" , 10]
sample_list2 = ["ram" , "sham" , "govind"]
sample_list = []*6
print(sample_list)
print(len(sample_list))
#read about element
print(sample_list1[1])
#write about
sample_list2[2] ="pravati"
print(sample_list2)
#adding another element
sample_list2.append("furry")
print(sample_list2)

list_of_airlines=["AI","EM","BA"]

print("Iterating the list using range()")
for index in range(0,len(list_of_airlines)):
    print(list_of_airlines[index])



print("Iterating the list using keyword in")
for airline in list_of_airlines:
    print(airline)

list_of_airlines=["AI","EM","BA"]
airline = "AI"
if airline in list_of_airlines:
    print("airline found in the list")
else:
    print("not in the list")

#Note: Here "airline" is just another user defined variable. It is not a keyword.
sublist = sample_list1[1:4]
print(sublist)
print(sample_list1[1:])
print(sample_list1[:2])
num_list=[10,20,30,40,50]
num_list.append("arko")
print(num_list)
res = num_list.index("arko")
print(res)
num_list.insert(6,"pravati")
print(num_list)
num_list.pop()
print(num_list)

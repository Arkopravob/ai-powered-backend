
def get_count(num_list):
    count=0
    index=0
    while index<len(num_list)-1:
        if num_list[index]==num_list[index+1]:
            count+=1
        index+=1

    # Write your logic here using for loop
    # for i in range(len(num_list)-1):
    #     if num_list[i] == num_list[i+1]:
    #         count=count+1

    return count
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
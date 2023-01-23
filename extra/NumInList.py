

num_input = int(input("Enter a number: "))
in_list = False
true_num = 0
list1 = [2, 5, 7, 19, 20, 54, 12, 11, 23, 40]

for nums in list1: 
    if num_input == nums:
        in_list = True
        true_num = nums
    else : 
        in_list = False
    print(in_list, nums)

print("The number", true_num, "is in the list")
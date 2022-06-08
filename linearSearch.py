# Linear Search Implementation
def linearSearch(nums, query):
    for i in range(len(nums)):
        if( query == nums[i]):
            return i
    return -1

# numbers_string is taking input the whole line and making a list
# from it whose elements are string 
numbers_string = input("Enter Numbers : \n").split(' ')


#taking every string in the above list and making them integer and
#storing them in a new list called nums
nums =[]
for x in numbers_string :
    nums.append(int(x))

# what to search for write in q
q = int(input("what to search\n"))


result = linearSearch(nums, q)
print(f"{q} is at {result}th index")
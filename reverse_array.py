##### Interview Question #1 #####

# The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well - so no additional memory can be used!

# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]


# Non algorithm solution
# print(nums[::-1]) 

# Algorithm Solution
def reverse(nums):

    # index pointing to the first item
    start_index = 0
    # index pointing to the last item
    end_index = len(nums)-1

    while end_index > start_index:
        # keep swaping the items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        # increment start_index by 1
        start_index += start_index
        # decrease end_index by 1
        end_index -= end_index

if __name__ == '__main__':
    n = [1,2,3,4,5,6,7,8,9,10]
    if len(n)-1 % 2 == 1:
        reverse(n)
        print(n)
    else:
        print(n[::-1])
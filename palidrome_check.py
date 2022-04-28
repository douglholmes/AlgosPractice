# Interview Question #2

# "A palindrome is a string that reads the same forward and backward"

# For example: radar or madam

# Our task is to design an optimal algorithm for checking whether a given string is palindrome or not! 


def palindromCheck(str):
    # convert to lowercase
    str = str.lower()
    # splice string to check if it is the same
    if str == str[::-1]:
        print('This is a palindrome!')
    else:
        print('This is not a palindrome.')


if __name__ == '__main__':
    
    # test cases 
    palindrome = 'Racecar'
    palindromCheck(palindrome)
    palindrome_2 = 'miami'
    palindromCheck(palindrome_2)


# OR #

def is_palindrome(str):
    """
    This to check if a give string is palindrome or not.
    :param str:
    :return:
    """
    start_index = 0
    end_index = len(str) - 1
    while start_index < end_index:
        if str[start_index] == str[end_index]:
            start_index += 1
            end_index -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    string_input = "TaCoCaT"
    if is_palindrome(string_input):
        print("String entered is palindrome")
    else:
        print("The String is not palindrome")
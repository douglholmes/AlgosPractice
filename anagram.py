# Interview Question #4

# Construct an algorithm to check whether two words (or phrases) are anagrams or not!

# "An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once"

# For example: restful and fluster

def isAnagram(str1, str2):
    # if length is not the same, they are not anagrams
    if len(str1) != len(str2):
        return False
    
    #sort letters of string then compare the letters with the same indexes
    str1 = sorted(str1)
    str2 = sorted(str2)

    print(str1)
    print(str2)
    # check letter with the same indexes

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    
    return True

if __name__ == '__main__':
    s1 = 'fluster'
    s2 = 'comma'

    print(isAnagram(s1,s2))
    
    
    
    
    
    

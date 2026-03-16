# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Prime Number)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices checking divisibility carefully using loops and conditionals.

# U -- Understand
# 1. Should 1 be considered a prime number? (No, because prime numbers must be greater than 1.)
# 2. Should the function return True/False instead of printing? (Yes, it should return a boolean.)

# P -- Plan
# I will check if n is less than or equal to 1 first.
# Then I will test divisors from 2 up to n - 1 using a while loop.
# If any divisor divides n evenly, return False.
# If none divide evenly, return True.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Pseudocode
# - if n <= 1, return False
# - set divisor = 2
# - while divisor < n:
# -     if n % divisor == 0:
# -         return False
# -     increase divisor by 1
# - return True

# I -- Implement
def is_prime(n):
    if n <= 1:
        return False

    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Two-Pointer Reverse List)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it introduces the two-pointer technique for modifying a list in-place.

# U -- Understand
# 1. Should the list be changed directly instead of creating a new list? (Yes.)
# 2. Can I use slicing like lst[::-1]? (No, the problem says not to use slicing.)

# P -- Plan
# I will use one pointer at the start and one at the end.
# While the pointers have not crossed, I will swap the values and move inward.
# Then I will return the same list.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Pseudocode
# - set left = 0
# - set right = len(lst) - 1
# - while left < right:
# -     swap lst[left] and lst[right]
# -     move left rightward
# -     move right leftward
# - return lst

# I -- Implement
def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Evaluating Solutions)
# Time Limit: 8 minutes
# Problem Importance:
# This problem matters because it helps compare solutions by both speed and memory usage.

# U -- Understand
# 1. Do I need to compare both time complexity and space complexity? (Yes.)
# 2. Does the slicing solution create extra memory? (Yes, because it makes a reversed copy.)

# P -- Plan
# I will store the complexity comparison in a dictionary so the answer is still valid Python code.
# The two-pointer solution and the slicing solution both visit the list, but the slicing solution uses extra space.
# Time Complexity: O(1) for reporting the final comparison values
# Space Complexity: O(1) for reporting the final comparison values

# Pseudocode
# - create a dictionary with the complexity of the two-pointer solution
# - create a dictionary with the complexity of the slicing solution
# - record which is better for time
# - record which is better for space
# - return the dictionary

# I -- Implement
def evaluate_reverse_list_solutions():
    return {
        "two_pointer_time": "O(n)",
        "two_pointer_space": "O(1)",
        "slicing_time": "O(n)",
        "slicing_space": "O(n)",
        "better_time_complexity": "They have the same time complexity: O(n).",
        "better_space_complexity": "The two-pointer solution has better space complexity: O(1)."
    }


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Move Even Integers)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices grouping values based on a condition.

# U -- Understand
# 1. Do the even and odd numbers need to stay in their original order? (No, any valid order is allowed.)
# 2. Should the function return a list with evens first and odds after? (Yes.)

# P -- Plan
# I will loop through the list and separate numbers into evens and odds.
# Then I will return evens + odds.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Pseudocode
# - create empty evens list
# - create empty odds list
# - for each number in nums:
# -     if number is even, add to evens
# -     else, add to odds
# - return evens + odds

# I -- Implement
def sort_array_by_parity(nums):
    evens = []
    odds = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    return evens + odds


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Palindrome)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices using a helper check and searching through a list.

# U -- Understand
# 1. Should I return the first palindrome only? (Yes.)
# 2. What should I return if none of the strings are palindromes? (Return an empty string.)

# P -- Plan
# I will write a helper function that checks whether a word is a palindrome.
# Then I will loop through the list and return the first word that is palindromic.
# Time Complexity: O(n * m), where n is number of words and m is average word length
# Space Complexity: O(1)

# Pseudocode
# - make helper function to check palindrome
# - for each word in words:
# -     if word is palindrome:
# -         return word
# - return ""

# I -- Implement
def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Remove Duplicates with O(1))
# Time Limit: 12 minutes
# Problem Importance:
# This problem matters because it teaches in-place list updates using a read and write pointer.

# U -- Understand
# 1. Is the list already sorted? (Yes.)
# 2. Should I modify the same list instead of making a new one? (Yes.)

# P -- Plan
# I will use one pointer to track where the next unique number should go.
# I will scan the list, and whenever I find a new value, I will place it at the write position.
# After that, I will remove the extra duplicate tail from the same list.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Pseudocode
# - if nums is empty, return 0
# - set write = 1
# - for read from 1 to end of list:
# -     if nums[read] is different from nums[read - 1]:
# -         place nums[read] at nums[write]
# -         increase write
# - delete everything from index write to end
# - return write

# I -- Implement
def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    del nums[write:]
    return write


# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Perfect Number)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it builds number reasoning skills with divisors and accumulation.

# U -- Understand
# 1. Do I sum only proper divisors and not the number itself? (Yes.)
# 2. Is 1 a perfect number? (No.)

# P -- Plan
# I will loop from 1 up to n - 1 and add every divisor that divides n evenly.
# At the end, I will compare the sum to n.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Pseudocode
# - if n <= 1, return False
# - set divisor_sum = 0
# - set divisor = 1
# - while divisor < n:
# -     if n % divisor == 0:
# -         add divisor to divisor_sum
# -     increase divisor
# - return whether divisor_sum equals n

# I -- Implement
def is_perfect_number(n):
    if n <= 1:
        return False

    divisor_sum = 0
    divisor = 1

    while divisor < n:
        if n % divisor == 0:
            divisor_sum += divisor
        divisor += 1

    return divisor_sum == n


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (2-Pointer Palindrome)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices comparing characters from both ends efficiently.

# U -- Understand
# 1. Can I assume the string only has lowercase letters? (Yes.)
# 2. Should I return True/False and not print? (Yes.)

# P -- Plan
# I will use a left pointer and a right pointer.
# If characters do not match, return False right away.
# If all matching pairs are equal, return True.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Pseudocode
# - set left = 0
# - set right = len(s) - 1
# - while left < right:
# -     if s[left] != s[right]:
# -         return False
# -     move left forward
# -     move right backward
# - return True

# I -- Implement
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Evaluate Palindrome)
# Time Limit: 8 minutes
# Problem Importance:
# This problem matters because it shows how two correct solutions can use different amounts of memory.

# U -- Understand
# 1. Do I compare both solutions for time and space? (Yes.)
# 2. Does slicing create a reversed copy of the string? (Yes.)

# P -- Plan
# I will return a dictionary that clearly compares the two-pointer solution and the reverse-copy solution.
# Both check all characters in the worst case, but the reverse-copy solution needs extra memory.
# Time Complexity: O(1) for reporting the comparison values
# Space Complexity: O(1) for reporting the comparison values

# Pseudocode
# - create a dictionary
# - record time and space for two-pointer solution
# - record time and space for reverse-copy solution
# - record which is better for time
# - record which is better for space
# - return dictionary

# I -- Implement
def evaluate_palindrome_solutions():
    return {
        "two_pointer_time": "O(n)",
        "two_pointer_space": "O(1)",
        "reverse_copy_time": "O(n)",
        "reverse_copy_space": "O(n)",
        "better_time_complexity": "They have the same time complexity: O(n).",
        "better_space_complexity": "The two-pointer solution has better space complexity: O(1)."
    }


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Make Palindromes)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it combines greedy choices with palindrome construction.

# U -- Understand
# 1. Should I use the minimum number of changes first before thinking about lexicographic order? (Yes.)
# 2. If two different letters do not match, should I keep the smaller one to get the lexicographically smallest answer? (Yes.)

# P -- Plan
# I will convert the string into a list so I can change characters.
# Then I will use two pointers. If the letters are different, I will replace both with the smaller letter.
# That gives the minimum number of operations and also the lexicographically smallest result among minimum-change answers.
# Time Complexity: O(n)
# Space Complexity: O(n), because strings are immutable and I build a list

# Pseudocode
# - turn s into a list of characters
# - set left = 0 and right = len(chars) - 1
# - while left < right:
# -     if chars are different:
# -         set both to the smaller character
# -     move both pointers inward
# - join the list back into a string
# - return it

# I -- Implement
def make_palindrome(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        if chars[left] != chars[right]:
            smaller = min(chars[left], chars[right])
            chars[left] = smaller
            chars[right] = smaller
        left += 1
        right -= 1

    return "".join(chars)


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Reverse Vowels)
# Time Limit: 12 minutes
# Problem Importance:
# This problem matters because it uses two pointers to reverse only selected characters.

# U -- Understand
# 1. Are both lowercase and uppercase vowels included? (Yes.)
# 2. Should consonants stay in the same positions? (Yes.)

# P -- Plan
# I will use two pointers from both ends.
# I will move the pointers until both point to vowels, then swap them.
# At the end, I will join the list of characters into a string.
# Time Complexity: O(n)
# Space Complexity: O(n), because I convert the string to a list

# Pseudocode
# - make a set of vowels
# - turn string into a list
# - set left = 0 and right = len(chars) - 1
# - while left < right:
# -     move left until it points to a vowel
# -     move right until it points to a vowel
# -     if left < right, swap them
# - join and return the string

# I -- Implement
def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        while left < right and chars[left] not in vowels:
            left += 1
        while left < right and chars[right] not in vowels:
            right -= 1

        if left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Two-Pointer Remove Element)
# Time Limit: 12 minutes
# Problem Importance:
# This problem matters because it teaches how to overwrite unwanted values in-place.

# U -- Understand
# 1. Should all occurrences of val be removed from the same list? (Yes.)
# 2. Should the function return the new length after removal? (Yes.)

# P -- Plan
# I will use a write pointer to place the values I want to keep.
# Then I will delete the remaining tail of the list so the printed list matches the example output.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Pseudocode
# - set write = 0
# - for each number in nums:
# -     if number is not val:
# -         place it at nums[write]
# -         increase write
# - delete everything from index write onward
# - return write

# I -- Implement
def remove_element(nums, val):
    write = 0

    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1

    del nums[write:]
    return write


# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Highest Exponent)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices repeated multiplication and stopping conditions.

# U -- Understand
# 1. Should I return the largest exponent such that base^exponent <= limit? (Yes.)
# 2. Can I assume base is greater than 1? (For this beginner problem, yes.)

# P -- Plan
# I will keep multiplying by the base while the value stays within the limit.
# Every time multiplication is still allowed, I will increase the exponent.
# Time Complexity: O(log_base(limit))
# Space Complexity: O(1)

# Pseudocode
# - set exponent = 0
# - set value = 1
# - while value * base <= limit:
# -     multiply value by base
# -     increase exponent
# - return exponent

# I -- Implement
def find_highest_exponent(base, limit):
    exponent = 0
    value = 1

    while value * base <= limit:
        value *= base
        exponent += 1

    return exponent


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Two-Pointer Target Sum)
# Time Limit: 12 minutes
# Problem Importance:
# This problem matters because it is a classic use of two pointers on a sorted list.

# U -- Understand
# 1. Is the input list already sorted? (Yes.)
# 2. Is there always exactly one valid answer? (Yes.)

# P -- Plan
# I will use one pointer at the start and one at the end.
# If the sum is too small, move left forward. If the sum is too large, move right backward.
# When the sum matches target, return the indices.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Pseudocode
# - set left = 0
# - set right = len(nums) - 1
# - while left < right:
# -     current_sum = nums[left] + nums[right]
# -     if current_sum == target:
# -         return [left, right]
# -     if current_sum < target:
# -         left += 1
# -     else:
# -         right -= 1

# I -- Implement
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Evaluate Two Sum)
# Time Limit: 8 minutes
# Problem Importance:
# This problem matters because it compares a sorted two-pointer strategy with a hash map strategy.

# U -- Understand
# 1. Do I need to compare both time and space complexity? (Yes.)
# 2. Does the hash map solution use extra memory? (Yes.)

# P -- Plan
# I will return a dictionary comparing the two-pointer and hash map solutions.
# Both are O(n) time, but the two-pointer method uses less extra space when the list is sorted.
# Time Complexity: O(1) for reporting the comparison values
# Space Complexity: O(1) for reporting the comparison values

# Pseudocode
# - create comparison dictionary
# - store time and space for two-pointer solution
# - store time and space for hash map solution
# - record which is better for time
# - record which is better for space
# - return dictionary

# I -- Implement
def evaluate_two_sum_solutions():
    return {
        "two_pointer_time": "O(n)",
        "two_pointer_space": "O(1)",
        "hash_map_time": "O(n)",
        "hash_map_space": "O(n)",
        "better_time_complexity": "They have the same time complexity: O(n).",
        "better_space_complexity": "The two-pointer solution has better space complexity: O(1), assuming the list is sorted."
    }


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Two-Pointer Reverse Letters)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it shows how to reverse only certain characters while keeping others fixed.

# U -- Understand
# 1. Should non-letter characters stay exactly where they are? (Yes.)
# 2. Should I reverse only alphabetic letters? (Yes.)

# P -- Plan
# I will turn the string into a list and use two pointers from both ends.
# I will skip non-letters and swap only letters.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Pseudocode
# - convert string to list
# - set left = 0 and right = len(chars) - 1
# - while left < right:
# -     if chars[left] is not a letter, move left
# -     elif chars[right] is not a letter, move right
# -     else swap them and move both
# - join and return the string

# I -- Implement
def reverse_only_letters(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        if not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha():
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Reverse Prefix)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices string searching and partial reversal.

# U -- Understand
# 1. Should I reverse from index 0 through the first occurrence of ch? (Yes.)
# 2. If ch is not found, should I return the original word? (Yes.)

# P -- Plan
# I will find the first index of ch by looping through the word.
# If found, I will reverse that prefix and attach the rest of the word.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Pseudocode
# - find the first index where word[index] == ch
# - if not found, return word
# - reverse word from 0 to index
# - add the rest of the word after that
# - return result

# I -- Implement
def reverse_prefix(word, ch):
    index = -1

    for i in range(len(word)):
        if word[i] == ch:
            index = i
            break

    if index == -1:
        return word

    prefix = word[:index + 1]
    reversed_prefix = prefix[::-1]
    return reversed_prefix + word[index + 1:]


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Squash Spaces)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it practices cleaning strings without built-in trim methods.

# U -- Understand
# 1. Should multiple spaces between words become a single space? (Yes.)
# 2. Should leading and trailing spaces be removed in the final result? (Yes.)

# P -- Plan
# I will use one pointer to read the string and a list to build the cleaned result.
# I will only add one space between words, and I will skip extra leading and trailing spaces.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Pseudocode
# - create empty result list
# - set index = 0
# - skip all leading spaces
# - while index is inside string:
# -     if current char is not a space, add it
# -     if current char is a space:
# -         add one space only if next meaningful part exists and last added char is not a space
# -     move index forward
# - if result ends with a space, remove it
# - join and return result

# I -- Implement
def squash_spaces(s):
    result = []
    i = 0

    # Skip leading spaces
    while i < len(s) and s[i] == " ":
        i += 1

    while i < len(s):
        if s[i] != " ":
            result.append(s[i])
        else:
            # Add one space only if last result character is not a space
            # and there is a non-space character later
            if len(result) > 0 and result[-1] != " ":
                j = i
                while j < len(s) and s[j] == " ":
                    j += 1
                if j < len(s):
                    result.append(" ")
        i += 1

    return "".join(result)


# ---------------------------------------------------------
# Example Usage / Output Checks
# These prints are included so the file runs and matches the given examples.

# Version 1, Problem 1
print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

# Version 1, Problem 2
print(reverse_list([1, 2, 3, 4, 5]))

# Version 1, Problem 3
print(evaluate_reverse_list_solutions())

# Version 1, Problem 4
nums = [3, 1, 2, 4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

# Version 1, Problem 5
words = ["abc", "car", "ada", "racecar", "cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc", "racecar", "cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

# Version 1, Problem 6
nums = [1, 1, 2, 3, 4, 4, 4, 5]
print(nums)
print(remove_duplicates(nums))
print(nums)

# Version 2, Problem 1
print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))

# Version 2, Problem 2
s = "amanaplanacanalpanama"
s2 = "helloworld"
print(is_palindrome(s))
print(is_palindrome(s2))

# Version 2, Problem 3
print(evaluate_palindrome_solutions())

# Version 2, Problem 4
s = "egcfe"
print(make_palindrome(s))

s = "abcd"
print(make_palindrome(s))

s = "seven"
print(make_palindrome(s))

# Version 2, Problem 5
s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)

# Version 2, Problem 6
nums = [5, 4, 4, 3, 4, 1]
nums_len = remove_element(nums, 4)
print(nums)
print(nums_len)

# Version 3, Problem 1
exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)

# Version 3, Problem 2
nums = [2, 7, 11, 15, 17]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)

# Version 3, Problem 3
print(evaluate_two_sum_solutions())

# Version 3, Problem 4
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

# Version 3, Problem 5
word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)

# Version 3, Problem 6
print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))
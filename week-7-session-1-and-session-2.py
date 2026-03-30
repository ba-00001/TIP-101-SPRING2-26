# WEEK 7: SESSION 1 AND SESSION 2

def print_section(title):
    print('\n' + '=' * 60)
    print(title)
    print('=' * 60)

# SESSION 1 - PROBLEM SET VERSION 1

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Hello Hello)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it compares recursion and loops.
#
# U -- Understand
# 1) Print Hello n times? Yes.
# 2) If n <= 0? Print nothing.
#
# P -- Plan
# Use the given recursive pattern and a while-loop version.
# Time Complexity: O(n)
# Space Complexity: O(1) iterative
#
# Pseudocode
# - while n > 0: print Hello and subtract 1
#
# I -- Implement

def repeat_hello(n):
    if n > 0:
        print('Hello')
        repeat_hello(n - 1)

def repeat_hello_iterative(n):
    while n > 0:
        print('Hello')
        n -= 1

# Test Cases
print_section('S1 V1 P1')
repeat_hello(2)
repeat_hello_iterative(2)

# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Factorial Cases)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because factorial is a classic recursion pattern.
#
# U -- Understand
# 1) Base case? 0! = 1.
# 2) Recursive case? n * factorial(n - 1).
#
# P -- Plan
# Return 1 for 0, else n times factorial of n - 1.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if n == 0 return 1
# - else return n * factorial(n - 1)
#
# I -- Implement

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test Cases
print_section('S1 V1 P2')
print(factorial(5))
print(factorial(0))

# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Recursive Sum)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it shows recursion on lists.
#
# U -- Understand
# 1) Base case? Empty list returns 0.
# 2) Recursive case? First value plus sum of the rest.
#
# P -- Plan
# Return 0 for empty list, else lst[0] + sum_list(lst[1:]).
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if list empty return 0
# - return first + recursive sum of rest
#
# I -- Implement

def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

# Test Cases
print_section('S1 V1 P3')
print(sum_list([1, 2, 3, 4, 5]))
print(sum_list([]))

# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Recursive Power of 2)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it uses repeated recursive reduction.
#
# U -- Understand
# 1) Smallest true case? 1.
# 2) Odd numbers bigger than 1? False.
#
# P -- Plan
# Keep dividing by 2 until I hit 1 or fail.
# Time Complexity: O(log n)
# Space Complexity: O(log n)
#
# Pseudocode
# - if n == 1 return True
# - if n < 1 or odd return False
# - recurse on n // 2
#
# I -- Implement

def is_power_of_two(n):
    if n == 1:
        return True
    if n < 1 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

# Test Cases
print_section('S1 V1 P4')
print(is_power_of_two(16))
print(is_power_of_two(18))

# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Binary Search I)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because binary search is a core fast search tool.
#
# U -- Understand
# 1) Input list sorted? Yes.
# 2) Missing target? Return -1.
#
# P -- Plan
# Use left and right pointers and cut the search space in half.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - while left <= right check middle
# - move left or right based on comparison
#
# I -- Implement

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test Cases
print_section('S1 V1 P5')
print(binary_search([1, 3, 5, 7, 9, 11, 13, 15], 11))
print(binary_search([1, 3, 5], 2))

# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Backwards Binary Search)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it handles duplicates with binary search.
#
# U -- Understand
# 1) Return what? Last index of target.
# 2) If missing? Return -1.
#
# P -- Plan
# Save a found index and keep searching right.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - do binary search
# - on match save answer and move left pointer right
#
# I -- Implement

def find_last(lst, target):
    left, right, answer = 0, len(lst) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            answer = mid
            left = mid + 1
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

# Test Cases
print_section('S1 V1 P6')
print(find_last([1, 3, 5, 7, 9, 11, 11, 13], 11))
print(find_last([1, 2, 3], 7))

# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (Find Floor)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it finds the best smaller answer with binary search.
#
# U -- Understand
# 1) Floor means what? Largest value <= x.
# 2) If no floor exists? Return -1.
#
# P -- Plan
# Track the best valid index while doing binary search.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - if middle <= x save it and go right
# - else go left
#
# I -- Implement

def find_floor(lst, x):
    left, right, answer = 0, len(lst) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] <= x:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

# Test Cases
print_section('S1 V1 P7')
print(find_floor([1, 2, 8, 10, 11, 12, 19], 5))
print(find_floor([1, 2, 8, 10], 0))

# SESSION 1 - PROBLEM SET VERSION 2

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Counting Down)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it compares recursive and iterative countdowns.
#
# U -- Understand
# 1) Print what? n down to 1.
# 2) If n <= 0? Print nothing.
#
# P -- Plan
# Keep the recursive version and add a while-loop version.
# Time Complexity: O(n)
# Space Complexity: O(1) iterative
#
# Pseudocode
# - while n > 0 print n and subtract 1
#
# I -- Implement

def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)

def countdown_iterative(n):
    while n > 0:
        print(n)
        n -= 1

# Test Cases
print_section('S1 V2 P1')
countdown(3)
countdown_iterative(3)

# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Fibonacci Cases)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because fibonacci is a common recursion example.
#
# U -- Understand
# 1) Base cases? 0 and 1.
# 2) Recursive case? fib(n-1) + fib(n-2).
#
# P -- Plan
# Return n for 0 or 1, otherwise add the two previous answers.
# Time Complexity: O(2^n)
# Space Complexity: O(n)
#
# Pseudocode
# - if n in (0,1) return n
# - else return fibonacci(n-1)+fibonacci(n-2)
#
# I -- Implement

def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test Cases
print_section('S1 V2 P2')
print(fibonacci(6))
print(fibonacci(1))

# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Recursive Product)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it is recursive multiplication over a list.
#
# U -- Understand
# 1) Empty list product? 1.
# 2) Recursive case? First value times rest.
#
# P -- Plan
# Return 1 for empty list, else multiply first item by recursive result.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if list empty return 1
# - return first * recursive product of rest
#
# I -- Implement

def list_product(lst):
    if not lst:
        return 1
    return lst[0] * list_product(lst[1:])

# Test Cases
print_section('S1 V2 P3')
print(list_product([1, 2, 3, 4, 5]))
print(list_product([7]))

# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Recursive Power of 4)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it checks repeated division by 4.
#
# U -- Understand
# 1) Smallest true case? 1.
# 2) When false? n < 1 or not divisible by 4.
#
# P -- Plan
# Keep dividing by 4 until I hit 1 or fail.
# Time Complexity: O(log n)
# Space Complexity: O(log n)
#
# Pseudocode
# - if n == 1 return True
# - if invalid return False
# - recurse on n // 4
#
# I -- Implement

def is_power_of_four(n):
    if n == 1:
        return True
    if n < 1 or n % 4 != 0:
        return False
    return is_power_of_four(n // 4)

# Test Cases
print_section('S1 V2 P4')
print(is_power_of_four(16))
print(is_power_of_four(8))

# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Binary Search II)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it compares recursive and iterative binary search.
#
# U -- Understand
# 1) Sorted input? Yes.
# 2) Missing target? Return -1.
#
# P -- Plan
# Use the recursive helper provided and build the iterative version.
# Time Complexity: O(log n)
# Space Complexity: O(1) iterative
#
# Pseudocode
# - while left <= right check middle
# - move left or right until found or exhausted
#
# I -- Implement

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    return binary_search_recursive(arr, target, mid + 1, right)

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test Cases
print_section('S1 V2 P5')
nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search_recursive(nums, 11, 0, len(nums) - 1))
print(binary_search_iterative(nums, 4))

# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Find Ceiling)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it finds the best bigger answer with binary search.
#
# U -- Understand
# 1) Ceiling means what? Smallest value >= x.
# 2) If no ceiling? Return -1.
#
# P -- Plan
# Track the best valid index while moving left when possible.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - if middle >= x save it and go left
# - else go right
#
# I -- Implement

def find_ceiling(lst, x):
    left, right, answer = 0, len(lst) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] >= x:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

# Test Cases
print_section('S1 V2 P6')
print(find_ceiling([1, 2, 8, 10, 11, 12, 19], 5))
print(find_ceiling([1, 2, 8], 20))

# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (Ternary Search)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it is another divide-and-conquer search idea.
#
# U -- Understand
# 1) How many midpoints? Two.
# 2) If missing? Return -1.
#
# P -- Plan
# Split the search window into thirds and keep only the correct third.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - compute mid1 and mid2
# - compare target and shrink to one third
#
# I -- Implement

def ternary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third
        if lst[mid1] == target:
            return mid1
        if lst[mid2] == target:
            return mid2
        if target < lst[mid1]:
            right = mid1 - 1
        elif target > lst[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1

# Test Cases
print_section('S1 V2 P7')
print(ternary_search([1, 3, 5, 7, 9, 11, 13, 15], 11))
print(ternary_search([1, 3, 5], 2))

# SESSION 1 - PROBLEM SET VERSION 3

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (In The Stars)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices recursion on strings.
#
# U -- Understand
# 1) Add what between letters? A star.
# 2) Base case? Empty or one-char string.
#
# P -- Plan
# Keep the recursive version and build an iterative version without join().
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - loop through chars and add * between them
#
# I -- Implement

def insert_stars(s):
    if len(s) <= 1:
        return s
    return s[0] + '*' + insert_stars(s[1:])

def insert_stars_iterative(s):
    if len(s) <= 1:
        return s
    result = ''
    i = 0
    while i < len(s):
        result += s[i]
        if i != len(s) - 1:
            result += '*'
        i += 1
    return result

# Test Cases
print_section('S1 V3 P1')
print(insert_stars('abc'))
print(insert_stars_iterative('abc'))

# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (String Length Cases)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it finds string length recursively.
#
# U -- Understand
# 1) Base case? Empty string is 0.
# 2) Recursive case? 1 + length of s[1:].
#
# P -- Plan
# Return 0 for empty string, else 1 + recursive result.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if empty return 0
# - else return 1 + recurse on rest
#
# I -- Implement

def string_length(s):
    if s == '':
        return 0
    return 1 + string_length(s[1:])

# Test Cases
print_section('S1 V3 P2')
print(string_length('abc'))
print(string_length(''))

# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Recursive Digits Sum)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it combines recursion and digit math.
#
# U -- Understand
# 1) Base case? Single digit.
# 2) Split digits how? % 10 and // 10.
#
# P -- Plan
# Add the last digit to the recursive sum of the remaining digits.
# Time Complexity: O(d)
# Space Complexity: O(d)
#
# Pseudocode
# - if n < 10 return n
# - return last digit + recurse on rest
#
# I -- Implement

def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

# Test Cases
print_section('S1 V3 P3')
print(sum_digits(523))
print(sum_digits(0))

# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Recursive Count 7s)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it gives more digit recursion practice.
#
# U -- Understand
# 1) What counts? Digits equal to 7.
# 2) Base case? Single digit check.
#
# P -- Plan
# Check the last digit, then recurse on the rest.
# Time Complexity: O(d)
# Space Complexity: O(d)
#
# Pseudocode
# - return 1 or 0 for single digit
# - else add match for last digit + recurse
#
# I -- Implement

def count_sevens(n):
    if n < 10:
        return 1 if n == 7 else 0
    return (1 if n % 10 == 7 else 0) + count_sevens(n // 10)

# Test Cases
print_section('S1 V3 P4')
print(count_sevens(727))
print(count_sevens(12345))

# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Binary Search III)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because sometimes I only need a True/False answer.
#
# U -- Understand
# 1) Found target? Return True.
# 2) Missing target? Return False.
#
# P -- Plan
# Use iterative binary search and return booleans.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - binary search until found or exhausted
#
# I -- Implement

def binary_search_exists(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Test Cases
print_section('S1 V3 P5')
print(binary_search_exists([1, 3, 5, 7, 9, 11], 11))
print(binary_search_exists([1, 3, 5], 4))

# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Find Missing)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it uses indices and values together.
#
# U -- Understand
# 1) Array contains what? Numbers 0..n with one missing.
# 2) Key rule? Before the missing value, nums[i] == i.
#
# P -- Plan
# Find the first mismatch with binary search.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - if nums[mid] == mid go right
# - else go left
# - return left
#
# I -- Implement

def find_missing(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Test Cases
print_section('S1 V3 P6')
print(find_missing([0, 1, 3]))
print(find_missing([1, 2, 3]))

# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (Square Root)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it finds a numeric answer with binary search.
#
# U -- Understand
# 1) Perfect square? Return exact root.
# 2) Not perfect? Return floor of root.
#
# P -- Plan
# Search for the biggest number whose square is <= x.
# Time Complexity: O(log x)
# Space Complexity: O(1)
#
# Pseudocode
# - binary search from 0 to x
# - track best valid middle
#
# I -- Implement

def sqrt(x):
    if x < 2:
        return x
    left, right, answer = 0, x, 0
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return mid
        if square < x:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

# Test Cases
print_section('S1 V3 P7')
print(sqrt(8))
print(sqrt(16))

# SESSION 2 - PROBLEM SET VERSION 1

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Neatly Nested)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it uses recursion on parentheses strings.
#
# U -- Understand
# 1) Valid nested string? Empty or outer pair around a valid inside.
# 2) Bad shape? Return False.
#
# P -- Plan
# Check the outside pair, then recurse on the inside.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if empty return True
# - if ends are not () return False
# - recurse on inside
#
# I -- Implement

def is_nested(s):
    if s == '':
        return True
    if len(s) % 2 != 0 or s[0] != '(' or s[-1] != ')':
        return False
    return is_nested(s[1:-1])

# Test Cases
print_section('S2 V1 P1')
print(is_nested('(())'))
print(is_nested('()()'))

# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (How Many 1s)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it counts values in O(log n).
#
# U -- Understand
# 1) Sorted list of what? Only 0s and 1s.
# 2) Main trick? Find the first 1.
#
# P -- Plan
# Binary search for the first 1, then subtract that index from the length.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - binary search for first 1
# - if none found return 0
# - return len(lst) - index
#
# I -- Implement

def count_ones(lst):
    left, right, first_one = 0, len(lst) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == 1:
            first_one = mid
            right = mid - 1
        else:
            left = mid + 1
    return 0 if first_one == -1 else len(lst) - first_one

# Test Cases
print_section('S2 V1 P2')
print(count_ones([0, 0, 0, 0, 1, 1, 1]))
print(count_ones([0, 0, 0]))

# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Binary Search IV)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because recursive binary search is a classic divide-and-conquer pattern.
#
# U -- Understand
# 1) Missing target? Return -1.
# 2) Input sorted? Yes.
#
# P -- Plan
# Use a helper with left and right bounds.
# Time Complexity: O(log n)
# Space Complexity: O(log n)
#
# Pseudocode
# - if left > right return -1
# - check middle and recurse left or right
#
# I -- Implement

def binary_search_recursive_main(nums, target):
    def helper(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return helper(mid + 1, right)
        return helper(left, mid - 1)
    return helper(0, len(nums) - 1)

# Test Cases
print_section('S2 V1 P3')
print(binary_search_recursive_main([1, 3, 5, 7, 9, 11], 11))
print(binary_search_recursive_main([1, 3, 5], 4))

# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Count Rotations)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it finds the pivot in a rotated list.
#
# U -- Understand
# 1) Answer equals what? Index of the smallest value.
# 2) Already sorted? Return 0.
#
# P -- Plan
# Binary search for the smallest element.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - compare middle and right values
# - keep the half with the smallest value
#
# I -- Implement

def count_rotations(nums):
    if not nums:
        return 0
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left

# Test Cases
print_section('S2 V1 P4')
print(count_rotations([8, 9, 10, 2, 5, 6]))
print(count_rotations([2, 5, 6, 8]))

# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Merge Sort I)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because merge sort is a key divide-and-conquer sort.
#
# U -- Understand
# 1) Base case? Length 0 or 1.
# 2) Combine how? Merge two sorted halves.
#
# P -- Plan
# Recursively sort left and right halves, then merge them.
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Pseudocode
# - split list
# - sort halves
# - merge halves
#
# I -- Implement

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    while i < len(left):
        result.append(left[i]); i += 1
    while j < len(right):
        result.append(right[j]); j += 1
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))

# Test Cases
print_section('S2 V1 P5')
print(merge_sort([5, 3, 4, 2, 1]))
print(merge_sort([9, 1, 7, 1]))

# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Circle Search)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it searches inside a rotated sorted list.
#
# U -- Understand
# 1) Duplicates? No.
# 2) Missing target? Return -1.
#
# P -- Plan
# At each step, one side is sorted. Use that to decide which side to keep.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - check which half is sorted
# - keep only the half that can contain target
#
# I -- Implement

def search_circular_list(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Test Cases
print_section('S2 V1 P6')
print(search_circular_list([8, 9, 10, 2, 5, 6], 10))
print(search_circular_list([8, 9, 10, 2, 5, 6], 7))

# SESSION 2 - PROBLEM SET VERSION 2

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Substring Search)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it counts non-overlapping matches recursively.
#
# U -- Understand
# 1) Overlaps count? No.
# 2) Empty sub? Return 0.
#
# P -- Plan
# If the string starts with sub, count 1 and skip that many letters.
# Otherwise, move forward by one letter.
# Time Complexity: O(n * m)
# Space Complexity: O(n)
#
# Pseudocode
# - if too short return 0
# - if startswith sub, count 1 and skip sub
# - else skip one char
#
# I -- Implement

def count_substring(s, sub):
    if sub == '' or len(s) < len(sub):
        return 0
    if s[:len(sub)] == sub:
        return 1 + count_substring(s[len(sub):], sub)
    return count_substring(s[1:], sub)

# Test Cases
print_section('S2 V2 P1')
print(count_substring('abcdeabcde', 'abc'))
print(count_substring('aaaaa', 'aa'))

# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (How Many 0s (Iterative))
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it counts zeroes in O(log n).
#
# U -- Understand
# 1) Sorted list of what? 0s and 1s.
# 2) Trick? Find the first 1.
#
# P -- Plan
# Binary search for the first 1, then return its index.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - search for first 1
# - if none found return len(lst)
#
# I -- Implement

def count_zeroes_iterative(lst):
    left, right, first_one = 0, len(lst) - 1, len(lst)
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == 1:
            first_one = mid
            right = mid - 1
        else:
            left = mid + 1
    return first_one

# Test Cases
print_section('S2 V2 P2')
print(count_zeroes_iterative([0, 0, 0, 0, 1, 1, 1]))
print(count_zeroes_iterative([1, 1, 1]))

# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (How Many 0s (Recursive))
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it makes the same idea recursive.
#
# U -- Understand
# 1) Recursive helper finds what? First 1.
# 2) No 1 found? Return len(lst).
#
# P -- Plan
# Recurse left for earlier 1s and right for later 0s.
# Time Complexity: O(log n)
# Space Complexity: O(log n)
#
# Pseudocode
# - helper(left,right)
# - if invalid return len(lst)
# - recurse appropriately
#
# I -- Implement

def count_zeroes_recursive(lst):
    def helper(left, right):
        if left > right:
            return len(lst)
        mid = (left + right) // 2
        if lst[mid] == 1:
            earlier = helper(left, mid - 1)
            return mid if earlier == len(lst) else earlier
        return helper(mid + 1, right)
    return helper(0, len(lst) - 1)

# Test Cases
print_section('S2 V2 P3')
print(count_zeroes_recursive([0, 0, 0, 1, 1, 1, 1]))
print(count_zeroes_recursive([0, 0, 0]))

# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Special Numbers)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it combines sorting and counting logic.
#
# U -- Understand
# 1) Special means what? Exactly x numbers are >= x.
# 2) Must x be in nums? No.
#
# P -- Plan
# Try each x from 0 to n and use binary search to count values >= x.
# Time Complexity: O(n log n)
# Space Complexity: O(1)
#
# Pseudocode
# - for x in 0..n
# - find first value >= x
# - if count equals x return x
#
# I -- Implement

def is_special(nums):
    n = len(nums)
    for x in range(n + 1):
        left, right, first_big = 0, n - 1, n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= x:
                first_big = mid
                right = mid - 1
            else:
                left = mid + 1
        if n - first_big == x:
            return x
    return -1

# Test Cases
print_section('S2 V2 P4')
print(is_special([3, 5]))
print(is_special([0, 0]))

# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Merge Sort II)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because merging is the heart of merge sort.
#
# U -- Understand
# 1) Inputs? Two sorted lists.
# 2) Output? One sorted combined list.
#
# P -- Plan
# Compare the current front values and append the smaller one.
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Pseudocode
# - compare left[i] and right[j]
# - append leftovers at the end
#
# I -- Implement

def merge_two(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    while i < len(left):
        result.append(left[i]); i += 1
    while j < len(right):
        result.append(right[j]); j += 1
    return result

def merge_sort_two(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    return merge_two(merge_sort_two(lst[:mid]), merge_sort_two(lst[mid:]))

# Test Cases
print_section('S2 V2 P5')
print(merge_two([1, 3, 5], [2, 4]))
print(merge_sort_two([5, 3, 4, 2, 1]))

# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Circle Majority)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it uses divide and conquer for majority element.
#
# U -- Understand
# 1) Majority means what? More than n // 2 times.
# 2) Does it exist? Yes.
#
# P -- Plan
# Find left and right majority candidates recursively, then count them.
# Time Complexity: O(n log n)
# Space Complexity: O(log n)
#
# Pseudocode
# - recurse on left and right halves
# - if candidates differ, count both and keep larger
#
# I -- Implement

def circle_majority(nums):
    def helper(left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        left_major = helper(left, mid)
        right_major = helper(mid + 1, right)
        if left_major == right_major:
            return left_major
        left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_major)
        right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_major)
        return left_major if left_count > right_count else right_major
    return helper(0, len(nums) - 1)

# Test Cases
print_section('S2 V2 P6')
print(circle_majority([3, 2, 3]))
print(circle_majority([2, 2, 1, 1, 1, 2, 2]))

# SESSION 2 - PROBLEM SET VERSION 3

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Recursive Remove Char)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it recursively builds a filtered string.
#
# U -- Understand
# 1) Remove what? Every copy of char.
# 2) Base case? Empty string.
#
# P -- Plan
# Skip matching chars and keep non-matching chars.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if empty return ''
# - if first char matches, skip it
# - else keep it and recurse
#
# I -- Implement

def remove_char(s, char):
    if s == '':
        return ''
    if s[0] == char:
        return remove_char(s[1:], char)
    return s[0] + remove_char(s[1:], char)

# Test Cases
print_section('S2 V3 P1')
print(remove_char('xaxbxc', 'x'))
print(remove_char('banana', 'a'))

# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Where Does it Go (Iterative))
# Time Limit: 15 minutes
# Problem Importance:
# This matters because search-insert is a very common binary-search pattern.
#
# U -- Understand
# 1) Found target? Return its index.
# 2) Missing target? Return insertion index.
#
# P -- Plan
# Use binary search, then return left when the loop ends.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - do binary search
# - if not found return left
#
# I -- Implement

def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Test Cases
print_section('S2 V3 P2')
print(search_insert([1, 3, 5, 7, 9, 11, 13, 15], 20))
print(search_insert([1, 3, 5, 6], 5))

# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Where Does it Go (Recursive))
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it rewrites search-insert recursively.
#
# U -- Understand
# 1) Found target? Return index.
# 2) Invalid window? Return left.
#
# P -- Plan
# Use a helper with left and right bounds.
# Time Complexity: O(log n)
# Space Complexity: O(log n)
#
# Pseudocode
# - if left > right return left
# - compare target and recurse
#
# I -- Implement

def search_insert_recursive(nums, target):
    def helper(left, right):
        if left > right:
            return left
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return helper(mid + 1, right)
        return helper(left, mid - 1)
    return helper(0, len(nums) - 1)

# Test Cases
print_section('S2 V3 P3')
print(search_insert_recursive([1, 3, 5, 6], 5))
print(search_insert_recursive([1, 3, 5, 6], 2))

# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Find Frequencies)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it groups duplicate values efficiently.
#
# U -- Understand
# 1) Return what? A dictionary of frequencies.
# 2) Why sorted helps? Equal values stay in one block.
#
# P -- Plan
# For each new value, binary search for its last occurrence, store the count, then jump.
# Time Complexity: O(k log n)
# Space Complexity: O(k)
#
# Pseudocode
# - start at i = 0
# - find last index of lst[i]
# - save count and jump to next group
#
# I -- Implement

def find_frequencies(lst):
    frequencies = {}
    i = 0
    while i < len(lst):
        value = lst[i]
        left, right, last_index = i, len(lst) - 1, i
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] == value:
                last_index = mid
                left = mid + 1
            elif lst[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        frequencies[value] = last_index - i + 1
        i = last_index + 1
    return frequencies

# Test Cases
print_section('S2 V3 P4')
print(find_frequencies([2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]))
print(find_frequencies([]))

# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Merge Sort III)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it brings together full merge sort again.
#
# U -- Understand
# 1) Base case? 0 or 1 item.
# 2) Main steps? Split, sort, merge.
#
# P -- Plan
# Write a merge helper and recursively sort both halves.
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# Pseudocode
# - split list
# - sort halves recursively
# - merge halves
#
# I -- Implement

def merge_three(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    while i < len(left):
        result.append(left[i]); i += 1
    while j < len(right):
        result.append(right[j]); j += 1
    return result

def merge_sort_three(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    return merge_three(merge_sort_three(lst[:mid]), merge_sort_three(lst[mid:]))

# Test Cases
print_section('S2 V3 P5')
print(merge_sort_three([5, 3, 4, 2, 1]))
print(merge_sort_three([10, -1, 7, 7, 3]))

# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (What a Nice String)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it is a strong divide-and-conquer string problem.
#
# U -- Understand
# 1) Nice means what? Every used letter appears in both cases.
# 2) Tie rule? Return the earliest longest one.
#
# P -- Plan
# If a bad character breaks the rule, split around it and recurse on both sides.
# Time Complexity: O(n^2) worst case
# Space Complexity: O(n)
#
# Pseudocode
# - if string too short return ''
# - find a bad char with missing swapcase
# - recurse left and right, keep longer, left on tie
#
# I -- Implement

def longest_nice_substring(s):
    if len(s) < 2:
        return ''
    chars = set(s)
    for i, char in enumerate(s):
        if char.swapcase() not in chars:
            left = longest_nice_substring(s[:i])
            right = longest_nice_substring(s[i + 1:])
            return left if len(left) >= len(right) else right
    return s

# Test Cases
print_section('S2 V3 P6')
print(longest_nice_substring('YazaAay'))
print(longest_nice_substring('Bb'))
print(longest_nice_substring('c'))

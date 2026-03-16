# =========================================================
# WEEK 3: SESSION 1
# FULL SET -- Version 1, Version 2, Version 3
# Each problem includes:
# 1) Why this problem was chosen
# 2) UMPIRE
# 3) Python solution with comments
# =========================================================


# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Problem 1: Calling Mississippi
# Why chosen:
# This problem is a simple warm-up for practicing function calls,
# loops, and formatted string output.

# UMPIRE
# Understand:
# We need to call the function one time so it prints:
# 1 mississippi through 5 mississippi.
# Match:
# This is a simple loop / function call problem.
# Plan:
# Use the given function and call it with limit = 6
# because range(1, 6) prints 1 through 5.
# Implement:
def count_mississippi(limit):
    for num in range(1, limit):
        print(f"{num} mississippi")

# Review:
count_mississippi(6)

# Evaluate:
# Time: O(n)
# Space: O(1)


# ---------------------------------------------------------
# Problem 2: Swap Ends
# Why chosen:
# This problem helps practice string indexing and slicing.

# UMPIRE
# Understand:
# Return a new string where the first and last characters are swapped.
# Match:
# String slicing / indexing.
# Plan:
# If the string is short, return it as-is.
# Otherwise return: last + middle + first.
# Implement:
def swap_ends(my_str):
    if len(my_str) <= 1:
        return my_str
    return my_str[-1] + my_str[1:-1] + my_str[0]

# Review:
# boat -> toab

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 3: Is Pangram
# Why chosen:
# This problem is good practice for string traversal and checking
# whether all letters of the alphabet appear.

# UMPIRE
# Understand:
# Return True if the string contains every letter a-z.
# Match:
# String + set problem.
# Plan:
# Lowercase the string, collect only letters into a set,
# and check if it contains all 26 letters.
# Implement:
def is_pangram(my_str):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters_in_string = set()

    for char in my_str.lower():
        if 'a' <= char <= 'z':
            letters_in_string.add(char)

    return alphabet.issubset(letters_in_string)

# Review:
# "The quick brown fox jumps over the lazy dog" -> True

# Evaluate:
# Time: O(n)
# Space: O(1), since alphabet size is fixed


# ---------------------------------------------------------
# Problem 4: Reverse String
# Why chosen:
# This is a basic string manipulation problem that reinforces slicing.

# UMPIRE
# Understand:
# Return the reverse of the input string.
# Match:
# String slicing.
# Plan:
# Use slicing with step -1.
# Implement:
def reverse_string(my_str):
    return my_str[::-1]

# Review:
# live -> evil

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 5: First Unique
# Why chosen:
# This problem helps practice frequency counting and scanning for
# the first non-repeating character.

# UMPIRE
# Understand:
# Return the index of the first character that appears once.
# If none exists, return -1.
# Match:
# Hash map / frequency dictionary.
# Plan:
# First count each character, then scan again to find the first
# one with count 1.
# Implement:
def first_unique_char(my_str):
    freq = {}

    for char in my_str:
        freq[char] = freq.get(char, 0) + 1

    for i in range(len(my_str)):
        if freq[my_str[i]] == 1:
            return i

    return -1

# Review:
# leetcode -> 0
# loveleetcode -> 2
# aabb -> -1

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 6: Minimum Distance
# Why chosen:
# This problem helps practice scanning lists and tracking positions.

# UMPIRE
# Understand:
# Return the smallest distance between two words in a list.
# Match:
# Array traversal with index tracking.
# Plan:
# Track latest positions of word1 and word2.
# Update minimum distance each time both have been seen.
# Implement:
def min_distance(words, word1, word2):
    pos1 = -1
    pos2 = -1
    best = float("inf")

    for i in range(len(words)):
        if words[i] == word1:
            pos1 = i
        if words[i] == word2:
            pos2 = i

        if pos1 != -1 and pos2 != -1:
            best = min(best, abs(pos1 - pos2))

    return best

# Review:
# ["the", "quick", "brown", "fox", "jumped", "the"], quick, jumped -> 3

# Evaluate:
# Time: O(n)
# Space: O(1)


# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Problem 1: Perfect Match
# Why chosen:
# This is another quick warm-up for dictionaries and string formatting.

# UMPIRE
# Understand:
# Use the provided function so it prints the 3 lines shown.
# Match:
# Dictionary iteration.
# Plan:
# Make a dictionary with the given pairs and call the function once.
# Implement:
def match_made(dictionary):
    for key, value in dictionary.items():
        print(f"{key} and {value} are a perfect match.")

perfect_pairs = {
    "Peanut butter": "Jelly",
    "Spongebob": "Patrick",
    "Ash": "Pikachu"
}

match_made(perfect_pairs)

# Evaluate:
# Time: O(n)
# Space: O(1) extra


# ---------------------------------------------------------
# Problem 2: Remove Char
# Why chosen:
# Good practice for removing part of a string using slicing.

# UMPIRE
# Understand:
# Remove the character at index n.
# Match:
# String slicing.
# Plan:
# Return the part before n plus the part after n.
# Implement:
def remove_char(s, n):
    return s[:n] + s[n+1:]

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 3: Count Vowels
# Why chosen:
# This problem reinforces string scanning and conditional checks.

# UMPIRE
# Understand:
# Return the number of vowels in the string.
# Match:
# String traversal.
# Plan:
# Loop through the string and count letters in "aeiouAEIOU".
# Implement:
def vowel_count(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count

# Evaluate:
# Time: O(n)
# Space: O(1)


# ---------------------------------------------------------
# Problem 4: Reverse Sentence
# Why chosen:
# Helps practice splitting strings into words and rebuilding them.

# UMPIRE
# Understand:
# Reverse the order of words, not the letters in each word.
# Match:
# String split/join problem.
# Plan:
# Split into words, reverse the list, join back.
# Implement:
def reverse_sentence(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 5: String Compression
# Why chosen:
# This is a classic compression-style problem using grouped counts.

# UMPIRE
# Understand:
# Compress repeated letters into letter+count.
# Return original if compressed is not shorter.
# Match:
# String traversal with counting streaks.
# Plan:
# Count consecutive repeated letters and build compressed string.
# Implement:
def compress_string(my_str):
    if not my_str:
        return my_str

    compressed = []
    count = 1

    for i in range(1, len(my_str)):
        if my_str[i] == my_str[i - 1]:
            count += 1
        else:
            compressed.append(my_str[i - 1] + str(count))
            count = 1

    compressed.append(my_str[-1] + str(count))
    compressed_str = "".join(compressed)

    if len(compressed_str) < len(my_str):
        return compressed_str
    return my_str

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 6: Needle in a Haystack
# Why chosen:
# This problem is good for substring searching logic.

# UMPIRE
# Understand:
# Return the first index of needle in haystack, or -1.
# Match:
# String scan / substring comparison.
# Plan:
# Check every possible start position in haystack.
# Implement:
def find_the_needle(haystack, needle):
    if needle == "":
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1

# Evaluate:
# Time: O(n * m)
# Space: O(1)


# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Problem 1: Choose Your Pokemon
# Why chosen:
# This problem is a simple way to practice loops, lists, and printing.

# UMPIRE
# Understand:
# Call the given function so it prints all three Pokemon lines.
# Match:
# List iteration.
# Plan:
# Pass a list with the three Pokemon names.
# Implement:
def choose_pokemon(my_pokemon):
    for pokemon in my_pokemon:
        print(f"{pokemon} I choose you!")

choose_pokemon(["Pikachu", "Charizard", "Eevee"])

# Evaluate:
# Time: O(n)
# Space: O(1) extra


# ---------------------------------------------------------
# Problem 2: Rotate Left
# Why chosen:
# Good practice for string slicing and rearranging parts of a string.

# UMPIRE
# Understand:
# Move the first n characters to the end.
# Match:
# String slicing.
# Plan:
# Return s[n:] + s[:n]
# Implement:
def rotate_left(s, n):
    return s[n:] + s[:n]

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 3: First Duplicate
# Why chosen:
# This problem helps build skill with tracking previously seen items.

# UMPIRE
# Understand:
# Return the index of the first repeated character.
# Return None if there is none.
# Match:
# Set-based scan.
# Plan:
# Use a set to track seen characters as you loop.
# Implement:
def first_repeated_char(s):
    seen = set()

    for i in range(len(s)):
        if s[i] in seen:
            return i
        seen.add(s[i])

    return None

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 4: Find the Imposter
# Why chosen:
# This problem is useful for practicing character counting.

# UMPIRE
# Understand:
# s2 is s1 shuffled plus one extra character. Find that extra character.
# Match:
# Frequency counting.
# Plan:
# Count characters in both strings, then find the one with a bigger count in s2.
# Implement:
def find_difference(s1, s2):
    counts = {}

    for char in s2:
        counts[char] = counts.get(char, 0) + 1

    for char in s1:
        counts[char] -= 1

    for char in counts:
        if counts[char] > 0:
            return char

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 5: Longest Substring
# Why chosen:
# This is an important sliding window problem that comes up often.

# UMPIRE
# Understand:
# Return the length of the longest substring with no repeated characters.
# Match:
# Sliding window.
# Plan:
# Expand the window with right pointer and shrink with left pointer
# when repeats appear.
# Implement:
def length_of_longest_substring(s):
    seen = {}
    left = 0
    longest = 0

    for right in range(len(s)):
        char = s[right]

        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        longest = max(longest, right - left + 1)

    return longest

# Evaluate:
# Time: O(n)
# Space: O(n)


# ---------------------------------------------------------
# Problem 6: Roman to Integer
# Why chosen:
# This is a classic string parsing problem with simple rules and edge cases.

# UMPIRE
# Understand:
# Convert a Roman numeral string into an integer.
# Match:
# String scan with value lookup.
# Plan:
# Map each Roman symbol to its value.
# If a symbol is smaller than the one after it, subtract it.
# Otherwise add it.
# Implement:
def roman_to_int(s):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i in range(len(s)):
        if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]

    return total

# Evaluate:
# Time: O(n)
# Space: O(1)


# =========================================================
# QUICK EXAMPLE TESTS
# =========================================================

print("swap_ends:", swap_ends("boat"))                      # toab
print("is_pangram:", is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print("reverse_string:", reverse_string("live"))           # evil
print("first_unique_char:", first_unique_char("leetcode")) # 0
print("min_distance:", min_distance(["the", "quick", "brown", "fox", "jumped", "the"], "the", "jumped"))  # 1
print("remove_char:", remove_char("typpo", 2))             # typo
print("vowel_count:", vowel_count("hello world"))          # 3
print("reverse_sentence:", reverse_sentence("I solemnly swear I am up to no good"))
print("compress_string:", compress_string("aaaaabbcccd"))  # a5b2c3d1
print("find_the_needle:", find_the_needle("tobeornottobe", "be"))  # 2
print("rotate_left:", rotate_left("rotation", 2))          # tationro
print("first_repeated_char:", first_repeated_char("hello world"))  # 3
print("find_difference:", find_difference("abcd", "baedc"))        # e
print("length_of_longest_substring:", length_of_longest_substring("abcdeefghhhhh"))  # 5
print("roman_to_int:", roman_to_int("MCMXCIV"))            # 1994





# Session 2

# =========================================================
# WEEK 3: SESSION 2
# FULL SOLUTIONS
# =========================================================

# ---------------------------------------------------------
# Problem Set Version 1
# ---------------------------------------------------------

# Problem 1: Sum of Strings
def sum_of_number_strings(nums):
    total = 0
    for num in nums:
        total += int(num)
    return total

nums = ["10", "20", "30"]
sum_result = sum_of_number_strings(nums)
print(sum_result)  # 60


# Problem 2: Remove Duplicates
def remove_duplicates(nums):
    if not nums:
        return []

    result = []
    i = 0

    while i < len(nums):
        result.append(nums[i])
        current = nums[i]

        while i < len(nums) and nums[i] == current:
            i += 1

    return result

nums = [1,1,1,2,3,4,4,5,6,6]
no_dups = remove_duplicates(nums)
print(no_dups)  # [1, 2, 3, 4, 5, 6]


# Problem 3: Reverse Letters
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

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)  # j-Ih-gfE-dCba


# Problem 4: Longest Uniform Substring
def longest_uniform_substring(s):
    if not s:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)  # 4

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)  # 1


# Problem 5: Teemo's Attack
def find_poisoned_duration(time_series, duration):
    if not time_series:
        return 0

    total = 0

    for i in range(len(time_series) - 1):
        total += min(duration, time_series[i + 1] - time_series[i])

    total += duration
    return total

time_series = [1, 4, 9]
damage = find_poisoned_duration(time_series, 3)
print(damage)  # 8


# Problem 6: Sum Unique Elements
def sum_of_unique_elements(lst1, lst2):
    freq = {}
    for num in lst1:
        freq[num] = freq.get(num, 0) + 1

    lst2_set = set(lst2)
    total = 0

    for num in lst1:
        if freq[num] == 1 and num not in lst2_set:
            total += num

    return total

lstA = [1, 2, 3, 4]
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)  # 3

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)  # 0


# ---------------------------------------------------------
# Problem Set Version 2
# ---------------------------------------------------------

# Problem 1: String to Integer
def string_to_integer_mapping(s):
    result = []
    for char in s:
        result.append(int(char))
    return result

print(string_to_integer_mapping("12345"))  # [1, 2, 3, 4, 5]


# Problem 2: Delete Minimum
def delete_minimum_elements(nums):
    nums = nums[:]  # copy so original list is not changed
    removed = []

    while nums:
        minimum = min(nums)
        nums.remove(minimum)
        removed.append(minimum)

    return removed

nums = [5, 3, 2, 8, 3, 1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)  # [1, 2, 3, 3, 5, 8]


# Problem 3: Longest Common Prefix
def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]

    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix

strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
print(common_string)  # fl

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
print(common_str)  # ""


# Problem 4: Consecutive Characters
def count_consecutive_characters(str1):
    if not str1:
        return 0

    max_count = 1
    current = 1

    for i in range(1, len(str1)):
        if str1[i] == str1[i - 1]:
            current += 1
            max_count = max(max_count, current)
        else:
            current = 1

    return max_count

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)  # 4

str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)  # 1


# Problem 5: Partition Labels
def partition_label(s):
    last_index = {}

    for i, char in enumerate(s):
        last_index[char] = i

    result = []
    start = 0
    end = 0

    for i, char in enumerate(s):
        end = max(end, last_index[char])

        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result

s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))  # [9, 7, 8]

s2 = "abcabcbadefffeda"
print(partition_label(s2))  # [16]


# Problem 6: Interleave Lists
def interleave_lists(lst1, lst2):
    result = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        result.append(lst1[i])
        result.append(lst2[j])
        i += 1
        j += 1

    while i < len(lst1):
        result.append(lst1[i])
        i += 1

    while j < len(lst2):
        result.append(lst2[j])
        j += 1

    return result

lst1 = [1, 2, 3, 4]
lst2 = [10, 20]
inter_lst = interleave_lists(lst1, lst2)
print(inter_lst)  # [1, 10, 2, 20, 3, 4]


# ---------------------------------------------------------
# Problem Set Version 3
# ---------------------------------------------------------

# Problem 1: Remove Vowels
def remove_vowels(s):
    vowels = set("aeiouAEIOU")
    result = []

    for char in s:
        if char not in vowels:
            result.append(char)

    return "".join(result)

s = "Hello World"
new_string = remove_vowels(s)
print(new_string)  # Hll Wrld


# Problem 2: Missing Integer
def find_missing_positive(nums):
    expected = 1
    i = 0

    while i < len(nums):
        if nums[i] != expected:
            return expected
        expected += 1
        i += 1

    return expected

nums1 = [1, 2, 3, 5, 6, 10]
print(find_missing_positive(nums1))  # 4

nums2 = [1, 2, 3, 4, 5]
print(find_missing_positive(nums2))  # 6


# Problem 3: Word Follows Pattern
def wordPattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word and char_to_word[char] != word:
            return False
        if word in word_to_char and word_to_char[word] != char:
            return False

        char_to_word[char] = word
        word_to_char[word] = char

    return True

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))  # True

s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))  # False

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))  # False

s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))  # True


# Problem 4: Binary Substrings
def binary_substrings_count(s):
    groups = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)

    total = 0
    for i in range(1, len(groups)):
        total += min(groups[i - 1], groups[i])

    return total

s = "00110011"
print(binary_substrings_count(s))  # 6

s2 = "10101"
print(binary_substrings_count(s2))  # 4

s3 = "1111"
print(binary_substrings_count(s3))  # 0


# Problem 5: Exclusive Elements
def exclusive_elements(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)

    result = []

    for num in lst1:
        if num not in set2:
            result.append(num)

    for num in lst2:
        if num not in set1:
            result.append(num)

    return result

lst1 = [3, 1, 8, 10]
lst2 = [4, 5, 3, 7, 8]
excl_lst = exclusive_elements(lst1, lst2)
print(excl_lst)  # [1, 10, 4, 5, 7]


# Problem 6: Flowerbed
def can_place_flowers(flowerbed, n):
    flowerbed = flowerbed[:]  # avoid changing original list
    count = 0

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            left_empty = (i == 0 or flowerbed[i - 1] == 0)
            right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

            if left_empty and right_empty:
                flowerbed[i] = 1
                count += 1

                if count >= n:
                    return True

    return count >= n

flowerbed = [1, 0, 0, 0, 1]
approved = can_place_flowers(flowerbed, 1)
approved2 = can_place_flowers(flowerbed, 2)
print(approved)   # True
print(approved2)  # False

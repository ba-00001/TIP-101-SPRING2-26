"""
Week 2: Session 1
Problem Set Version 1 + Version 2 + Version 3
ALL problems + solutions + function calls.
UPI (Understand / Plan / Implement) is included as comments for each problem.
"""

# =========================================================
# Problem Set Version 1
# =========================================================

# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 1 (All In)
# Time Limit: 15 minutes
# Problem Importance:
# This is testing membership checking across two lists. In real life, it’s like “do we have all required permissions/items?”
# In interviews, it’s a clean way to show I understand loops + fast lookups.
#
# U — Understand
# 1) Do duplicates matter? Like if a has [1,1], does b need two 1s? (I’ll assume no—just “is it in b”.)
# 2) If a is empty, should it return True? (Usually yes—everything in an empty list is “already included”.)
#
# P — Plan
# Easiest: turn b into a set for fast checking, then loop through a and verify each item is in that set.
# Time: O(len(a) + len(b)) because I build the set once and scan a once.
# Space: O(len(b)) for the set.
#
# Pseudocode:
# - b_set = set(b)
# - for x in a:
#   - if x not in b_set: return False
# - return True
#
# I — Implement
# ---------------------------------------------------------
def all_in(a, b):
    b_set = set(b)
    for x in a:
        if x not in b_set:
            return False
    return True

lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))  # True
print(all_in(lst_2, lst_1))  # False


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 2 (Create a Dictionary)
# Time Limit: 15 minutes
# Problem Importance:
# This tests pairing two lists into a dictionary. That’s super common when you’re matching IDs to names, keys to values, etc.
#
# U — Understand
# 1) keys and values are the same length, right? (Yes, stated.)
# 2) If keys has duplicates, do we overwrite? (Python dict will overwrite; that’s fine.)
#
# P — Plan
# Loop over indices, set result[keys[i]] = values[i].
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - result = {}
# - for i in range(len(keys)):
#   - result[keys[i]] = values[i]
# - return result
#
# I — Implement
# ---------------------------------------------------------
def create_dictionary(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys, values))


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 3 (Print Pair)
# Time Limit: 10 minutes
# Problem Importance:
# This tests safe dictionary access. In real apps, missing keys happen all the time, so you can’t just crash.
#
# U — Understand
# 1) Print exactly two lines for an existing key: “Key: …” then “Value: …”? (Yes.)
# 2) If missing, print exactly “That pair does not exist!”? (Yes.)
#
# P — Plan
# Check if target in dictionary:
# - if yes, print key line + value line
# - else print missing message
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if target in dictionary:
#   - print "Key: target"
#   - print "Value: dictionary[target]"
# - else:
#   - print "That pair does not exist!"
#
# I — Implement
# ---------------------------------------------------------
def print_pair(dictionary, target):
    if target in dictionary:
        print("Key: " + str(target))
        print("Value: " + str(dictionary[target]))
    else:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 4 (Keys Versus Values)
# Time Limit: 15 minutes
# Problem Importance:
# This tests looping through dicts and tracking sums. That’s useful for analytics stuff and also shows I know .items().
#
# U — Understand
# 1) Keys and values are integers only? (Yes.)
# 2) If equal sums, return "balanced"? (Yes.)
#
# P — Plan
# Loop through key-value pairs, add keys to key_sum and values to value_sum.
# Compare and return the right string.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - key_sum = 0, value_sum = 0
# - for k, v in dictionary.items():
#   - key_sum += k
#   - value_sum += v
# - if key_sum > value_sum: return "keys"
# - elif value_sum > key_sum: return "values"
# - else: return "balanced"
#
# I — Implement
# ---------------------------------------------------------
def keys_v_values(dictionary):
    key_sum = 0
    value_sum = 0

    for k, v in dictionary.items():
        key_sum += k
        value_sum += v

    if key_sum > value_sum:
        return "keys"
    elif value_sum > key_sum:
        return "values"
    else:
        return "balanced"

dictionary1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(keys_v_values(dictionary1))  # values

dictionary2 = {100: 10, 200: 20, 300: 30, 400: 40, 500: 50, 600: 60}
print(keys_v_values(dictionary2))  # keys


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 5 (Restock Inventory)
# Time Limit: 20 minutes
# Problem Importance:
# This is basically “merge/update dictionaries” which is real-world inventory / configs / counts.
#
# U — Understand
# 1) If the item exists, we add quantities. If not, we create it. Correct? (Yes.)
# 2) We should modify and return current_inventory (same dict object), right? (That’s what it says.)
#
# P — Plan
# Loop through restock_list items:
# - if item in current_inventory: add the amount
# - else: set it to the amount
# Return current_inventory.
# Time: O(r) where r = number of restock items
# Space: O(1) extra
#
# Pseudocode:
# - for item, qty in restock_list.items():
#   - if item in current_inventory:
#       current_inventory[item] += qty
#     else:
#       current_inventory[item] = qty
# - return current_inventory
#
# I — Implement
# ---------------------------------------------------------
def restock_inventory(current_inventory, restock_list):
    for item, qty in restock_list.items():
        if item in current_inventory:
            current_inventory[item] += qty
        else:
            current_inventory[item] = qty
    return current_inventory

current_inventory = {"apples": 30, "bananas": 15, "oranges": 10}
restock_list = {"oranges": 20, "apples": 10, "pears": 5}
print(restock_inventory(current_inventory, restock_list))
# expected apples 40, bananas 15, oranges 30, pears 5


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 6 (Calculate GPA)
# Time Limit: 20 minutes
# Problem Importance:
# This tests mapping strings to numbers and averaging. That’s like a mini real-world “data transform + compute metric”.
#
# U — Understand
# 1) All grades are only A/B/C/D/F? (Assume yes.)
# 2) If report_card is empty, what do we do? (I’ll return 0.0 to avoid divide-by-zero.)
#
# P — Plan
# Create a grade_points dict, loop through report_card values, convert to points, sum them.
# Divide by number of courses and return.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - grade_points = {"A":4, "B":3, "C":2, "D":1, "F":0}
# - if report_card empty: return 0.0
# - total = 0
# - for course, grade in report_card.items():
#   - total += grade_points[grade]
# - return total / number_of_courses
#
# I — Implement
# ---------------------------------------------------------
def calculate_gpa(report_card):
    grade_points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

    if not report_card:
        return 0.0

    total = 0
    for grade in report_card.values():
        total += grade_points[grade]

    return total / len(report_card)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 7 (Best Book / Highest Rated)
# Time Limit: 20 minutes
# Problem Importance:
# This tests scanning a list of dictionaries and tracking a “best so far”.
# That’s super common in ranking problems (top score, max rating, best metric).
#
# U — Understand
# 1) Are we guaranteed at least one book? (Not stated—I'll handle empty list.)
# 2) If there’s a tie, return the first highest-rated one? (I’ll do first.)
#
# P — Plan
# If books empty -> return None.
# Set best = books[0], loop through books, if book["rating"] > best["rating"], update best.
# Return best.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - if not books: return None
# - best = books[0]
# - for book in books:
#   - if book["rating"] > best["rating"]:
#     - best = book
# - return best
#
# I — Implement
# ---------------------------------------------------------
def highest_rated(books):
    if not books:
        return None

    best = books[0]
    for book in books:
        if book["rating"] > best["rating"]:
            best = book
    return best

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow", "author": "Gabrielle Zevin", "rating": 4.18},
    {"title": "A Fortune For Your Disaster", "author": "Hanif Abdurraqib", "rating": 4.47},
    {"title": "The Seven Husbands of Evenlyn Hugo", "author": "Taylor Jenkins Reid", "rating": 4.40},
]
print(highest_rated(books))


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 8 (Index-Value Map)
# Time Limit: 15 minutes
# Problem Importance:
# This tests turning a list into a dictionary using indices. That’s useful for lookups and labeling data.
#
# U — Understand
# 1) Keys should be indices 0..n-1, values are the list values, right? (Yes.)
# 2) If list is empty, return {}? (Yes.)
#
# P — Plan
# Make dict result.
# Loop i over range(len(lst)):
# - result[i] = lst[i]
# Return result.
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - result = {}
# - for i in range(len(lst)):
#   - result[i] = lst[i]
# - return result
#
# I — Implement
# ---------------------------------------------------------
def index_to_value_map(lst):
    result = {}
    for i in range(len(lst)):
        result[i] = lst[i]
    return result

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))


# =========================================================
# Problem Set Version 2
# =========================================================

# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 1 (Is Monotonic)
# Time Limit: 20 minutes
# Problem Importance:
# This tests comparing neighbors in a list and checking a pattern across the whole list.
# Interviews love “walk through once and verify a rule”.
#
# U — Understand
# 1) Equal neighbors are allowed in both increasing and decreasing? (Yes, >= and <=.)
# 2) For lists of length 0 or 1, should it be True? (Yes, it’s automatically monotonic.)
#
# P — Plan
# Track two flags: inc = True, dec = True.
# Walk through pairs:
# - if nums[i] < nums[i-1] => not increasing
# - if nums[i] > nums[i-1] => not decreasing
# At the end, return inc or dec.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - if len(nums) <= 2: return True
# - inc = True, dec = True
# - for i from 1 to end:
#   - if nums[i] < nums[i-1]: inc = False
#   - if nums[i] > nums[i-1]: dec = False
# - return inc or dec
#
# I — Implement
# ---------------------------------------------------------
def is_monotonic(nums):
    if len(nums) <= 2:
        return True

    inc = True
    dec = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            inc = False
        if nums[i] > nums[i - 1]:
            dec = False

    return inc or dec

nums1 = [1, 2, 2, 3, 10]
print(is_monotonic(nums1))  # True
nums2 = [12, 9, 8, 3, 1]
print(is_monotonic(nums2))  # True
nums3 = [1, 1, 1]
print(is_monotonic(nums3))  # True
nums4 = [1, 9, 8, 3, 5]
print(is_monotonic(nums4))  # False


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 2 (Student Directory)
# Time Limit: 15 minutes
# Problem Importance:
# This tests building a dictionary with unique IDs. That’s like user IDs, row numbers, internal keys, etc.
#
# U — Understand
# 1) IDs start at 1 (not 0), right? (Example shows 1..n.)
# 2) Assume all names are unique? (Not required, but duplicates would overwrite in dict.)
#
# P — Plan
# Loop through list with index, assign name -> index+1.
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - directory = {}
# - for i in range(len(student_names)):
#   - directory[student_names[i]] = i + 1
# - return directory
#
# I — Implement
# ---------------------------------------------------------
def student_directory(student_names):
    directory = {}
    for i in range(len(student_names)):
        directory[student_names[i]] = i + 1
    return directory

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print(student_directory(student_names))


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 3 (Dictionary Description - fix bug)
# Time Limit: 15 minutes
# Problem Importance:
# This tests safe dictionary access. The bug is that info[key] crashes if key isn’t in the dictionary.
#
# U — Understand
# 1) If key doesn’t exist, print None (literally), right? (Yes.)
# 2) Should we print one line per key in the keys list? (Yes.)
#
# P — Plan
# Loop keys:
# - if key in info: print info[key]
# - else: print None
# Time: O(k)
# Space: O(1)
#
# Pseudocode:
# - for key in keys:
#   - if key in info:
#     - print info[key]
#   - else:
#     - print None
#
# I — Implement
# ---------------------------------------------------------
def get_description(info, keys):
    for key in keys:
        if key in info:
            print(info[key])
        else:
            print(None)

info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 4 (Sum Even Values)
# Time Limit: 15 minutes
# Problem Importance:
# This tests looping through dictionary values and filtering by even-ness.
#
# U — Understand
# 1) Only values matter, keys don’t? (Yes.)
# 2) Empty dictionary returns 0? (Makes sense.)
#
# P — Plan
# total = 0, loop values, if even add.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - total = 0
# - for v in dictionary.values():
#   - if v % 2 == 0: total += v
# - return total
#
# I — Implement
# ---------------------------------------------------------
def sum_even_values(dictionary):
    total = 0
    for v in dictionary.values():
        if v % 2 == 0:
            total += v
    return total

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8}
print(sum_even_values(dictionary))  # 14


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 5 (Merge Catalogs)
# Time Limit: 15 minutes
# Problem Importance:
# This is dictionary merging with overwrite rules. That’s super real-world (settings, pricing updates, syncing data).
#
# U — Understand
# 1) If catalog2 has a product, it should overwrite catalog1’s price? (Yes.)
# 2) Return the updated catalog1? (Yes.)
#
# P — Plan
# Loop catalog2 items, set catalog1[product] = price.
# Time: O(n2)
# Space: O(1) extra
#
# Pseudocode:
# - for product, price in catalog2.items():
#   - catalog1[product] = price
# - return catalog1
#
# I — Implement
# ---------------------------------------------------------
def merge_catalogs(catalog1, catalog2):
    for product, price in catalog2.items():
        catalog1[product] = price
    return catalog1

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 6 (Items to Restock)
# Time Limit: 15 minutes
# Problem Importance:
# This tests filtering dictionary items and returning a list of keys that match a condition.
#
# U — Understand
# 1) “Less than threshold” is strict (<), right? (Yes.)
# 2) If products is empty, return []? (Yes.)
#
# P — Plan
# result=[], loop items, if qty < threshold append product name.
# Time: O(n)
# Space: O(k)
#
# Pseudocode:
# - result = []
# - for name, qty in products.items():
#   - if qty < restock_threshold:
#     - result.append(name)
# - return result
#
# I — Implement
# ---------------------------------------------------------
def get_items_to_restock(products, restock_threshold):
    result = []
    for name, qty in products.items():
        if qty < restock_threshold:
            result.append(name)
    return result

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products, restock_threshold))  # ['Product2', 'Product4']


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 7 (Best Movie Genre)
# Time Limit: 25 minutes
# Problem Importance:
# This tests grouping + averaging. That’s like real analytics: aggregate per category and pick the best.
#
# U — Understand
# 1) Each movie dict has "genre" and "rating"? (Yes.)
# 2) Return the genre name (string), not the movie? (Yes.)
#
# P — Plan
# Use two dictionaries:
# - totals[genre] = sum of ratings
# - counts[genre] = number of movies
# Then compute average for each genre and track best.
# Time: O(n + g)
# Space: O(g)
#
# Pseudocode:
# - totals = {}, counts = {}
# - for movie in movies:
#   - g = movie["genre"]; r = movie["rating"]
#   - totals[g] += r (init to 0 if missing)
#   - counts[g] += 1 (init to 0 if missing)
# - best_genre = None, best_avg = -inf
# - for g in totals:
#   - avg = totals[g] / counts[g]
#   - if avg > best_avg: update
# - return best_genre
#
# I — Implement
# ---------------------------------------------------------
def most_popular_genre(movies):
    if not movies:
        return None

    totals = {}
    counts = {}

    for movie in movies:
        genre = movie["genre"]
        rating = movie["rating"]

        if genre not in totals:
            totals[genre] = 0
            counts[genre] = 0

        totals[genre] += rating
        counts[genre] += 1

    best_genre = None
    best_avg = float("-inf")

    for genre in totals:
        avg = totals[genre] / counts[genre]
        if avg > best_avg:
            best_avg = avg
            best_genre = genre

    return best_genre

movies = [
    {"title": "Inception", "genre": "Science Fiction", "rating": 8.8},
    {"title": "The Matrix", "genre": "Science Fiction", "rating": 8.7},
    {"title": "Pride and Prejudice", "genre": "Romance", "rating": 7.8},
    {"title": "Sense and Sensibility", "genre": "Romance", "rating": 7.7},
]
print(most_popular_genre(movies))  # Science Fiction


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 8 (Quality Control)
# Time Limit: 15 minutes
# Problem Importance:
# This is transforming one dictionary into another based on a rule. That’s very real-world (labeling, classification).
#
# U — Understand
# 1) threshold is pass if score >= threshold? (Yes.)
# 2) Return a new dictionary (don’t modify original)? (Yes.)
#
# P — Plan
# result = {}
# Loop through product_scores:
# - if score >= threshold: result[id] = "pass"
# - else: result[id] = "fail"
# Return result.
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - result = {}
# - for pid, score in product_scores.items():
#   - if score >= threshold: result[pid] = "pass"
#   - else: result[pid] = "fail"
# - return result
#
# I — Implement
# ---------------------------------------------------------
def quality_control(product_scores, threshold):
    result = {}
    for pid, score in product_scores.items():
        if score >= threshold:
            result[pid] = "pass"
        else:
            result[pid] = "fail"
    return result

product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60
print(quality_control(product_scores, threshold))


# =========================================================
# Problem Set Version 3
# =========================================================

# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 1 (Mountain Peak)
# Time Limit: 20 minutes
# Problem Importance:
# This tests finding the “peak index” in a mountain list. It’s a good intro to pattern checking in arrays.
#
# U — Understand
# 1) We assume the input is always a valid mountain list? (Sounds like yes.)
# 2) Return the index of the maximum element, not the value, right? (Yes.)
#
# P — Plan
# Simple approach: scan and track the best index so far.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - best_idx = 0
# - for i in range(len(lst)):
#   - if lst[i] > lst[best_idx]:
#     - best_idx = i
# - return best_idx
#
# I — Implement
# ---------------------------------------------------------
def peak_index_in_mountain_list(lst):
    if not lst:
        return None

    best_idx = 0
    for i in range(len(lst)):
        if lst[i] > lst[best_idx]:
            best_idx = i
    return best_idx

mountain_lst = [0, 3, 8, 0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)  # 2


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 2 (Build Inventory)
# Time Limit: 15 minutes
# Problem Importance:
# This is pairing two lists into a dictionary again, but with product names/prices (very realistic).
#
# U — Understand
# 1) Lists are same length? (Yes.)
# 2) Return dict mapping name -> price? (Yes.)
#
# P — Plan
# Loop indices and set inventory[name] = price.
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - inventory = {}
# - for i in range(len(product_names)):
#   - inventory[product_names[i]] = product_prices[i]
# - return inventory
#
# I — Implement
# ---------------------------------------------------------
def build_inventory(product_names, product_prices):
    inventory = {}
    for i in range(len(product_names)):
        inventory[product_names[i]] = product_prices[i]
    return inventory

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 3 (Update or Warn)
# Time Limit: 15 minutes
# Problem Importance:
# This tests conditional dictionary update without accidentally creating new keys.
# That’s like “only update existing records”.
#
# U — Understand
# 1) If item missing, print "<item> not found!" exactly? (Yes.)
# 2) If item exists, update and don’t print anything? (Seems yes.)
#
# P — Plan
# - if item in records: records[item] = update_value
# - else: print not found
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if item in records:
#   - records[item] = update_value
# - else:
#   - print f"{item} not found!"
#
# I — Implement
# ---------------------------------------------------------
def update_or_warn(records, item, update_value):
    if item in records:
        records[item] = update_value
    else:
        print(f"{item} not found!")

records = {"apple": 1, "banana": 2, "orange": 3}
update_or_warn(records, "grape", 4)
print(records)
update_or_warn(records, "banana", 5)
print(records)


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 4 (Attendance Rate)
# Time Limit: 15 minutes
# Problem Importance:
# This tests counting based on a value and then computing a percentage (super common in reporting/analytics).
#
# U — Understand
# 1) Status is exactly "Present" or "Absent"? (Assume yes.)
# 2) If attendance_list is empty, return 0.0? (I’ll do 0.0 to avoid divide-by-zero.)
#
# P — Plan
# Count total students and present students.
# Return (present / total) * 100.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - if not attendance_list: return 0.0
# - present = 0
# - total = 0
# - for status in attendance_list.values():
#   - total += 1
#   - if status == "Present": present += 1
# - return (present / total) * 100
#
# I — Implement
# ---------------------------------------------------------
def attendance_rate(attendance_list):
    if not attendance_list:
        return 0.0

    present = 0
    total = 0

    for status in attendance_list.values():
        total += 1
        if status == "Present":
            present += 1

    return (present / total) * 100

attendance_list = {"Bluey": "Present", "Bingo": "Absent", "Snickers": "Present", "Winton": "Absent"}
print(attendance_rate(attendance_list))  # 50.0


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 5 (Average Book Ratings)
# Time Limit: 25 minutes
# Problem Importance:
# This tests nested data: each book maps to a list of ratings. It’s like real analytics: average per category/item.
#
# U — Understand
# 1) Ratings list is non-empty for each book? (Assume yes, but I’ll handle empty safely.)
# 2) Return a new dictionary of averages? (Yes.)
#
# P — Plan
# For each book:
# - compute average = sum(ratings)/len(ratings) (if empty -> 0.0)
# Store in result dict.
# Time: O(total number of ratings across all books)
# Space: O(number of books)
#
# Pseudocode:
# - result = {}
# - for title, ratings in book_ratings.items():
#   - if ratings empty: result[title] = 0.0
#   - else:
#       total = sum of ratings
#       result[title] = total / len(ratings)
# - return result
#
# I — Implement
# ---------------------------------------------------------
def average_book_ratings(book_ratings):
    result = {}
    for title, ratings in book_ratings.items():
        if not ratings:
            result[title] = 0.0
        else:
            total = 0
            for r in ratings:
                total += r
            result[title] = total / len(ratings)
    return result

book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
print(average_book_ratings(book_ratings))


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 6 (Odd Keys Even Values)
# Time Limit: 15 minutes
# Problem Importance:
# This tests filtering by BOTH key and value conditions at the same time.
#
# U — Understand
# 1) Odd key means key % 2 != 0, even value means value % 2 == 0, right? (Yes.)
# 2) Return list of keys only? (Yes.)
#
# P — Plan
# Loop items:
# - if key odd and value even, append key.
# Time: O(n)
# Space: O(k)
#
# Pseudocode:
# - result = []
# - for k, v in dictionary.items():
#   - if k % 2 != 0 and v % 2 == 0:
#     - result.append(k)
# - return result
#
# I — Implement
# ---------------------------------------------------------
def odd_keys_even_values(dictionary):
    result = []
    for k, v in dictionary.items():
        if k % 2 != 0 and v % 2 == 0:
            result.append(k)
    return result

dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)  # [1, 5]


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 7 (Best Team)
# Time Limit: 30 minutes
# Problem Importance:
# This is grouping + averaging again, but with teams. It’s a realistic sports analytics pattern.
#
# U — Understand
# 1) Return the team name (string), not the whole dict? (Yes.)
# 2) Teams appear multiple times and we average across all their games? (Yes.)
#
# P — Plan
# Use totals and counts per team.
# Compute averages and keep the best.
# Time: O(n)
# Space: O(t) where t = number of teams
#
# Pseudocode:
# - totals = {}, counts = {}
# - for game in games:
#   - team = game["team_name"], score = game["score"]
#   - totals[team] += score, counts[team] += 1
# - best_team = None, best_avg = -inf
# - for team in totals:
#   - avg = totals[team] / counts[team]
#   - if avg > best_avg: update
# - return best_team
#
# I — Implement
# ---------------------------------------------------------
def team_with_best_average_score(games):
    if not games:
        return None

    totals = {}
    counts = {}

    for game in games:
        team = game["team_name"]
        score = game["score"]

        if team not in totals:
            totals[team] = 0
            counts[team] = 0

        totals[team] += score
        counts[team] += 1

    best_team = None
    best_avg = float("-inf")

    for team in totals:
        avg = totals[team] / counts[team]
        if avg > best_avg:
            best_avg = avg
            best_team = team

    return best_team

games = [
    {"team_name": "Lions", "score": 23},
    {"team_name": "Tigers", "score": 30},
    {"team_name": "Lions", "score": 27},
    {"team_name": "Bears", "score": 20},
    {"team_name": "Tigers", "score": 24},
    {"team_name": "Bears", "score": 22},
]
print(team_with_best_average_score(games))  # Tigers


# ---------------------------------------------------------
# Session: 1 (Week 2)
# Problem #: 8 (First Unique Items)
# Time Limit: 25 minutes
# Problem Importance:
# This tests set thinking and comparing two lists. Very common in “diff” problems and data cleaning.
#
# U — Understand
# 1) Output only includes items that are unique between the lists (appear in one but not the other)? (Yes from example.)
# 2) Value True means unique to first list, False means unique to second list? (Yes.)
#
# P — Plan
# Convert both lists to sets for fast membership checks.
# - items unique to A: in setA but not setB -> True
# - items unique to B: in setB but not setA -> False
# Return dict of those.
# Time: O(a + b)
# Space: O(a + b)
#
# Pseudocode:
# - setA = set(list_a), setB = set(list_b)
# - result = {}
# - for item in setA:
#   - if item not in setB: result[item] = True
# - for item in setB:
#   - if item not in setA: result[item] = False
# - return result
#
# I — Implement
# ---------------------------------------------------------
def find_unique_items(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)

    result = {}

    for item in set_a:
        if item not in set_b:
            result[item] = True

    for item in set_b:
        if item not in set_a:
            result[item] = False

    return result

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
print(find_unique_items(list_a, list_b))  # {"carrot": True, "date": False}


# =========================================================
# =========================================================
# Week 2
# Session # 2
# =========================================================
# =========================================================

"""
Week 2: Session 2
Problem Set Version 1 + Version 2 + Version 3
ALL problems + solutions + function calls.
UPI (Understand / Plan / Implement) is included as comments for each problem.
"""

# =========================================================
# Problem Set Version 1
# =========================================================

# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 1 (Cast Vote)
# Time Limit: 10 minutes
# Problem Importance:
# This is a basic “update counts in a dictionary” pattern. Real-world: votes, likes, inventory, scoreboards.
# Interview-wise, it shows I can safely update a dict whether the key exists or not.
#
# U — Understand
# 1) If candidate exists, increment by 1. If not, add with 1, right? (Yes.)
# 2) Should this modify the original votes dict? (Yes, and return it too.)
#
# P — Plan
# Check if candidate in votes:
# - if yes: votes[candidate] += 1
# - else: votes[candidate] = 1
# Return votes.
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if candidate in votes:
#     votes[candidate] += 1
#   else:
#     votes[candidate] = 1
# - return votes
#
# I — Implement
# ---------------------------------------------------------
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 2 (Keys in Common)
# Time Limit: 15 minutes
# Problem Importance:
# Finding shared keys is like comparing two datasets/configs. It’s a simple set-intersection idea.
# In interviews, it shows I know how to loop keys and check membership.
#
# U — Understand
# 1) Return the keys that exist in BOTH dicts, right? (Yes.)
# 2) Does order matter? Example shows ['b','c'] but I’ll keep dict1 iteration order.
#
# P — Plan
# Loop through dict1 keys, if key in dict2 append to result list.
# Time: O(n) (average constant-time membership in dict2)
# Space: O(k) for the output list
#
# Pseudocode:
# - result = []
# - for key in dict1:
#   - if key in dict2: append key
# - return result
#
# I — Implement
# ---------------------------------------------------------
def common_keys(dict1, dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
    return result

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)  # ['b', 'c']


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 3 (Frequency Count)
# Time Limit: 15 minutes
# Problem Importance:
# Frequency maps show up everywhere: counting duplicates, analytics, “most common element”, etc.
# Interviews LOVE this because it’s a core pattern for list problems.
#
# U — Understand
# 1) Keys are the numbers, values are counts, right? (Yes.)
# 2) Empty list returns empty dict? (Yes.)
#
# P — Plan
# Make counts dict. For each num:
# - if num exists: increment
# - else: set to 1
# Return counts.
# Time: O(n)
# Space: O(u) where u = number of unique numbers
#
# Pseudocode:
# - counts = {}
# - for num in nums:
#   - if num in counts: counts[num] += 1
#   - else: counts[num] = 1
# - return counts
#
# I — Implement
# ---------------------------------------------------------
def count_occurrences(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))  # {1: 1, 2: 2, 3: 3, 4: 1}


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 4 (Highest Priority Task)
# Time Limit: 25 minutes
# Problem Importance:
# This tests selecting the “best” item and removing it, which is like scheduling systems and task queues.
# Also tests tie-breaking rules (alphabetical) which interviews care about a lot.
#
# U — Understand
# 1) We remove the task from the dictionary and return its name, right? (Yes.)
# 2) If tasks is empty, what do we do? (Not stated—I'll return None.)
#
# P — Plan
# If empty -> None.
# Find max priority value.
# Collect tasks that have that max priority.
# Pick alphabetically smallest one (min()).
# Delete it from dict and return it.
# Time: O(n) each call (scan tasks)
# Space: O(k) for the tie list (small)
#
# Pseudocode:
# - if not tasks: return None
# - max_p = max(tasks.values())
# - candidates = []
# - for name, p in tasks.items():
#   - if p == max_p: candidates.append(name)
# - chosen = min(candidates)
# - delete tasks[chosen]
# - return chosen
#
# I — Implement
# ---------------------------------------------------------
def get_highest_priority_task(tasks):
    if not tasks:
        return None

    max_priority = max(tasks.values())

    candidates = []
    for name, p in tasks.items():
        if p == max_priority:
            candidates.append(name)

    chosen = min(candidates)  # alphabetical tie-break
    del tasks[chosen]
    return chosen

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = get_highest_priority_task(tasks)
print(perform_task)
perform_task = get_highest_priority_task(tasks)
print(perform_task)
perform_task = get_highest_priority_task(tasks)
print(perform_task)
print(tasks)


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 5 (Find Majority Element)
# Time Limit: 20 minutes
# Problem Importance:
# Majority element is a classic. It tests frequency counting and edge cases.
# Real-world: finding the most dominant signal/class in data.
#
# U — Understand
# 1) Majority means strictly more than n/2 times, right? (Yes.)
# 2) If no majority, return None? (Yes.)
#
# P — Plan
# Use a frequency map, then check if any count > len(elements)//2.
# Time: O(n)
# Space: O(u)
#
# Pseudocode:
# - counts = {}
# - for x in elements:
#   - counts[x] += 1 (with init)
# - threshold = len(elements) // 2
# - for x, c in counts.items():
#   - if c > threshold: return x
# - return None
#
# I — Implement
# ---------------------------------------------------------
def find_majority_element(elements):
    if not elements:
        return None

    counts = {}
    for x in elements:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    threshold = len(elements) // 2
    for x, c in counts.items():
        if c > threshold:
            return x

    return None

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))  # 2


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 6 (Has Duplicates Within K)
# Time Limit: 30 minutes
# Problem Importance:
# This is a “sliding window / nearby duplicate” problem. It’s common in interviews because it tests efficient thinking.
# Real-world: detecting repeated events close together (fraud, spam, sensor glitches).
#
# U — Understand
# 1) “Within k inclusive indices” means if the same value appears at i and j, check if abs(i-j) <= k? (Yes.)
# 2) If k >= len(nums), we just check if there are any duplicates at all? (Yes.)
#
# P — Plan
# Use a dictionary last_seen that stores the last index where we saw each value.
# Walk through nums with index i:
# - if value in last_seen and i - last_seen[value] <= k: return True
# - update last_seen[value] = i
# If finish, return False.
# Time: O(n)
# Space: O(u)
#
# Pseudocode:
# - last_seen = {}
# - for i in range(len(nums)):
#   - val = nums[i]
#   - if val in last_seen and i - last_seen[val] <= k: return True
#   - last_seen[val] = i
# - return False
#
# I — Implement
# ---------------------------------------------------------
def has_duplicates(nums, k):
    last_seen = {}

    for i in range(len(nums)):
        val = nums[i]
        if val in last_seen:
            if i - last_seen[val] <= k:
                return True
        last_seen[val] = i

    return False

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = has_duplicates(nums, 2)
print(check1)
check2 = has_duplicates(nums, 5)
print(check2)
check3 = has_duplicates(nums, 3)
print(check3)


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 7 (Make Pairs / Divide List)
# Time Limit: 20 minutes
# Problem Importance:
# This tests “can all elements be paired up perfectly?” which is a counting problem.
# Real-world: matching socks, pairing IDs, batching identical items.
#
# U — Understand
# 1) The list length is always even (2*n)? (Yes, stated.)
# 2) We can reorder the list however we want, right? Pairing doesn’t depend on original order. (Yes.)
#
# P — Plan
# Use frequency map. For each number, count it.
# If any count is odd, you can’t make perfect pairs -> False.
# Otherwise True.
# Time: O(n)
# Space: O(u)
#
# Pseudocode:
# - counts = {}
# - for x in nums:
#   - counts[x] += 1
# - for count in counts.values():
#   - if count % 2 != 0: return False
# - return True
#
# I — Implement
# ---------------------------------------------------------
def divide_list(nums):
    counts = {}
    for x in nums:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    for c in counts.values():
        if c % 2 != 0:
            return False

    return True

nums = [3, 2, 3, 2, 2, 2]
print(divide_list(nums))  # True
nums = [1, 2, 3, 4]
print(divide_list(nums))  # False


# =========================================================
# Problem Set Version 2
# =========================================================

# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 1 (Update Score)
# Time Limit: 10 minutes
# Problem Importance:
# Same pattern as voting/inventory: update a running total in a dictionary.
# Super common for scoreboards, points, stats tracking.
#
# U — Understand
# 1) If player exists, add points. If not, create player with points. (Yes.)
# 2) Function signature in prompt has a typo (players vs player). I’ll implement with player.
#
# P — Plan
# If player in scores: scores[player] += points else scores[player] = points.
# Return scores.
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if player in scores:
#     scores[player] += points
#   else:
#     scores[player] = points
# - return scores
#
# I — Implement
# ---------------------------------------------------------
def update_score(scores, player, points):
    if player in scores:
        scores[player] += points
    else:
        scores[player] = points
    return scores

scores = {"Alice": 100, "Bob": 90}
update_score(scores, "Alice", 10)
print(scores)
update_score(scores, "Calvin", 20)
print(scores)
update_score(scores, "Calvin", 5)
print(scores)


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 2 (Dictionary Intersection)
# Time Limit: 20 minutes
# Problem Importance:
# This tests matching key-value pairs exactly across two dictionaries.
# Real-world: syncing config values, verifying data matches between systems.
#
# U — Understand
# 1) Only include pairs where key exists in both AND values are equal? (Yes, based on example.)
# 2) Return a new dictionary? (Yes.)
#
# P — Plan
# Loop through d1 items:
# - if key in d2 and d2[key] == value: add to result
# Time: O(n)
# Space: O(k)
#
# Pseudocode:
# - result = {}
# - for k, v in d1.items():
#   - if k in d2 and d2[k] == v:
#     - result[k] = v
# - return result
#
# I — Implement
# ---------------------------------------------------------
def dict_intersection(d1, d2):
    result = {}
    for k, v in d1.items():
        if k in d2 and d2[k] == v:
            result[k] = v
    return result

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
print(dict_intersection(d1, d2))  # {'b': 2}


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 3 (Filter by Price / Remove Items Below Price)
# Time Limit: 25 minutes
# Problem Importance:
# This tests deleting from a dict safely and returning what was removed.
# Real-world: filtering products, cleaning datasets, applying thresholds.
#
# U — Understand
# 1) Remove items where value < threshold (strict), right? (Yes.)
# 2) If nothing removed, return None. Also dictionary should stay unchanged in that case. (Yes.)
#
# P — Plan
# We can’t delete while iterating directly over items view, so:
# - First collect keys to remove.
# - Then delete them.
# - If removed list is empty, return None.
# Time: O(n)
# Space: O(r) removed keys list
#
# Pseudocode:
# - to_remove = []
# - for name, price in items.items():
#   - if price < price_threshold:
#     - to_remove.append(name)
# - for name in to_remove:
#   - del items[name]
# - if to_remove empty: return None
# - return to_remove
#
# I — Implement
# ---------------------------------------------------------
def remove_items_below_price(items, price_threshold):
    to_remove = []

    for name, price in items.items():
        if price < price_threshold:
            to_remove.append(name)

    for name in to_remove:
        del items[name]

    if not to_remove:
        return None

    return to_remove

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)  # ["banana", "date"]
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)  # None


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 4 (Find Odd Occurrences)
# Time Limit: 25 minutes
# Problem Importance:
# This is a frequency-map problem with a twist: everything is even-count except two odd-count numbers.
# It’s good practice for “find the unique / unusual items” tasks.
#
# U — Understand
# 1) Exactly two numbers occur odd times, always? (Yes.)
# 2) Return them as a list (any order)? (Example shows [1,3], so order doesn’t seem strict.)
#
# P — Plan
# Count occurrences, then collect keys with odd counts.
# Time: O(n)
# Space: O(u)
#
# Pseudocode:
# - counts = {}
# - for x in numbers:
#   - counts[x] += 1
# - result = []
# - for x, c in counts.items():
#   - if c % 2 == 1: result.append(x)
# - return result
#
# I — Implement
# ---------------------------------------------------------
def find_odd_occurrences(numbers):
    counts = {}
    for x in numbers:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    result = []
    for x, c in counts.items():
        if c % 2 == 1:
            result.append(x)

    return result

numbers = [1, 4, 2, 3, 2, 3, 3, 4, 4, 4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)  # [1, 3] (order may vary)


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 5 (Find Mode)
# Time Limit: 25 minutes
# Problem Importance:
# Mode is a classic stats/counting problem. Tie-breaking by “first appearance” is a very interview-y detail.
#
# U — Understand
# 1) Return the value with the highest frequency, right? (Yes.)
# 2) If tie, return the one that appeared first in the original list. (Yes.)
#
# P — Plan
# Count frequencies, then scan the original list in order and keep the best:
# - best_val starts None, best_count = 0
# - for val in lst (in order):
#   - if counts[val] > best_count:
#       update best
# This tie rule works because we only update on strictly greater, not equal.
# Time: O(n)
# Space: O(u)
#
# Pseudocode:
# - counts = frequency map
# - best_val = None, best_count = 0
# - for val in lst:
#   - if counts[val] > best_count:
#     - best_count = counts[val]
#     - best_val = val
# - return best_val
#
# I — Implement
# ---------------------------------------------------------
def find_mode(lst):
    counts = {}
    for x in lst:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    best_val = None
    best_count = 0

    for x in lst:
        if counts[x] > best_count:
            best_count = counts[x]
            best_val = x

    return best_val

lst = [1, 2, 3, 2, 3, 3, 4, 4, 4, 4]
mode = find_mode(lst)
print(mode)  # 4


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 6 (How Many Smaller)
# Time Limit: 30 minutes
# Problem Importance:
# This tests comparing each element to others. Naive is O(n^2), but we can do better by sorting.
# Interview-wise, it’s about spotting a faster approach.
#
# U — Understand
# 1) For each nums[i], count how many nums[j] are smaller, excluding i? (Yes.)
# 2) Duplicates exist and should be handled correctly, right? (Yes.)
#
# P — Plan (efficient)
# Sort a copy of nums.
# Build a dict that maps each number to the first index it appears in the sorted list.
# That first index equals “how many numbers are smaller”.
# Then build answer by looking up each original number.
# Time: O(n log n) due to sorting
# Space: O(n)
#
# Pseudocode:
# - sorted_nums = sorted(nums)
# - first_index = {}
# - for i in range(len(sorted_nums)):
#   - if sorted_nums[i] not in first_index:
#       first_index[sorted_nums[i]] = i
# - result = []
# - for x in nums:
#   - result.append(first_index[x])
# - return result
#
# I — Implement
# ---------------------------------------------------------
def smaller_numbers_than_current(nums):
    sorted_nums = sorted(nums)

    first_index = {}
    for i in range(len(sorted_nums)):
        if sorted_nums[i] not in first_index:
            first_index[sorted_nums[i]] = i

    result = []
    for x in nums:
        result.append(first_index[x])

    return result

nums = [6, 1, 2, 2, 3]
print(smaller_numbers_than_current(nums))  # [4,0,1,1,3]


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 7 (Good Pairs)
# Time Limit: 25 minutes
# Problem Importance:
# This tests counting pairs efficiently. It’s a great example of using math + frequency instead of brute force.
#
# U — Understand
# 1) Good pair means i < j and nums[i] == nums[j], right? (Yes.)
# 2) Return just the count, not the pairs? (Yes.)
#
# P — Plan
# As I scan nums, keep a count dict.
# When I see a value x again, it forms new pairs with all previous x’s.
# So add counts[x] to answer, then increment counts[x].
# Time: O(n)
# Space: O(u)
#
# Pseudocode:
# - counts = {}
# - pairs = 0
# - for x in nums:
#   - if x in counts:
#     - pairs += counts[x]
#     - counts[x] += 1
#   - else:
#     - counts[x] = 1
# - return pairs
#
# I — Implement
# ---------------------------------------------------------
def num_identical_pairs(nums):
    counts = {}
    pairs = 0

    for x in nums:
        if x in counts:
            pairs += counts[x]
            counts[x] += 1
        else:
            counts[x] = 1

    return pairs

nums = [1, 2, 3, 1, 1, 3]
print(num_identical_pairs(nums))  # 4
nums = [1, 2, 3]
print(num_identical_pairs(nums))  # 0
nums = [1, 1, 1, 1]
print(num_identical_pairs(nums))  # 6


# =========================================================
# Problem Set Version 3
# =========================================================

# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 1 (Return Book)
# Time Limit: 10 minutes
# Problem Importance:
# Same exact pattern as votes/scores/inventory: increment if exists, otherwise create.
# This is like real library stock systems.
#
# U — Understand
# 1) Always add 1 copy for the given title? (Yes.)
# 2) Modify and return the same library dict? (Yes.)
#
# P — Plan
# If title in library: library[title] += 1 else library[title] = 1
# Return library.
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if title in library:
#   - library[title] += 1
# - else:
#   - library[title] = 1
# - return library
#
# I — Implement
# ---------------------------------------------------------
def return_book(title, library):
    if title in library:
        library[title] += 1
    else:
        library[title] = 1
    return library

library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 2 (Dictionary Difference)
# Time Limit: 20 minutes
# Problem Importance:
# This tests set-like difference but for dictionaries: keep only keys from first dict not in second.
# Real-world: finding what settings exist in one config but not another.
#
# U — Understand
# 1) Return pairs that are ONLY in the first dictionary by key (not checking values), right? (Yes.)
# 2) Return a new dict, don’t modify inputs? (Yes.)
#
# P — Plan
# Loop through d1 items:
# - if key not in d2: add to result
# Return result.
# Time: O(n1)
# Space: O(k)
#
# Pseudocode:
# - result = {}
# - for k, v in d1.items():
#   - if k not in d2:
#     - result[k] = v
# - return result
#
# I — Implement
# ---------------------------------------------------------
def dict_difference(d1, d2):
    result = {}
    for k, v in d1.items():
        if k not in d2:
            result[k] = v
    return result

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d1, d2))  # {'a': 1, 'c': 3}


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 3 (Take from Stock)
# Time Limit: 25 minutes
# Problem Importance:
# This tests real validation logic: missing item, not enough stock, otherwise decrement.
# Interviews like this because it’s “business rules + edge cases”.
#
# U — Understand
# 1) If item missing -> return "Item does not exist." exactly (with period)? (Yes.)
# 2) If quantity > stock -> return "Not enough stock."? (Yes.)
#
# P — Plan
# - if item not in items: return error string
# - if quantity > items[item]: return error string
# - else: items[item] -= quantity; return items
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if item_name not in items: return "Item does not exist."
# - if quantity > items[item_name]: return "Not enough stock."
# - items[item_name] -= quantity
# - return items
#
# I — Implement
# ---------------------------------------------------------
def pop_stock(items, item_name, quantity):
    if item_name not in items:
        return "Item does not exist."
    if quantity > items[item_name]:
        return "Not enough stock."

    items[item_name] -= quantity
    return items

items = {"chocolate": 20, "candy": 5, "chips": 10}

resultA = pop_stock(items, "candy", 2)
resultB = pop_stock(items, "candy", 5)
resultC = pop_stock(items, "lollipops", 5)
resultD = pop_stock(items, "chocolate", 5)

print(resultA)
print(resultB)
print(resultC)
print(resultD)


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 4 (Group By Frequency)
# Time Limit: 30 minutes
# Problem Importance:
# This tests a two-step frequency map: count first, then group by count.
# Real-world: grouping events/users/items by how often they show up.
#
# U — Understand
# 1) Output dict keys are frequencies (ints) and values are lists of elements with that frequency? (Yes.)
# 2) Order inside each list—does it matter? Example suggests a stable-ish order; I’ll keep the order of first appearance.
#
# P — Plan
# Step 1: count occurrences with a dict.
# Step 2: create a grouping dict:
# - for each unique item, freq = counts[item]
# - group[freq].append(item)
# To keep “nice” order, I’ll loop the original list and only add the item to the group the first time I see it.
# Time: O(n)
# Space: O(u)
#
# Pseudocode:
# - counts = {}
# - for x in lst:
#   - counts[x] += 1
# - grouped = {}
# - seen = set()
# - for x in lst:
#   - if x in seen: continue
#   - seen.add(x)
#   - freq = counts[x]
#   - if freq not in grouped: grouped[freq] = []
#   - grouped[freq].append(x)
# - return grouped
#
# I — Implement
# ---------------------------------------------------------
def group_by_frequency(lst):
    counts = {}
    for x in lst:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    grouped = {}
    seen = set()

    for x in lst:
        if x in seen:
            continue
        seen.add(x)

        freq = counts[x]
        if freq not in grouped:
            grouped[freq] = []
        grouped[freq].append(x)

    return grouped

lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))  # {1: ['a', 'b'], 2: ['c', 'd'], 3: ['e']}


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 5 (No Duplicates Allowed - keep last occurrence order)
# Time Limit: 30 minutes
# Problem Importance:
# This is a tricky “unique but keep the order of LAST occurrence” problem.
# Interviews like it because it’s a small twist on the normal “remove duplicates”.
#
# U — Understand
# 1) We keep only one copy of each number, but based on its last appearance? (Yes.)
# 2) Output order should match the order of those last occurrences from left to right? (Yes; example ends with ...8,3 because 3’s last is at the end.)
#
# P — Plan
# Easiest clean trick:
# - walk from right to left
# - keep a set of seen
# - if not seen, add to result
# Then reverse result at the end.
# Time: O(n)
# Space: O(u)
#
# Pseudocode:
# - seen = set()
# - result_reversed = []
# - for i from len(nums)-1 down to 0:
#   - x = nums[i]
#   - if x not in seen:
#       seen.add(x)
#       result_reversed.append(x)
# - reverse result_reversed
# - return it
#
# I — Implement
# ---------------------------------------------------------
def remove_duplicates_from_front(nums):
    seen = set()
    result_reversed = []

    for i in range(len(nums) - 1, -1, -1):
        x = nums[i]
        if x not in seen:
            seen.add(x)
            result_reversed.append(x)

    result_reversed.reverse()
    return result_reversed

nums = [6, 5, 3, 5, 2, 8, 3]
print(remove_duplicates_from_front(nums))  # [6, 5, 2, 8, 3]


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 6 (First Repeating Element - minimum index with a duplicate, single traversal)
# Time Limit: 35 minutes
# Problem Importance:
# This tests “single pass + tracking seen” and also returning the MIN index among repeating elements.
# It’s a good interview problem because the requirement (single traversal) forces a smart approach.
#
# U — Understand
# 1) We want the smallest index i such that nums[i] appears again somewhere later, right? (Yes.)
# 2) If no repeats, return None? (Yes.)
#
# P — Plan
# Single traversal approach:
# - Keep a dict first_index to remember where we first saw a number.
# - Keep best = None (the smallest repeating index we’ve found so far).
# When we see a number again:
# - its repeating “start” index is first_index[num]
# - update best = min(best, that first_index)
# At the end return best.
# Time: O(n)
# Space: O(u)
#
# Pseudocode:
# - first_index = {}
# - best = None
# - for i in range(len(nums)):
#   - x = nums[i]
#   - if x not in first_index:
#       first_index[x] = i
#     else:
#       if best is None or first_index[x] < best:
#         best = first_index[x]
# - return best
#
# I — Implement
# ---------------------------------------------------------
def find_min_index_of_repeating(nums):
    first_index = {}
    best = None

    for i in range(len(nums)):
        x = nums[i]
        if x not in first_index:
            first_index[x] = i
        else:
            if best is None or first_index[x] < best:
                best = first_index[x]

    return best

nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))   # 1
print(find_min_index_of_repeating(nums2))  # None
print(find_min_index_of_repeating(nums3))  # 3


# ---------------------------------------------------------
# Session: 2 (Week 2)
# Problem #: 7 (Target Sum / Two Sum)
# Time Limit: 30 minutes
# Problem Importance:
# Two-sum is a classic interview problem. The key is using a hashmap for fast lookup instead of brute force.
#
# U — Understand
# 1) Exactly one solution exists for each call? (Yes.)
# 2) Can’t use the same element twice, so indices must be different. (Yes.)
#
# P — Plan
# Use a dict seen that maps number -> its index.
# Walk through nums with i:
# - complement = target - nums[i]
# - if complement in seen: return [seen[complement], i]
# - else store nums[i]: i
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - seen = {}
# - for i in range(len(nums)):
#   - x = nums[i]
#   - comp = target - x
#   - if comp in seen:
#       return [seen[comp], i]
#   - seen[x] = i
#
# I — Implement
# ---------------------------------------------------------
def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        x = nums[i]
        comp = target - x

        if comp in seen:
            return [seen[comp], i]

        seen[x] = i

    return None  # shouldn't happen if guaranteed one solution

nums = [2, 7, 11, 15]
q_1 = two_sum(nums, 9)
q_2 = two_sum(nums, 18)

nums2 = [3, 3]
q_3 = two_sum(nums2, 6)

print(q_1)  # [0, 1]
print(q_2)  # [1, 2]
print(q_3)  # [0, 1]


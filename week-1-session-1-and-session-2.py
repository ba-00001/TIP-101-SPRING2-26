"""
Week 1:
Problem Set Version 1 + Version 2
ALL problems in one file.
UPI (Understand / Plan / Implement) is included as comments for each problem.
"""

# =========================================================
# Problem Set Version 1
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Hello World!)
# Time Limit: 5 minutes
# Problem Importance:
# This is testing if I know the basic order: define the function first, then call it.
# That matters because forgetting to call a function (or calling it before it exists) breaks code fast.
#
# U -- Understand
# 1) Do you want the print inside the function (so the function actually does something)?
# 2) Should it print exactly: Hello world! (same caps + punctuation)?
#
# P -- Plan
# I'll define hello_world(), put the print inside, then call it once.
# Time: O(1) because it prints once.
# Space: O(1) because it uses no extra memory.
#
# Pseudocode:
# - define hello_world():
#   - print "Hello world!"
# - call hello_world()
#
# I -- Implement
# ---------------------------------------------------------
def hello_world():
    print("Hello world!")


hello_world()


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Today's Mood)
# Time Limit: 5 minutes
# Problem Importance:
# This checks that I understand variables inside a function and that changing a variable changes output.
# In real coding, variables store everything (user input, settings, data), so this is a must.
#
# U -- Understand
# 1) Do we keep the variable name mood, or can I rename it? (I'll keep it.)
# 2) Should it match the format exactly: Today's mood: <emoji> ?
#
# P -- Plan
# I'll change mood to my emoji and call the function.
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - define todays_mood():
#   - mood = "my emoji"
#   - print "Today's mood: " + mood
# - call todays_mood()
#
# I -- Implement
# ---------------------------------------------------------
def todays_mood():
    mood = "🥱"  # change this to your mood
    print("Today's mood: " + mood)


todays_mood()


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Lunch Menu)
# Time Limit: 5 minutes
# Problem Importance:
# This tests parameters and passing an argument when calling a function.
# That's important because real code relies on inputs instead of hardcoding.
#
# U -- Understand
# 1) Should the function print or return? (It says print.)
# 2) Is menu always a string/emoji? (Assume yes.)
#
# P -- Plan
# I'll call print_menu("🍕") so it prints the example output.
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - define print_menu(menu):
#   - print "Lunch today is: " + menu
# - call print_menu("🍕")
#
# I -- Implement
# ---------------------------------------------------------
def print_menu(menu):
    print("Lunch today is: " + menu)


print_menu("🍕")


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Sum of Two Integers)
# Time Limit: 10 minutes
# Problem Importance:
# This tests reusing a function result and following constraints (no +, -, *, / outside sum()).
# Interviews love constraint rules like this.
#
# U -- Understand
# 1) "Double the calculated sum" means add it to itself using sum(), right? (Yes.)
# 2) Only print the final doubled result? (Yes.)
#
# P -- Plan
# - total = sum(13, 27)
# - doubled = sum(total, total)
# - print doubled
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - total = sum(13, 27)
# - doubled = sum(total, total)
# - print doubled
#
# I -- Implement
# ---------------------------------------------------------
def sum(a, b):
    return a + b


first_sum = sum(13, 27)
double_sum = sum(first_sum, first_sum)
print(double_sum)


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Product of Two Integers)
# Time Limit: 10 minutes
# Problem Importance:
# This checks if I can write a function that returns a value (not just prints).
# Returning is important because other code can use the result.
#
# U -- Understand
# 1) Return the product, not print it, correct? (Yes.)
# 2) Can a and b be negative/0? (It should still work.)
#
# P -- Plan
# Define product(a, b) and return a * b.
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - define product(a, b):
#   - return a * b
#
# I -- Implement
# ---------------------------------------------------------
def product(a, b):
    return a * b


print(product(22, 7))  # expected 154


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Classify Age)
# Time Limit: 10 minutes
# Problem Importance:
# This is basic conditionals. Real apps do this type of rule-checking constantly.
#
# U -- Understand
# 1) If age is exactly 18, should it be "adult"? (Yes, since < 18 is child.)
# 2) Do we assume age is a valid integer? (Yes.)
#
# P -- Plan
# If age < 18 return "child", else return "adult".
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if age < 18: return "child"
# - else: return "adult"
#
# I -- Implement
# ---------------------------------------------------------
def classify_age(age):
    if age < 18:
        return "child"
    return "adult"


output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)


# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (What time is it?)
# Time Limit: 10 minutes
# Problem Importance:
# This tests multiple condition branches + a default case. That's common in interviews and real logic.
#
# U -- Understand
# 1) Should the function return the string (not print it)? (Yes.)
# 2) Is hour always an int? (Assume yes.)
#
# P -- Plan
# - if hour == 2 return taco time
# - elif hour == 12 return pbj time
# - else return nap time
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if hour == 2: return "taco time 🌮"
# - elif hour == 12: return "peanut butter jelly time 🥪"
# - else: return "nap time 😴"
#
# I -- Implement
# ---------------------------------------------------------
def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
    if hour == 12:
        return "peanut butter jelly time 🥪"
    return "nap time 😴"


time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)


# ---------------------------------------------------------
# Session: 1
# Problem #: 8 (Blackjack)
# Time Limit: 15 minutes
# Problem Importance:
# This tests condition ordering. Checking the wrong order gives wrong outputs.
#
# U -- Understand
# 1) This function prints messages (doesn't return), correct? (Yes.)
# 2) Are scores integers? (Assume yes.)
#
# P -- Plan
# Check in this order:
# - score == 21 -> Blackjack!
# - score > 21 -> Bust!
# - 17 <= score < 21 -> Nice hand!
# - else -> Hit me!
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if score == 21: print "Blackjack!"
# - elif score > 21: print "Bust!"
# - elif score >= 17: print "Nice hand!"
# - else: print "Hit me!"
#
# I -- Implement
# ---------------------------------------------------------
def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17:
        print("Nice hand!")
    else:
        print("Hit me!")


blackjack(21)
blackjack(24)
blackjack(19)
blackjack(10)


# ---------------------------------------------------------
# Session: 1
# Problem #: 9 (First Item)
# Time Limit: 10 minutes
# Problem Importance:
# This checks list indexing and handling empty lists without crashing.
#
# U -- Understand
# 1) If the list is empty, return None exactly? (Yes.)
# 2) Can the list contain any type? (Yes, but indexing is the same.)
#
# P -- Plan
# - if list is empty: return None
# - else: return lst[0]
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if not lst: return None
# - return lst[0]
#
# I -- Implement
# ---------------------------------------------------------
def get_first(lst):
    if not lst:
        return None
    return lst[0]


print(get_first([3, 1, 6, 7, 5]))
print(get_first([]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 10 (Last Item)
# Time Limit: 10 minutes
# Problem Importance:
# Same idea as first item, but last item. Empty list is the main edge case.
#
# U -- Understand
# 1) Return None if empty, correct? (Yes.)
# 2) Using lst[-1] is allowed? (Yes.)
#
# P -- Plan
# - if empty: return None
# - else return lst[-1]
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if not lst: return None
# - return lst[-1]
#
# I -- Implement
# ---------------------------------------------------------
def get_last(lst):
    if not lst:
        return None
    return lst[-1]


print(get_last([3, 1, 6, 7, 5]))
print(get_last([]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 11 (Counter)
# Time Limit: 10 minutes
# Problem Importance:
# This tests basic for-loops with range and inclusive endpoints.
#
# U -- Understand
# 1) Should stop be included? (Yes, inclusive.)
# 2) Print one number per line? (Yes.)
#
# P -- Plan
# Use range(1, stop + 1) and print each number.
# Time: O(stop)
# Space: O(1)
#
# Pseudocode:
# - for i in range(1, stop+1):
#   - print i
#
# I -- Implement
# ---------------------------------------------------------
def counter(stop):
    for i in range(1, stop + 1):
        print(i)


counter(7)


# ---------------------------------------------------------
# Session: 1
# Problem #: 12 (Sum of 1 to 10)
# Time Limit: 10 minutes
# Problem Importance:
# This is the accumulator pattern (running total), which shows up in tons of interview problems.
#
# U -- Understand
# 1) Return the sum (don't print inside)? (Yes.)
# 2) Always 1..10, not variable? (Yes.)
#
# P -- Plan
# total=0; loop 1..10; add into total; return total.
# Time: O(1) (fixed 10 loops)
# Space: O(1)
#
# Pseudocode:
# - total = 0
# - for i in 1..10:
#   - total += i
# - return total
#
# I -- Implement
# ---------------------------------------------------------
def sum_ten():
    total = 0
    for i in range(1, 11):
        total += i
    return total


print(sum_ten())


# ---------------------------------------------------------
# Session: 1
# Problem #: 13 (Total Sum)
# Time Limit: 10 minutes
# Problem Importance:
# Same accumulator idea, but now it goes to a variable stop.
#
# U -- Understand
# 1) stop is inclusive? (Yes.)
# 2) stop is positive? (Assume yes.)
#
# P -- Plan
# total=0; loop 1..stop; add; return.
# Time: O(stop)
# Space: O(1)
#
# Pseudocode:
# - total = 0
# - for i in 1..stop:
#   - total += i
# - return total
#
# I -- Implement
# ---------------------------------------------------------
def sum_positive_range(stop):
    total = 0
    for i in range(1, stop + 1):
        total += i
    return total


print(sum_positive_range(6))


# ---------------------------------------------------------
# Session: 1
# Problem #: 14 (Total Sum in Range)
# Time Limit: 15 minutes
# Problem Importance:
# This tests correct use of range(start, stop+1) and avoiding off-by-one errors.
#
# U -- Understand
# 1) Inclusive on both ends? (Yes.)
# 2) Assume start <= stop? (Assume yes.)
#
# P -- Plan
# total=0; loop start..stop; add; return.
# Time: O(stop-start)
# Space: O(1)
#
# Pseudocode:
# - total = 0
# - for i in start..stop:
#   - total += i
# - return total
#
# I -- Implement
# ---------------------------------------------------------
def sum_range(start, stop):
    total = 0
    for i in range(start, stop + 1):
        total += i
    return total


print(sum_range(3, 9))


# ---------------------------------------------------------
# Session: 1
# Problem #: 15 (Negative Numbers)
# Time Limit: 15 minutes
# Problem Importance:
# This is filtering while looping. The only trick is what to do if none are negative.
#
# U -- Understand
# 1) If no negatives, do we print None (literally)? (Example shows None, so yes.)
# 2) Only printing is needed, no return? (Yes.)
#
# P -- Plan
# Loop through list, print negatives, track if we printed any.
# If we printed none, print None.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - found = False
# - for num in lst:
#   - if num < 0:
#     - print num
#     - found = True
# - if not found: print None
#
# I -- Implement
# ---------------------------------------------------------
def print_negatives(lst):
    found_negative = False
    for num in lst:
        if num < 0:
            print(num)
            found_negative = True
    if not found_negative:
        print(None)


print_negatives([3, -2, 2, 1, -5])
print_negatives([1, 2, 3, 4, 5])


# =========================================================
# Problem Set Version 2
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Hello User!)
# Time Limit: 5 minutes
# Problem Importance:
# This tests parameters + printing a message using the input.
#
# U -- Understand
# 1) Print (not return), correct? (Yes.)
# 2) name is a string? (Assume yes.)
#
# P -- Plan
# Print "Hello " + name.
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - define greet_user(name):
#   - print "Hello " + name
#
# I -- Implement
# ---------------------------------------------------------
def greet_user(name):
    print("Hello " + name)


greet_user("Michael")


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Calculate Difference)
# Time Limit: 10 minutes
# Problem Importance:
# This checks returning a value and correct subtraction order.
#
# U -- Understand
# 1) It's a - b, right? (Yes.)
# 2) Return the result, not print inside? (Yes.)
#
# P -- Plan
# Return a - b.
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - define difference(a, b):
#   - return a - b
#
# I -- Implement
# ---------------------------------------------------------
def difference(a, b):
    return a - b


print(difference(8, 3))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (List Concatenation)
# Time Limit: 15 minutes
# Problem Importance:
# This is a classic array/list construction pattern: build a new list that repeats content.
#
# U -- Understand
# 1) Return a new list, not modify original? (Yes.)
# 2) If nums is empty, return empty list? (Yes.)
#
# P -- Plan
# Return nums + nums.
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - return nums + nums
#
# I -- Implement
# ---------------------------------------------------------
def concatenate_list(nums):
    return nums + nums


print(concatenate_list([1, 2, 3, 4]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Sleep Assessment)
# Time Limit: 10 minutes
# Problem Importance:
# This tests correct conditional ranges (less than, between, greater than).
#
# U -- Understand
# 1) 8 and 10 are included in "good rest"? (Yes.)
# 2) Print only? (Yes.)
#
# P -- Plan
# - if < 8: oof
# - elif <= 10: good rest
# - else: prodigy
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if hours < 8: print msg1
# - elif hours <= 10: print msg2
# - else: print msg3
#
# I -- Implement
# ---------------------------------------------------------
def sleep_assessment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours <= 10:
        print("You got a good night's rest!")
    else:
        print("You're a sleep prodigy!")


sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Calculate Tip)
# Time Limit: 15 minutes
# Problem Importance:
# This tests mapping a string category to a numeric percent and returning the computed value.
#
# U -- Understand
# 1) service_quality is exactly "poor"/"average"/"excellent"? (Assume yes.)
# 2) Anything else returns None? (Yes.)
#
# P -- Plan
# Check service_quality and return bill * percent.
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if poor: return bill * 0.10
# - elif average: return bill * 0.15
# - elif excellent: return bill * 0.20
# - else: return None
#
# I -- Implement
# ---------------------------------------------------------
def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return bill * 0.10
    if service_quality == "average":
        return bill * 0.15
    if service_quality == "excellent":
        return bill * 0.20
    return None


print(calculate_tip(44.53, "average"))
print(calculate_tip(44.53, "poor"))
print(calculate_tip(44.53, "excellent"))
print(calculate_tip(44.53, "amazing"))  # None


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Rock, Paper, Scissors)
# Time Limit: 15 minutes
# Problem Importance:
# This tests translating rules into logic and handling ties cleanly.
#
# U -- Understand
# 1) Inputs are only rock/paper/scissors? (Assume yes.)
# 2) Print results (not return)? (Yes.)
#
# P -- Plan
# - if same: tie
# - elif player1 has a winning combo: player 1 wins
# - else: player 2 wins
# Time: O(1)
# Space: O(1)
#
# Pseudocode:
# - if p1 == p2: print tie
# - elif (p1 beats p2): print p1 wins
# - else: print p2 wins
#
# I -- Implement
# ---------------------------------------------------------
def rock_paper_scissors(player1, player2):
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or (
        player1 == "scissors" and player2 == "paper"
    ) or (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")


# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (Unscramble and Divide)
# Time Limit: 15 minutes
# Problem Importance:
# This tests function structure + looping + building a result list.
#
# U -- Understand
# 1) Return the list (not just print)? (Yes.)
# 2) Division uses / so results can be floats? (Yes.)
#
# P -- Plan
# Build result list by looping and appending number/2.
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - result = []
# - for number in lst:
#   - halved = number / 2
#   - append halved
# - return result
#
# I -- Implement
# ---------------------------------------------------------
def halve_lst(lst):
    result = []
    for number in lst:
        halved = number / 2
        result.append(halved)
    return result


print(halve_lst([2, 4, 6, 8]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 8 (Above the Threshold)
# Time Limit: 15 minutes
# Problem Importance:
# This is list filtering. Super common pattern in interviews (filter by condition).
#
# U -- Understand
# 1) Only keep numbers strictly greater than threshold? (Yes.)
# 2) Return a new list? (Yes.)
#
# P -- Plan
# Loop and append numbers > threshold into result.
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - result = []
# - for num in lst:
#   - if num > threshold: append num
# - return result
#
# I -- Implement
# ---------------------------------------------------------
def above_threshold(lst, threshold):
    result = []
    for num in lst:
        if num > threshold:
            result.append(num)
    return result


lst = [8, 2, 13, 11, 4, 10, 14]
print(above_threshold(lst, 10))


# ---------------------------------------------------------
# Session: 1
# Problem #: 9 (Countdown)
# Time Limit: 10 minutes
# Problem Importance:
# This tests reverse range usage without missing the endpoint.
#
# U -- Understand
# 1) Assume m >= n? (Yes.)
# 2) Print one per line? (Yes.)
#
# P -- Plan
# Use range(m, n-1, -1) and print each number.
# Time: O(m-n)
# Space: O(1)
#
# Pseudocode:
# - for i in range(m, n-1, -1):
#   - print i
#
# I -- Implement
# ---------------------------------------------------------
def countdown(m, n):
    for i in range(m, n - 1, -1):
        print(i)


countdown(5, 1)


# ---------------------------------------------------------
# Session: 1
# Problem #: 10 (Calculate Power)
# Time Limit: 15 minutes
# Problem Importance:
# This tests accumulator multiplication (repeat multiply), which is a standard loop skill.
#
# U -- Understand
# 1) exponent is non-negative? (Assume yes.)
# 2) If exponent is 0, return 1? (Yes.)
#
# P -- Plan
# Start result=1, multiply by base exponent times.
# Time: O(exponent)
# Space: O(1)
#
# Pseudocode:
# - result = 1
# - repeat exponent times:
#   - result *= base
# - return result
#
# I -- Implement
# ---------------------------------------------------------
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


print(power(2, 5))
print(power(3, 3))


# ---------------------------------------------------------
# Session: 1
# Problem #: 11 (Length of List) -- No len()
# Time Limit: 15 minutes
# Problem Importance:
# This checks that I understand what len() does: loop and count items.
#
# U -- Understand
# 1) No len() at all, correct? (Yes.)
# 2) Return the length, not print inside? (Yes.)
#
# P -- Plan
# Use a counter variable and add 1 per element.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - count = 0
# - for item in lst:
#   - count += 1
# - return count
#
# I -- Implement
# ---------------------------------------------------------
def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


print(list_length([2, 4, 6, 8, 10]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 12 (Calculate Factorial)
# Time Limit: 15 minutes
# Problem Importance:
# Factorial is a classic loop problem and checks if I handle repeated multiplication.
#
# U -- Understand
# 1) n is non-negative integer? (Assume yes.)
# 2) If n is 0, return 1? (Yes.)
#
# P -- Plan
# Multiply 1..n into result.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - result = 1
# - for i in 1..n:
#   - result *= i
# - return result
#
# I -- Implement
# ---------------------------------------------------------
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(3))


# ---------------------------------------------------------
# Session: 1
# Problem #: 13 (Calculate the Squares)
# Time Limit: 15 minutes
# Problem Importance:
# This is a "transform each element" pattern (map). Super common in data processing.
#
# U -- Understand
# 1) Return a new list of squares? (Yes.)
# 2) Input is integers? (Assume yes.)
#
# P -- Plan
# Loop through nums, append num*num to result, return it.
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - result = []
# - for num in nums:
#   - append num*num
# - return result
#
# I -- Implement
# ---------------------------------------------------------
def squares(nums):
    result = []
    for num in nums:
        result.append(num * num)
    return result


print(squares([1, 2, 3, 4]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 14 (Multiply List)
# Time Limit: 15 minutes
# Problem Importance:
# Another transform pattern, but now includes a parameter multiplier.
#
# U -- Understand
# 1) Return a new list? (Yes.)
# 2) multiplier can be any integer? (Assume yes.)
#
# P -- Plan
# Loop and append value*multiplier into result.
# Time: O(n)
# Space: O(n)
#
# Pseudocode:
# - result = []
# - for value in lst:
#   - append value * multiplier
# - return result
#
# I -- Implement
# ---------------------------------------------------------
def multiply_list(lst, multiplier):
    result = []
    for value in lst:
        result.append(value * multiplier)
    return result


print(multiply_list([1, 2, 3], 3))


# ---------------------------------------------------------
# Session: 1
# Problem #: 15 (Count Evens)
# Time Limit: 15 minutes
# Problem Importance:
# This tests modulus (%) and counting condition matches, a super common interview pattern.
#
# U -- Understand
# 1) Even means num % 2 == 0, correct? (Yes.)
# 2) Return the count, not print inside? (Yes.)
#
# P -- Plan
# Use count=0, loop list, if even increment count, return count.
# Time: O(n)
# Space: O(1)
#
# Pseudocode:
# - count = 0
# - for num in lst:
#   - if num % 2 == 0:
#     - count += 1
# - return count
#
# I -- Implement
# ---------------------------------------------------------
def count_evens(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


print(count_evens([1, 5, 7, 9]))
print(count_evens([2, 4, 6, 8]))

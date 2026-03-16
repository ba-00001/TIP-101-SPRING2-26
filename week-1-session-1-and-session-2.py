"""
Week 1:
Problem Set Version 1 + Version 2
All problems in one file with full UPI structure.
"""


# =========================================================
# Problem Set Version 1
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Hello World!)
# Time Limit: 5 minutes
# Problem Importance:
# This problem matters because it practices defining and calling a basic function in the correct order.
# U -- Understand
# 1) Should the function print the message directly instead of returning it?
# 2) Should the output match the exact capitalization and punctuation shown?
# P -- Plan
# I will define a function named hello_world() that prints the required message and then call it once.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define hello_world()
# - print "Hello world!"
# - call hello_world()
# I -- Implement
def hello_world():
    print("Hello world!")


hello_world()


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Today's Mood)
# Time Limit: 5 minutes
# Problem Importance:
# This problem matters because it introduces variables inside functions and shows how variable values affect output.
# U -- Understand
# 1) Should the mood be stored in a variable before printing?
# 2) Should the printed format start with exactly "Today's mood: "?
# P -- Plan
# I will store an emoji in a variable called mood and print it with the required label.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define todays_mood()
# - set mood to an emoji
# - print "Today's mood: " plus mood
# - call todays_mood()
# I -- Implement
def todays_mood():
    mood = "🥱"
    print("Today's mood: " + mood)


todays_mood()


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Lunch Menu)
# Time Limit: 5 minutes
# Problem Importance:
# This problem matters because it practices using parameters so a function can work with different inputs.
# U -- Understand
# 1) Should the function print the menu item instead of returning it?
# 2) Should the menu argument be passed in when the function is called?
# P -- Plan
# I will create a function with one parameter and print the sentence using that argument.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define print_menu(menu)
# - print "Lunch today is: " plus menu
# - call print_menu with "🍕"
# I -- Implement
def print_menu(menu):
    print("Lunch today is: " + menu)


print_menu("🍕")


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Sum of Two Integers)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices reusing a function result while following a specific rule about operations.
# U -- Understand
# 1) Should the first result be found by calling the helper function once with 13 and 27?
# 2) Should the doubled total be made by adding the first sum to itself through the same helper function?
# P -- Plan
# I will define a helper function that adds two numbers, use it to get the first total, then use it again to double that result.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define add_numbers(a, b)
# - return a + b
# - set first_sum to add_numbers(13, 27)
# - set double_sum to add_numbers(first_sum, first_sum)
# - print double_sum
# I -- Implement
def add_numbers(a, b):
    return a + b


first_sum = add_numbers(13, 27)
double_sum = add_numbers(first_sum, first_sum)
print(double_sum)


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Product of Two Integers)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices returning a value from a function so it can be used later.
# U -- Understand
# 1) Should the function return the product instead of printing it inside the function?
# 2) Should the example call show the returned result by printing it outside the function?
# P -- Plan
# I will write a function that multiplies two integers and returns the result, then print the sample output.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define product(a, b)
# - return a * b
# - print product(22, 7)
# I -- Implement
def product(a, b):
    return a * b


print(product(22, 7))


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Classify Age)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it introduces basic conditional logic used to sort inputs into categories.
# U -- Understand
# 1) Should age 18 be classified as "adult" because only values less than 18 are children?
# 2) Should the function return the category string instead of printing it directly?
# P -- Plan
# I will use an if statement to return "child" for ages under 18 and "adult" otherwise.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define classify_age(age)
# - if age < 18, return "child"
# - otherwise return "adult"
# - print function results for sample ages
# I -- Implement
def classify_age(age):
    if age < 18:
        return "child"
    return "adult"


print(classify_age(18))
print(classify_age(7))
print(classify_age(50))


# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (What time is it?)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices multiple condition checks and a default case in one function.
# U -- Understand
# 1) Should the function return a string message based on the hour?
# 2) Should any hour other than 2 or 12 return the nap message?
# P -- Plan
# I will use if, elif, and else to match the hour to the correct message.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define what_time_is_it(hour)
# - if hour is 2, return taco message
# - elif hour is 12, return peanut butter jelly message
# - else return nap message
# - print sample results
# I -- Implement
def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else:
        return "nap time 😴"


print(what_time_is_it(2))
print(what_time_is_it(7))
print(what_time_is_it(12))


# ---------------------------------------------------------
# Session: 1
# Problem #: 8 (Blackjack)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it shows how the order of conditions affects program correctness.
# U -- Understand
# 1) Should a score of exactly 21 print "Blackjack!" before any other check?
# 2) Should scores below 17 print "Hit me!" as the default case?
# P -- Plan
# I will check the score from most specific to most general so each score prints the correct message.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define blackjack(score)
# - if score == 21, print "Blackjack!"
# - elif score > 21, print "Bust!"
# - elif score >= 17, print "Nice hand!"
# - else print "Hit me!"
# - call function with sample scores
# I -- Implement
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
# This problem matters because it practices list indexing and handling empty lists safely.
# U -- Understand
# 1) Should the function return None when the list is empty?
# 2) Should the function return the element itself instead of printing it inside the function?
# P -- Plan
# I will first check if the list is empty and return None, otherwise return the first item.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define get_first(lst)
# - if lst is empty, return None
# - otherwise return lst[0]
# - print sample results
# I -- Implement
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
# This problem matters because it reinforces list indexing and empty-list edge cases.
# U -- Understand
# 1) Should the function return None when no last item exists?
# 2) Should the last element be returned using list indexing?
# P -- Plan
# I will check for an empty list first and then return the last item with negative indexing.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define get_last(lst)
# - if lst is empty, return None
# - otherwise return lst[-1]
# - print sample results
# I -- Implement
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
# This problem matters because it practices using loops and ranges to repeat an action a set number of times.
# U -- Understand
# 1) Should the numbers start at 1 and include the stop value?
# 2) Should each number be printed on its own line?
# P -- Plan
# I will loop from 1 through stop using range and print each number.
# Time Complexity: O(stop)
# Space Complexity: O(1)
# Pseudocode
# - define counter(stop)
# - loop from 1 to stop inclusive
# - print each number
# - call counter(7)
# I -- Implement
def counter(stop):
    for number in range(1, stop + 1):
        print(number)


counter(7)


# ---------------------------------------------------------
# Session: 1
# Problem #: 12 (Sum of 1 to 10)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it introduces the accumulator pattern for building a running total.
# U -- Understand
# 1) Should the function return the final sum instead of printing during the loop?
# 2) Should the loop always add the numbers from 1 through 10?
# P -- Plan
# I will create a total variable, add each number from 1 to 10, and return the result.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define sum_ten()
# - set total to 0
# - loop from 1 to 10 inclusive
# - add each number to total
# - return total
# - print the result
# I -- Implement
def sum_ten():
    total = 0
    for number in range(1, 11):
        total += number
    return total


print(sum_ten())


# ---------------------------------------------------------
# Session: 1
# Problem #: 13 (Total Sum)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it extends the running-total pattern to work with a variable stopping point.
# U -- Understand
# 1) Should the stop value be included in the total?
# 2) Should the function return the sum instead of printing inside the loop?
# P -- Plan
# I will use a loop from 1 to stop inclusive and add each number into a total variable.
# Time Complexity: O(stop)
# Space Complexity: O(1)
# Pseudocode
# - define sum_positive_range(stop)
# - set total to 0
# - loop from 1 to stop inclusive
# - add each number to total
# - return total
# - print sample result
# I -- Implement
def sum_positive_range(stop):
    total = 0
    for number in range(1, stop + 1):
        total += number
    return total


print(sum_positive_range(6))


# ---------------------------------------------------------
# Session: 1
# Problem #: 14 (Total Sum in Range)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it practices summing values across a start and stop range without off-by-one mistakes.
# U -- Understand
# 1) Should both start and stop be included in the total?
# 2) Can the function assume start is less than or equal to stop?
# P -- Plan
# I will loop from start to stop inclusive, add each value to a running total, and return it.
# Time Complexity: O(stop - start + 1)
# Space Complexity: O(1)
# Pseudocode
# - define sum_range(start, stop)
# - set total to 0
# - loop from start to stop inclusive
# - add each number to total
# - return total
# - print sample result
# I -- Implement
def sum_range(start, stop):
    total = 0
    for number in range(start, stop + 1):
        total += number
    return total


print(sum_range(3, 9))


# ---------------------------------------------------------
# Session: 1
# Problem #: 15 (Negative Numbers)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it practices filtering values in a list and handling the case where no matches exist.
# U -- Understand
# 1) Should only negative numbers be printed from the list?
# 2) Should the function print None if there are no negative numbers at all?
# P -- Plan
# I will loop through the list, print every negative value, and track whether any negative values were found.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pseudocode
# - define print_negatives(lst)
# - set found_negative to False
# - loop through each number in lst
# - if number is negative, print it and set found_negative to True
# - after loop, if found_negative is False, print None
# - call function with sample lists
# I -- Implement
def print_negatives(lst):
    found_negative = False
    for number in lst:
        if number < 0:
            print(number)
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
# This problem matters because it practices using a function parameter to personalize output.
# U -- Understand
# 1) Should the function print the greeting instead of returning it?
# 2) Should the name be inserted directly after the word "Hello"?
# P -- Plan
# I will define a function with one parameter and print the greeting using string concatenation.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define greet_user(name)
# - print "Hello " plus name
# - call greet_user("Michael")
# I -- Implement
def greet_user(name):
    print("Hello " + name)


greet_user("Michael")


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Calculate Difference)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices returning the result of arithmetic in the correct order.
# U -- Understand
# 1) Should the subtraction be a minus b in that exact order?
# 2) Should the function return the answer instead of printing it inside the function?
# P -- Plan
# I will return the result of subtracting the second number from the first, then print the sample call.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define difference(a, b)
# - return a - b
# - print difference(8, 3)
# I -- Implement
def difference(a, b):
    return a - b


print(difference(8, 3))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (List Concatenation)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it shows how to build a new list from existing list data.
# U -- Understand
# 1) Should the function return a new list instead of changing the original list?
# 2) Should the result contain the list items repeated twice in the same order?
# P -- Plan
# I will return the list added to itself so the elements appear two times.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pseudocode
# - define concatenate_list(nums)
# - return nums + nums
# - print sample result
# I -- Implement
def concatenate_list(nums):
    return nums + nums


print(concatenate_list([1, 2, 3, 4]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Sleep Assessment)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices checking number ranges with conditionals.
# U -- Understand
# 1) Should values from 8 through 10 print the good-rest message?
# 2) Should values greater than 10 print the sleep-prodigy message?
# P -- Plan
# I will use if, elif, and else to print the correct sentence based on the number of hours.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define sleep_assessment(hours)
# - if hours < 8, print first message
# - elif hours <= 10, print second message
# - else print third message
# - call function with sample values
# I -- Implement
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
# This problem matters because it practices mapping text categories to numeric calculations.
# U -- Understand
# 1) Should "poor", "average", and "excellent" map to fixed tip percentages?
# 2) Should any other service quality return None?
# P -- Plan
# I will check the service quality with conditionals and return the correct percentage of the bill.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define calculate_tip(bill, service_quality)
# - if quality is poor, return bill * 0.10
# - elif quality is average, return bill * 0.15
# - elif quality is excellent, return bill * 0.20
# - else return None
# - print sample results
# I -- Implement
def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return bill * 0.10
    elif service_quality == "average":
        return bill * 0.15
    elif service_quality == "excellent":
        return bill * 0.20
    else:
        return None


print(calculate_tip(44.53, "average"))
print(calculate_tip(44.53, "poor"))
print(calculate_tip(44.53, "excellent"))
print(calculate_tip(44.53, "amazing"))


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Rock, Paper, Scissors)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it practices translating game rules into clear conditional logic.
# U -- Understand
# 1) Should the function print a tie message when both players choose the same item?
# 2) Should the remaining cases be decided by the standard rock-paper-scissors rules?
# P -- Plan
# I will first check for a tie, then check the winning combinations for player 1, and otherwise player 2 wins.
# Time Complexity: O(1)
# Space Complexity: O(1)
# Pseudocode
# - define rock_paper_scissors(player1, player2)
# - if player1 equals player2, print tie message
# - elif player1 has a winning combination, print player 1 wins
# - else print player 2 wins
# - call function with sample rounds
# I -- Implement
def rock_paper_scissors(player1, player2):
    if player1 == player2:
        print("It's a tie!")
    elif (
        (player1 == "rock" and player2 == "scissors")
        or (player1 == "scissors" and player2 == "paper")
        or (player1 == "paper" and player2 == "rock")
    ):
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
# This problem matters because it practices looping through a list and building a new result list.
# U -- Understand
# 1) Should each number in the list be divided by 2?
# 2) Should the function return the new list instead of printing each value one by one?
# P -- Plan
# I will loop through the list, divide each number by 2, append it to a result list, and return the result.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pseudocode
# - define halve_lst(lst)
# - create empty result list
# - loop through each number in lst
# - divide number by 2 and append to result
# - return result
# - print sample result
# I -- Implement
def halve_lst(lst):
    result = []
    for number in lst:
        result.append(number / 2)
    return result


print(halve_lst([2, 4, 6, 8]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 8 (Above the Threshold)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it practices filtering list items based on a condition.
# U -- Understand
# 1) Should the result include only numbers strictly greater than the threshold?
# 2) Should the function return a new list instead of changing the original list?
# P -- Plan
# I will loop through the list, keep the numbers greater than the threshold, and return them in a new list.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pseudocode
# - define above_threshold(lst, threshold)
# - create empty result list
# - loop through each number in lst
# - if number > threshold, append it to result
# - return result
# - print sample result
# I -- Implement
def above_threshold(lst, threshold):
    result = []
    for number in lst:
        if number > threshold:
            result.append(number)
    return result


numbers = [8, 2, 13, 11, 4, 10, 14]
print(above_threshold(numbers, 10))


# ---------------------------------------------------------
# Session: 1
# Problem #: 9 (Countdown)
# Time Limit: 10 minutes
# Problem Importance:
# This problem matters because it practices looping backward through a range without skipping endpoints.
# U -- Understand
# 1) Should the function print from m down to n inclusive?
# 2) Can the function assume m is greater than or equal to n?
# P -- Plan
# I will use range with a step of -1 so the loop counts down from m to n.
# Time Complexity: O(m - n + 1)
# Space Complexity: O(1)
# Pseudocode
# - define countdown(m, n)
# - loop from m down to n inclusive
# - print each number
# - call countdown(5, 1)
# I -- Implement
def countdown(m, n):
    for number in range(m, n - 1, -1):
        print(number)


countdown(5, 1)


# ---------------------------------------------------------
# Session: 1
# Problem #: 10 (Calculate Power)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it practices repeated multiplication with a loop.
# U -- Understand
# 1) Should exponent 0 return 1?
# 2) Should the function multiply the base by itself exponent times?
# P -- Plan
# I will start with 1 and multiply by the base during a loop that runs exponent times.
# Time Complexity: O(exponent)
# Space Complexity: O(1)
# Pseudocode
# - define power(base, exponent)
# - set result to 1
# - repeat exponent times
# - multiply result by base
# - return result
# - print sample results
# I -- Implement
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
# This problem matters because it helps show how list length can be counted manually with a loop.
# U -- Understand
# 1) Should the function avoid using len() completely inside the solution?
# 2) Should the function return the count instead of printing during the loop?
# P -- Plan
# I will create a counter variable, add 1 for every item in the list, and return the final count.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pseudocode
# - define list_length(lst)
# - set count to 0
# - loop through each item in lst
# - add 1 to count
# - return count
# - print sample result
# I -- Implement
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
# This problem matters because factorial is a classic example of repeated multiplication in a loop.
# U -- Understand
# 1) Should factorial of 0 be 1?
# 2) Should the function multiply all integers from 1 through n?
# P -- Plan
# I will start with 1 and multiply it by each number from 1 to n inclusive.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pseudocode
# - define factorial(n)
# - set result to 1
# - loop from 1 to n inclusive
# - multiply result by the loop number
# - return result
# - print sample result
# I -- Implement
def factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result


print(factorial(3))


# ---------------------------------------------------------
# Session: 1
# Problem #: 13 (Calculate the Squares)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it practices transforming every item in a list into a new value.
# U -- Understand
# 1) Should the function return a new list of squared values?
# 2) Should each number be multiplied by itself?
# P -- Plan
# I will loop through the list, square each number, add it to a result list, and return that list.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pseudocode
# - define squares(nums)
# - create empty result list
# - loop through nums
# - append num * num to result
# - return result
# - print sample result
# I -- Implement
def squares(nums):
    result = []
    for number in nums:
        result.append(number * number)
    return result


print(squares([1, 2, 3, 4]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 14 (Multiply List)
# Time Limit: 15 minutes
# Problem Importance:
# This problem matters because it combines list transformation with a parameter that changes the calculation.
# U -- Understand
# 1) Should every list item be multiplied by the given multiplier?
# 2) Should the function return a new list instead of changing the original one?
# P -- Plan
# I will loop through the list, multiply each value by the multiplier, and store the results in a new list.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pseudocode
# - define multiply_list(lst, multiplier)
# - create empty result list
# - loop through each value in lst
# - append value * multiplier to result
# - return result
# - print sample result
# I -- Implement
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
# This problem matters because it practices counting how many items in a list meet a condition.
# U -- Understand
# 1) Should even numbers be identified with num % 2 == 0?
# 2) Should the function return the final count instead of printing while looping?
# P -- Plan
# I will loop through the list, increase a counter for each even number, and return the counter.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pseudocode
# - define count_evens(lst)
# - set count to 0
# - loop through each number in lst
# - if the number is even, add 1 to count
# - return count
# - print sample results
# I -- Implement
def count_evens(lst):
    count = 0
    for number in lst:
        if number % 2 == 0:
            count += 1
    return count


print(count_evens([1, 5, 7, 9]))
print(count_evens([2, 4, 6, 8]))

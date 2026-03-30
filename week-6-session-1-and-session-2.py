# =========================================================
# WEEK 6: SESSION 1 AND SESSION 2
# LINKED LISTS
# =========================================================


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def linked_list_to_string(head):
    values = []
    current = head
    steps = 0
    while current is not None and steps < 50:
        values.append(str(current.value))
        current = current.next
        steps += 1
    if current is not None:
        values.append("...")
    return " -> ".join(values)


def print_list(head):
    print(linked_list_to_string(head))


# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Nested Constructors)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it helps me practice building a whole linked list in one line.
#
# U -- Understand
# 1) Do I need to create the list 4 -> 3 -> 2 in one assignment? Yes.
# 2) Should the last node point to None automatically? Yes.
#
# P -- Plan
# I will use nested Node constructors so each node is created inside the previous one.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create a Node with value 4
# - make its next node 3
# - make that next node 2
#
# I -- Implement

head = Node(4, Node(3, Node(2)))

# Test Cases
print("V1 P1 Test 1:", linked_list_to_string(head))
second_head = Node(9, Node(8, Node(7)))
print("V1 P1 Test 2:", linked_list_to_string(second_head))


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Find Frequency)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because counting values in a linked list is a basic traversal skill.
#
# U -- Understand
# 1) Do I return how many times val appears in the list? Yes.
# 2) What should happen if the list is empty? Return 0.
#
# P -- Plan
# I will walk through the list one node at a time and count every match.
# Time Complexity: O(n), because I may visit every node once.
# Space Complexity: O(1), because I only use a few extra variables.
#
# Pseudocode
# - start count at 0
# - set current to head
# - while current exists
#   - if current value equals val, add 1 to count
#   - move current to next node
# - return count
#
# I -- Implement

def count_element(head, val):
    count = 0
    current = head

    while current is not None:
        if current.value == val:
            count += 1
        current = current.next

    return count


# Test Cases
freq_head = Node(3, Node(1, Node(2, Node(1))))
print("V1 P2 Test 1:", count_element(freq_head, 1))
print("V1 P2 Test 2:", count_element(freq_head, 3))
print("V1 P2 Test 3:", count_element(None, 5))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Remove Tail)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because fixing pointer bugs is a big part of working with linked lists.
#
# U -- Understand
# 1) What node should be removed? The last node in the list.
# 2) What was the bug? The loop went too far and landed on the tail instead of the second-to-last node.
#
# P -- Plan
# I will stop at the second-to-last node by checking current.next.next.
# Time Complexity: O(n), because I may travel through most of the list once.
# Space Complexity: O(1), because I only use one pointer variable.
#
# Pseudocode
# - if list is empty, return None
# - if list has one node, return None
# - move current until current.next.next is None
# - set current.next to None
# - return head
#
# I -- Implement

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None

    current = head
    while current.next.next is not None:
        current = current.next

    current.next = None
    return head


# Test Cases
tail_head = Node(1, Node(2, Node(3, Node(4))))
print("V1 P3 Test 1 - before:", linked_list_to_string(tail_head))
tail_head = remove_tail(tail_head)
print("V1 P3 Test 1 - after:", linked_list_to_string(tail_head))

single_node = Node(99)
print("V1 P3 Test 2 - before:", linked_list_to_string(single_node))
single_node = remove_tail(single_node)
print("V1 P3 Test 2 - after:", single_node)


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Find the Middle)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because slow and fast pointers are a super common linked list technique.
#
# U -- Understand
# 1) If there are two middle nodes, which one do I return? The second middle node.
# 2) What should happen if the list is empty? Return None.
#
# P -- Plan
# I will move slow one step and fast two steps. When fast reaches the end, slow will be at the middle.
# Time Complexity: O(n), because the list is scanned once.
# Space Complexity: O(1), because I only use two pointers.
#
# Pseudocode
# - set slow to head
# - set fast to head
# - while fast and fast.next exist
#   - move slow one step
#   - move fast two steps
# - return slow
#
# I -- Implement

def find_middle_element(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# Test Cases
middle_head_1 = Node(1, Node(2, Node(3)))
middle_node_1 = find_middle_element(middle_head_1)
print("V1 P4 Test 1:", middle_node_1.value if middle_node_1 else None)

middle_head_2 = Node(1, Node(2, Node(3, Node(4))))
middle_node_2 = find_middle_element(middle_head_2)
print("V1 P4 Test 2:", middle_node_2.value if middle_node_2 else None)


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Is Palindrome?)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it combines two pointers with list comparison logic.
#
# U -- Understand
# 1) Should I return True only when the values read the same forward and backward? Yes.
# 2) Is an empty list a palindrome? Yes.
#
# P -- Plan
# I will use slow and fast pointers to find the middle, store the second half values, reverse that value list, and compare.
# Time Complexity: O(n), because I move through the list a constant number of times.
# Space Complexity: O(n), because I store values from half of the list in a Python list.
#
# Pseudocode
# - find the middle using slow and fast
# - store values from the second half in a list
# - compare first half values with the reversed second half list
# - return True if all values match, otherwise False
#
# I -- Implement

def is_palindrome(head):
    if head is None:
        return True

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    second_half_values = []
    current = slow
    while current is not None:
        second_half_values.append(current.value)
        current = current.next

    current = head
    for value in reversed(second_half_values):
        if current.value != value:
            return False
        current = current.next

    return True


# Test Cases
pal_head_1 = Node(1, Node(2, Node(1)))
print("V1 P5 Test 1:", is_palindrome(pal_head_1))

pal_head_2 = Node(1, Node(2, Node(3)))
print("V1 P5 Test 2:", is_palindrome(pal_head_2))


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Put it in Reverse)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because reversing a linked list is one of the main pointer skills to learn.
#
# U -- Understand
# 1) Do I need to reverse the list in place? Yes.
# 2) What should I return? The new head of the reversed list.
#
# P -- Plan
# I will use previous, current, and next_node pointers to flip the arrows one by one.
# Time Complexity: O(n), because each node is visited once.
# Space Complexity: O(1), because I only use a few pointers.
#
# Pseudocode
# - set previous to None
# - set current to head
# - while current exists
#   - save current.next
#   - point current.next to previous
#   - move previous forward
#   - move current forward
# - return previous
#
# I -- Implement

def reverse(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


# Test Cases
reverse_head_1 = Node(1, Node(2, Node(3, Node(4))))
print("V1 P6 Test 1 - before:", linked_list_to_string(reverse_head_1))
reverse_head_1 = reverse(reverse_head_1)
print("V1 P6 Test 1 - after:", linked_list_to_string(reverse_head_1))

reverse_head_2 = Node(5)
print("V1 P6 Test 2 - before:", linked_list_to_string(reverse_head_2))
reverse_head_2 = reverse(reverse_head_2)
print("V1 P6 Test 2 - after:", linked_list_to_string(reverse_head_2))


# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (One to Many)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it helps me see how one nested line becomes separate linked steps.
#
# U -- Understand
# 1) Do I need one constructor call per line? Yes.
# 2) Should the final list still be Mario -> Luigi -> Wario? Yes.
#
# P -- Plan
# I will create the nodes from back to front so each node can point to the next one.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create Wario
# - create Luigi and point it to Wario
# - create Mario and point it to Luigi
#
# I -- Implement

wario = Node("Wario")
luigi = Node("Luigi", wario)
head = Node("Mario", luigi)

# Test Cases
print("V2 P1 Test 1:", linked_list_to_string(head))
print("V2 P1 Test 2:", head.value, head.next.value, head.next.next.value)


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Find Max)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because scanning for the largest value is a simple but important list pattern.
#
# U -- Understand
# 1) What should happen if the list is empty? I will return None.
# 2) Are the node values integers? Yes.
#
# P -- Plan
# I will keep track of the biggest value seen as I walk through the list.
# Time Complexity: O(n), because I check each node once.
# Space Complexity: O(1), because I only store one max value and one pointer.
#
# Pseudocode
# - if head is None, return None
# - set max_value to head.value
# - move through the list
#   - if current value is bigger, update max_value
# - return max_value
#
# I -- Implement

def find_max(head):
    if head is None:
        return None

    max_value = head.value
    current = head.next

    while current is not None:
        if current.value > max_value:
            max_value = current.value
        current = current.next

    return max_value


# Test Cases
max_head_1 = Node(5, Node(6, Node(7, Node(8))))
print("V2 P2 Test 1:", find_max(max_head_1))

max_head_2 = Node(-4, Node(-9, Node(-2)))
print("V2 P2 Test 2:", find_max(max_head_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Remove First Value)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because removing a node by value is a really common linked list task.
#
# U -- Understand
# 1) Should I remove only the first matching node? Yes.
# 2) What was the bug? The old loop skipped checking the final node in some cases.
#
# P -- Plan
# I will walk through the list while current exists, and reconnect previous.next when I find the value.
# Time Complexity: O(n), because I may look through the full list once.
# Space Complexity: O(1), because I only use pointers.
#
# Pseudocode
# - if list is empty, return head
# - if head matches, return head.next
# - set previous to head and current to head.next
# - while current exists
#   - if current matches, skip it and return head
#   - move both pointers forward
# - return head
#
# I -- Implement

def remove_by_value(head, val):
    if head is None:
        return head

    if head.value == val:
        return head.next

    previous = head
    current = head.next

    while current is not None:
        if current.value == val:
            previous.next = current.next
            return head
        previous = current
        current = current.next

    return head


# Test Cases
remove_value_head_1 = Node(1, Node(2, Node(3, Node(4))))
print("V2 P3 Test 1 - before:", linked_list_to_string(remove_value_head_1))
remove_value_head_1 = remove_by_value(remove_value_head_1, 3)
print("V2 P3 Test 1 - after:", linked_list_to_string(remove_value_head_1))

remove_value_head_2 = Node(7, Node(8, Node(9)))
print("V2 P3 Test 2 - before:", linked_list_to_string(remove_value_head_2))
remove_value_head_2 = remove_by_value(remove_value_head_2, 9)
print("V2 P3 Test 2 - after:", linked_list_to_string(remove_value_head_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Middle Match)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it builds more confidence using slow and fast pointers.
#
# U -- Understand
# 1) If the list has two middle nodes, which one should I check? The second middle node.
# 2) What should I return? True or False.
#
# P -- Plan
# I will find the middle with slow and fast pointers, then compare slow.value to val.
# Time Complexity: O(n), because I move through the list once.
# Space Complexity: O(1), because I only use pointers.
#
# Pseudocode
# - set slow and fast to head
# - move slow by one and fast by two
# - when loop ends, slow is at the middle
# - return whether slow value equals val
#
# I -- Implement

def middle_match(head, val):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    if slow is None:
        return False

    return slow.value == val


# Test Cases
middle_match_head_1 = Node(1, Node(2, Node(3)))
print("V2 P4 Test 1:", middle_match(middle_match_head_1, 2))

middle_match_head_2 = Node(1, Node(2, Node(3, Node(4))))
print("V2 P4 Test 2:", middle_match(middle_match_head_2, 2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Where Do We Begin?)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because finding the start of a cycle is a classic linked list interview problem.
#
# U -- Understand
# 1) What should I return if there is no cycle? None.
# 2) If there is a cycle, what should I return? The node where the cycle begins.
#
# P -- Plan
# I will first detect whether slow and fast meet. If they do, I will start one pointer at the head and move both one step at a time until they meet again at the loop start.
# Time Complexity: O(n), because each pointer only moves through the list a limited number of times.
# Space Complexity: O(1), because I only use pointers.
#
# Pseudocode
# - use slow and fast to detect a cycle
# - if they never meet, return None
# - set one pointer to head
# - move both pointers one step at a time
# - when they meet, return that node
#
# I -- Implement

def get_loop_start(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            finder = head
            while finder != slow:
                finder = finder.next
                slow = slow.next
            return finder

    return None


# Test Cases
loop_head_1 = Node(1)
loop_two = Node(2)
loop_three = Node(3)
loop_four = Node(4)
loop_head_1.next = loop_two
loop_two.next = loop_three
loop_three.next = loop_four
loop_four.next = loop_two
loop_start = get_loop_start(loop_head_1)
print("V2 P5 Test 1:", loop_start.value if loop_start else None)

loop_head_2 = Node(10, Node(20, Node(30)))
loop_start_2 = get_loop_start(loop_head_2)
print("V2 P5 Test 2:", loop_start_2)


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Was That a Crit?)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it helps me compare each node with its neighbors while traversing a list.
#
# U -- Understand
# 1) Can the head or tail be critical points? No.
# 2) What counts as critical? A local minimum or local maximum.
#
# P -- Plan
# I will look at triples of nodes: previous, current, and next. If current is bigger than both neighbors or smaller than both neighbors, I will count it.
# Time Complexity: O(n), because I scan the list once.
# Space Complexity: O(1), because I only use a few pointers and a counter.
#
# Pseudocode
# - if list is too short, return 0
# - set previous, current, and next pointers
# - while next exists
#   - check if current is local min or local max
#   - if yes, add 1
#   - move all pointers forward
# - return count
#
# I -- Implement

def count_critical_points(head):
    if head is None or head.next is None or head.next.next is None:
        return 0

    count = 0
    previous = head
    current = head.next

    while current.next is not None:
        next_node = current.next

        is_local_min = current.value < previous.value and current.value < next_node.value
        is_local_max = current.value > previous.value and current.value > next_node.value

        if is_local_min or is_local_max:
            count += 1

        previous = current
        current = next_node

    return count


# Test Cases
critical_head_1 = Node(1, Node(2, Node(3, Node(3, Node(3, Node(5, Node(1, Node(3))))))))
print("V2 P6 Test 1:", count_critical_points(critical_head_1))

critical_head_2 = Node(2, Node(1, Node(2, Node(1, Node(2)))))
print("V2 P6 Test 2:", count_critical_points(critical_head_2))


# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 3
# Problem #: 1 (The Power of One)
# Time Limit: 5 minutes
# Problem Importance:
# This matters because it gives me more practice turning separate nodes into one clean nested line.
#
# U -- Understand
# 1) What list do I need to recreate? Ash -> Misty -> Brock.
# 2) Is the original code buggy? Yes, because it uses luigi.next instead of misty.next.
#
# P -- Plan
# I will rebuild the whole list in one nested constructor statement.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create Ash
# - inside it create Misty
# - inside that create Brock
#
# I -- Implement

head = Node("Ash", Node("Misty", Node("Brock")))

# Test Cases
print("V3 P1 Test 1:", linked_list_to_string(head))
another_trainer_head = Node("Red", Node("Blue", Node("Green")))
print("V3 P1 Test 2:", linked_list_to_string(another_trainer_head))


# ---------------------------------------------------------
# Session: 3
# Problem #: 2 (Frequency Map)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it helps me track repeated values in a linked list using a dictionary.
#
# U -- Understand
# 1) What should the function return? A dictionary of value counts.
# 2) What if the list is empty? Return an empty dictionary.
#
# P -- Plan
# I will walk through the list and update a dictionary count for each value.
# Time Complexity: O(n), because I visit each node once.
# Space Complexity: O(n), because the dictionary may store many unique values.
#
# Pseudocode
# - make empty dictionary
# - move through list
# - add 1 to the current value count
# - return dictionary
#
# I -- Implement

def frequency_map(head):
    counts = {}
    current = head

    while current is not None:
        if current.value not in counts:
            counts[current.value] = 0
        counts[current.value] += 1
        current = current.next

    return counts


# Test Cases
map_head_1 = Node(1, Node(2, Node(3, Node(4, Node(2, Node(3))))))
print("V3 P2 Test 1:", frequency_map(map_head_1))

map_head_2 = Node("a", Node("b", Node("a")))
print("V3 P2 Test 2:", frequency_map(map_head_2))


# ---------------------------------------------------------
# Session: 3
# Problem #: 3 (Get it Out of Here!)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because pointer assignment bugs are easy to make and important to fix.
#
# U -- Understand
# 1) What was the bug? The code changed current itself instead of changing current.next.
# 2) Should I remove only the first matching node? Yes.
#
# P -- Plan
# I will walk through the list and when current.next matches the target, I will skip that node by reconnecting the pointer correctly.
# Time Complexity: O(n), because I may scan the whole list once.
# Space Complexity: O(1), because I only use one pointer.
#
# Pseudocode
# - if list is empty, return None
# - if head matches, return head.next
# - set current to head
# - while current.next exists
#   - if current.next matches value
#     - set current.next to current.next.next
#     - return head
#   - move current
# - return head
#
# I -- Implement

def remove_by_value(head, val):
    if head is None:
        return None

    if head.value == val:
        return head.next

    current = head

    while current.next is not None:
        if current.next.value == val:
            current.next = current.next.next
            return head
        current = current.next

    return head


# Test Cases
remove_bug_head_1 = Node(1, Node(2, Node(3, Node(4))))
print("V3 P3 Test 1 - before:", linked_list_to_string(remove_bug_head_1))
remove_bug_head_1 = remove_by_value(remove_bug_head_1, 3)
print("V3 P3 Test 1 - after:", linked_list_to_string(remove_bug_head_1))

remove_bug_head_2 = Node(4, Node(5, Node(6)))
print("V3 P3 Test 2 - before:", linked_list_to_string(remove_bug_head_2))
remove_bug_head_2 = remove_by_value(remove_bug_head_2, 4)
print("V3 P3 Test 2 - after:", linked_list_to_string(remove_bug_head_2))


# ---------------------------------------------------------
# Session: 3
# Problem #: 4 (Does it Cycle?)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because being able to detect a cycle prevents infinite traversal bugs.
#
# U -- Understand
# 1) What should I return if the list loops back on itself? True.
# 2) What should I return if it does not loop? False.
#
# P -- Plan
# I will use slow and fast pointers. If they ever meet, the list has a cycle.
# Time Complexity: O(n), because the pointers move through the list at most a limited number of times.
# Space Complexity: O(1), because I only use two pointers.
#
# Pseudocode
# - set slow and fast to head
# - while fast and fast.next exist
#   - move slow one step
#   - move fast two steps
#   - if they meet, return True
# - return False
#
# I -- Implement

def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Test Cases
cycle_head_1 = Node(1)
cycle_two = Node(2)
cycle_three = Node(3)
cycle_four = Node(4)
cycle_head_1.next = cycle_two
cycle_two.next = cycle_three
cycle_three.next = cycle_four
cycle_four.next = cycle_two
print("V3 P4 Test 1:", has_cycle(cycle_head_1))

cycle_head_2 = Node(1, Node(2, Node(3)))
print("V3 P4 Test 2:", has_cycle(cycle_head_2))


# ---------------------------------------------------------
# Session: 3
# Problem #: 5 (Are We There Yet?)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it goes one step further than cycle detection and measures the loop.
#
# U -- Understand
# 1) What should I return if there is no cycle? 0.
# 2) How do I count the cycle length? Once slow and fast meet, move one pointer around the loop until it comes back.
#
# P -- Plan
# I will first detect the cycle with slow and fast. If they meet, I will walk around the loop once and count the steps.
# Time Complexity: O(n), because cycle detection and counting are both linear.
# Space Complexity: O(1), because I only use pointers and a counter.
#
# Pseudocode
# - detect cycle with slow and fast
# - if no meeting point, return 0
# - set count to 1
# - move one pointer around the cycle until it returns
# - return count
#
# I -- Implement

def cycle_length(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1
            current = slow.next
            while current != slow:
                count += 1
                current = current.next
            return count

    return 0


# Test Cases
cycle_length_head = Node(1)
cycle_length_two = Node(2)
cycle_length_three = Node(3)
cycle_length_four = Node(4)
cycle_length_head.next = cycle_length_two
cycle_length_two.next = cycle_length_three
cycle_length_three.next = cycle_length_four
cycle_length_four.next = cycle_length_two
print("V3 P5 Test 1:", cycle_length(cycle_length_head))

no_cycle_length_head = Node(8, Node(9, Node(10)))
print("V3 P5 Test 2:", cycle_length(no_cycle_length_head))


# ---------------------------------------------------------
# Session: 3
# Problem #: 6 (Reverse Them, K?)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it mixes pointer reversal with reconnecting the rest of the list.
#
# U -- Understand
# 1) What part of the list do I reverse? The first k nodes.
# 2) What if k is bigger than the list length? Reverse the whole list.
#
# P -- Plan
# I will reverse up to k nodes using the normal linked list reverse pattern, then connect the old head to the remaining part.
# Time Complexity: O(min(n, k)), because I only reverse up to k nodes or the whole list.
# Space Complexity: O(1), because I only use pointer variables.
#
# Pseudocode
# - if list is empty or k is 1 or less, return head
# - set previous to None and current to head
# - repeat while current exists and count is less than k
#   - save next node
#   - reverse current pointer
#   - move pointers forward
# - connect old head to the remaining list
# - return new head
#
# I -- Implement

def reverse_first_k(head, k):
    if head is None or k <= 1:
        return head

    previous = None
    current = head
    count = 0

    while current is not None and count < k:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        count += 1

    head.next = current
    return previous


# Test Cases
reverse_k_head_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print("V3 P6 Test 1 - before:", linked_list_to_string(reverse_k_head_1))
reverse_k_head_1 = reverse_first_k(reverse_k_head_1, 3)
print("V3 P6 Test 1 - after:", linked_list_to_string(reverse_k_head_1))

reverse_k_head_2 = Node(1, Node(2, Node(3)))
print("V3 P6 Test 2 - before:", linked_list_to_string(reverse_k_head_2))
reverse_k_head_2 = reverse_first_k(reverse_k_head_2, 10)
print("V3 P6 Test 2 - after:", linked_list_to_string(reverse_k_head_2))

# =========================================================
# WEEK 6: SESSION 2 ADDITIONAL PRACTICE
# LINKED LISTS
# =========================================================


def circular_list_to_string(head, limit=12):
    if head is None:
        return ""

    values = []
    current = head
    steps = 0

    while current is not None and steps < limit:
        values.append(str(current.value))
        current = current.next
        steps += 1
        if current == head:
            values.append(str(current.value))
            break

    if steps == limit and current is not None and current != head:
        values.append("...")

    return " -> ".join(values)


def doubly_list_to_string(head):
    values = []
    current = head
    while current is not None:
        values.append(str(current.value))
        current = current.next
    return " <-> ".join(values)


# =========================================================
# SESSION 2 - PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Detect Circular Linked List)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it helps me tell the difference between a regular cycle and a true circular list.
#
# U -- Understand
# 1) What makes the list circular here? The tail must point back to the head exactly.
# 2) What if the list is empty? Return False.
#
# P -- Plan
# I will walk to the end of the list and check whether the last reachable node points back to the head.
# Time Complexity: O(n), because I may visit each node once.
# Space Complexity: O(1), because I only use one pointer.
#
# Pseudocode
# - if head is None, return False
# - set current to head
# - move through the list until next is None or next is head
# - return whether current.next is head
#
# I -- Implement

def is_circular(head):
    if head is None:
        return False

    current = head
    while current.next is not None and current.next != head:
        current = current.next

    return current.next == head


# Test Cases
c1 = Node("num1")
c2 = Node("num2")
c3 = Node("num3")
c1.next = c2
c2.next = c3
c3.next = c1
print("S2 V1 P1 Test 1:", is_circular(c1))

n1 = Node("var1", Node("var2", Node("var3")))
print("S2 V1 P1 Test 2:", is_circular(n1))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Find Last Node in a Linked List Cycle)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it helps me understand the shape of a cycle, not just whether one exists.
#
# U -- Understand
# 1) What node do I return? The node whose next pointer goes back to the start of the cycle.
# 2) What if there is no cycle? Return None.
#
# P -- Plan
# I will first find the cycle start using slow and fast pointers, then walk around the cycle until I find the node right before that start node.
# Time Complexity: O(n), because cycle detection and one loop around the cycle are both linear.
# Space Complexity: O(1), because I only use pointers.
#
# Pseudocode
# - detect a cycle with slow and fast
# - if no cycle, return None
# - find the cycle start
# - move a pointer around the cycle until pointer.next is the cycle start
# - return that pointer
#
# I -- Implement

def find_last_node_in_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            start = head
            while start != slow:
                start = start.next
                slow = slow.next

            current = start
            while current.next != start:
                current = current.next
            return current

    return None


# Test Cases
cycle_a = Node("num1")
cycle_b = Node("num2")
cycle_c = Node("num3")
cycle_d = Node("num4")
cycle_a.next = cycle_b
cycle_b.next = cycle_c
cycle_c.next = cycle_d
cycle_d.next = cycle_b
last_cycle_node = find_last_node_in_cycle(cycle_a)
print("S2 V1 P2 Test 1:", last_cycle_node.value if last_cycle_node else None)

plain_cycle_test = Node(1, Node(2, Node(3)))
print("S2 V1 P2 Test 2:", find_last_node_in_cycle(plain_cycle_test))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Partition List Around Value)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it shows how to rebuild a linked list based on a rule.
#
# U -- Understand
# 1) Where should values smaller than val go? Before values greater than or equal to val.
# 2) Do I need to keep the original relative order inside each group? It is nice to keep it, so I will.
#
# P -- Plan
# I will build two temporary lists, one for smaller values and one for bigger-or-equal values, then join them.
# Time Complexity: O(n), because I visit each node once.
# Space Complexity: O(1), because I only rearrange pointers and use a few helper nodes.
#
# Pseudocode
# - create dummy heads for small and large lists
# - walk through the original list
# - attach each node to the correct list
# - connect small list to large list
# - return the correct new head
#
# I -- Implement

def partition(head, val):
    small_dummy = Node(0)
    large_dummy = Node(0)
    small_tail = small_dummy
    large_tail = large_dummy
    current = head

    while current is not None:
        next_node = current.next
        current.next = None

        if current.value < val:
            small_tail.next = current
            small_tail = small_tail.next
        else:
            large_tail.next = current
            large_tail = large_tail.next

        current = next_node

    small_tail.next = large_dummy.next
    return small_dummy.next if small_dummy.next is not None else large_dummy.next


# Test Cases
partition_head_1 = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
print("S2 V1 P3 Test 1 - before:", linked_list_to_string(partition_head_1))
partition_head_1 = partition(partition_head_1, 3)
print("S2 V1 P3 Test 1 - after:", linked_list_to_string(partition_head_1))

partition_head_2 = Node(5, Node(1, Node(6, Node(2))))
print("S2 V1 P3 Test 2 - before:", linked_list_to_string(partition_head_2))
partition_head_2 = partition(partition_head_2, 4)
print("S2 V1 P3 Test 2 - after:", linked_list_to_string(partition_head_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Convert Binary Number in a Linked List to Integer)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it connects linked lists to a real number conversion idea.
#
# U -- Understand
# 1) What values can each node store? Only 0 or 1.
# 2) Is the leftmost bit at the head? Yes.
#
# P -- Plan
# I will keep updating the number by multiplying the current total by 2 and adding the new bit.
# Time Complexity: O(n), because I read each bit once.
# Space Complexity: O(1), because I only store the running total.
#
# Pseudocode
# - set total to 0
# - walk through the list
# - update total to total * 2 + current bit
# - return total
#
# I -- Implement

def binary_to_int(head):
    total = 0
    current = head

    while current is not None:
        total = total * 2 + current.value
        current = current.next

    return total


# Test Cases
binary_head_1 = Node(1, Node(0, Node(1)))
print("S2 V1 P4 Test 1:", binary_to_int(binary_head_1))

binary_head_2 = Node(1, Node(1, Node(1, Node(0))))
print("S2 V1 P4 Test 2:", binary_to_int(binary_head_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Add Two Numbers Represented by Linked Lists)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it mixes linked list traversal with carrying digits like regular addition.
#
# U -- Understand
# 1) Are the digits stored in reverse order? Yes.
# 2) What should I return? A new linked list for the sum.
#
# P -- Plan
# I will add matching digits from both lists plus a carry, make a new node for each result digit, and continue until everything is used.
# Time Complexity: O(max(n, m)), because I walk through both lists once.
# Space Complexity: O(max(n, m)), because I create a new answer list.
#
# Pseudocode
# - create dummy head
# - set carry to 0
# - while either list has nodes or carry exists
#   - get digit from each list or 0
#   - add them with carry
#   - create a node with ones digit
#   - update carry to tens digit
# - return dummy.next
#
# I -- Implement

def add_two_numbers(head_a, head_b):
    dummy = Node(0)
    tail = dummy
    carry = 0
    current_a = head_a
    current_b = head_b

    while current_a is not None or current_b is not None or carry > 0:
        value_a = current_a.value if current_a is not None else 0
        value_b = current_b.value if current_b is not None else 0

        total = value_a + value_b + carry
        carry = total // 10
        tail.next = Node(total % 10)
        tail = tail.next

        if current_a is not None:
            current_a = current_a.next
        if current_b is not None:
            current_b = current_b.next

    return dummy.next


# Test Cases
sum_a_1 = Node(2, Node(4, Node(3)))
sum_b_1 = Node(5, Node(6, Node(4)))
sum_result_1 = add_two_numbers(sum_a_1, sum_b_1)
print("S2 V1 P5 Test 1:", linked_list_to_string(sum_result_1))

sum_a_2 = Node(9, Node(9))
sum_b_2 = Node(1)
sum_result_2 = add_two_numbers(sum_a_2, sum_b_2)
print("S2 V1 P5 Test 2:", linked_list_to_string(sum_result_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Reverse Sublist of a Linked List)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it helps me reverse only one part of a list without touching the rest.
#
# U -- Understand
# 1) Are m and n using 1-based indexing? Yes.
# 2) What should happen if m equals n? The list stays the same.
#
# P -- Plan
# I will use a dummy node, walk to the node before position m, and then reverse the part from m to n by moving nodes to the front of that section.
# Time Complexity: O(n), because I only scan the list a constant number of times.
# Space Complexity: O(1), because I only rearrange pointers.
#
# Pseudocode
# - create dummy node before head
# - move previous to node before position m
# - set current to start of reversal section
# - repeat n - m times
#   - take next node out
#   - move it to front of the section
# - return dummy.next
#
# I -- Implement

def reverse_between(head, m, n):
    if head is None or m == n:
        return head

    dummy = Node(0, head)
    previous = dummy

    for _ in range(m - 1):
        previous = previous.next

    current = previous.next

    for _ in range(n - m):
        next_node = current.next
        current.next = next_node.next
        next_node.next = previous.next
        previous.next = next_node

    return dummy.next


# Test Cases
reverse_between_head_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print("S2 V1 P6 Test 1 - before:", linked_list_to_string(reverse_between_head_1))
reverse_between_head_1 = reverse_between(reverse_between_head_1, 2, 5)
print("S2 V1 P6 Test 1 - after:", linked_list_to_string(reverse_between_head_1))

reverse_between_head_2 = Node(1, Node(2, Node(3, Node(4))))
print("S2 V1 P6 Test 2 - before:", linked_list_to_string(reverse_between_head_2))
reverse_between_head_2 = reverse_between(reverse_between_head_2, 1, 3)
print("S2 V1 P6 Test 2 - after:", linked_list_to_string(reverse_between_head_2))

# =========================================================
# SESSION 2 - PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Convert a Singly Linked List to a Circular Linked List)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it helps me actively create a circular structure instead of only checking for one.
#
# U -- Understand
# 1) What should the tail point to after the change? Back to the head.
# 2) What if the list is empty? Return None.
#
# P -- Plan
# I will move to the tail and connect its next pointer back to the head.
# Time Complexity: O(n), because I need to find the tail.
# Space Complexity: O(1), because I only use one pointer.
#
# Pseudocode
# - if head is None, return None
# - move to the tail node
# - set tail.next to head
# - return head
#
# I -- Implement

def make_circular(head):
    if head is None:
        return None

    current = head
    while current.next is not None:
        current = current.next

    current.next = head
    return head


# Test Cases
make_circular_head_1 = Node("num1", Node("num2", Node("num3")))
make_circular(make_circular_head_1)
print("S2 V2 P1 Test 1:", is_circular(make_circular_head_1))
print("S2 V2 P1 Test 2:", circular_list_to_string(make_circular_head_1))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Collect Nodes of a Cycle in a Linked List)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it helps me pull out the exact repeating part of a linked list.
#
# U -- Understand
# 1) What should I return if there is no cycle? An empty list.
# 2) What should be in the result list? The values from the cycle nodes in order.
#
# P -- Plan
# I will find the cycle start with slow and fast pointers, then walk around the loop once and collect the values.
# Time Complexity: O(n), because I detect the cycle and then loop through it once.
# Space Complexity: O(c), because I store the cycle values in a Python list.
#
# Pseudocode
# - detect cycle with slow and fast
# - if no cycle, return []
# - find cycle start
# - collect values until I get back to the start
# - return the collected list
#
# I -- Implement

def collect_cycle_nodes(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            start = head
            while start != slow:
                start = start.next
                slow = slow.next

            values = []
            current = start
            while True:
                values.append(current.value)
                current = current.next
                if current == start:
                    break
            return values

    return []


# Test Cases
collect_a = Node("num1")
collect_b = Node("num2")
collect_c = Node("num3")
collect_d = Node("num4")
collect_a.next = collect_b
collect_b.next = collect_c
collect_c.next = collect_d
collect_d.next = collect_b
print("S2 V2 P2 Test 1:", collect_cycle_nodes(collect_a))

collect_plain = Node("var1", Node("var2", Node("var3", Node("var4"))))
print("S2 V2 P2 Test 2:", collect_cycle_nodes(collect_plain))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Delete Duplicates in a Linked List)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it helps me remove repeated values completely from a sorted list.
#
# U -- Understand
# 1) If a value appears more than once, do I keep one copy? No, I remove all copies of that value.
# 2) Is the list sorted? Yes, and that makes duplicates appear together.
#
# P -- Plan
# I will use a dummy head and skip every full block of duplicate values.
# Time Complexity: O(n), because I move through the list once.
# Space Complexity: O(1), because I only use pointer variables.
#
# Pseudocode
# - create dummy before head
# - use previous and current pointers
# - if current value repeats, skip the whole duplicate block
# - otherwise move previous forward
# - return dummy.next
#
# I -- Implement

def delete_dupes(head):
    dummy = Node(0, head)
    previous = dummy
    current = head

    while current is not None:
        has_duplicate = False

        while current.next is not None and current.value == current.next.value:
            has_duplicate = True
            current = current.next

        if has_duplicate:
            previous.next = current.next
        else:
            previous = previous.next

        current = current.next

    return dummy.next


# Test Cases
delete_dupes_head_1 = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
print("S2 V2 P3 Test 1 - before:", linked_list_to_string(delete_dupes_head_1))
delete_dupes_head_1 = delete_dupes(delete_dupes_head_1)
print("S2 V2 P3 Test 1 - after:", linked_list_to_string(delete_dupes_head_1))

delete_dupes_head_2 = Node(1, Node(1, Node(2, Node(2, Node(3, Node(4, Node(4)))))))
print("S2 V2 P3 Test 2 - before:", linked_list_to_string(delete_dupes_head_2))
delete_dupes_head_2 = delete_dupes(delete_dupes_head_2)
print("S2 V2 P3 Test 2 - after:", linked_list_to_string(delete_dupes_head_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Identical Linked Lists)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because comparing two linked lists is a basic and useful check.
#
# U -- Understand
# 1) When are two lists identical? When they have the same values in the same order.
# 2) What if one list is longer than the other? Return False.
#
# P -- Plan
# I will walk through both lists together and compare each pair of values.
# Time Complexity: O(n), because I compare nodes one by one.
# Space Complexity: O(1), because I only use two pointers.
#
# Pseudocode
# - walk through both lists at the same time
# - if values ever differ, return False
# - at the end, return True only if both lists ended together
#
# I -- Implement

def is_identical(head_a, head_b):
    current_a = head_a
    current_b = head_b

    while current_a is not None and current_b is not None:
        if current_a.value != current_b.value:
            return False
        current_a = current_a.next
        current_b = current_b.next

    return current_a is None and current_b is None


# Test Cases
identical_a_1 = Node(1, Node(2, Node(3, Node(4))))
identical_b_1 = Node(1, Node(2, Node(3, Node(4))))
print("S2 V2 P4 Test 1:", is_identical(identical_a_1, identical_b_1))

identical_a_2 = Node(1, Node(2, Node(3, Node(4))))
identical_b_2 = Node(1, Node(3, Node(4, Node(2))))
print("S2 V2 P4 Test 2:", is_identical(identical_a_2, identical_b_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Circular Linked List Rotate)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because rotating a list is a great pointer exercise.
#
# U -- Understand
# 1) What does rotate right by k mean? Move the last k nodes to the front.
# 2) What if k is bigger than the list length? I only need the remainder after dividing by the length.
#
# P -- Plan
# I will find the length and tail, connect the tail to head to make a temporary circle, then break the circle at the right spot.
# Time Complexity: O(n), because I walk through the list a constant number of times.
# Space Complexity: O(1), because I only use a few pointers.
#
# Pseudocode
# - if list is empty or has one node, return head
# - find the length and tail
# - reduce k with modulo length
# - make the list circular
# - move to the new tail
# - break the circle and return new head
#
# I -- Implement

def rotate_right(head, k):
    if head is None or head.next is None or k == 0:
        return head

    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    tail.next = head
    steps_to_new_tail = length - k - 1
    new_tail = head

    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head


# Test Cases
rotate_head_1 = Node("num1", Node("num2", Node("num3", Node("num4", Node("num5")))))
print("S2 V2 P5 Test 1 - before:", linked_list_to_string(rotate_head_1))
rotate_head_1 = rotate_right(rotate_head_1, 2)
print("S2 V2 P5 Test 1 - after:", linked_list_to_string(rotate_head_1))

rotate_head_2 = Node("num1", Node("num2", Node("num3")))
print("S2 V2 P5 Test 2 - before:", linked_list_to_string(rotate_head_2))
rotate_head_2 = rotate_right(rotate_head_2, 4)
print("S2 V2 P5 Test 2 - after:", linked_list_to_string(rotate_head_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Circular Linked List Delete)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because deleting from a circular list has extra edge cases around the head.
#
# U -- Understand
# 1) What if the node to delete is the head? I need to move the head and also fix the tail link.
# 2) What if the list has one node and it matches? Return None.
#
# P -- Plan
# I will handle head deletion first, then walk around the circular list to find and remove the first matching node.
# Time Complexity: O(n), because I may scan the whole circle once.
# Space Complexity: O(1), because I only use pointers.
#
# Pseudocode
# - if head is None, return None
# - if head matches, handle one-node case or move head and fix tail
# - otherwise walk around until next node matches or I return to head
# - if found, skip that node
# - return head
#
# I -- Implement

def delete_node(head, val):
    if head is None:
        return None

    if head.value == val:
        if head.next == head:
            return None

        tail = head
        while tail.next != head:
            tail = tail.next

        new_head = head.next
        tail.next = new_head
        return new_head

    current = head
    while current.next != head:
        if current.next.value == val:
            current.next = current.next.next
            return head
        current = current.next

    return head


# Test Cases
cd1 = Node(1)
cd2 = Node(2)
cd3 = Node(3)
cd1.next = cd2
cd2.next = cd3
cd3.next = cd1
print("S2 V2 P6 Test 1 - before:", circular_list_to_string(cd1))
cd_head = delete_node(cd1, 2)
print("S2 V2 P6 Test 1 - after:", circular_list_to_string(cd_head))

cd4 = Node(1)
cd5 = Node(2)
cd6 = Node(3)
cd4.next = cd5
cd5.next = cd6
cd6.next = cd4
print("S2 V2 P6 Test 2 - before:", circular_list_to_string(cd4))
cd_head_2 = delete_node(cd4, 1)
print("S2 V2 P6 Test 2 - after:", circular_list_to_string(cd_head_2))

# =========================================================
# SESSION 2 - PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Circular List Length)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because counting in a circular list needs a careful stopping rule.
#
# U -- Understand
# 1) When do I stop counting? When I get back to the head.
# 2) What if the list is empty? Return 0.
#
# P -- Plan
# I will start at the head, count one node at a time, and stop when I return to the head again.
# Time Complexity: O(n), because I visit each node once.
# Space Complexity: O(1), because I only use a counter and pointer.
#
# Pseudocode
# - if head is None, return 0
# - set count to 1
# - move current to head.next
# - while current is not head
#   - add 1 to count
#   - move current
# - return count
#
# I -- Implement

def circular_list_length(head):
    if head is None:
        return 0

    count = 1
    current = head.next

    while current != head:
        count += 1
        current = current.next

    return count


# Test Cases
cl1 = Node(1)
cl2 = Node(2)
cl3 = Node(3)
cl1.next = cl2
cl2.next = cl3
cl3.next = cl1
print("S2 V3 P1 Test 1:", circular_list_length(cl1))

single_circular = Node(9)
single_circular.next = single_circular
print("S2 V3 P1 Test 2:", circular_list_length(single_circular))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Detect and Remove Cycle in a Linked List)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it helps me safely turn a broken looping list back into a normal one.
#
# U -- Understand
# 1) What should happen if there is no cycle? Return the list unchanged.
# 2) How do I remove the cycle? Find the last node in the cycle and set its next to None.
#
# P -- Plan
# I will detect the cycle, find the cycle start, find the node right before that start inside the cycle, and cut the link.
# Time Complexity: O(n), because detection and cleanup are linear.
# Space Complexity: O(1), because I only use pointers.
#
# Pseudocode
# - detect cycle with slow and fast
# - if no cycle, return head
# - find cycle start
# - move around the cycle to the node before the start
# - set that node.next to None
# - return head
#
# I -- Implement

def detect_and_remove_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            start = head
            while start != slow:
                start = start.next
                slow = slow.next

            last = start
            while last.next != start:
                last = last.next

            last.next = None
            return head

    return head


# Test Cases
remove_cycle_1 = Node(1)
remove_cycle_2 = Node(2)
remove_cycle_3 = Node(3)
remove_cycle_1.next = remove_cycle_2
remove_cycle_2.next = remove_cycle_3
remove_cycle_3.next = remove_cycle_1
print("S2 V3 P2 Test 1 - before has cycle:", has_cycle(remove_cycle_1))
detect_and_remove_cycle(remove_cycle_1)
print("S2 V3 P2 Test 1 - after has cycle:", has_cycle(remove_cycle_1))
print("S2 V3 P2 Test 1 - list:", linked_list_to_string(remove_cycle_1))

remove_cycle_plain = Node(7, Node(8, Node(9)))
detect_and_remove_cycle(remove_cycle_plain)
print("S2 V3 P2 Test 2:", linked_list_to_string(remove_cycle_plain))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Merge Two Sorted Linked Lists)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because merging sorted lists is a classic linked list pattern.
#
# U -- Understand
# 1) Are both input lists already sorted? Yes.
# 2) Do I make new nodes? No, I can reuse and splice the existing nodes.
#
# P -- Plan
# I will use a dummy head and keep attaching the smaller front node from either list until one list runs out.
# Time Complexity: O(n + m), because I visit each node once.
# Space Complexity: O(1), because I only rearrange pointers.
#
# Pseudocode
# - create dummy head
# - while both lists have nodes
#   - attach the smaller node
# - attach the remaining nodes
# - return dummy.next
#
# I -- Implement

def merge_two_lists(head_a, head_b):
    dummy = Node(0)
    tail = dummy
    current_a = head_a
    current_b = head_b

    while current_a is not None and current_b is not None:
        if current_a.value <= current_b.value:
            tail.next = current_a
            current_a = current_a.next
        else:
            tail.next = current_b
            current_b = current_b.next
        tail = tail.next

    if current_a is not None:
        tail.next = current_a
    else:
        tail.next = current_b

    return dummy.next


# Test Cases
merge_a_1 = Node(1, Node(2, Node(4)))
merge_b_1 = Node(2, Node(3, Node(4)))
merge_result_1 = merge_two_lists(merge_a_1, merge_b_1)
print("S2 V3 P3 Test 1:", linked_list_to_string(merge_result_1))

merge_a_2 = Node(1, Node(5))
merge_b_2 = Node(2, Node(3, Node(6)))
merge_result_2 = merge_two_lists(merge_a_2, merge_b_2)
print("S2 V3 P3 Test 2:", linked_list_to_string(merge_result_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Skip and Remove Nodes in a Linked List)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it helps me practice repeating pointer patterns across a full list.
#
# U -- Understand
# 1) What do I do first in each cycle? Keep the first m nodes.
# 2) What do I do next? Delete the next n nodes.
#
# P -- Plan
# I will move through the list in chunks: keep m nodes, skip over n nodes, then reconnect and continue.
# Time Complexity: O(n), because I move through the list once.
# Space Complexity: O(1), because I only use pointers.
#
# Pseudocode
# - if head is None or m is 0, handle those cases
# - keep m nodes
# - delete next n nodes by moving a pointer forward
# - connect the kept part to the remaining list
# - repeat until the list ends
#
# I -- Implement

def skip_and_remove(head, m, n):
    if head is None:
        return None
    if m <= 0:
        return None

    current = head

    while current is not None:
        for _ in range(1, m):
            if current is None:
                return head
            current = current.next

        if current is None:
            return head

        delete_current = current.next
        for _ in range(n):
            if delete_current is None:
                break
            delete_current = delete_current.next

        current.next = delete_current
        current = delete_current

    return head


# Test Cases
skip_head_1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))
print("S2 V3 P4 Test 1 - before:", linked_list_to_string(skip_head_1))
skip_head_1 = skip_and_remove(skip_head_1, 2, 3)
print("S2 V3 P4 Test 1 - after:", linked_list_to_string(skip_head_1))

skip_head_2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print("S2 V3 P4 Test 2 - before:", linked_list_to_string(skip_head_2))
skip_head_2 = skip_and_remove(skip_head_2, 1, 1)
print("S2 V3 P4 Test 2 - after:", linked_list_to_string(skip_head_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Rotate a Doubly Linked List to the Left)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it helps me work with both next and prev pointers together.
#
# U -- Understand
# 1) What does rotate left by k mean? Move the first k nodes to the end.
# 2) What if k is larger than the list length? Use k % length.
#
# P -- Plan
# I will find the length and tail, connect head and tail temporarily, walk to the new head, then break the links in the right place.
# Time Complexity: O(n), because I walk through the list a constant number of times.
# Space Complexity: O(1), because I only use pointer variables.
#
# Pseudocode
# - if list is empty or one node, return head
# - find length and tail
# - reduce k with modulo
# - if k is 0, return head
# - connect tail to head both ways
# - move to the new head after k steps
# - cut the circle and return new head
#
# I -- Implement

class DNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


def rotate_doubly_linked_list(head, k):
    if head is None or head.next is None or k == 0:
        return head

    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    tail.next = head
    head.prev = tail

    new_head = head
    for _ in range(k):
        new_head = new_head.next

    new_tail = new_head.prev
    new_tail.next = None
    new_head.prev = None

    return new_head


# Test Cases
d1 = DNode(1)
d2 = DNode(2)
d3 = DNode(3)
d4 = DNode(4)
d5 = DNode(5)
d1.next = d2
d2.prev = d1
d2.next = d3
d3.prev = d2
d3.next = d4
d4.prev = d3
d4.next = d5
d5.prev = d4
print("S2 V3 P5 Test 1 - before:", doubly_list_to_string(d1))
rotated_d_head_1 = rotate_doubly_linked_list(d1, 2)
print("S2 V3 P5 Test 1 - after:", doubly_list_to_string(rotated_d_head_1))

d6 = DNode(0)
d7 = DNode(1)
d8 = DNode(2)
d6.next = d7
d7.prev = d6
d7.next = d8
d8.prev = d7
print("S2 V3 P5 Test 2 - before:", doubly_list_to_string(d6))
rotated_d_head_2 = rotate_doubly_linked_list(d6, 4)
print("S2 V3 P5 Test 2 - after:", doubly_list_to_string(rotated_d_head_2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Merge Nodes Between Zeros in a Linked List)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it helps me group parts of a linked list and combine them into cleaner results.
#
# U -- Understand
# 1) What do the zero nodes do? They separate groups of values.
# 2) Should zeros appear in the final list? No.
#
# P -- Plan
# I will walk through the list, keep a running sum between zeros, and create one new node for each finished group.
# Time Complexity: O(n), because I visit each node once.
# Space Complexity: O(g), because I create one result node per group.
#
# Pseudocode
# - skip the first zero
# - keep a running sum
# - when I hit a zero, add a node with that sum if needed and reset sum
# - return the built result list
#
# I -- Implement

def merge_nodes(head):
    dummy = Node(0)
    tail = dummy
    current = head.next
    running_sum = 0

    while current is not None:
        if current.value == 0:
            tail.next = Node(running_sum)
            tail = tail.next
            running_sum = 0
        else:
            running_sum += current.value
        current = current.next

    return dummy.next


# Test Cases
merge_zero_head_1 = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(2, Node(0))))))))
print("S2 V3 P6 Test 1 - before:", linked_list_to_string(merge_zero_head_1))
merge_zero_result_1 = merge_nodes(merge_zero_head_1)
print("S2 V3 P6 Test 1 - after:", linked_list_to_string(merge_zero_result_1))

merge_zero_head_2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))
print("S2 V3 P6 Test 2 - before:", linked_list_to_string(merge_zero_head_2))
merge_zero_result_2 = merge_nodes(merge_zero_head_2)
print("S2 V3 P6 Test 2 - after:", linked_list_to_string(merge_zero_result_2))




from collections import defaultdict, deque
from math import gcd

# =========================================================
# WEEK 10: SESSION 1 AND SESSION 2
# =========================================================


def print_section(title):
    print('\n' + '=' * 72)
    print(title)
    print('=' * 72)


def sll_to_string(head):
    parts = []
    current = head
    while current:
        parts.append(str(getattr(current, 'value', getattr(current, 'val', None))))
        current = current.next
    return ' -> '.join(parts) if parts else 'EMPTY'


def circular_to_list(start_node, count):
    if start_node is None:
        return []
    result = []
    current = start_node
    for _ in range(count):
        result.append(current.val)
        current = current.next
    return result


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.value = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_values(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# =========================================================
# WEEK 10: SESSION 1
# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Valid Parentheses)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because stacks are a core pattern for matching structure in strings.
#
# U -- Understand
# 1) What makes the string valid? Every opener closes in the right order with the right symbol.
# 2) What if a closing bracket appears too early? Return False.
#
# P -- Plan
# I will use a stack of opening brackets and match each closing bracket with the top of the stack.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - push open brackets onto stack
# - for close brackets check top of stack
# - return True only if stack ends empty
#
# I -- Implement

def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

# Test Cases
print_section('Session 1 - Version 1 - Problem 1')
print(is_valid('()'))
print(is_valid('()[]{}'))
print(is_valid('([)]'))


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Best Time to Buy & Sell Stock)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it teaches a clean one-pass optimization pattern.
#
# U -- Understand
# 1) Can I sell before I buy? No.
# 2) What if no profit is possible? Return 0.
#
# P -- Plan
# I will track the cheapest price so far and the best profit I can make at each step.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - keep smallest price seen
# - update best profit with current price minus smallest
#
# I -- Implement

def max_profit(prices):
    smallest = float('inf')
    best = 0
    for price in prices:
        smallest = min(smallest, price)
        best = max(best, price - smallest)
    return best

# Test Cases
print_section('Session 1 - Version 1 - Problem 2')
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Shuffle Merge)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it combines pointer updates across two linked lists.
#
# U -- Understand
# 1) How should nodes be merged? Alternate between the two lists.
# 2) What if one list ends first? Append the rest of the other list.
#
# P -- Plan
# I will walk through both lists, connect nodes one by one in alternating order, and then attach leftovers.
# Time Complexity: O(n + m)
# Space Complexity: O(1)
#
# Pseudocode
# - use a dummy head
# - alternate nodes from list A and B
# - attach remaining nodes at the end
#
# I -- Implement

def shuffle_merge(head_a, head_b):
    dummy = Node(0)
    tail = dummy
    take_a = True
    while head_a and head_b:
        if take_a:
            tail.next = head_a
            head_a = head_a.next
        else:
            tail.next = head_b
            head_b = head_b.next
        tail = tail.next
        take_a = not take_a
    tail.next = head_a if head_a else head_b
    return dummy.next

# Test Cases
print_section('Session 1 - Version 1 - Problem 3')
list_a = Node(1, Node(2, Node(3)))
list_b = Node(4, Node(5, Node(6)))
print(sll_to_string(shuffle_merge(list_a, list_b)))
list_c = Node(1, Node(2, Node(3)))
list_d = Node(4)
print(sll_to_string(shuffle_merge(list_c, list_d)))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Group Anagrams)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because hashing grouped by a normalized key is a common interview idea.
#
# U -- Understand
# 1) What makes two strings anagrams? They use the same letters with the same counts.
# 2) Can the groups come back in any order? Yes.
#
# P -- Plan
# I will sort each word to build a key and group matching keys in a dictionary.
# Time Complexity: O(n * k log k)
# Space Complexity: O(nk)
#
# Pseudocode
# - for each string sort it for a key
# - append string into dictionary[key]
# - return dictionary values
#
# I -- Implement

def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        groups[''.join(sorted(word))].append(word)
    return list(groups.values())

# Test Cases
print_section('Session 1 - Version 1 - Problem 4')
print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
print(group_anagrams(['']))
print(group_anagrams(['a']))


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Sum Root to Leaf Numbers)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it combines path building with DFS on a binary tree.
#
# U -- Understand
# 1) What number does a path make? Concatenate the digits from root to leaf.
# 2) What should happen at a leaf? Add the completed number into the total.
#
# P -- Plan
# I will carry the current number down the tree by multiplying by 10 and adding the next digit.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - build running number while traversing
# - when leaf is reached return that number
# - sum left and right answers
#
# I -- Implement

def sum_numbers(root):
    def dfs(node, current):
        if node is None:
            return 0
        current = current * 10 + node.val
        if node.left is None and node.right is None:
            return current
        return dfs(node.left, current) + dfs(node.right, current)

    return dfs(root, 0)

# Test Cases
print_section('Session 1 - Version 1 - Problem 5')
print(sum_numbers(TreeNode(1, TreeNode(2), TreeNode(3))))
print(sum_numbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))

# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Flowerbed)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it uses greedy local decisions on an array.
#
# U -- Understand
# 1) When can I plant a flower? Only if the current spot and both neighbors are empty.
# 2) What should I return? Whether I can plant at least n flowers.
#
# P -- Plan
# I will scan the flowerbed and greedily plant whenever a valid open spot appears.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - check each plot and neighbors
# - plant when allowed and reduce n
# - return whether n is now 0 or less
#
# I -- Implement

def can_place_flowers(flowerbed, n):
    for i in range(len(flowerbed)):
        left_empty = i == 0 or flowerbed[i - 1] == 0
        right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
        if flowerbed[i] == 0 and left_empty and right_empty:
            flowerbed[i] = 1
            n -= 1
            if n <= 0:
                return True
    return n <= 0

# Test Cases
print_section('Session 1 - Version 2 - Problem 1')
print(can_place_flowers([1, 0, 0, 0, 1], 1))
print(can_place_flowers([1, 0, 0, 0, 1], 2))


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Reverse Linked List)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because pointer reversal is a core linked list skill.
#
# U -- Understand
# 1) What should be returned? The new head of the reversed list.
# 2) Should I reuse the same nodes? Yes.
#
# P -- Plan
# I will reverse the next pointers one at a time with previous, current, and next variables.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - move through list
# - point current.next to previous
# - shift all pointers forward
#
# I -- Implement

def reverse(head):
    previous = None
    current = head
    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    return previous

# Test Cases
print_section('Session 1 - Version 2 - Problem 2')
rev_list = Node(1, Node(2, Node(3, Node(4))))
print(sll_to_string(rev_list))
print(sll_to_string(reverse(rev_list)))
print(sll_to_string(reverse(Node(9))))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Valid Word Abbreviation)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it combines string parsing with pointer movement.
#
# U -- Understand
# 1) What makes an abbreviation invalid right away? Leading zero in a number block.
# 2) What should numbers do? Skip that many letters in the word.
#
# P -- Plan
# I will walk through word and abbr with two pointers, parsing multi-digit numbers when needed.
# Time Complexity: O(n + m)
# Space Complexity: O(1)
#
# Pseudocode
# - if abbr char is digit parse full number
# - move word pointer by that number
# - else letters must match exactly
#
# I -- Implement

def valid_word_abbreviation(word, abbr):
    i = 0
    j = 0
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0':
                return False
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1
    return i == len(word) and j == len(abbr)

# Test Cases
print_section('Session 1 - Version 2 - Problem 3')
print(valid_word_abbreviation('internationalization', 'i12iz4n'))
print(valid_word_abbreviation('apple', 'a2e'))
print(valid_word_abbreviation('substitution', 's010n'))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Sum Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it compares a node with the total of all its descendants.
#
# U -- Understand
# 1) What should be checked? root.val equals the sum of every descendant value.
# 2) What tree value do I need to compute? The total subtree sum.
#
# P -- Plan
# I will compute the sum of descendants as subtree sum minus root value, then compare it to root.val.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - recursively get subtree sum
# - compare root value to subtree sum minus root value
#
# I -- Implement

def check_root_sum(root):
    def subtree_sum(node):
        if node is None:
            return 0
        return node.val + subtree_sum(node.left) + subtree_sum(node.right)

    if root is None:
        return False
    total = subtree_sum(root)
    return root.val == total - root.val

# Test Cases
print_section('Session 1 - Version 2 - Problem 4')
sum_tree_one = TreeNode(14, TreeNode(4, TreeNode(3), TreeNode(1)), TreeNode(6))
sum_tree_two = TreeNode(10, TreeNode(3), TreeNode(4))
print(check_root_sum(sum_tree_one))
print(check_root_sum(sum_tree_two))


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Container With Most Water)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because two pointers can optimize a brute-force area search.
#
# U -- Understand
# 1) How is area found? Width times the shorter of the two heights.
# 2) Which pointer should move? The one with the shorter height.
#
# P -- Plan
# I will use two pointers from both ends and shrink inward while tracking the best area.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - compute area from left and right
# - move shorter side inward
# - keep the max area
#
# I -- Implement

def max_area(height):
    left = 0
    right = len(height) - 1
    best = 0
    while left < right:
        width = right - left
        best = max(best, width * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

# Test Cases
print_section('Session 1 - Version 2 - Problem 5')
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))


# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Climbing Stairs)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it is a classic dynamic programming counting problem.
#
# U -- Understand
# 1) What choices do I have each step? Climb 1 or 2 stairs.
# 2) What does the recurrence look like? ways(n) = ways(n-1) + ways(n-2).
#
# P -- Plan
# I will build the answer iteratively like Fibonacci numbers.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - handle small n
# - build from 1 up to n with two running variables
#
# I -- Implement

def climb_stairs(n):
    if n <= 2:
        return n
    first = 1
    second = 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second

# Test Cases
print_section('Session 1 - Version 3 - Problem 1')
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(5))


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Set Mismatch)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it finds one duplicate and one missing value together.
#
# U -- Understand
# 1) What should be returned? [duplicate, missing].
# 2) What numbers should exist originally? Every number from 1 to n exactly once.
#
# P -- Plan
# I will count seen numbers with a set, find the duplicate, then scan 1 through n to find the missing number.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - track seen numbers and duplicate
# - scan 1..n for the missing value
#
# I -- Implement

def find_error_nums(nums):
    seen = set()
    duplicate = None
    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)
    missing = None
    for num in range(1, len(nums) + 1):
        if num not in seen:
            missing = num
            break
    return [duplicate, missing]

# Test Cases
print_section('Session 1 - Version 3 - Problem 2')
print(find_error_nums([1, 2, 2, 4]))
print(find_error_nums([1, 1]))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Delete N Nodes after M Nodes)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it combines list traversal with repeated keep/delete blocks.
#
# U -- Understand
# 1) What should I do repeatedly? Keep m nodes, then delete n nodes.
# 2) What should be returned? The original head after modification.
#
# P -- Plan
# I will walk m nodes, then skip n nodes by reconnecting the list, and repeat until the end.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - keep m nodes
# - skip n nodes
# - connect kept part to remaining list
#
# I -- Implement

def delete_nodes(head, m, n):
    current = head
    while current:
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
print_section('Session 1 - Version 3 - Problem 3')
del_list_one = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))
print(sll_to_string(delete_nodes(del_list_one, 2, 3)))
del_list_two = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11)))))))))))
print(sll_to_string(delete_nodes(del_list_two, 1, 3)))

# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Diameter of Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it combines subtree heights into a global best path.
#
# U -- Understand
# 1) What should be counted? Edges on the longest path between two nodes.
# 2) Can the longest path avoid the root? Yes.
#
# P -- Plan
# I will compute heights recursively and update the best diameter at each node.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - helper returns height
# - update answer with left height + right height
#
# I -- Implement

def get_diameter(root):
    best = 0

    def height(node):
        nonlocal best
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)

    height(root)
    return best

# Test Cases
print_section('Session 1 - Version 3 - Problem 4')
print(get_diameter(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
print(get_diameter(TreeNode(1)))


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Two Sum II)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because sorted arrays often allow an O(1)-space two-pointer solution.
#
# U -- Understand
# 1) Is the list sorted? Yes.
# 2) What indices should I return? 0-indexed indices of the matching pair.
#
# P -- Plan
# I will use one pointer at each end and move inward based on whether the sum is too small or too large.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - start left at 0 and right at end
# - if sum small move left up
# - if sum large move right down
# - return indices on match
#
# I -- Implement

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        current = numbers[left] + numbers[right]
        if current == target:
            return [left, right]
        if current < target:
            left += 1
        else:
            right -= 1

# Test Cases
print_section('Session 1 - Version 3 - Problem 5')
print(two_sum([1, 2, 3, 4], 3))
print(two_sum([2, 7, 11, 15], 9))


# =========================================================
# WEEK 10: SESSION 2
# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Contains Duplicates)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because sets are one of the fastest ways to detect repeats.
#
# U -- Understand
# 1) What makes the answer True? At least one value appears twice.
# 2) What should happen if all values are distinct? Return False.
#
# P -- Plan
# I will compare the length of the list to the length of a set of the same values.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - build set from nums
# - compare sizes
#
# I -- Implement

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Test Cases
print_section('Session 2 - Version 1 - Problem 1')
print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Remove Element)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it practices in-place array updates with a write pointer.
#
# U -- Understand
# 1) What should be returned? The count k of kept elements.
# 2) Do I need to preserve the values after index k? No.
#
# P -- Plan
# I will use a write pointer and copy over every value that is not equal to val.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - write kept values at the front
# - return write pointer count
#
# I -- Implement

def remove_element(nums, val):
    write = 0
    for num in nums:
        if num != val:
            nums[write] = num
            write += 1
    return write

# Test Cases
print_section('Session 2 - Version 1 - Problem 2')
nums_one = [3, 2, 2, 3]
k_one = remove_element(nums_one, 3)
print(k_one, nums_one[:k_one])
nums_two = [0, 1, 2, 2, 3, 0, 4, 2]
k_two = remove_element(nums_two, 2)
print(k_two, nums_two[:k_two])


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Greatest Common Divisor of Strings)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it mixes string repetition with the gcd idea.
#
# U -- Understand
# 1) When can a shared divisor string exist? Only when str1 + str2 equals str2 + str1.
# 2) How long should the best divisor be? gcd of the two lengths.
#
# P -- Plan
# I will first check whether the strings are compatible, then use the gcd of lengths to slice the answer.
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Pseudocode
# - if concatenations mismatch return ''
# - find gcd of lengths
# - return prefix of that length
#
# I -- Implement

def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''
    return str1[:gcd(len(str1), len(str2))]

# Test Cases
print_section('Session 2 - Version 1 - Problem 3')
print(gcd_of_strings('ABCABC', 'ABC'))
print(gcd_of_strings('ABABAB', 'ABAB'))
print(gcd_of_strings('LEET', 'CODE'))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Check Balanced Binary Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it reviews an important tree property from earlier units.
#
# U -- Understand
# 1) What makes a tree balanced? Every node's subtree heights differ by at most 1.
# 2) What should happen for an empty tree? Return True.
#
# P -- Plan
# I will reuse the height-or-fail helper pattern to detect imbalance early.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - helper returns height or -1
# - bubble -1 upward on any imbalance
#
# I -- Implement

def is_balanced(root):
    def helper(node):
        if node is None:
            return 0
        left = helper(node.left)
        if left == -1:
            return -1
        right = helper(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return helper(root) != -1

# Test Cases
print_section('Session 2 - Version 1 - Problem 4')
print(is_balanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(is_balanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))))
print(is_balanced(None))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Subarray Sum Equals K)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because prefix sums and hashing make a hard counting problem efficient.
#
# U -- Understand
# 1) What counts as a subarray? A contiguous block.
# 2) What should be returned? The number of subarrays whose sum equals k.
#
# P -- Plan
# I will use a prefix sum map. If current_sum - k appeared before, that means a subarray ending here sums to k.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - keep running prefix sum
# - add count of prefix_sum - k into answer
# - store current prefix sum frequency
#
# I -- Implement

def subarray_sum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    prefix = 0
    answer = 0
    for num in nums:
        prefix += num
        answer += counts[prefix - k]
        counts[prefix] += 1
    return answer

# Test Cases
print_section('Session 2 - Version 1 - Problem 5')
print(subarray_sum([1, 1, 1], 2))
print(subarray_sum([1, 2, 3], 3))

# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Add Two Numbers Represented By Linked Lists)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it combines digit math with linked list construction.
#
# U -- Understand
# 1) In what order are digits stored? Reverse order.
# 2) What if a carry remains at the end? Add one last node.
#
# P -- Plan
# I will walk through both lists together, add digits plus carry, and build a new result list.
# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m))
#
# Pseudocode
# - add current digits and carry
# - create node with ones digit
# - move forward until both lists and carry are done
#
# I -- Implement

def add_two_numbers(l1, l2):
    dummy = Node(0)
    tail = dummy
    carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        carry = total // 10
        tail.next = Node(total % 10)
        tail = tail.next
    return dummy.next

# Test Cases
print_section('Session 2 - Version 1 - Problem 6')
num_a = Node(2, Node(4, Node(3)))
num_b = Node(5, Node(6, Node(4)))
print(sll_to_string(add_two_numbers(num_a, num_b)))
print(sll_to_string(add_two_numbers(Node(0), Node(0))))


# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Flip Game)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it practices generating all valid one-step outcomes.
#
# U -- Understand
# 1) What move is allowed? Replace any '++' with '--'.
# 2) What if there is no valid move? Return an empty list.
#
# P -- Plan
# I will scan the string and build a new string every time I find a '++' pair.
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
#
# Pseudocode
# - loop through string
# - if s[i:i+2] is '++', build new state and save it
#
# I -- Implement

def generate_possible_next_moves(current_state):
    result = []
    for i in range(len(current_state) - 1):
        if current_state[i:i + 2] == '++':
            result.append(current_state[:i] + '--' + current_state[i + 2:])
    return result

# Test Cases
print_section('Session 2 - Version 2 - Problem 1')
print(generate_possible_next_moves('++++'))
print(generate_possible_next_moves('+'))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Intersection of Two Lists)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because sets make unique overlap problems much simpler.
#
# U -- Understand
# 1) Should duplicates appear multiple times in the answer? No, each result value must be unique.
# 2) Can the result come back in any order? Yes.
#
# P -- Plan
# I will use set intersection and convert the answer back to a list.
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Pseudocode
# - convert both lists to sets
# - return list of shared values
#
# I -- Implement

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# Test Cases
print_section('Session 2 - Version 2 - Problem 2')
print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Buildings with an Ocean View)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because scanning from the right can simplify visibility problems.
#
# U -- Understand
# 1) What gives a building an ocean view? Every building to its right is shorter.
# 2) What order should indices be returned in? Increasing order.
#
# P -- Plan
# I will scan from right to left, keep the tallest height seen so far, and record buildings taller than that.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - scan from right to left
# - if current height greater than max_right save index
# - reverse saved indices at the end
#
# I -- Implement

def find_buildings(heights):
    result = []
    max_right = -1
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > max_right:
            result.append(i)
            max_right = heights[i]
    return result[::-1]

# Test Cases
print_section('Session 2 - Version 2 - Problem 3')
print(find_buildings([4, 2, 3, 1]))
print(find_buildings([4, 3, 2, 1]))
print(find_buildings([1, 3, 2, 4]))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Leaf-Similar Trees)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it compares trees using one specific traversal-based signature.
#
# U -- Understand
# 1) What should be compared? The left-to-right leaf sequence of each tree.
# 2) What makes the answer True? The two sequences match exactly.
#
# P -- Plan
# I will collect the leaves from both trees in left-to-right order and compare the two lists.
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Pseudocode
# - collect leaves from root1
# - collect leaves from root2
# - compare the lists
#
# I -- Implement

def leaf_similar(root1, root2):
    def leaves(node, result):
        if node is None:
            return
        if node.left is None and node.right is None:
            result.append(node.val)
            return
        leaves(node.left, result)
        leaves(node.right, result)

    first = []
    second = []
    leaves(root1, first)
    leaves(root2, second)
    return first == second

# Test Cases
print_section('Session 2 - Version 2 - Problem 4')
leaf_a = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
leaf_b = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
print(leaf_similar(leaf_a, leaf_b))
print(leaf_similar(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(3), TreeNode(2))))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Insert into a Sorted Circular Linked List)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because circular linked lists need careful pointer logic.
#
# U -- Understand
# 1) What if the list is empty? Create one node that points to itself.
# 2) What if I am at the max-to-min turning point? Values bigger than max or smaller than min can be inserted there.
#
# P -- Plan
# I will walk around the circle until I find a normal sorted spot or the turning point where values wrap around.
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Pseudocode
# - if list empty make single self-loop node
# - walk around circle
# - insert when value fits between current and next, or at wrap point
#
# I -- Implement

def insert(start_node, insert_val):
    new_node = Node(insert_val)
    if start_node is None:
        new_node.next = new_node
        return new_node
    current = start_node
    while True:
        nxt = current.next
        normal_spot = current.val <= insert_val <= nxt.val
        wrap_spot = current.val > nxt.val and (insert_val >= current.val or insert_val <= nxt.val)
        full_loop = nxt is start_node
        if normal_spot or wrap_spot or full_loop:
            current.next = new_node
            new_node.next = nxt
            return start_node
        current = nxt

# Test Cases
print_section('Session 2 - Version 2 - Problem 5')
c1 = Node(3)
c2 = Node(4)
c3 = Node(1)
c1.next = c2
c2.next = c3
c3.next = c1
start = insert(c1, 2)
print(circular_to_list(start, 5))
solo = insert(None, 1)
print(circular_to_list(solo, 3))


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Sequential Digits)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it builds numbers from a clean digit pattern.
#
# U -- Understand
# 1) What is a sequential digit number? Each digit is exactly one more than the previous digit.
# 2) What order should the answer be in? Sorted increasing order.
#
# P -- Plan
# I will generate all sequential substrings from '123456789', turn them into integers, and keep the ones inside the range.
# Time Complexity: O(1) for this fixed digit range
# Space Complexity: O(1) ignoring output
#
# Pseudocode
# - try every substring length and start
# - convert substring to number
# - keep it if inside range
#
# I -- Implement

def sequential_digits(low, high):
    digits = '123456789'
    result = []
    for length in range(2, 10):
        for start in range(0, 10 - length):
            num = int(digits[start:start + length])
            if low <= num <= high:
                result.append(num)
    return result

# Test Cases
print_section('Session 2 - Version 2 - Problem 6')
print(sequential_digits(100, 300))
print(sequential_digits(1000, 13000))

# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Count of Matches in Tournament)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it turns a word problem into a clean loop or math insight.
#
# U -- Understand
# 1) What happens each round? Some matches are played and fewer teams remain.
# 2) When does the tournament stop? When one team remains.
#
# P -- Plan
# I will simulate the rounds and add the number of matches played each time.
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Pseudocode
# - while n > 1
# - if even add n//2 and halve n
# - if odd add (n-1)//2 and set n to that plus 1
#
# I -- Implement

def number_of_matches(n):
    matches = 0
    while n > 1:
        if n % 2 == 0:
            matches += n // 2
            n //= 2
        else:
            matches += (n - 1) // 2
            n = (n - 1) // 2 + 1
    return matches

# Test Cases
print_section('Session 2 - Version 3 - Problem 1')
print(number_of_matches(7))
print(number_of_matches(14))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Intersection of Two Linked Lists)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because shared-node problems are common linked list interview questions.
#
# U -- Understand
# 1) What should be returned? The actual intersecting node object, not just its value.
# 2) What if the lists do not intersect? Return None.
#
# P -- Plan
# I will use two pointers that switch heads when they hit the end. That lines them up by distance.
# Time Complexity: O(n + m)
# Space Complexity: O(1)
#
# Pseudocode
# - walk pointer A through list A then B
# - walk pointer B through list B then A
# - return the node where they meet
#
# I -- Implement

def find_intersection(headA, headB):
    a = headA
    b = headB
    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

# Test Cases
print_section('Session 2 - Version 3 - Problem 2')
shared = Node(8, Node(10))
headA = Node(3, Node(7, shared))
headB = Node(99, Node(1, shared))
print(find_intersection(headA, headB).val)
print(find_intersection(Node(1, Node(2)), Node(3, Node(4))))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Power of Four)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it reviews repeated division and strong base cases.
#
# U -- Understand
# 1) What is the smallest power of four? 1.
# 2) When should I return False? If n is less than 1 or not divisible by 4 when needed.
#
# P -- Plan
# I will recursively divide by 4 until I reach 1 or fail.
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
print_section('Session 2 - Version 3 - Problem 3')
print(is_power_of_four(16))
print(is_power_of_four(5))
print(is_power_of_four(1))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Leaves of a Binary Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it groups nodes by the round when they would be removed.
#
# U -- Understand
# 1) What should be returned? A list of lists, one list per removal round.
# 2) How can I tell when a node gets removed? By its height from the nearest leaf.
#
# P -- Plan
# I will compute each node's height from the bottom. Nodes with the same height belong in the same round.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - leaf nodes have height 0
# - group node values by computed height
# - return groups in height order
#
# I -- Implement

def find_leaves(root):
    groups = []

    def height(node):
        if node is None:
            return -1
        h = 1 + max(height(node.left), height(node.right))
        if h == len(groups):
            groups.append([])
        groups[h].append(node.val)
        return h

    height(root)
    return groups

# Test Cases
print_section('Session 2 - Version 3 - Problem 4')
leaves_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(find_leaves(leaves_tree))
print(find_leaves(TreeNode(1)))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Custom Sort String)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because custom ordering with counts is a common hashing pattern.
#
# U -- Understand
# 1) What should follow the given order? Characters from s that appear in order.
# 2) What about characters not in order? They can appear anywhere after the ordered part.
#
# P -- Plan
# I will count characters in s, then build the answer by first using the custom order and then adding leftover characters.
# Time Complexity: O(n + m)
# Space Complexity: O(n)
#
# Pseudocode
# - count chars in s
# - append chars following order
# - append remaining chars not in order
#
# I -- Implement

def custom_sort_string(order, s):
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1
    result = []
    for char in order:
        if char in counts:
            result.append(char * counts[char])
            del counts[char]
    for char, count in counts.items():
        result.append(char * count)
    return ''.join(result)

# Test Cases
print_section('Session 2 - Version 3 - Problem 5')
print(custom_sort_string('cba', 'abcd'))
print(custom_sort_string('bcafg', 'abcd'))


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Find Sum Pair)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because hashing pair sums can reveal hidden equal-sum relationships.
#
# U -- Understand
# 1) What should be returned? Four integers a, b, c, d such that a + b = c + d.
# 2) What if no match exists? Return an empty list.
#
# P -- Plan
# I will store the first pair I see for each sum. If I see the same sum again with four distinct indices, I found an answer.
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
#
# Pseudocode
# - try every pair of indices
# - if sum seen before check indices are all different
# - return the four values on success
#
# I -- Implement

def find_sum_pair(numbers):
    sums = {}
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            total = numbers[i] + numbers[j]
            if total in sums:
                a, b = sums[total]
                if len({a, b, i, j}) == 4:
                    return [numbers[a], numbers[b], numbers[i], numbers[j]]
            else:
                sums[total] = (i, j)
    return []

# Test Cases
print_section('Session 2 - Version 3 - Problem 6')
print(find_sum_pair([3, 10, 4, 5, 2, 14]))
print(find_sum_pair([60, 0, 10, -35, 90]))

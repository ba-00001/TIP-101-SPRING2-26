
from collections import deque, defaultdict

# =========================================================
# WEEK 9: SESSION 1 AND SESSION 2
# =========================================================


def print_section(title):
    print('\n' + '=' * 72)
    print(title)
    print('=' * 72)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_values(root):
    if root is None:
        return []
    return [root.val] + preorder_values(root.left) + preorder_values(root.right)


def inorder_values(root):
    if root is None:
        return []
    return inorder_values(root.left) + [root.val] + inorder_values(root.right)


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
# WEEK 9: SESSION 1
# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Is Symmetric Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it checks mirror structure and values at the same time.
#
# U -- Understand
# 1) What makes a tree symmetric? The left and right sides mirror each other.
# 2) What should happen for an empty tree? Return True.
#
# P -- Plan
# I will compare the left and right subtree with a helper that checks mirrored positions.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - write helper(left, right)
# - if both are None return True
# - if only one is None return False
# - compare values and opposite children
#
# I -- Implement

def is_symmetric(root):
    def mirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)

    if root is None:
        return True
    return mirror(root.left, root.right)

# Test Cases
print_section('Session 1 - Version 1 - Problem 1')
sym_tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
not_sym_tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(sym_tree))
print(is_symmetric(not_sym_tree))


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Root-to-Leaf Paths)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it builds strings while exploring every root-to-leaf path.
#
# U -- Understand
# 1) What counts as a path? A full path from the root to a leaf.
# 2) What should a single-node tree return? A list with that one value as a string.
#
# P -- Plan
# I will use DFS. At each node I add its value to the current path, and when I reach a leaf I save the path string.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return []
# - walk down tree with current path string
# - if leaf save the path
#
# I -- Implement

def binary_tree_paths(root):
    if root is None:
        return []

    paths = []

    def dfs(node, path):
        if node.left is None and node.right is None:
            paths.append(path)
            return
        if node.left:
            dfs(node.left, path + '->' + str(node.left.val))
        if node.right:
            dfs(node.right, path + '->' + str(node.right.val))

    dfs(root, str(root.val))
    return paths

# Test Cases
print_section('Session 1 - Version 1 - Problem 2')
path_tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(binary_tree_paths(path_tree))
print(binary_tree_paths(TreeNode(1)))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Minimum Difference in BST)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because inorder traversal turns a BST into sorted order.
#
# U -- Understand
# 1) Why is BST important here? Inorder traversal gives values in sorted order.
# 2) Where does the smallest difference appear? Between two neighboring sorted values.
#
# P -- Plan
# I will do an inorder traversal, compare each value with the previous one, and keep the smallest difference.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - inorder traverse BST
# - compare current value with previous value
# - keep smallest difference
#
# I -- Implement

def min_diff_in_bst(root):
    previous = None
    answer = float('inf')

    def inorder(node):
        nonlocal previous, answer
        if node is None:
            return
        inorder(node.left)
        if previous is not None:
            answer = min(answer, node.val - previous)
        previous = node.val
        inorder(node.right)

    inorder(root)
    return answer

# Test Cases
print_section('Session 1 - Version 1 - Problem 3')
bst_one = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
bst_two = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
print(min_diff_in_bst(bst_one))
print(min_diff_in_bst(bst_two))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Increasing Order Search Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it rearranges a BST using inorder order.
#
# U -- Understand
# 1) What shape should the final tree have? Only right children and no left children.
# 2) What order should the values appear in? Increasing inorder order.
#
# P -- Plan
# I will collect the nodes with inorder traversal, then reconnect them into a right-only chain.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - collect nodes in inorder
# - loop through nodes
# - set each node.left to None and node.right to next node
#
# I -- Implement

def increasing_bst(root):
    nodes = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        nodes.append(node)
        inorder(node.right)

    inorder(root)
    for i in range(len(nodes)):
        nodes[i].left = None
        nodes[i].right = nodes[i + 1] if i + 1 < len(nodes) else None
    return nodes[0] if nodes else None

# Test Cases
print_section('Session 1 - Version 1 - Problem 4')
inc_one = increasing_bst(TreeNode(5, TreeNode(1), TreeNode(7)))
print(level_values(inc_one))
inc_two_tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
inc_two = increasing_bst(inc_two_tree)
print(level_values(inc_two))


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Equal Tree Split)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it uses subtree sizes to test a tree split.
#
# U -- Understand
# 1) What makes a valid split? One removed edge creates two trees with the same number of nodes.
# 2) When is that impossible right away? If the total number of nodes is odd.
#
# P -- Plan
# I will compute every subtree size. If any subtree has size total // 2, then removing the edge above it makes an equal split.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - get all subtree sizes
# - total size is root subtree size
# - if total odd return False
# - check whether any non-root subtree equals half
#
# I -- Implement

def can_split(root):
    sizes = []

    def subtree_size(node):
        if node is None:
            return 0
        total = 1 + subtree_size(node.left) + subtree_size(node.right)
        sizes.append(total)
        return total

    total_size = subtree_size(root)
    sizes.pop()
    if total_size % 2 != 0:
        return False
    return (total_size // 2) in sizes

# Test Cases
print_section('Session 1 - Version 1 - Problem 5')
split_true_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
split_false_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(can_split(split_true_tree))
print(can_split(split_false_tree))

# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Evaluate Boolean Full Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it evaluates a full expression tree from the leaves upward.
#
# U -- Understand
# 1) What do leaf nodes hold? True or False.
# 2) What do non-leaf nodes hold? OR or AND.
#
# P -- Plan
# I will recursively evaluate the left and right subtree and then apply the operator at the current node.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if node is a leaf return its value
# - evaluate left and right
# - apply OR or AND
#
# I -- Implement

def evaluate_tree_boolean(root):
    if root.left is None and root.right is None:
        return root.val
    left_value = evaluate_tree_boolean(root.left)
    right_value = evaluate_tree_boolean(root.right)
    if root.val == 'OR':
        return left_value or right_value
    return left_value and right_value

# Test Cases
print_section('Session 1 - Version 2 - Problem 1')
bool_tree = TreeNode('OR', TreeNode(True), TreeNode('AND', TreeNode(False), TreeNode(True)))
print(evaluate_tree_boolean(bool_tree))
print(evaluate_tree_boolean(TreeNode('AND', TreeNode(True), TreeNode(False))))


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Find Lonely Nodes)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it checks parent-child relationships while traversing a tree.
#
# U -- Understand
# 1) What is a lonely node? A node that is its parent's only child.
# 2) Does the root count? No.
#
# P -- Plan
# I will traverse the tree and whenever a node has only one child, I will add that child's value.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - visit node
# - if exactly one child exists add that child value
# - recurse on both children
#
# I -- Implement

def find_lonely_nodes(root):
    lonely = []

    def dfs(node):
        if node is None:
            return
        if node.left and not node.right:
            lonely.append(node.left.val)
        if node.right and not node.left:
            lonely.append(node.right.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return lonely

# Test Cases
print_section('Session 1 - Version 2 - Problem 2')
lonely_one = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
lonely_two = TreeNode(7, TreeNode(1, TreeNode(6), None), TreeNode(4, TreeNode(5), TreeNode(3, None, TreeNode(2))))
print(find_lonely_nodes(lonely_one))
print(find_lonely_nodes(lonely_two))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Kth Smallest node in a BST)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because BST inorder traversal gives values in sorted order.
#
# U -- Understand
# 1) What order should I use? Inorder traversal.
# 2) What does kth smallest mean? The kth value in sorted order.
#
# P -- Plan
# I will do inorder traversal and stop once I visit the kth node.
# Time Complexity: O(h + k)
# Space Complexity: O(h)
#
# Pseudocode
# - inorder traverse BST
# - count visited nodes
# - when count equals k save answer
#
# I -- Implement

def kth_smallest(root, k):
    count = 0
    answer = None

    def inorder(node):
        nonlocal count, answer
        if node is None or answer is not None:
            return
        inorder(node.left)
        count += 1
        if count == k:
            answer = node.val
            return
        inorder(node.right)

    inorder(root)
    return answer

# Test Cases
print_section('Session 1 - Version 2 - Problem 3')
k_tree = TreeNode(15, TreeNode(10, TreeNode(8), TreeNode(12)), TreeNode(20, TreeNode(16), TreeNode(26)))
print(kth_smallest(k_tree, 4))
print(kth_smallest(k_tree, 1))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Second Minimum Value in a Special Binary Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it uses a special tree rule to search for the next bigger value.
#
# U -- Understand
# 1) What is guaranteed about each parent? Its value is the smaller of its two children.
# 2) What if there is no second minimum? Return -1.
#
# P -- Plan
# I will store the root value as the minimum and search for the smallest value bigger than it.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - keep root value as smallest
# - DFS through tree
# - update answer when value is bigger than smallest but smaller than current answer
#
# I -- Implement

def find_second_minimum_value(root):
    smallest = root.val
    answer = float('inf')

    def dfs(node):
        nonlocal answer
        if node is None:
            return
        if smallest < node.val < answer:
            answer = node.val
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return -1 if answer == float('inf') else answer

# Test Cases
print_section('Session 1 - Version 2 - Problem 4')
second_min_tree_one = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
second_min_tree_two = TreeNode(2, TreeNode(2), TreeNode(2))
print(find_second_minimum_value(second_min_tree_one))
print(find_second_minimum_value(second_min_tree_two))


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Transformable Binary Trees by Swapping Subtrees)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it compares trees while allowing mirror swaps.
#
# U -- Understand
# 1) What operation is allowed? Swapping the left and right subtree of any node.
# 2) When should I return True? If the trees can match after any number of those swaps.
#
# P -- Plan
# I will recursively check two possibilities at every pair of nodes: no swap or swap.
# Time Complexity: O(n) for matching trees in these small practice cases, though repeated branching can be worse in general.
# Space Complexity: O(h)
#
# Pseudocode
# - if both None return True
# - if only one None or values differ return False
# - return no-swap match or swapped match
#
# I -- Implement

def can_swap(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None or root1.val != root2.val:
        return False
    no_swap = can_swap(root1.left, root2.left) and can_swap(root1.right, root2.right)
    do_swap = can_swap(root1.left, root2.right) and can_swap(root1.right, root2.left)
    return no_swap or do_swap

# Test Cases
print_section('Session 1 - Version 2 - Problem 5')
swap_tree_one = TreeNode(6, TreeNode(3, TreeNode(1), TreeNode(7)), TreeNode(8, TreeNode(4, TreeNode(7), TreeNode(1)), TreeNode(2, None, TreeNode(3))))
swap_tree_two = TreeNode(6, TreeNode(8, TreeNode(2, TreeNode(3), None), TreeNode(4, TreeNode(1), TreeNode(7))), TreeNode(3, TreeNode(7), TreeNode(1)))
print(can_swap(swap_tree_one, swap_tree_two))
print(can_swap(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(4))))


# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Evaluate Mathematical Expression Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it evaluates arithmetic from a full binary expression tree.
#
# U -- Understand
# 1) What do leaf nodes hold? Integers.
# 2) What do non-leaf nodes hold? One of +, -, *, or /.
#
# P -- Plan
# I will recursively evaluate the children and then apply the current math operator.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if leaf return value
# - evaluate left and right
# - apply operator and return result
#
# I -- Implement

def evaluate_tree_math(root):
    if root.left is None and root.right is None:
        return root.val
    left_value = evaluate_tree_math(root.left)
    right_value = evaluate_tree_math(root.right)
    if root.val == '+':
        return left_value + right_value
    if root.val == '-':
        return left_value - right_value
    if root.val == '*':
        return left_value * right_value
    return left_value // right_value

# Test Cases
print_section('Session 1 - Version 3 - Problem 1')
math_tree = TreeNode('+', TreeNode('*', TreeNode(5), TreeNode(2)), TreeNode('-', TreeNode(60), TreeNode(20)))
print(evaluate_tree_math(math_tree))
print(evaluate_tree_math(TreeNode('/', TreeNode(20), TreeNode(5))))

# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (Find Corresponding Node in Cloned Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it matches positions across two identical tree structures.
#
# U -- Understand
# 1) What should I return? The matching node reference from the cloned tree.
# 2) How do I know it matches? It sits in the same position as target in the original tree.
#
# P -- Plan
# I will walk both trees at the same time. When the original node is target, I will return the cloned node.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if original is None return None
# - if original is target return cloned
# - search left then right
#
# I -- Implement

def get_target_copy(original, cloned, target):
    if original is None:
        return None
    if original is target:
        return cloned
    left_answer = get_target_copy(original.left, cloned.left, target)
    if left_answer:
        return left_answer
    return get_target_copy(original.right, cloned.right, target)

# Test Cases
print_section('Session 1 - Version 3 - Problem 2')
orig = TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6), TreeNode(19)))
clone = TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6), TreeNode(19)))
target = orig.right
print(get_target_copy(orig, clone, target).val)
single_orig = TreeNode(7)
single_clone = TreeNode(7)
print(get_target_copy(single_orig, single_clone, single_orig).val)


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (Path Sum in Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because root-to-leaf path sums show up often in tree problems.
#
# U -- Understand
# 1) What path counts? A root-to-leaf path only.
# 2) What should happen for an empty tree? Return False.
#
# P -- Plan
# I will subtract the current node value from the target as I go down. At a leaf, I will check whether the remaining target equals the leaf value.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return False
# - if leaf return whether value equals target
# - recurse on children with reduced target
#
# I -- Implement

def has_path_sum(root, target_sum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == target_sum
    new_target = target_sum - root.val
    return has_path_sum(root.left, new_target) or has_path_sum(root.right, new_target)

# Test Cases
print_section('Session 1 - Version 3 - Problem 3')
path_sum_tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print(has_path_sum(path_sum_tree, 22))
print(has_path_sum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Check Balanced Binary Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because balanced trees are important for efficient recursion and search.
#
# U -- Understand
# 1) What makes a tree balanced? Every node's left and right subtree heights differ by at most 1.
# 2) What should happen for an empty tree? Return True.
#
# P -- Plan
# I will compute subtree heights with a helper. If I ever find an unbalanced subtree, I will return a special failure value.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - helper returns height or -1 for unbalanced
# - compare left and right heights
# - if difference > 1 return -1
#
# I -- Implement

def is_balanced(root):
    def height_or_fail(node):
        if node is None:
            return 0
        left_height = height_or_fail(node.left)
        if left_height == -1:
            return -1
        right_height = height_or_fail(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    return height_or_fail(root) != -1

# Test Cases
print_section('Session 1 - Version 3 - Problem 4')
balanced_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
unbalanced_tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
print(is_balanced(balanced_tree))
print(is_balanced(unbalanced_tree))
print(is_balanced(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Replace Node Value with Sum of Subtree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it updates a tree in place using postorder recursion.
#
# U -- Understand
# 1) What should each node become? The sum of the values in its left and right subtree.
# 2) What should a leaf become? 0, because it has no children.
#
# P -- Plan
# I will use postorder traversal. For each node I will first get the total sum of its original subtree, then replace the node value with just the left-plus-right part.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - recurse on left and right to get subtree sums
# - save original node value
# - replace node value with left sum + right sum
# - return full subtree sum including original value
#
# I -- Implement

def sum_transform(root):
    def transform(node):
        if node is None:
            return 0
        left_sum = transform(node.left)
        right_sum = transform(node.right)
        original = node.val
        node.val = left_sum + right_sum
        return original + left_sum + right_sum

    transform(root)
    return root

# Test Cases
print_section('Session 1 - Version 3 - Problem 5')
transform_tree = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7), TreeNode(8)), TreeNode(6)))
print('Before:', level_values(transform_tree))
sum_transform(transform_tree)
print('After:', level_values(transform_tree))
small_transform = TreeNode(10)
sum_transform(small_transform)
print('Leaf after transform:', small_transform.val)


# =========================================================
# WEEK 9: SESSION 2
# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Level Order Traversal of Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because level order traversal is the main BFS pattern for trees.
#
# U -- Understand
# 1) What order should values appear in? Level by level from left to right.
# 2) What should an empty tree return? An empty list.
#
# P -- Plan
# I will use a queue. I pop the front node, record its value, and add its children to the back.
# Time Complexity: O(n)
# Space Complexity: O(w), where w is the maximum width of the tree.
#
# Pseudocode
# - if root is None return []
# - push root into queue
# - while queue not empty pop left, save value, push children
#
# I -- Implement

def level_order(root):
    if root is None:
        return []
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited

# Test Cases
print_section('Session 2 - Version 1 - Problem 1')
level_tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(level_order(level_tree))
print(level_order(None))

# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Find Minimum Depth of Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because BFS finds the nearest leaf efficiently.
#
# U -- Understand
# 1) What is minimum depth? The number of nodes on the shortest root-to-leaf path.
# 2) What traversal works well here? BFS, because the first leaf found is the shallowest one.
#
# P -- Plan
# I will use a queue of (node, depth) pairs. The first leaf I remove from the queue gives the answer.
# Time Complexity: O(n)
# Space Complexity: O(w)
#
# Pseudocode
# - if root is None return 0
# - queue starts with (root, 1)
# - pop nodes in BFS order
# - when a leaf is found return its depth
#
# I -- Implement

def min_depth(root):
    if root is None:
        return 0
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if node.left is None and node.right is None:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

# Test Cases
print_section('Session 2 - Version 1 - Problem 2')
min_tree_one = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
min_tree_two = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
print(min_depth(min_tree_one))
print(min_depth(min_tree_two))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Odd-Even Level Sum Difference in Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it tracks level-based totals during BFS.
#
# U -- Understand
# 1) What levels are odd and even? Root is level 1, then 2, then 3, and so on.
# 2) What should I return? Odd level sum minus even level sum.
#
# P -- Plan
# I will do BFS with level numbers and add values into odd or even totals.
# Time Complexity: O(n)
# Space Complexity: O(w)
#
# Pseudocode
# - queue stores (node, level)
# - pop nodes and add value to odd or even total
# - push children with level + 1
#
# I -- Implement

def level_difference(root):
    if root is None:
        return 0
    odd_sum = 0
    even_sum = 0
    queue = deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if level % 2 == 1:
            odd_sum += node.val
        else:
            even_sum += node.val
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return odd_sum - even_sum

# Test Cases
print_section('Session 2 - Version 1 - Problem 3')
diff_tree = TreeNode(6, TreeNode(3, TreeNode(5), None), TreeNode(8, TreeNode(4, TreeNode(1), TreeNode(7)), TreeNode(2, None, TreeNode(3))))
print(level_difference(diff_tree))
print(level_difference(TreeNode(10)))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Level Order Traversal of Binary Tree with Nested Lists)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because grouped levels are useful in many BFS tree problems.
#
# U -- Understand
# 1) What should each inner list hold? All node values from one level.
# 2) What should an empty tree return? An empty list.
#
# P -- Plan
# I will use BFS and process the queue one level at a time.
# Time Complexity: O(n)
# Space Complexity: O(w)
#
# Pseudocode
# - while queue not empty
# - measure current level size
# - pop exactly that many nodes into one list
# - append the level list to answer
#
# I -- Implement

def level_order_nested(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# Test Cases
print_section('Session 2 - Version 1 - Problem 4')
nested_tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order_nested(nested_tree))
print(level_order_nested(None))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Sum of Binary Tree Node Tilts)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it combines subtree sums with a node-by-node calculation.
#
# U -- Understand
# 1) What is a node's tilt? The absolute difference between left subtree sum and right subtree sum.
# 2) How can I avoid recomputing sums many times? Return subtree sums during postorder traversal.
#
# P -- Plan
# I will use postorder traversal to get left and right subtree sums. At each node I add its tilt into a running total.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - recurse left and right to get sums
# - add abs(left_sum - right_sum) to answer
# - return subtree total
#
# I -- Implement

def find_tilt(root):
    total_tilt = 0

    def subtree_sum(node):
        nonlocal total_tilt
        if node is None:
            return 0
        left_sum = subtree_sum(node.left)
        right_sum = subtree_sum(node.right)
        total_tilt += abs(left_sum - right_sum)
        return node.val + left_sum + right_sum

    subtree_sum(root)
    return total_tilt

# Test Cases
print_section('Session 2 - Version 1 - Problem 5')
print(find_tilt(TreeNode(1, TreeNode(2), TreeNode(3))))
print(find_tilt(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))))


# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Print Level Order Traversal of Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because printing BFS order is a good queue practice problem.
#
# U -- Understand
# 1) What order should values be printed in? Level by level from left to right.
# 2) What should happen for an empty tree? Print nothing.
#
# P -- Plan
# I will use the same queue idea as level order traversal, but print each popped value instead of storing it.
# Time Complexity: O(n)
# Space Complexity: O(w)
#
# Pseudocode
# - if root is None return
# - BFS through queue
# - print popped value and add children
#
# I -- Implement

def print_by_level(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Test Cases
print_section('Session 2 - Version 2 - Problem 1')
print_by_level(level_tree)
print_by_level(None)

# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Sum of Node Values by Level in Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because level-by-level totals are a common BFS pattern.
#
# U -- Understand
# 1) What should I return? A list of sums, one per level.
# 2) What should an empty tree return? An empty list.
#
# P -- Plan
# I will process one level at a time with BFS and add the values from that level.
# Time Complexity: O(n)
# Space Complexity: O(w)
#
# Pseudocode
# - BFS by levels
# - sum values in current level
# - append sum to result
#
# I -- Implement

def level_sum(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_total = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_total += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_total)
    return result

# Test Cases
print_section('Session 2 - Version 2 - Problem 2')
print(level_sum(level_tree))
print(level_sum(None))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Maximum Nodes at Any Level in Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because tree width is an important structural measurement.
#
# U -- Understand
# 1) What should I return? The largest number of nodes on any one level.
# 2) What should an empty tree return? 0.
#
# P -- Plan
# I will do BFS and compare the size of each level to the best width seen so far.
# Time Complexity: O(n)
# Space Complexity: O(w)
#
# Pseudocode
# - BFS by levels
# - update answer with current queue length
#
# I -- Implement

def level_max(root):
    if root is None:
        return 0
    queue = deque([root])
    answer = 0
    while queue:
        answer = max(answer, len(queue))
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return answer

# Test Cases
print_section('Session 2 - Version 2 - Problem 3')
print(level_max(level_tree))
full_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(level_max(full_tree))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Vertical Order Traversal of Binary Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it groups nodes by column instead of by level.
#
# U -- Understand
# 1) How do I track columns? Root starts at column 0, left is -1, right is +1.
# 2) How do I keep top-to-bottom and left-to-right order? Use BFS.
#
# P -- Plan
# I will do BFS with (node, column) pairs and collect values by column in a dictionary. Then I will return columns from smallest to largest.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - queue stores node and column
# - append node value into column list
# - push left with col-1 and right with col+1
# - return lists from min column to max column
#
# I -- Implement

def vertical_order(root):
    if root is None:
        return []
    columns = defaultdict(list)
    queue = deque([(root, 0)])
    min_col = 0
    max_col = 0
    while queue:
        node, col = queue.popleft()
        columns[col].append(node.val)
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))
    return [columns[col] for col in range(min_col, max_col + 1)]

# Test Cases
print_section('Session 2 - Version 2 - Problem 4')
vert_one = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
vert_two = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
print(vertical_order(vert_one))
print(vertical_order(vert_two))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Find the Diameter of Binary Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because diameter combines subtree heights into a global tree answer.
#
# U -- Understand
# 1) What should the answer count? Number of edges on the longest path.
# 2) Can the longest path skip the root? Yes.
#
# P -- Plan
# I will compute subtree heights with DFS. At each node, left height plus right height is the longest path through that node.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - helper returns height in edges-from-node-down style using node counts
# - update diameter with left height + right height
# - return 1 + max(left, right)
#
# I -- Implement

def find_diameter(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        diameter = max(diameter, left_height + right_height)
        return 1 + max(left_height, right_height)

    height(root)
    return diameter

# Test Cases
print_section('Session 2 - Version 2 - Problem 5')
diameter_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(find_diameter(diameter_tree))
print(find_diameter(TreeNode(1)))


# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Level Order Traversal in Dictionary)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it stores BFS results with explicit level numbers.
#
# U -- Understand
# 1) What are the dictionary keys? Level numbers.
# 2) What should the values be? Lists of node values from left to right for that level.
#
# P -- Plan
# I will use a queue of (node, level) pairs and build the dictionary as I do BFS.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - queue starts with (root, 1)
# - pop node and level
# - append value to dictionary[level]
# - push children with level + 1
#
# I -- Implement

def level_dict(root):
    if root is None:
        return {}
    result = {}
    queue = deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if level not in result:
            result[level] = []
        result[level].append(node.val)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return result

# Test Cases
print_section('Session 2 - Version 3 - Problem 1')
print(level_dict(level_tree))
print(level_dict(None))

# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Node Values Between Given Levels in Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it filters BFS results by a level range.
#
# U -- Understand
# 1) Which levels should I include? Every level from start_level through end_level.
# 2) In what order should values appear? The same left-to-right order BFS visits them.
#
# P -- Plan
# I will do BFS with levels and collect values only when the level is inside the requested range.
# Time Complexity: O(n)
# Space Complexity: O(w)
#
# Pseudocode
# - queue stores node and level
# - if level inside range add value to answer
# - push children with next level
#
# I -- Implement

def get_level_range(root, start_level, end_level):
    if root is None:
        return []
    result = []
    queue = deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if start_level <= level <= end_level:
            result.append(node.val)
        if level < end_level:
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
    return result

# Test Cases
print_section('Session 2 - Version 3 - Problem 2')
range_tree = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(get_level_range(range_tree, 2, 4))
print(get_level_range(range_tree, 1, 2))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (Cousins in Binary Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it compares both depth and parent relationships.
#
# U -- Understand
# 1) What makes two nodes cousins? Same depth and different parents.
# 2) What should happen if one value is missing? Return False.
#
# P -- Plan
# I will use BFS by level and keep track of each node's parent. If x and y show up on the same level with different parents, they are cousins.
# Time Complexity: O(n)
# Space Complexity: O(w)
#
# Pseudocode
# - queue stores node and parent
# - check one level at a time
# - if both targets found compare parents
#
# I -- Implement

def is_cousins(root, x, y):
    if root is None:
        return False
    queue = deque([(root, None)])
    while queue:
        found_x_parent = None
        found_y_parent = None
        for _ in range(len(queue)):
            node, parent = queue.popleft()
            if node.val == x:
                found_x_parent = parent
            if node.val == y:
                found_y_parent = parent
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        if found_x_parent or found_y_parent:
            return found_x_parent is not None and found_y_parent is not None and found_x_parent != found_y_parent
    return False

# Test Cases
print_section('Session 2 - Version 3 - Problem 3')
cousin_one = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3))
cousin_two = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
print(is_cousins(cousin_one, 4, 3))
print(is_cousins(cousin_two, 5, 4))
print(is_cousins(cousin_two, 2, 3))


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (Print Corner Nodes of Each Level in Binary Tree)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it uses BFS to pull out just the edge values of each level.
#
# U -- Understand
# 1) What are corner nodes? The first and last node in a level.
# 2) If a level has one node, how many times should it print? Once.
#
# P -- Plan
# I will do BFS one level at a time and print the first and last value from that level.
# Time Complexity: O(n)
# Space Complexity: O(w)
#
# Pseudocode
# - process each level into a temporary list
# - print first value
# - if different also print last value
#
# I -- Implement

def print_corner_nodes(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(level[0])
        if len(level) > 1:
            print(level[-1])

# Test Cases
print_section('Session 2 - Version 3 - Problem 4')
corner_tree = diff_tree
print_corner_nodes(corner_tree)
print_corner_nodes(TreeNode(10))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (Lowest Common Ancestor in Binary Tree)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because LCA is one of the most common binary tree interview patterns.
#
# U -- Understand
# 1) What counts as an ancestor here? A node can be a descendant of itself.
# 2) What should be returned? The TreeNode that is the lowest common ancestor.
#
# P -- Plan
# I will use recursion. If one target is found in the left subtree and the other is found in the right subtree, the current node is the LCA.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return None
# - if root is p or q return root
# - recurse left and right
# - if both sides return something, root is LCA
#
# I -- Implement

def find_lca(root, p, q):
    if root is None or root is p or root is q:
        return root
    left_answer = find_lca(root.left, p, q)
    right_answer = find_lca(root.right, p, q)
    if left_answer and right_answer:
        return root
    return left_answer if left_answer else right_answer

# Test Cases
print_section('Session 2 - Version 3 - Problem 5')
lca_tree = range_tree
p = lca_tree.left
q = lca_tree.right
print(find_lca(lca_tree, p, q).val)
p2 = lca_tree.left
q2 = lca_tree.left.right.right
print(find_lca(lca_tree, p2, q2).val)

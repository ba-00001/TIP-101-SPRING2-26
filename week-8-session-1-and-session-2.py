
# =========================================================
# WEEK 8: SESSION 1 AND SESSION 2
# BINARY TREES AND BSTS
# =========================================================


def print_section(title):
    print('\n' + '=' * 72)
    print(title)
    print('=' * 72)


def preorder_values(root):
    if root is None:
        return []
    return [root.val] + preorder_values(root.left) + preorder_values(root.right)


def inorder_values(root):
    if root is None:
        return []
    return inorder_values(root.left) + [root.val] + inorder_values(root.right)


def postorder_values(root):
    if root is None:
        return []
    return postorder_values(root.left) + postorder_values(root.right) + [root.val]


def bst_inorder_keys(root):
    if root is None:
        return []
    return bst_inorder_keys(root.left) + [root.key] + bst_inorder_keys(root.right)


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class KeyValueNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


# =========================================================
# WEEK 8: SESSION 1
# =========================================================

# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Build a Binary Tree I)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because building trees by hand helps me understand parent-child links.
#
# U -- Understand
# 1) The image is not shown in the text here, so what tree should I build? I will use a simple root with two children.
# 2) What should I create? Actual TreeNode objects connected together.
#
# P -- Plan
# I will make a root node with value 1, a left child with value 2, and a right child with value 3.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create left child 2
# - create right child 3
# - create root 1 using those children
#
# I -- Implement

build_tree_one = TreeNode(1, TreeNode(2), TreeNode(3))

# Test Cases
print_section('Session 1 - Version 1 - Problem 1')
print(preorder_values(build_tree_one))
print(build_tree_one.left.val, build_tree_one.right.val)


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (3-Node Sum I)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it practices reading values from a tree in a tiny case.
#
# U -- Understand
# 1) How many nodes are guaranteed? Exactly 3 nodes.
# 2) What do I compare? The root value and the sum of both children.
#
# P -- Plan
# I will add the left and right child values and compare the result to the root value.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - return whether root.val equals root.left.val + root.right.val
#
# I -- Implement

def check_tree_sum_exact(root):
    return root.val == root.left.val + root.right.val

# Test Cases
print_section('Session 1 - Version 1 - Problem 2')
print(check_tree_sum_exact(TreeNode(10, TreeNode(4), TreeNode(6))))
print(check_tree_sum_exact(TreeNode(5, TreeNode(3), TreeNode(1))))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (3-Node Sum II)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it adds missing-child edge cases to the same tree idea.
#
# U -- Understand
# 1) What if one child is missing? I will treat the missing child as 0 because that matches the examples.
# 2) What if root is None? Return False.
#
# P -- Plan
# I will return False for an empty tree. Otherwise, I will use 0 for any missing child and compare the sum to the root.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - if root is None return False
# - get left value or 0
# - get right value or 0
# - compare left + right to root value
#
# I -- Implement

def check_tree_sum_up_to_three(root):
    if root is None:
        return False
    left_value = root.left.val if root.left else 0
    right_value = root.right.val if root.right else 0
    return root.val == left_value + right_value

# Test Cases
print_section('Session 1 - Version 1 - Problem 3')
print(check_tree_sum_up_to_three(TreeNode(10, TreeNode(10), None)))
print(check_tree_sum_up_to_three(TreeNode(5, TreeNode(3), TreeNode(2))))
print(check_tree_sum_up_to_three(TreeNode(5, None, TreeNode(2))))
print(check_tree_sum_up_to_three(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Find Leftmost Node I)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it reinforces following one path in a tree carefully.
#
# U -- Understand
# 1) Do I search the whole tree for the farthest-left value? No, the examples show I should follow the left pointers from the root.
# 2) What if the tree is empty? Return None.
#
# P -- Plan
# I will start at the root and keep moving left until I cannot move left anymore.
# Time Complexity: O(h)
# Space Complexity: O(1)
#
# Pseudocode
# - if root is None return None
# - while current.left exists move left
# - return current value
#
# I -- Implement

def left_most_iterative(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.val

# Test Cases
print_section('Session 1 - Version 1 - Problem 4')
left_tree_one = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
left_tree_two = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(left_most_iterative(left_tree_one))
print(left_most_iterative(left_tree_two))
print(left_most_iterative(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Find Leftmost Node II)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it gives me both iterative and recursive practice.
#
# U -- Understand
# 1) What version should this be? I will do the recursive version here.
# 2) What if root is None? Return None.
#
# P -- Plan
# If there is no left child, the current node is the leftmost node on that path. Otherwise, recurse left.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return None
# - if root.left is None return root.val
# - return recursive call on root.left
#
# I -- Implement

def left_most_recursive(root):
    if root is None:
        return None
    if root.left is None:
        return root.val
    return left_most_recursive(root.left)

# Test Cases
print_section('Session 1 - Version 1 - Problem 5')
print(left_most_recursive(left_tree_one))
print(left_most_recursive(left_tree_two))
print(left_most_recursive(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (In-order Traversal)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because inorder traversal is one of the main tree traversal patterns.
#
# U -- Understand
# 1) What order do I visit nodes? Left, current, right.
# 2) What should an empty tree return? An empty list.
#
# P -- Plan
# I will recursively gather the inorder traversal of the left subtree, then the root value, then the right subtree.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if root is None return []
# - return inorder(left) + [root] + inorder(right)
#
# I -- Implement

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Test Cases
print_section('Session 1 - Version 1 - Problem 6')
print(inorder_traversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))))
print(inorder_traversal(None))
print(inorder_traversal(TreeNode(1)))


# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (Binary Tree Size)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because counting nodes is a basic recursive tree skill.
#
# U -- Understand
# 1) What should an empty tree return? 0.
# 2) How do I count a non-empty tree? Count the root plus both subtrees.
#
# P -- Plan
# I will return 0 for None. Otherwise, I will return 1 plus the size of the left and right subtrees.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return 0
# - return 1 + size(left) + size(right)
#
# I -- Implement

def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

# Test Cases
print_section('Session 1 - Version 1 - Problem 7')
size_tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(size(size_tree))
print(size(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 8 (Binary Tree Find)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because searching a normal binary tree requires checking both sides.
#
# U -- Understand
# 1) Is this a BST? No, it is just a balanced binary tree.
# 2) What if the value is missing? Return False.
#
# P -- Plan
# I will use recursion. If the current node is not the value, I will search both subtrees.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return False
# - if root value matches return True
# - return find(left) or find(right)
#
# I -- Implement

def find(root, value):
    if root is None:
        return False
    if root.val == value:
        return True
    return find(root.left, value) or find(root.right, value)

# Test Cases
print_section('Session 1 - Version 1 - Problem 8')
find_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(find(find_tree, 5))
print(find(find_tree, 10))


# ---------------------------------------------------------
# Session: 1
# Problem #: 9 (BST Find)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because BST rules let me search faster than a normal tree.
#
# U -- Understand
# 1) Why is BST different here? I only need to search one side each step.
# 2) What if the value is not there? Return False.
#
# P -- Plan
# I will compare the target to the current node and move left or right like binary search.
# Time Complexity: O(h)
# Space Complexity: O(1)
#
# Pseudocode
# - while current exists
# - if match return True
# - move left if target smaller else move right
# - return False
#
# I -- Implement

def find_bst(root, value):
    current = root
    while current:
        if current.val == value:
            return True
        if value < current.val:
            current = current.left
        else:
            current = current.right
    return False

# Test Cases
print_section('Session 1 - Version 1 - Problem 9')
bst_tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(find_bst(bst_tree, 5))
print(find_bst(bst_tree, 10))


# ---------------------------------------------------------
# Session: 1
# Problem #: 10 (BST Descending Leaves)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it mixes BST traversal order with leaf checking.
#
# U -- Understand
# 1) What counts as a leaf? A node with no left and no right child.
# 2) How do I get descending order? Visit right subtree before left subtree.
#
# P -- Plan
# I will do a reverse inorder style traversal. Whenever I hit a leaf, I will add its value.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - recurse right
# - if current is leaf add value
# - recurse left
#
# I -- Implement

def descending_leaves(root):
    leaves = []

    def dfs(node):
        if node is None:
            return
        dfs(node.right)
        if node.left is None and node.right is None:
            leaves.append(node.val)
        dfs(node.left)

    dfs(root)
    return leaves

# Test Cases
print_section('Session 1 - Version 1 - Problem 10')
print(descending_leaves(bst_tree))
print(descending_leaves(TreeNode(10)))

# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Build A Binary Tree II)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it gives more practice making a tree by hand.
#
# U -- Understand
# 1) What values go in the tree? Root 5, left 10, right 20.
# 2) How many nodes are there? Three nodes.
#
# P -- Plan
# I will create the left and right children and connect them to the root.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create left child 10
# - create right child 20
# - create root 5
#
# I -- Implement

build_tree_two = TreeNode(5, TreeNode(10), TreeNode(20))

# Test Cases
print_section('Session 1 - Version 2 - Problem 1')
print(preorder_values(build_tree_two))
print(build_tree_two.left.val, build_tree_two.right.val)


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (3-Node Product I)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it checks a simple tree expression with multiplication.
#
# U -- Understand
# 1) How many nodes are guaranteed? Exactly 3.
# 2) What should be compared? Root value and the product of both children.
#
# P -- Plan
# I will multiply the two child values and compare the result to the root value.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - return whether root equals left times right
#
# I -- Implement

def check_tree_product_exact(root):
    return root.val == root.left.val * root.right.val

# Test Cases
print_section('Session 1 - Version 2 - Problem 2')
print(check_tree_product_exact(TreeNode(10, TreeNode(2), TreeNode(5))))
print(check_tree_product_exact(TreeNode(5, TreeNode(3), TreeNode(1))))


# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (3-Node Product II)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it adds edge cases to a small tree multiplication problem.
#
# U -- Understand
# 1) The text and examples conflict on one-child cases, so what rule should I use? I will follow the examples and treat a missing child as 1.
# 2) What should happen for an empty tree? Return False.
#
# P -- Plan
# I will return False for None. Otherwise, I will treat a missing child as 1 and compare the product to the root value.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - if root is None return False
# - left value is child value or 1
# - right value is child value or 1
# - compare product to root
#
# I -- Implement

def check_tree_product_up_to_three(root):
    if root is None:
        return False
    left_value = root.left.val if root.left else 1
    right_value = root.right.val if root.right else 1
    return root.val == left_value * right_value

# Test Cases
print_section('Session 1 - Version 2 - Problem 3')
print(check_tree_product_up_to_three(TreeNode(10, TreeNode(10), None)))
print(check_tree_product_up_to_three(TreeNode(5, TreeNode(5), TreeNode(1))))
print(check_tree_product_up_to_three(TreeNode(5, None, TreeNode(2))))
print(check_tree_product_up_to_three(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Find Rightmost Node I)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it is the mirror version of following left pointers.
#
# U -- Understand
# 1) Do I search the whole tree? No, I follow the right pointers from the root.
# 2) What if the tree is empty? Return None.
#
# P -- Plan
# I will keep moving right until there is no more right child.
# Time Complexity: O(h)
# Space Complexity: O(1)
#
# Pseudocode
# - if root is None return None
# - while current.right exists move right
# - return current value
#
# I -- Implement

def right_most_iterative(root):
    if root is None:
        return None
    current = root
    while current.right:
        current = current.right
    return current.val

# Test Cases
print_section('Session 1 - Version 2 - Problem 4')
right_tree_one = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
right_tree_two = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(right_most_iterative(right_tree_one))
print(right_most_iterative(right_tree_two))
print(right_most_iterative(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Find Rightmost Node II)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it gives me the recursive mirror pattern too.
#
# U -- Understand
# 1) What version should I do here? I will do the recursive version.
# 2) What if root is None? Return None.
#
# P -- Plan
# If there is no right child, that node is the rightmost one on that path. Otherwise, recurse right.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return None
# - if root.right is None return root value
# - recurse on root.right
#
# I -- Implement

def right_most_recursive(root):
    if root is None:
        return None
    if root.right is None:
        return root.val
    return right_most_recursive(root.right)

# Test Cases
print_section('Session 1 - Version 2 - Problem 5')
print(right_most_recursive(right_tree_one))
print(right_most_recursive(right_tree_two))
print(right_most_recursive(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Post-order Traversal)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because postorder is a core traversal order for trees.
#
# U -- Understand
# 1) What order do I visit nodes? Left, right, current.
# 2) What should an empty tree return? An empty list.
#
# P -- Plan
# I will recursively traverse the left subtree, then the right subtree, then add the current node.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if root is None return []
# - return post(left) + post(right) + [root]
#
# I -- Implement

def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

# Test Cases
print_section('Session 1 - Version 2 - Problem 6')
post_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
print(postorder_traversal(post_tree))
print(postorder_traversal(None))
print(postorder_traversal(TreeNode(1)))


# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (Binary Tree Product)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it combines recursion with values across a whole tree.
#
# U -- Understand
# 1) What should an empty tree return? 1.
# 2) How do I combine subtree answers? Multiply them with the current node value.
#
# P -- Plan
# I will return 1 for None. Otherwise, I will multiply the current value by the left and right subtree products.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return 1
# - return root times left product times right product
#
# I -- Implement

def product_tree(root):
    if root is None:
        return 1
    return root.val * product_tree(root.left) * product_tree(root.right)

# Test Cases
print_section('Session 1 - Version 2 - Problem 7')
print(product_tree(size_tree))
print(product_tree(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 8 (Binary Tree Is Leaf)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it mixes searching with checking node type.
#
# U -- Understand
# 1) What counts as a leaf? No left child and no right child.
# 2) Is this a BST? No, this is a normal binary tree search.
#
# P -- Plan
# I will search the full tree. When I find the value, I will return whether that node is a leaf.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return False
# - if value matches check if leaf
# - else search left or right
#
# I -- Implement

def is_leaf(root, value):
    if root is None:
        return False
    if root.val == value:
        return root.left is None and root.right is None
    return is_leaf(root.left, value) or is_leaf(root.right, value)

# Test Cases
print_section('Session 1 - Version 2 - Problem 8')
leaf_tree_one = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
leaf_tree_two = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(5))
print(is_leaf(leaf_tree_one, 5))
print(is_leaf(leaf_tree_two, 2))


# ---------------------------------------------------------
# Session: 1
# Problem #: 9 (BST Is Leaf)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because BST order lets me search for the leaf faster.
#
# U -- Understand
# 1) What should happen if the value is missing? Return False.
# 2) When do I stop? When I find the node or fall off the tree.
#
# P -- Plan
# I will search down the BST. If I find the value, I will check if it has no children.
# Time Complexity: O(h)
# Space Complexity: O(1)
#
# Pseudocode
# - walk down BST
# - if match return whether node is leaf
# - move left or right based on value
#
# I -- Implement

def is_leaf_bst(root, value):
    current = root
    while current:
        if current.val == value:
            return current.left is None and current.right is None
        if value < current.val:
            current = current.left
        else:
            current = current.right
    return False

# Test Cases
print_section('Session 1 - Version 2 - Problem 9')
print(is_leaf_bst(bst_tree, 5))
print(is_leaf_bst(bst_tree, 10))


# ---------------------------------------------------------
# Session: 1
# Problem #: 10 (BST Is Full)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it checks an important structural tree property.
#
# U -- Understand
# 1) What is a full tree? Every node has either 0 or 2 children.
# 2) What about an empty tree? I will treat it as True.
#
# P -- Plan
# I will recursively check each node. A node with exactly one child makes the tree not full.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return True
# - if exactly one child return False
# - recurse on both children
#
# I -- Implement

def is_full_tree(root):
    if root is None:
        return True
    if (root.left is None) != (root.right is None):
        return False
    return is_full_tree(root.left) and is_full_tree(root.right)

# Test Cases
print_section('Session 1 - Version 2 - Problem 10')
print(is_full_tree(bst_tree))
not_full_tree = TreeNode(10, TreeNode(2, None, TreeNode(3)), TreeNode(1))
print(is_full_tree(not_full_tree))


# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 1
# Problem #: 1 (Build A Binary Tree III)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it gives practice building an uneven tree shape by hand.
#
# U -- Understand
# 1) What shape should I build? a as root, b on the left, c on the right, and d as c's right child.
# 2) What should be connected? Actual TreeNode left and right references.
#
# P -- Plan
# I will build the bottom node first, then the right side, then the root.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - create d
# - create c with right d
# - create b
# - create a with left b and right c
#
# I -- Implement

build_tree_three = TreeNode('a', TreeNode('b'), TreeNode('c', None, TreeNode('d')))

# Test Cases
print_section('Session 1 - Version 3 - Problem 1')
print(preorder_values(build_tree_three))
print(build_tree_three.right.right.val)


# ---------------------------------------------------------
# Session: 1
# Problem #: 2 (3-Node Booleans)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it evaluates a tiny expression tree.
#
# U -- Understand
# 1) What values can the root hold? AND or OR.
# 2) What values do the children hold? True or False.
#
# P -- Plan
# I will check the root operator and apply the matching boolean operation to the children.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - if root is AND return left and right
# - else return left or right
#
# I -- Implement

def tree_expression(root):
    if root.val == 'AND':
        return root.left.val and root.right.val
    return root.left.val or root.right.val

# Test Cases
print_section('Session 1 - Version 3 - Problem 2')
print(tree_expression(TreeNode('OR', TreeNode(True), TreeNode(False))))
print(tree_expression(TreeNode('AND', TreeNode(True), TreeNode(False))))

# ---------------------------------------------------------
# Session: 1
# Problem #: 3 (3-Node Equality)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it adds simple child comparison practice.
#
# U -- Understand
# 1) Do both children need to exist? Yes, otherwise they cannot be equal here.
# 2) What should happen if one child is missing? Return False.
#
# P -- Plan
# I will check that both children exist and then compare their values.
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Pseudocode
# - if root or either child is missing return False
# - return whether left value equals right value
#
# I -- Implement

def equality(root):
    if root is None or root.left is None or root.right is None:
        return False
    return root.left.val == root.right.val

# Test Cases
print_section('Session 1 - Version 3 - Problem 3')
print(equality(TreeNode(1, TreeNode(2), TreeNode(2))))
print(equality(TreeNode(1, TreeNode(2), None)))


# ---------------------------------------------------------
# Session: 1
# Problem #: 4 (Find Leftmost Path I)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it turns a tree path into a list of values.
#
# U -- Understand
# 1) What path should I record? The path made by following left pointers from the root.
# 2) What should an empty tree return? An empty list.
#
# P -- Plan
# I will start at the root and keep adding values while moving left.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - create empty list
# - while current exists add value and move left
# - return list
#
# I -- Implement

def left_path_iterative(root):
    path = []
    current = root
    while current:
        path.append(current.val)
        current = current.left
    return path

# Test Cases
print_section('Session 1 - Version 3 - Problem 4')
print(left_path_iterative(left_tree_one))
print(left_path_iterative(left_tree_two))
print(left_path_iterative(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 5 (Find Leftmost Path II)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it gives recursive path-building practice.
#
# U -- Understand
# 1) What version should I do here? I will do the recursive version.
# 2) What should an empty tree return? An empty list.
#
# P -- Plan
# I will add the current value and recurse left until the path ends.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return []
# - return [root value] + left path of root.left
#
# I -- Implement

def left_path_recursive(root):
    if root is None:
        return []
    return [root.val] + left_path_recursive(root.left)

# Test Cases
print_section('Session 1 - Version 3 - Problem 5')
print(left_path_recursive(left_tree_one))
print(left_path_recursive(left_tree_two))
print(left_path_recursive(None))


# ---------------------------------------------------------
# Session: 1
# Problem #: 6 (Pre-order Traversal)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because preorder is another fundamental tree traversal pattern.
#
# U -- Understand
# 1) What order do I visit nodes? Current, left, right.
# 2) What should an empty tree return? An empty list.
#
# P -- Plan
# I will add the current value first, then recurse on the left subtree, then the right subtree.
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Pseudocode
# - if root is None return []
# - return [root] + preorder(left) + preorder(right)
#
# I -- Implement

def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Test Cases
print_section('Session 1 - Version 3 - Problem 6')
print(preorder_traversal(left_tree_one))
print(preorder_traversal(None))
print(preorder_traversal(TreeNode(1)))


# ---------------------------------------------------------
# Session: 1
# Problem #: 7 (Binary Tree All Lesser)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it checks one condition across every node in a tree.
#
# U -- Understand
# 1) What should happen for an empty tree? Return False.
# 2) What makes the answer True? Every node value is less than val.
#
# P -- Plan
# I will return False for None. Otherwise, I will check the current node and both subtrees.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return False
# - if root value is not less than val return False
# - recursively check both subtrees
#
# I -- Implement

def is_lesser(root, val):
    if root is None:
        return False
    if root.val >= val:
        return False
    left_ok = True if root.left is None else is_lesser(root.left, val)
    right_ok = True if root.right is None else is_lesser(root.right, val)
    return left_ok and right_ok

# Test Cases
print_section('Session 1 - Version 3 - Problem 7')
print(is_lesser(size_tree, 5))
print(is_lesser(size_tree, 6))


# ---------------------------------------------------------
# Session: 1
# Problem #: 8 (Binary Tree Any Greater)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it searches for a condition anywhere in a general tree.
#
# U -- Understand
# 1) What should happen if the tree is empty? Return False.
# 2) What makes the answer True? At least one node is greater than the given value.
#
# P -- Plan
# I will check the current node. If it is not greater, I will search both subtrees.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return False
# - if root value > target return True
# - search left or right
#
# I -- Implement

def contains_greater(root, value):
    if root is None:
        return False
    if root.val > value:
        return True
    return contains_greater(root.left, value) or contains_greater(root.right, value)

# Test Cases
print_section('Session 1 - Version 3 - Problem 8')
greater_tree = TreeNode(1, TreeNode(5, TreeNode(4), TreeNode(3)), TreeNode(2))
print(contains_greater(greater_tree, 3))
print(contains_greater(greater_tree, 10))


# ---------------------------------------------------------
# Session: 1
# Problem #: 9 (BST Any Greater)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because BST order gives me a faster way to answer the question.
#
# U -- Understand
# 1) What if the current node is already greater than the target? Then the answer is True.
# 2) If the current node is not greater, where can a greater value still be? Only in the right subtree.
#
# P -- Plan
# I will use BST logic. If the current value is greater than the target, I can stop early. Otherwise, I will move right.
# Time Complexity: O(h)
# Space Complexity: O(1)
#
# Pseudocode
# - while current exists
# - if current value > target return True
# - move right
# - return False
#
# I -- Implement

def contains_greater_bst(root, value):
    current = root
    while current:
        if current.val > value:
            return True
        current = current.right
    return False

# Test Cases
print_section('Session 1 - Version 3 - Problem 9')
print(contains_greater_bst(bst_tree, 3))
print(contains_greater_bst(bst_tree, 10))


# ---------------------------------------------------------
# Session: 1
# Problem #: 10 (BST Leaves Sum to Root)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it combines leaf detection with an accumulated tree calculation.
#
# U -- Understand
# 1) What should happen for a one-node tree? The example shows it should return False.
# 2) Which leaves count? All leaf nodes in the tree.
#
# P -- Plan
# I will return False for an empty tree or a single-node tree. Otherwise, I will sum the leaf values and compare that total to the root value.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None or a leaf return False
# - recursively sum all leaves
# - compare sum to root value
#
# I -- Implement

def sum_leaves(root):
    if root is None or (root.left is None and root.right is None):
        return False

    def leaf_total(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.val
        return leaf_total(node.left) + leaf_total(node.right)

    return leaf_total(root) == root.val

# Test Cases
print_section('Session 1 - Version 3 - Problem 10')
leaf_sum_tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), None)
print(sum_leaves(leaf_sum_tree))
print(sum_leaves(TreeNode(10)))


# =========================================================
# WEEK 8: SESSION 2
# =========================================================

# =========================================================
# PROBLEM SET VERSION 1
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Is Uni-valued)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it checks one repeated rule across a whole tree.
#
# U -- Understand
# 1) What makes a tree uni-valued? Every node has the same value.
# 2) What should happen for an empty tree? I will return True here because there is no mismatch.
#
# P -- Plan
# I will compare every node to the root value using recursion.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - remember root value
# - recursively check each node against it
#
# I -- Implement

def is_univalued(root):
    if root is None:
        return True

    target = root.val

    def dfs(node):
        if node is None:
            return True
        if node.val != target:
            return False
        return dfs(node.left) and dfs(node.right)

    return dfs(root)

# Test Cases
print_section('Session 2 - Version 1 - Problem 1')
unival_tree = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
not_unival_tree = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(2, None, TreeNode(1)))
print(is_univalued(unival_tree))
print(is_univalued(not_unival_tree))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Binary Tree Height)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because height is a key tree measurement used in many other problems.
#
# U -- Understand
# 1) What is the height of a single-node tree? 1.
# 2) How do I build the height of a bigger tree? 1 plus the larger subtree height.
#
# P -- Plan
# I will recursively find the height of the left and right subtrees and use the bigger one.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return 0
# - return 1 + max(height(left), height(right))
#
# I -- Implement

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Test Cases
print_section('Session 2 - Version 1 - Problem 2')
print(height(size_tree))
print(height(TreeNode(4)))

# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (BST Insert I)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because insert is one of the main BST update operations.
#
# U -- Understand
# 1) What if the key already exists? Update the value.
# 2) What if the tree is empty? Return a new root node.
#
# P -- Plan
# I will recursively walk left or right based on the key. If I find the key, I will update its value.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None create node
# - if key matches update value
# - if key smaller insert left else insert right
# - return root
#
# I -- Implement

def insert(root, key, value):
    if root is None:
        return KeyValueNode(key, value)
    if key == root.key:
        root.val = value
    elif key < root.key:
        root.left = insert(root.left, key, value)
    else:
        root.right = insert(root.right, key, value)
    return root

# Test Cases
print_section('Session 2 - Version 1 - Problem 3')
kv_root = KeyValueNode(10, 'A', KeyValueNode(5, 'B', KeyValueNode(1, 'C'), KeyValueNode(6, 'D')), KeyValueNode(15, 'E'))
kv_root = insert(kv_root, 9, 'Naruto')
print(bst_inorder_keys(kv_root))
empty_kv_root = insert(None, 4, 'Sailor Moon')
print(empty_kv_root.key, empty_kv_root.val)


# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (BST Remove I)
# Time Limit: 25 minutes
# Problem Importance:
# This matters because deletion is one of the trickiest BST operations.
#
# U -- Understand
# 1) What do I use for a node with two children? The in-order successor.
# 2) What if the key is missing? Return the original root unchanged.
#
# P -- Plan
# I will search for the key recursively. For the two-child case, I will copy in the smallest key from the right subtree and then delete that successor.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - search left or right for key
# - if found and node has 0 or 1 child return replacement child
# - if node has 2 children find smallest in right subtree
# - copy successor data into node
# - remove successor from right subtree
#
# I -- Implement

def remove_bst_successor(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = remove_bst_successor(root.left, key)
    elif key > root.key:
        root.right = remove_bst_successor(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = root.right
        while successor.left:
            successor = successor.left
        root.key = successor.key
        root.val = successor.val
        root.right = remove_bst_successor(root.right, successor.key)
    return root

# Test Cases
print_section('Session 2 - Version 1 - Problem 4')
remove_root_one = KeyValueNode(10, 'x', KeyValueNode(5, 'x', KeyValueNode(1, 'x'), KeyValueNode(8, 'x')), KeyValueNode(15, 'x', KeyValueNode(13, 'x'), KeyValueNode(16, 'x')))
remove_root_one = remove_bst_successor(remove_root_one, 10)
print(bst_inorder_keys(remove_root_one))
remove_root_two = KeyValueNode(10, 'x', KeyValueNode(5, 'x', KeyValueNode(1, 'x'), KeyValueNode(8, 'x', None, KeyValueNode(9, 'x'))), KeyValueNode(15, 'x', KeyValueNode(13, 'x'), KeyValueNode(16, 'x')))
remove_root_two = remove_bst_successor(remove_root_two, 8)
print(bst_inorder_keys(remove_root_two))
remove_root_two = remove_bst_successor(remove_root_two, 9)
print(bst_inorder_keys(remove_root_two))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (BST In-order Successor)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because successor logic is useful for BST navigation and deletion.
#
# U -- Understand
# 1) If current has a right subtree, where is the successor? The leftmost node in that right subtree.
# 2) If current has no right subtree, how do I find the successor? Track the last bigger ancestor while searching from the root.
#
# P -- Plan
# I will handle the right-subtree case first. Otherwise, I will search from the root and remember the best bigger ancestor.
# Time Complexity: O(h)
# Space Complexity: O(1)
#
# Pseudocode
# - if current.right exists go to leftmost node there
# - else walk from root and track last bigger node
#
# I -- Implement

def inorder_successor(root, current):
    if current is None:
        return None
    if current.right:
        node = current.right
        while node.left:
            node = node.left
        return node
    successor = None
    node = root
    while node:
        if current.key < node.key:
            successor = node
            node = node.left
        elif current.key > node.key:
            node = node.right
        else:
            break
    return successor

# Test Cases
print_section('Session 2 - Version 1 - Problem 5')
n1 = KeyValueNode(1, None)
n6 = KeyValueNode(6, None)
n9 = KeyValueNode(9, None)
n8 = KeyValueNode(8, None, n6, n9)
n5 = KeyValueNode(5, None, n1, n8)
n15 = KeyValueNode(15, None)
n10 = KeyValueNode(10, None, n5, n15)
succ_one = inorder_successor(n10, n5)
succ_two = inorder_successor(n10, n6)
print(succ_one.key if succ_one else None)
print(succ_two.key if succ_two else None)


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Merge Binary Trees)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it combines two trees node-by-node in a recursive way.
#
# U -- Understand
# 1) What if one node is missing? Use the node that exists.
# 2) What if both nodes exist? Sum their values.
#
# P -- Plan
# I will recursively create a new tree. If both nodes exist, I will sum them; otherwise I will copy the node that is present.
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# Pseudocode
# - if both nodes None return None
# - if one node None copy the other
# - else create node with summed value and merge children
#
# I -- Implement

def merge_trees(root1, root2):
    if root1 is None and root2 is None:
        return None
    if root1 is None:
        return TreeNode(root2.val, merge_trees(None, root2.left), merge_trees(None, root2.right))
    if root2 is None:
        return TreeNode(root1.val, merge_trees(root1.left, None), merge_trees(root1.right, None))
    return TreeNode(root1.val + root2.val, merge_trees(root1.left, root2.left), merge_trees(root1.right, root2.right))

# Test Cases
print_section('Session 2 - Version 1 - Problem 6')
merge_one = TreeNode(1, TreeNode(3, TreeNode(5), None), TreeNode(2))
merge_two = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
merged = merge_trees(merge_one, merge_two)
print(preorder_values(merged))
print(inorder_values(merged))


# =========================================================
# PROBLEM SET VERSION 2
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Is Even-valued)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it checks one value rule across the whole tree.
#
# U -- Understand
# 1) What makes the answer True? Every node value is even.
# 2) What should happen for an empty tree? I will return True because no node breaks the rule.
#
# P -- Plan
# I will recursively check that the current node is even and both subtrees are even-valued too.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return True
# - if value odd return False
# - recurse on both children
#
# I -- Implement

def is_even(root):
    if root is None:
        return True
    if root.val % 2 != 0:
        return False
    return is_even(root.left) and is_even(root.right)

# Test Cases
print_section('Session 2 - Version 2 - Problem 1')
even_tree = TreeNode(2, TreeNode(4, TreeNode(6), TreeNode(8)), TreeNode(10, None, TreeNode(12)))
odd_tree = TreeNode(2, TreeNode(4, TreeNode(1), TreeNode(6)), TreeNode(2, None, TreeNode(8)))
print(is_even(even_tree))
print(is_even(odd_tree))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Binary Tree Max)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because finding extremes is a common tree task.
#
# U -- Understand
# 1) What should an empty tree return? None.
# 2) What should a non-empty tree return? The greatest value in the tree.
#
# P -- Plan
# I will recursively find the max value in the left and right subtrees and compare them with the current node.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return None
# - get left max and right max
# - return the greatest of all existing values
#
# I -- Implement

def tree_max(root):
    if root is None:
        return None
    left_max = tree_max(root.left)
    right_max = tree_max(root.right)
    answer = root.val
    if left_max is not None and left_max > answer:
        answer = left_max
    if right_max is not None and right_max > answer:
        answer = right_max
    return answer

# Test Cases
print_section('Session 2 - Version 2 - Problem 2')
print(tree_max(size_tree))
print(tree_max(None))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (BST Insert II)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it shows how to handle duplicates with a consistent BST rule.
#
# U -- Understand
# 1) Where should duplicates go? Into the right subtree.
# 2) What if the tree is empty? Return the new node as the root.
#
# P -- Plan
# I will recurse left for smaller values and recurse right for greater or equal values.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - if root None create node
# - if value smaller go left else go right
#
# I -- Implement

def insert_with_duplicates_right(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insert_with_duplicates_right(root.left, value)
    else:
        root.right = insert_with_duplicates_right(root.right, value)
    return root

# Test Cases
print_section('Session 2 - Version 2 - Problem 3')
dup_right_root = TreeNode(10, TreeNode(8, TreeNode(1), TreeNode(6)), TreeNode(15))
dup_right_root = insert_with_duplicates_right(dup_right_root, 9)
print(inorder_values(dup_right_root))
dup_right_root = insert_with_duplicates_right(dup_right_root, 8)
print(inorder_values(dup_right_root))
print(insert_with_duplicates_right(None, 4).val)

# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (BST Remove II)
# Time Limit: 25 minutes
# Problem Importance:
# This matters because it gives me another important BST deletion strategy.
#
# U -- Understand
# 1) What do I use for two children here? The in-order predecessor.
# 2) What if the key is missing? Return the tree unchanged.
#
# P -- Plan
# I will recursively search for the key. In the two-child case, I will copy the largest node from the left subtree into the current node and then delete that predecessor.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - search for key
# - handle 0-child and 1-child cases directly
# - for 2 children find largest node in left subtree
# - copy predecessor data and remove predecessor
#
# I -- Implement

def remove_bst_predecessor(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = remove_bst_predecessor(root.left, key)
    elif key > root.key:
        root.right = remove_bst_predecessor(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        predecessor = root.left
        while predecessor.right:
            predecessor = predecessor.right
        root.key = predecessor.key
        root.val = predecessor.val
        root.left = remove_bst_predecessor(root.left, predecessor.key)
    return root

# Test Cases
print_section('Session 2 - Version 2 - Problem 4')
pred_root_one = KeyValueNode(10, 'x', KeyValueNode(5, 'x', KeyValueNode(1, 'x'), KeyValueNode(8, 'x')), KeyValueNode(15, 'x', KeyValueNode(13, 'x'), KeyValueNode(16, 'x')))
pred_root_one = remove_bst_predecessor(pred_root_one, 10)
print(bst_inorder_keys(pred_root_one))
pred_root_two = KeyValueNode(10, 'x', KeyValueNode(5, 'x', KeyValueNode(1, 'x'), KeyValueNode(8, 'x', KeyValueNode(7, 'x'), None)), KeyValueNode(15, 'x', KeyValueNode(13, 'x'), KeyValueNode(16, 'x')))
pred_root_two = remove_bst_predecessor(pred_root_two, 8)
print(bst_inorder_keys(pred_root_two))
pred_root_three = KeyValueNode(10, 'x', KeyValueNode(5, 'x', KeyValueNode(1, 'x'), KeyValueNode(8, 'x', None, KeyValueNode(9, 'x'))), KeyValueNode(15, 'x', KeyValueNode(13, 'x'), KeyValueNode(16, 'x')))
pred_root_three = remove_bst_predecessor(pred_root_three, 9)
print(bst_inorder_keys(pred_root_three))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (BST In-order Predecessor)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because predecessor logic is useful for BST navigation and deletion.
#
# U -- Understand
# 1) If current has a left subtree, where is the predecessor? The rightmost node in that left subtree.
# 2) If current has no left subtree, how do I find it? Track the last smaller ancestor while searching from the root.
#
# P -- Plan
# I will use the left-subtree case first. Otherwise, I will search from the root and remember the best smaller ancestor.
# Time Complexity: O(h)
# Space Complexity: O(1)
#
# Pseudocode
# - if current.left exists go to rightmost node there
# - else walk from root and track last smaller node
#
# I -- Implement

def inorder_predecessor(root, current):
    if current is None:
        return None
    if current.left:
        node = current.left
        while node.right:
            node = node.right
        return node
    predecessor = None
    node = root
    while node:
        if current.key > node.key:
            predecessor = node
            node = node.right
        elif current.key < node.key:
            node = node.left
        else:
            break
    return predecessor

# Test Cases
print_section('Session 2 - Version 2 - Problem 5')
p1 = KeyValueNode(1, None)
p3 = KeyValueNode(3, None)
p2 = KeyValueNode(2, None, p1, p3)
p8 = KeyValueNode(8, None)
p5 = KeyValueNode(5, None, p2, p8)
p15 = KeyValueNode(15, None)
p10 = KeyValueNode(10, None, p5, p15)
q1 = KeyValueNode(1, None)
q6 = KeyValueNode(6, None)
q9 = KeyValueNode(9, None)
q8 = KeyValueNode(8, None, q6, q9)
q5 = KeyValueNode(5, None, q1, q8)
q15 = KeyValueNode(15, None)
q10 = KeyValueNode(10, None, q5, q15)
print(inorder_predecessor(p10, p5).key)
print(inorder_predecessor(q10, q9).key)


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Identical Binary Trees)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because it compares tree structure and values at the same time.
#
# U -- Understand
# 1) What makes two trees identical? Same structure and same values everywhere.
# 2) What if one node is missing and the other is not? Return False.
#
# P -- Plan
# I will recursively compare both trees node by node.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if both None return True
# - if only one None return False
# - compare values and recurse on both sides
#
# I -- Implement

def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return root1.val == root2.val and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)

# Test Cases
print_section('Session 2 - Version 2 - Problem 6')
print(is_identical(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))))
print(is_identical(TreeNode(1, TreeNode(2), None), TreeNode(1, None, TreeNode(2))))
print(is_identical(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))))


# =========================================================
# PROBLEM SET VERSION 3
# =========================================================

# ---------------------------------------------------------
# Session: 2
# Problem #: 1 (Is Odd-valued)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it counts how many nodes match a value rule.
#
# U -- Understand
# 1) What should be counted? Nodes with odd values.
# 2) What should an empty tree return? 0.
#
# P -- Plan
# I will count 1 for the current node if it is odd, then add the counts from both subtrees.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return 0
# - count current if odd
# - add left count and right count
#
# I -- Implement

def count_odds(root):
    if root is None:
        return 0
    current = 1 if root.val % 2 != 0 else 0
    return current + count_odds(root.left) + count_odds(root.right)

# Test Cases
print_section('Session 2 - Version 3 - Problem 1')
odd_count_tree_one = TreeNode(2, TreeNode(3, TreeNode(6), TreeNode(7)), TreeNode(5, None, TreeNode(12)))
odd_count_tree_two = TreeNode(2, TreeNode(4, TreeNode(1), TreeNode(6)), TreeNode(2, None, TreeNode(8)))
print(count_odds(odd_count_tree_one))
print(count_odds(odd_count_tree_two))


# ---------------------------------------------------------
# Session: 2
# Problem #: 2 (Binary Tree Min)
# Time Limit: 10 minutes
# Problem Importance:
# This matters because it is the mirror idea of finding the maximum.
#
# U -- Understand
# 1) What should an empty tree return? None.
# 2) What should a non-empty tree return? The smallest value in the tree.
#
# P -- Plan
# I will recursively find the smallest value in the left and right subtrees and compare them to the current value.
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# Pseudocode
# - if root is None return None
# - get left min and right min
# - return smallest existing value
#
# I -- Implement

def tree_min(root):
    if root is None:
        return None
    left_min = tree_min(root.left)
    right_min = tree_min(root.right)
    answer = root.val
    if left_min is not None and left_min < answer:
        answer = left_min
    if right_min is not None and right_min < answer:
        answer = right_min
    return answer

# Test Cases
print_section('Session 2 - Version 3 - Problem 2')
print(tree_min(size_tree))
print(tree_min(None))


# ---------------------------------------------------------
# Session: 2
# Problem #: 3 (BST Insert III)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because it shows a different consistent rule for duplicates in a BST.
#
# U -- Understand
# 1) Where should duplicates go? Into the left subtree.
# 2) What if the tree is empty? Return the new node.
#
# P -- Plan
# I will recurse left for smaller or equal values and recurse right for larger values.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - if root None create node
# - if value <= root go left else go right
#
# I -- Implement

def insert_with_duplicates_left(root, value):
    if root is None:
        return TreeNode(value)
    if value <= root.val:
        root.left = insert_with_duplicates_left(root.left, value)
    else:
        root.right = insert_with_duplicates_left(root.right, value)
    return root

# Test Cases
print_section('Session 2 - Version 3 - Problem 3')
dup_left_root = TreeNode(10, TreeNode(8, TreeNode(1), TreeNode(6)), TreeNode(15))
dup_left_root = insert_with_duplicates_left(dup_left_root, 9)
print(inorder_values(dup_left_root))
dup_left_root = insert_with_duplicates_left(dup_left_root, 8)
print(inorder_values(dup_left_root))
print(insert_with_duplicates_left(None, 4).val)

# ---------------------------------------------------------
# Session: 2
# Problem #: 4 (BST Remove III)
# Time Limit: 25 minutes
# Problem Importance:
# This matters because deletion by merging is another useful BST deletion pattern.
#
# U -- Understand
# 1) What do I do when the node has two children? Attach the right subtree to the largest node in the left subtree.
# 2) What if the key is missing? Return the original root unchanged.
#
# P -- Plan
# I will search recursively for the key. In the two-child case, I will find the largest node in the left subtree, attach the right subtree there, and return the left subtree as the replacement.
# Time Complexity: O(h)
# Space Complexity: O(h)
#
# Pseudocode
# - search for key
# - if node has 0 or 1 child return replacement child
# - if node has 2 children find largest node in left subtree
# - attach old right subtree to that node
# - return left subtree
#
# I -- Implement

def remove_bst_merge(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = remove_bst_merge(root.left, key)
        return root
    if key > root.key:
        root.right = remove_bst_merge(root.right, key)
        return root
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left
    largest = root.left
    while largest.right:
        largest = largest.right
    largest.right = root.right
    return root.left

# Test Cases
print_section('Session 2 - Version 3 - Problem 4')
merge_remove_one = KeyValueNode(10, 'x', KeyValueNode(5, 'x', KeyValueNode(1, 'x'), KeyValueNode(8, 'x')), KeyValueNode(15, 'x', KeyValueNode(13, 'x'), KeyValueNode(16, 'x')))
merge_remove_one = remove_bst_merge(merge_remove_one, 10)
print(bst_inorder_keys(merge_remove_one))
merge_remove_two = KeyValueNode(10, 'x', KeyValueNode(5, 'x', KeyValueNode(1, 'x'), KeyValueNode(8, 'x', None, KeyValueNode(9, 'x'))), KeyValueNode(15, 'x', KeyValueNode(13, 'x'), KeyValueNode(16, 'x')))
merge_remove_two = remove_bst_merge(merge_remove_two, 8)
print(bst_inorder_keys(merge_remove_two))
merge_remove_two = remove_bst_merge(merge_remove_two, 9)
print(bst_inorder_keys(merge_remove_two))


# ---------------------------------------------------------
# Session: 2
# Problem #: 5 (BST Find Floor)
# Time Limit: 15 minutes
# Problem Importance:
# This matters because floor queries are a common BST search pattern.
#
# U -- Understand
# 1) What value should I return? The largest BST value less than or equal to the target.
# 2) What if no such value exists? Return None.
#
# P -- Plan
# I will walk down the BST and keep track of the best floor found so far.
# Time Complexity: O(h)
# Space Complexity: O(1)
#
# Pseudocode
# - start answer as None
# - if node value <= target save it and go right
# - else go left
#
# I -- Implement

def find_floor_bst(root, value):
    answer = None
    current = root
    while current:
        if current.val == value:
            return current.val
        if current.val < value:
            answer = current.val
            current = current.right
        else:
            current = current.left
    return answer

# Test Cases
print_section('Session 2 - Version 3 - Problem 5')
print(find_floor_bst(bst_tree, 3))
print(find_floor_bst(bst_tree, 4))
print(find_floor_bst(bst_tree, 0))


# ---------------------------------------------------------
# Session: 2
# Problem #: 6 (Nested Binary Trees)
# Time Limit: 20 minutes
# Problem Importance:
# This matters because subtree checking combines tree comparison and traversal.
#
# U -- Understand
# 1) What makes sub_root a subtree? Same structure and same values as some node and its descendants inside root.
# 2) What if sub_root is None? I will return True because an empty tree is a subtree.
#
# P -- Plan
# I will write one helper to compare two trees for exact equality, and another helper to try that comparison from every node in the main tree.
# Time Complexity: O(n * m) in the worst case
# Space Complexity: O(h)
#
# Pseudocode
# - write same_tree helper
# - if current root matches sub_root return True
# - otherwise check left subtree or right subtree
#
# I -- Implement

def is_subtree(root, sub_root):
    def same_tree(a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return a.val == b.val and same_tree(a.left, b.left) and same_tree(a.right, b.right)

    if sub_root is None:
        return True
    if root is None:
        return False
    if same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)

# Test Cases
print_section('Session 2 - Version 3 - Problem 6')
main_tree = TreeNode(2, TreeNode(3, TreeNode(6), TreeNode(7)), TreeNode(5, None, TreeNode(12)))
sub_tree_true = TreeNode(3, TreeNode(6), TreeNode(7))
sub_tree_false = TreeNode(3, TreeNode(1), TreeNode(2))
print(is_subtree(main_tree, sub_tree_true))
print(is_subtree(main_tree, sub_tree_false))
